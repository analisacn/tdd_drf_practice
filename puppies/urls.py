from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^puppies/(?P<pk>[0-9]+)$',
        views.get_delete_update_puppy,
        name='get_delete_update_puppy'
    ),
    url(
        r'^puppies/$',
        views.get_post_puppies,
        name='get_post_puppies'
    )
]
