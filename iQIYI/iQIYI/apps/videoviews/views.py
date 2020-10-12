from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.core.paginator import Paginator
from indexs.models import VideoModel
import random
from indexs.models import ClassificationModel

from indexs.models import MovieDelailModel


class VideoView(View):
    def get(self, request, view_id):
        try:
            video_delail = MovieDelailModel.objects.get(video_id=view_id)
        except:
            video_delail = ''
        try:
            video = VideoModel.objects.get(id=view_id)
            categroy = ClassificationModel.objects.filter(video=view_id)
            categroy = [i.categroy for i in categroy]
            reco = ClassificationModel.objects.filter(categroy__in=categroy)
            reco_video = [res.video for res in reco]
            video_order = VideoModel.objects.all().order_by("-activate")[:8]#7376-1

        except Exception as e:
            return http.HttpResponseNotFound(e)
        page = Paginator(reco_video,10)
        pagesize = page.num_pages
        intpage = random.randint(0,pagesize)
        reco_video = [] if intpage==0 else page.page(intpage)


        context = {
            "video":video,
            "categroy":categroy,
            "reco_video":reco_video,
            "video_order":video_order,
            "video_delail":video_delail,
        }
        return render(request, "views.html",context=context)