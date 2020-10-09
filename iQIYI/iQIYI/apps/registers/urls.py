from django.conf.urls import url, include
# from django.contrib import admin
from . import views
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.ResterView.as_view(),name="resters"),
    url(r'^regsterdelail/(?P<pass_id>.+)', views.RestView.as_view()),
    url(r'^code_name/$', views.CodeView.as_view()),
    url(r'^code_mblie/$', views.CodeemdilView.as_view())
]
