from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from common.choices import Status, Maturity, StoryType
from simple_history.models import HistoricalRecords
from django.forms import ModelForm, TextInput, Textarea


class Stage(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    content = models.TextField(verbose_name="内容", default="")
    author = models.ManyToManyField(User, verbose_name="作者")
    maturity = models.PositiveSmallIntegerField(
        default=Maturity.MATURITY_START,
        choices=Maturity.choices,
        verbose_name="阶段")
    status = models.PositiveSmallIntegerField(
        default=Status.STATUS_NORMAL,
        choices=Status.choices,
        verbose_name="状态")
    type = models.PositiveSmallIntegerField(
        default=StoryType.EVENT,
        choices=StoryType.choices,
        verbose_name="类型"
    )
    version = models.IntegerField(verbose_name="版本", default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="最近修改时间")
    history = HistoricalRecords(
        excluded_fields=['created_time', 'updated_time'])

    class Meta:
        verbose_name = verbose_name_plural = "故事"
        ordering = ['-id']

    def __str__(self) -> str:
        return self.name


class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-sm', }),
            'content': Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 5, }),
        }


class Era(models.Model):
    cycle = models.PositiveSmallIntegerField(verbose_name='纪周')
    veins = models.PositiveSmallIntegerField(verbose_name='纪脉')
    point = models.PositiveSmallIntegerField(verbose_name='纪点')
    dimen = models.PositiveSmallIntegerField(verbose_name='纪维')
    version = models.IntegerField(verbose_name="版本", default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    history = HistoricalRecords()

    class Meta:
        verbose_name = verbose_name_plural = "纪元"
