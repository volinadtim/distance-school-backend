from django.contrib.auth.models import AbstractUser
from django.db import models
from schedule.models import Schedule


class User(AbstractUser):
    """
    User model
    """
    DIRECTOR = 'D'
    STUDENT = 'S'
    TEACHER = 'T'
    PARENT = 'P'
    ADMIN = 'A'

    USER_TYPES = (
        (DIRECTOR, 'Director'),
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (PARENT, 'Parent'),
        (ADMIN, 'Admin'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(blank=True, max_length=150)
    user_type = models.CharField(max_length=1, choices=USER_TYPES,
                                 default=STUDENT)
    avatar = models.ImageField(
        upload_to='avatars', blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=15)

    REQUIRED_FIELDS = ['first_name', 'last_name']


class School(models.Model):
    """
    School model
    """
    location = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)


# class ClassesParallel(models.Model):
#     """
#     Classes Parallel model
#     """


class Grade(models.Model):
    """
    Grade model
    """
    entry_year = models.IntegerField()
    # parallel = models.ForeignKey(
    #     ClassesParallel, on_delete=models.CASCADE, related_name="grades")
    name = models.CharField(max_length=20)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="classes")

    def __str__(self):
        return f'{self.entry_year} {self.name}'


class Student(models.Model):
    """
    Student model
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="student", primary_key=True)
    school = models.ForeignKey(
        School, on_delete=models.SET_NULL, related_name="students", null=True)
    grade = models.ForeignKey(
        Grade, on_delete=models.SET_NULL, related_name="students", null=True)
    schedule = models.OneToOneField(
        Schedule, on_delete=models.SET_NULL, related_name="student", null=True)
    is_verified = models.BooleanField(default=False)


class Teacher(models.Model):
    """
    Teacher model
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="teacher", primary_key=True)
    is_director = models.BooleanField(default=False)
    school = models.ForeignKey(
        School, on_delete=models.SET_NULL, related_name="teachers", null=True)
    schedule = models.OneToOneField(
        Schedule, on_delete=models.SET_NULL, related_name="teacher", null=True)
    is_verified = models.BooleanField(default=False)


class Parent(models.Model):
    """
    Parent model
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="parent", primary_key=True)
    is_verified = models.BooleanField(default=False)


class Admin(models.Model):
    """
    Admin model
    """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="admin")
