from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import SwimPosts, JoinSwim
from .forms import AddSwimForm, EditSwimForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView, View  # noqa
from django.contrib.auth.mixins import LoginRequiredMixin

class ReviewView(CreateView):
    """
    Allows users to add a reivew to the site. It calls the ReviewForm 
    When the form is submitted with valid data, the review is created.
    A success message is displayed to the user upon successful submission.
    """
    model = Review
    template_name = "home/review.html"
    form_class = ReviewForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "Thanks for adding a review")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('review_list')


class ReviewList(generic.ListView):
    """
    Shows the list of reviews to users by retrieving all review objects from 
    the database and then showin them on the 'home/review.html' template. The reviews 
    are ordered by their creation date ('created_on').
    """
    model = Review
    template_name = "home/review.html"
    ordering = "created_on"
    context_object_name = "reviews"
    queryset = Review.objects.all()

    def get_queryset(self):
        return Review.objects.all()


# Delete Review View
class DeleteReviewView(DeleteView):
    """
    Allows user who created the review to delete it from the site
    """
    model = Review
    template_name = "home/delete_review.html"
    success_url = reverse_lazy('review_list')

    def review_delete(self, request):
        messages.success(self, request, "Review has been deleted")
        return super().delete(request)


# Edit Review View
class EditReviewView(UpdateView):
    """
    Allows user who created the review to edit it
    """
    model = Review
    template_name = "home/edit_review.html"
    form_class = EditReviewForm
    success_url = reverse_lazy('review_list')

    def review_edit(self, request):
        messages.success(self, request, "Review has been updated")
        return response