from django.urls import include, path
from rest_framework_nested import routers

from .views import (PostViewSet, CommentViewSet,
                    GroupViewSet, FollowViewSet)


router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register('follow', FollowViewSet, basename='follow')

comment_router = routers.NestedDefaultRouter(router, 'posts', lookup='post')
comment_router.register('comments', CommentViewSet, basename='comment')


v1_urls = [
    path('', include(router.urls)),
    path('', include(comment_router.urls)),
    path('', include('djoser.urls.jwt')),
]

urlpatterns = [
    path('v1/', include(v1_urls))
]
