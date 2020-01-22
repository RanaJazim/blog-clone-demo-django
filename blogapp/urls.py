from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.index, name='post_index'),
    path('create/', views.create, name='post_create'),
    path('edit/<post_id>/', views.edit, name='post_edit'),
    path('delete/<post_id>/', views.destroy, name='post_destroy'),
    # adding the comments url
    path('<post_id>/comment/store/', views.comment_store, name='comment_store'),
    path('<post_id>/comments/', views.comment_index, name='comment_index'),
    path('comment/<comment_id>/', views.approved_comment, name='comment_approved'),
]
