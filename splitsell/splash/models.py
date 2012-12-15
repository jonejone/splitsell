from django.db import models
from django_extensions.db.models import TimeStampedModel

class NewsletterSubscriber(TimeStampedModel):
    email = models.EmailField()

    CATEGORY_CHOICES = (
        ('publisher', 'Publisher'),
        ('merchant', 'Merchant'),
    )

    category = models.CharField(max_length=20,
        choices=CATEGORY_CHOICES)


