from django.test import TestCase
from django.urls import reverse
from .factories import JourneyFactory, UserFactory
from main.models import User, Journey, Response
from django.utils.text import slugify


class MainTest(TestCase):

    def setUp(self):
        user = UserFactory()
        user.set_password('1234')
        user.save()
        self.user = user
        self.client.login(email=user.email, password='1234')

    def test_landing(self):
        response = self.client.get(reverse('landing'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Journey.coop')

    def test_get_journeys(self):
        JourneyFactory(title='Custom Title Test')
        JourneyFactory.create_batch(10)
        response = self.client.get(reverse('journeys'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Custom Title Test')

    def test_get_journeys_count(self):
        JourneyFactory.create_batch(4)
        response = self.client.get(reverse('journeys_count'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'4')

    def test_get_signup(self):
        self.client.logout()
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sign up")

    def test_post_signup(self):
        self.client.logout()
        response = self.client.post(
            reverse('signup'),
            {
                'email': 'test@email.uk',
                'password1': 'sosecret',
                'password2': 'sosecret',
            }
        )
        self.assertEqual(response.status_code, 200)

        user = User.objects.latest('pk')
        self.assertEqual(user.email, 'test@email.uk')
        self.assertContains(
            response,
            'You have successfully created your account '
            'test@email.uk. You can login now!'
        )

    def test_get_login(self):
        self.client.logout()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Log in')

    def test_post_login(self):
        self.client.logout()
        user = UserFactory(email='test@email.uk')
        user.set_password('1234')
        user.save()
        response = self.client.post(
            reverse('login'),
            {
                'username': user.email,
                'password': '1234'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Journey.coop')

    def test_get_nickname(self):
        response = self.client.get(
            reverse('nickname', kwargs={'pk': self.user.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'Please enter your nickname and country to '
            'display alongside your activity.'
        )

    def test_post_nickname(self):
        response = self.client.post(
            reverse('nickname', kwargs={'pk': self.user.pk}),
            {
                'nickname': 'donbalon',
                'country': 'cl'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'enableBodyScroll()')

    #def test_get_logout(self):
    #    response = self.client.get(reverse('logout'))
    #    self.assertEqual(response.status_code, 401)

    def test_post_logout(self):
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Journey.coop')

    def test_get_password_reset(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            "Enter your email address below, and we'll "
            "email instructions for setting a new one."
        )

    def test_post_password_reset(self):
        response = self.client.post(
            reverse('password_reset'),
            {
                'email': 'test@test.uk'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'If the address test@test.uk exists in our datab'
            'ase, an email has been sent with instructions t'
            'o reset your password.'
        )

    def test_get_password_reset_confirm(self):
        pass

    def test_get_start(self):
        response = self.client.get(reverse('start'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Share your journey!')

    def test_post_start(self):

        response = self.client.post(
            reverse('start'),
            {
                'title': 'Test Title',
                'summary': 'Test summary that is no longer than 400 characters'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'Test summary that is no longer than 400 characters'
        )
        journey = Journey.objects.latest('pk')
        self.assertEqual(journey.title, 'Test Title')
        self.assertEqual(
            journey.summary,
            'Test summary that is no longer than 400 characters'
        )
        self.assertIn(slugify(journey.title), journey.slug)

    def test_get_journey(self):
        journey = JourneyFactory()
        response = self.client.get(
            reverse(
                'journey_detail',
                kwargs={'slug': journey.slug}
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, journey.title)
        self.assertContains(response, journey.summary)

    def test_post_journey_respond(self):
        journey = JourneyFactory()
        response = self.client.post(
            reverse(
                'journey_respond',
                kwargs={'slug': journey.slug}
            ),
            {
                'text': 'This is a test response to a journey. Regards!'
            }

        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'This is a test response to a journey. Regards!'
        )
        respond = Response.objects.latest('pk')
        self.assertEqual(
            respond.text,
            'This is a test response to a journey. Regards!'
        )
        self.assertEqual(respond.journey, journey)
        # self.assertEqual(respond.author, )
