from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()

router.register(
    r'posts', PostViewSet
)
router.register(
    r'groups', GroupViewSet
)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
    basename='comments'
)
router.register(
    r'follow', FollowViewSet,
    basename='follow'
)

app_name = 'api'

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
