from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("group/<str:slug>",views.group_posts),

    #раздел добавления публикации
    path("new/", views.new_post, name="new_post"),

    # Профайл пользователя
    path("<username>/", views.profile, name="profile"),
    # Просмотр записи
    path("<username>/<int:post_id>/", views.post_view, name="post"),
    path("<username>/<int:post_id>/edit", views.post_edit, name="post_edit"),
]