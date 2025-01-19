from rest_framework import serializers
from .models import *

# --- Форумы и темы ---
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'content', 'author']


class ThreadSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Thread
        fields = ['id', 'title', 'forum', 'messages']


class ForumSerializer(serializers.ModelSerializer):
    threads = ThreadSerializer(many=True, read_only=True)

    class Meta:
        model = Forum
        fields = ['id', 'name', 'description', 'threads']


# --- События ---
class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'name', 'email', 'event']


class EventSerializer(serializers.ModelSerializer):
    participants = ParticipantSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'location', 'date', 'participants']


class LocationSerializer(serializers.ModelSerializer):
    events = EventSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = ['id', 'name', 'address', 'events']


# --- Проекты и задачи ---
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'project', 'assignee', 'completed']


class ProjectSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'tasks']


# --- Учебные курсы ---
class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'title', 'content', 'course']


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'modules']


# --- Библиотека ---
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'value', 'review']


class ReviewSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'content', 'book', 'scores']


class BookSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'category', 'author', 'reviews']


class BookCategorySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = BookCategory
        fields = ['id', 'name', 'books']


# --- Социальная сеть ---
class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ['id', 'from_profile', 'to_profile']


class ProfileSerializer(serializers.ModelSerializer):
    friends = FriendshipSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'name', 'bio', 'friends']
