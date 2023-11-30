from django.db import models
# from django.contrib.auth.models import User


class User(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    # password = models.CharField(max_length=20, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    description = models.TextField(max_length=750, null=True)
    image = models.ImageField(blank=True)
    recordBook = models.PositiveIntegerField(unique=True)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, blank=True, null=True)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug


class Team(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=750, null=True)
    leader = models.OneToOneField('User', on_delete=models.CASCADE, related_name='Руководитель')
    users = models.ForeignKey('User', on_delete=models.CASCADE, related_name='Пользователи')
    tasks = models.ForeignKey('Task', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=750, null=True)
    status = models.ForeignKey('TaskStatus', on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class TaskStatus(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=255)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    description = models.TextField(max_length=750, null=True)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

