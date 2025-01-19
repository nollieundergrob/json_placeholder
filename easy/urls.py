from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ProfileViewSet, PostViewSet, CommentViewSet,
    ProductViewSet, CategoryViewSet, OrderViewSet, AuthorViewSet,
    BookViewSet, RatingViewSet, TagViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)
router.register('posts', PostViewSet)
router.register('comments', CommentViewSet)
router.register('products', ProductViewSet)
router.register('categories', CategoryViewSet)
router.register('orders', OrderViewSet)
router.register('authors', AuthorViewSet)
router.register('books', BookViewSet)
router.register('ratings', RatingViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
