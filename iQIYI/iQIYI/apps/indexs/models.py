from django.db import models

# Create your models here.
class CategroyModel(models.Model):#种类表
    # id = models.IntegerField(max_length=100, primary_key=True, auto_created=True, verbose_name="类别id")
    name = models.CharField(max_length=100, verbose_name="类别名")
    categroy = models.ForeignKey("self", max_length=100, null=True, related_name='subs', verbose_name="类别上级")

    class Meta:
        db_table = 'categroyMovieTable'

class VideoModel(models.Model):#视频表
    name = models.CharField(max_length=100, null=True, verbose_name="视频名字")
    time = models.CharField(max_length=100, null=True, verbose_name="电影播放长度")
    url = models.CharField(max_length=500, null=True, verbose_name="视频地址表")
    imagepath = models.CharField(max_length=2000, null=True, verbose_name="图片地址")
    saveimagepath = models.CharField(max_length=500, null=True, verbose_name="图片保存地址")
    score = models.FloatField(max_length=10, null=True, verbose_name="评分")
    secorews = models.IntegerField(default=1314,verbose_name="评分人数")
    status = models.IntegerField(max_length=10, null=True, verbose_name="状态")
    categroy = models.ForeignKey(CategroyModel,verbose_name="类型")
    activate = models.IntegerField(default=1, verbose_name="观看量")

    class Meta:
        db_table = "tb_video"

class ClassificationModel(models.Model):
    video = models.ForeignKey(VideoModel, max_length=100, verbose_name="视频")
    categroy = models.ForeignKey(CategroyModel, max_length=100, verbose_name="视频分类")

    class Meta:
        db_table = "tb_classificat"

class MovieDelailModel(models.Model):
    name = models.CharField(max_length=100, null=True, verbose_name="主演")
    refer = models.CharField(max_length=500, null=True)
    categroy = models.CharField(max_length=500, null=True)
    des = models.CharField(max_length=3000, null=True)
    video = models.ForeignKey(VideoModel)

    class Meta:
        db_table = "tb_moviedetailtable"


