from django.conf.urls import url, include
# from django.contrib import admin
from . import views
urlpatterns = [url(r"^views/(?P<view_id>\d+)/$", views.VideoView.as_view(), name="view"),
               ]