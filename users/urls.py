from django.urls import path
from users.views import users_view_profile, users_view_settings, users_view_follows, users_view_followers, users_view_likes
from users.views import users_view_comments, users_view_bookmarks

urlpatterns = [
    path('', users_view_profile),
    path('settings/', users_view_settings),
    path('follows/', users_view_follows),
    path('followers/', users_view_followers),
    path('likes/', users_view_likes),
    path('comments/', users_view_comments),
    path('bookmarks/', users_view_bookmarks),
]
