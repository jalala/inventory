from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^inventory/home/$', 'inventory.views.home', name='home'),
    (r'^inventory/sections/$', 'inventory.views.sections'),
    (r'^inventory/(?P<section_id>\d+)/section/$', 'inventory.views.section_rooms'),
    (r'^inventory/(?P<room_id>\d+)/room/$', 'inventory.views.room_items'),

#    url(r'^smja/', include('smja.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
#     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#     url(r'^accounts/', include('accounts.url')),
     url(r'^accounts/', include('django.contrib.auth.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
