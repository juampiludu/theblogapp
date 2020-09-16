from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    path('list/', views.PostListApiView.as_view(), name='posts'),
    path('list/author/<int:author>/', views.MyPosts.as_view(), name='myposts'),
    path('list/post/<int:id>/', views.ShowPost.as_view(), name='posts_detail'),
    path('add/', views.AddPost.as_view(), name="add_post"),
    path('delete/<int:id>/', views.DeletePost.as_view(), name="delete"),
    path('comment/list/<int:post>/', views.CommentList.as_view(), name="commet_list"),
    path('comment/add/', views.AddComment.as_view(), name="add_comment"),
    path('comment/delete/<int:id>/', views.DeleteComment.as_view(), name="delete_comment"),

]

urlpatterns = format_suffix_patterns(urlpatterns)
