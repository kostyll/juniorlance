from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


from rest_framework import viewsets, routers
from board.views import UserViewSet, GroupViewSet, DealerViewSet


# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)
router.register(r'dealers', DealerViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
resturlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^rest-api/', include('rest_framework_docs.urls')),
)


urlpatterns = resturlpatterns + patterns('',
    # Examples:
    # url(r'^$', 'juniorlance.views.home', name='home'),
    # url(r'^juniorlance/', include('juniorlance.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
