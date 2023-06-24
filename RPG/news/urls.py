from django.urls import path
from .views import PostList, PostCreate, PostDetail, PostUpdate, PostDelete, accept_response, reject_response,AuthorPage


urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('response/<int:response_id>/accept/', accept_response, name='accept_response'),
    path('response/<int:response_id>/reject/', reject_response, name='reject_response'),
    path('author/', AuthorPage.as_view(), name='author_page'),
]
