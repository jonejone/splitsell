from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('splitsell.splash.views',
    url(r'^$', 'index', name='splash-index'),
)
