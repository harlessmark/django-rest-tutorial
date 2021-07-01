from django.db import models

class Journalist(models.Model):
    name = models.CharField(max_length=50)

    # blank=True means an empty string is acceptable
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")
    title = models.CharField(max_length=50)
    descriptions = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)

    # auto_now_add adds date and time when instance is created
    created_at = models.DateTimeField(auto_now_add=True)

    # auto_now sets date and time when instance is updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.author } { self.title }"
