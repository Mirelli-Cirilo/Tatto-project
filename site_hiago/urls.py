from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.loginPage, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.logoutPage, name='logout'),
    path('newComment/', views.newComment, name='newComment'),
    path('deleteComment/<int:id>/', views.deleteComment, name='delete'),
    path('updateComment/<int:id>/', views.updateComment, name='update'),
    path('detailComment/<int:id>/', views.detailComment, name='detail_comment')

]