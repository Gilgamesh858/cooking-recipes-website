from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from . import views

urlpatterns = [
    #url(r'^index/$', views.index),
    url(r'^about/$', views.about),
    url(r'^search/(?P<choice1>\w+)/$', views.search_view),
    url(r'^search/$', views.searchFor_view),
    url(r'^cookbook/(?P<recipe_id>\d+)/$', views.show_recipe),
    url(r'^cookbook/$', views.cookbook),
    url(r'^addRecipe/$', views.recipe_create_view),
    url(r'^contact/$', views.contact),
    url(r'^profile/(?P<user_name>\w+)/$', views.profile_view, name="profile_view"),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^index/$', views.index),
    url(r'^$', views.index),
]

#Add to the bottom of your file
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
           {'document_root': settings.MEDIA_ROOT,}),
    ]
