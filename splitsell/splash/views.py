from django.shortcuts import render
from django.http import HttpResponseRedirect

from splitsell.splash.forms import NewsletterForm

def index(request):

    subscribed = False

    if request.method == 'POST':
        form = NewsletterForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?subscribed=true')
    else:
        form = NewsletterForm()

    if 'subscribed' in request.GET.keys():
        subscribed = True

    tmpl_data = {
        'form': form,
        'subscribed': subscribed,
    }

    return render(request,
        'splitsell/splash/index.html', tmpl_data)
