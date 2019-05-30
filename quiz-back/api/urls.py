from django.urls import path

from api import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('contacts/', views.ContactsApi.as_view(), name='contacts'),
    path('contacts/<int:pk>/', views.ContactApi.as_view(), name='contactById'),
]
