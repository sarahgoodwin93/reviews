from django import forms
from .models import SwimPosts, Review
from datetime import date

class ReviewForm(forms.ModelForm):
    """
    FORM: Review.
    """

    class Meta:
        model = Review
        fields = ['review_title', 'review_location', 'body']


class EditReviewForm(forms.ModelForm):
    """
    FORM: Edit Review.
    """

    class Meta:
        model = Review
        fields = ['review_title', 'review_location', 'body']