from django.urls import path

from apiOld import views

urlpatterns = [
    # path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('posts/', views.posts, name='posts'),
    path('posts/<int:id>/', views.postsWithId, name='postsWithId'),
    path('posts/<int:id>/like/', views.postsWithIdLike, name='postsWithIdLike'),
]
