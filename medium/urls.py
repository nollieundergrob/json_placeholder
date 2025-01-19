from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

# --- Форумы и темы ---
router.register('forums', ForumViewSet)
router.register('threads', ThreadViewSet)
router.register('messages', MessageViewSet)

# --- События ---
router.register('locations', LocationViewSet)
router.register('events', EventViewSet)
router.register('participants', ParticipantViewSet)

# --- Проекты и задачи ---
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)

# --- Учебные курсы ---
router.register('courses', CourseViewSet)
router.register('modules', ModuleViewSet)

# --- Библиотека ---
router.register('categories', BookCategoryViewSet)
router.register('books', BookViewSet)
router.register('reviews', ReviewViewSet)
router.register('scores', ScoreViewSet)

# --- Социальная сеть ---
router.register('profiles', ProfileViewSet)
router.register('friendships', FriendshipViewSet)

urlpatterns = router.urls
