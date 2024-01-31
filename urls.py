from . import views
from django.urls import path
from .views import (ReviewView, ReviewList, EditReviewView, DeleteReviewView)


urlpatterns = [
    path("swim/review", ReviewView.as_view(), name="review"),
    path("swim/reviews", ReviewList.as_view(), name="review_list"),
    path("article/delete_review/<int:pk>/", DeleteReviewView.as_view(), name="delete_review"),  # noqa
    path("article/edit_review/<int:pk>/", EditReviewView.as_view(), name="edit_review"),  # noqa
]