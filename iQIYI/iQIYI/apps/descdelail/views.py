from django import http
from django.shortcuts import render

# Create your views here.
from django.views import View

from descdelail.models import PerformerDetailModel

from descdelail.seriailser import DescSerialiser


class DescdelailModel(View):
    def get(self, request):

        descid = request.GET.get("name")
        if not descid:
            return http.HttpResponseNotFound("页面无郊")

        try:
            query = PerformerDetailModel.objects.get(name=descid)
        except Exception as e:
            return http.HttpResponseNotFound("页面无郊")
            print("ERRER:", e)
        # query = DescSerialiser(query)
        context = {
            "actor":query,
        }

        return render(request, "actor.html",context=context)