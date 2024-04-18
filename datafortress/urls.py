from django.urls import path
from . import views


urlpatterns = [
    path('' , views.index , name='index'),
    path('login_user' , views.login_user , name='login_user'),
    path('logout' , views.logout , name='logout'),
    path('signup' , views.signup , name='signup'),
    path('success', views.success , name='success'),
    path('welcome_editor', views.welcome_editor, name='welcome_editor'),
    path('welcome_creator', views.welcome_creator, name='welcome_creator'),
    path('upload_video', views.upload_video, name='upload_video'),
    path('video_list_editor', views.video_list_editor, name='video_list_editor'),
    path('video_list_creator', views.video_list_creator, name='video_list_creator'),
    path('delete_video_editor/<int:video_id>/', views.delete_video_editor, name='delete_video_editor'),
    path('delete_video_creator/<int:video_id>/', views.delete_video_creator, name='delete_video_creator'),
    path('approve_video/<int:video_id>/', views.approve_video, name='approve_video'),
    path('notification_send', views.notification_send, name='notification_send'),    
    path('notification_list/', views.notification_list, name='notification_list'),
    path('notifications/delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),

]
