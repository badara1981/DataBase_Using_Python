from django.db import models

# Create your models here.
class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"title: {self.title}"

    def to_json(self):
        return {"id": self.id, "title": self.title, "description": self.description}
