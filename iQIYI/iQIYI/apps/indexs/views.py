from django.shortcuts import render
from django.core.paginator import Paginator
from django.views import View
from django import http
# Create your views here.
from indexs.models import CategroyModel

from indexs.models import VideoModel

from indexs.models import ClassificationModel


class IndexView(View):
    def get(self, request):
        group_id = request.GET.get("group_id") or 6
        orders_id = request.GET.get("orders_id") or 2
        page_num = request.GET.get("page_num") or 1
        classificat = request.GET.get("classificat")

        channels = CategroyModel.objects.filter(categroy__isnull=True)
        orderels = CategroyModel.objects.filter(categroy=2)

        channels_title = CategroyModel.objects.filter(categroy=int(group_id))
        chan_text = {che.name:che.subs.all() for che in channels_title}

        order_dict = {2:"-id",3:"-score",4:"-id"}
        if classificat:
            classificat = eval(classificat)
            if len(classificat)==1:
                classificat =(classificat,)

            videos = ClassificationModel.objects.filter(categroy__in=classificat).order_by(order_dict.get(int(orders_id)))
            videos = [vi.video for vi in videos]

        else:
            videos = VideoModel.objects.filter(categroy=int(group_id)).order_by(order_dict.get(int(orders_id)))

        count = len(videos)
        page = Paginator(videos,30)
        try:
            pagequery = page.page(int(page_num))
        except Exception as e:
            return http.HttpResponseNotFound(e)

        pagesize = page.num_pages

        context = {
                    "count":count,
                    "pagnum":page_num,
                    "pagequery":pagequery,
                    "pagesize":pagesize,
                    "orders_id":orders_id,
                    "group_id": group_id,
                    "channels":channels,
                   "orderels":orderels,
                   "chan_text":chan_text,
        }
        return render(request, "index.html",context=context)

