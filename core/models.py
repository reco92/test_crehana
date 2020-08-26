from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    """
    """

    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False)
    modified = models.DateTimeField(auto_now=True,
                                    editable=False)


class Course(models.Model):
    """
    """

    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category,
                            related_name='courses',
                            on_delete=models.CASCADE,
                            db_index=True)
    created = models.DateTimeField(auto_now_add=True,
                                   editable=False)
    modified = models.DateTimeField(auto_now=True,
                                    editable=False)


class Registration(models.Model):
    """
    Also named 'Inscripcion'
    """ 

    course = models.ForeignKey(Course,
                            related_name='registers',
                            on_delete=models.CASCADE,
                            db_index=True)
    user = models.ForeignKey(User,
                            related_name='user_registers',
                            on_delete=models.CASCADE,
                            db_index=True)

    class Meta:
        unique_together = ('course', 'user')



class ProgressVideo(models.Model):
    """
    """ 

    course = models.ForeignKey(Course,
                            related_name='progress_videos',
                            on_delete=models.CASCADE,
                            db_index=True)
    user = models.ForeignKey(User,
                            related_name='progress_courses',
                            on_delete=models.CASCADE,
                            db_index=True)
    date = models.DateField()
    minutes = models.PositiveIntegerField(default=0)


    registration = models.ForeignKey(Registration,
                            related_name='progress_video_registration',
                            on_delete=models.CASCADE,
                            blank=True, null=True)
    category = models.ForeignKey(Category,
                            related_name='progress_video_category',
                            on_delete=models.CASCADE,
                            blank=True, null=True)

    class Meta:
        unique_together = ('course', 'user', 'date')