from django.urls import path
from fandoms.views import fandoms_view_main, fandoms_view_fandom

urlpatterns = [
    path('', fandoms_view_main),
    path('<str:fandom_name>/', fandoms_view_fandom),
]
