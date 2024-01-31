from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone


class Review(models.Model):
    """
    The revivew model stores information about a review,
    including the user who wrote it, the review title, location,
    body, and timestamps.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviewer")
    review_title = models.CharField(max_length=200, default="New Review")
    review_location = models.CharField(max_length=300, default="Where did you swim?")  # noqa
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review {self.body} by {self.user}"