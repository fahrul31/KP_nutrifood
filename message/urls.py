from django.urls import path

from . import views

app_name = 'message'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create_view, name='create'),
    path('<int:id>/detail/', views.detail_view, name='detail'),
    path('update/<int:id>', views.update_view, name='update'),
    path('delete/<int:id>', views.delete_view, name='delete'),
]