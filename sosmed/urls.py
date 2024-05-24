from django.urls import path, re_path

from . import views

app_name = 'sosmed'

urlpatterns = [
    re_path(r'delete/(?P<delete_id>[0-9]+)$', views.delete, name='delete'),
    re_path(r'update/(?P<update_id>[0-9]+)$', views.update, name='update'),
    re_path(r'^create/', views.create, name='create'),
    re_path(r'^$', views.list, name='list')
]