from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = DefaultRouter()

router.register(
    r'v1/posts', PostViewSet
)
router.register(
    r'v1/groups', GroupViewSet
)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
    basename='comments'
)
router.register(
    r'v1/follow', FollowViewSet,
    basename='follow'
)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
