from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from insta.views import PostLikeToggle

urlpatterns=[
    url(r'^$',views.index,name = 'index'),
    url(r'^search/', views.search_profile, name='search'),
    url(r'^registration_form/$', views.signup, name='signup'),
    url(r'^accounts/$', include('django.contrib.auth.urls')),
    url(r'^profile/<username>/$', views.profile, name='profile'),
    url(r'^user_profile/<username>/$', views.user_profile, name='user_profile'),
    url(r'post/(?P<id>\d+)', views.post_comment, name='comment'),
    url(r'post/(?P<id>\d+)/like$', PostLikeToggle.as_view(), name='liked'),
    url(r'like/$', views.like_post, name='like_post'),
    url(r'unfollow/<to_unfollow>$', views.unfollow, name='unfollow'),
    url(r'follow/<to_follow>$', views.follow, name='follow')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)