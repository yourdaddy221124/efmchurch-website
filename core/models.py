from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Media(models.Model):
    MEDIA_TYPES = (
        ('photo', 'Photo'),
        ('video', 'Video'),
    )
    title = models.CharField(max_length=200)
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='photo')
    file = models.FileField(upload_to='media/', null=True, blank=True)
    url = models.URLField(null=True, blank=True, help_text="For YouTube/Vimeo links")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Update(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PrayerRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Received'),
        ('praying', 'Praying in Progress'),
        ('answered', 'Answered'),
    )
    name = models.CharField(max_length=100, default='Anonymous')
    category = models.CharField(max_length=50, default='Other')
    request = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.status}"
