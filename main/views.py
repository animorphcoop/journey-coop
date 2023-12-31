from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import reverse_lazy, reverse
from .forms import UserCreationForm, AuthenticationForm, CreateJourneyForm, CreateResponseForm, UserResetForm, \
    SetNewPasswordForm, SetNicknameForm
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout
from django.utils.decorators import method_decorator

from .models import Journey, Response, User
from django.contrib import messages
from django.middleware.csrf import rotate_token


def landing(request):
    return render(request, 'index.html')


def error_handler(request, exception=None):
    return render(request, 'error_landing.html')


def journeys(request):
    journeys = Journey.objects.all()
    context = {
        'journeys': journeys.order_by('-created_on')
    }
    return render(request, 'partials/journeys.html', context)


def journeys_count(request):
    all_journeys = Journey.objects.all()
    return HttpResponse(all_journeys.count())


class UserCreate(CreateView):
    form_class = UserCreationForm
    template_name = "overlays/signup.html"

    def form_valid(self, form):
        self.object = form.save()
        context = {'username': self.object.email}
        return render(self.request, "partials/signup_success.html", context)


class UserLogin(LoginView):
    form_class = AuthenticationForm
    template_name = "overlays/login.html"

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        if str(form.get_user()) == str(form.get_user().email):
            response = render(self.request, "partials/nickname_trigger.html")
        else:
            response = HttpResponse("<script>setTimeout(()=>{layerEventTrigger('login', 'landing');}, 200)</script>")
        response['HX-Trigger'] = 'logged_in'
        return response

    def form_invalid(self, form):
        context = {'form': form}
        return render(self.request, "overlays/login.html", context)


# Need to rotate CSRF token and pass it to logout button for it to work
def get_logout(request):
    rotate_token(request)
    context = {
        'new_csrf': request.META["CSRF_COOKIE"]
    }
    return render(request, "partials/logout_button.html", context)


class UserLogout(LogoutView):
    template_name = "logout.html"

    def post(self, request, *args, **kwargs):
        auth_logout(request)
        return HttpResponse("<script>layerEventTrigger('loggedin', 'loggedout');</script>")


class UserReset(PasswordResetView):
    template_name = "overlays/password_reset.html"
    form_class = UserResetForm

    def form_valid(self, form):
        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": self.extra_email_context,
        }
        form.save(**opts)
        context = {
            'email': form.cleaned_data['email']
        }
        return render(self.request, "partials/password_reset_done.html", context)


class UserNickname(UpdateView):
    model = User
    form_class = SetNicknameForm
    template_name = "overlays/nickname.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.save()
        # return render(self.request, "partials/overlay_end.html")
        return HttpResponse("<script>layerEventTrigger('nickname', 'landing');</script>")


# source template in contrib/admin/templates/registration
class UserResetConfirm(PasswordResetConfirmView):
    form_class = SetNewPasswordForm
    template_name = "password_reset_confirm.html"

    def form_valid(self, form):
        user = form.save()
        del self.request.session["_password_reset_token"]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        messages.success(self.request,
                         'You have successfully reset your password, feel most welcome to log in using it now!')
        return redirect('landing')


class CreateJourney(CreateView):
    form_class = CreateJourneyForm
    template_name = 'overlays/journey_start.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return UserLogin.as_view()(request, *args, **kwargs)

        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # breakpoint() l & c

        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        response = render(self.request, "overlays/journey_detail.html", {'journey': self.object})
        # add custom trigger event so the newly created journey is triggers reloading of journey list
        response['HX-Trigger'] = 'created_journey'
        return response


class JourneyDetail(DetailView):
    model = Journey
    template_name = "overlays/journey_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['responses'] = Response.objects.filter(journey=self.object).order_by('created_on')
        context['form'] = CreateResponseForm()
        return context


class CreateResponse(CreateView):
    form_class = CreateResponseForm
    template_name = 'overlays/journey_start.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        journey = Journey.objects.filter(slug=self.kwargs['slug'])[0]
        self.object.journey = journey
        self.object.author = self.request.user
        self.object.save()
        responses = Response.objects.filter(journey=self.object.journey).order_by('created_on')
        context = {
            'responses': responses
        }

        return render(self.request, "partials/journey_responses.html", context)
