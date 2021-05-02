from django.urls import path

from music import views

urlpatterns = [
    path('', views.music, name='music'),
    path('author', views.author, name='author'),
    path('list', views.list_musics, name='List_musics'),
    path('new/', views.create_member, name = 'add_member'),
    path('update/<int:id>/', views.update_music, name = 'update_music'),
    path('delete/<int:id>/', views.delete_music, name = 'delete_member'),
]

]
