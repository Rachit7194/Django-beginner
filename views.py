from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
import os

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets, generics

class HomePageView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "base.html"


class ListVideosView(ListView):
    context_object_name = "myvideoslist"
    template_name = "listVideos.html"

    def get_queryset(self):
        return [item for item in os.listdir("/Users/panther/Desktop/myvideos")]


class DetailsofVideoView(DetailView):
    print("details page")
    template_name = "myvideodetails.html"

    def get(self, request, *args, **kwargs):
        print("IN DETAILS:......")
        print(self.kwargs.get("name"))
    # def get_queryset(self):

# def DetailsofVideoView(request, *args, **kwargs):

