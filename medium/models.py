from django.db import models

# --- Форумы и темы ---
class Forum(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Thread(models.Model):
    title = models.CharField(max_length=200)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE, related_name='threads')

    def __str__(self):
        return self.title


class Message(models.Model):
    content = models.TextField()
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='messages')
    author = models.CharField(max_length=100)

    def __str__(self):
        return f"Message by {self.author}"


# --- События ---
class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='events')
    date = models.DateTimeField()

    def __str__(self):
        return self.title


class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')

    def __str__(self):
        return self.name


# --- Проекты и задачи ---
class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    assignee = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# --- Учебные курсы ---
class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title


class Module(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.title


# --- Библиотека ---
class BookCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE, related_name='books')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Review(models.Model):
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review of {self.book.title}"


class Score(models.Model):
    value = models.IntegerField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='scores')

    def __str__(self):
        return f"Score {self.value}"


# --- Социальная сеть ---
class Profile(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Friendship(models.Model):
    from_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friends')
    to_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='friend_of')

    def __str__(self):
        return f"{self.from_profile.name} -> {self.to_profile.name}"
