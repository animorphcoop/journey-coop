from django.contrib.auth.forms import UserCreationForm as DjUserCreationForm
from django.contrib.auth.forms import AuthenticationForm as DjAuthenticationForm
from django.contrib.auth.forms import PasswordResetForm as DjPasswordResetForm
from django.contrib.auth.forms import SetPasswordForm as DjSetPasswordForm




from django.contrib.auth import get_user_model, authenticate
from django import forms

import unicodedata
from django.utils.translation import gettext_lazy as _
from django.utils.text import capfirst
from django.core.exceptions import ValidationError
from main.models import Journey, Response

import os
from django.template import loader
from django.core.mail import EmailMultiAlternatives


class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize("NFKC", super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            "autocapitalize": "none",
            "autocomplete": "email",
        }


class UserCreationForm(DjUserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email",)
        field_classes = {"email": UsernameField}


class AuthenticationForm(DjAuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "password",)

class UserResetForm(DjPasswordResetForm):

    from_email = None
    html_email_template_name = None
    subject_template_name = "registration/password_reset_subject.txt"
    # success_url = reverse_lazy("password_reset_done")
    template_name = "registration/password_reset_form.html"
    title = _("Password reset")

    def clean(self):
        cleaned_data = self.cleaned_data
        #print(cleaned_data)
        return cleaned_data


    def send_mail(
        self,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
    ):
        """
        Send a django.core.mail.EmailMultiAlternatives to `to_email`.
        """

        subject_template_name="auto/password_reset_subject.txt",
        email_template_name="auto/password_reset_email.html",

        subject = loader.render_to_string(subject_template_name, context)
        # Email subject *must not* contain newlines
        subject = "".join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)

        email_message = EmailMultiAlternatives(subject, body, from_email, [to_email])
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, "text/html")

        email_message.send()


class SetNewPasswordForm(DjSetPasswordForm):
    def clean(self):
        cleaned_data = self.cleaned_data
        print(cleaned_data)
        return cleaned_data



class CreateJourneyForm(forms.ModelForm):
    # ALLOWED_AUDIO_TYPES = ['wav', 'wma', 'mp3', 'aiff', 'aac', 'm4a']

    class Meta:
        model = Journey
        fields = ("title", "summary", "image", "audio",)

    '''
    def clean(self):
        cleaned_data = self.cleaned_data
        file = cleaned_data.get("audio")
        #print('here')

        #breakpoint()

        if file is not None:
            try:
                extension = os.path.splitext(file.name)[1][1:].lower()
                if extension in self.ALLOWED_AUDIO_TYPES:
                    return cleaned_data
                else:
                    raise forms.ValidationError('File types is not allowed')
            except Exception as e:
                raise forms.ValidationError('Cannot identify file type')

        return cleaned_data
        '''


class CreateResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ("text",)
