from django.db import models

class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title


class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    about = models.TextField()

    def str(self):
        return self.name