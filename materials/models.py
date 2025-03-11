from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    tutor = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

class Topic(models.Model):
    course = models.ForeignKey(Course, related_name='topics', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.course}"