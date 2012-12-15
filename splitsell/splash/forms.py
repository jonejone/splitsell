from django import forms
from splitsell.splash.models import NewsletterSubscriber 


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber 

    category = forms.CharField(widget=forms.RadioSelect(
        choices=NewsletterSubscriber.CATEGORY_CHOICES))
