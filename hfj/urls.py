from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'project.views.home'),
    url(r'^updatetime', 'project.views.updatetime'),
    url(r'^getRunners', 'project.views.getRunners'),
    url(r'^addRunner', 'project.views.addRunner'),
    # url(r'^hfj/', include('hfj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)