import factory
from factory import SubFactory

from main.models import User, Journey, Response


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: 'email_%d@test.uk' % n)
    nickname = factory.Sequence(lambda n: 'H3ll0_%d@' % n)


class JourneyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Journey

    slug = factory.Sequence(lambda n: 'slug-%d' % n)
    title = factory.Sequence(lambda n: 'Title %d' % n)
    summary = factory.Sequence(lambda n: 'Summary %d' % n)
    author = SubFactory(UserFactory)


class ResponseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Response

    factory.Sequence(lambda n: 'Summary %d' % n)
    author = SubFactory(UserFactory)
    journey = SubFactory(JourneyFactory)
