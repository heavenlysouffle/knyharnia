from django.urls import path, re_path
from works.views import works_view_main, works_view_create, works_view_work, works_view_chapter, works_view_edit_work
from works.views import works_view_add_chapter, works_view_edit_chapter

urlpatterns = [
    path('', works_view_main),
    path('create/', works_view_create),
    re_path(r'^(?P<work_id>[0-9]{9})/$', works_view_work),
    re_path(r'^(?P<work_id>[0-9]{9})/edit/$', works_view_edit_work),
    re_path(r'^(?P<work_id>[0-9]{9})/add_chapter/$', works_view_add_chapter),
    re_path(r'^(?P<work_id>[0-9]{9})/chapters/(?P<chapter_id>[0-9]{9})/$', works_view_chapter),
    re_path(r'^(?P<work_id>[0-9]{9})/chapters/(?P<chapter_id>[0-9]{9})/edit/$', works_view_edit_chapter),
]
