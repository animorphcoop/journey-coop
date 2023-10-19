from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify
import random
import string

from .models import Journey


@receiver(pre_save, sender=Journey)
def add_slug_to_journey(sender, instance, *args, **kwargs):

    if instance and not instance.slug:
        slug = slugify(instance.title)
        random_string = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(4))
        instance.slug = slug + "-" + random_string
