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
    path('video_list', views.video_list, name='video_list'),
    path('delete_video/<int:video_id>/', views.delete_video, name='delete_video'),
    path('approve_video/<int:video_id>/', views.approve_video, name='approve_video'),
    path('notification_list/', views.notification_list, name='notification_list'),
    path('notifications/delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('video_list', views.video_list, name='video_list'),
    path('homepage', views.homepage, name='homepage'),

]