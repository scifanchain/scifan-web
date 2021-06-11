from django.db import models
from django.contrib.auth.models import User
from common.choices import Status, Maturity
from simple_history.models import HistoricalRecords


class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name="标题")
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
    version = models.IntegerField(verbose_name="版本", default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    history = HistoricalRecords()

    class Meta:
        verbose_name = verbose_name_plural = "人物"
        ordering = ['-id']

    def __str__(self) -> str:
        return self.name


class Place(models.Model):
    name = models.CharField(verbose_name='名称', max_length=100)
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
    version = models.IntegerField(verbose_name="版本", default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now_add=True, verbose_name="修改时间")
    history = HistoricalRecords()

    class Meta:
        verbose_name = verbose_name_plural = "地点"
        ordering = ['-id']

    def __str__(self) -> str:
        return self.name


class Era(models.Model):
    cycle = models.PositiveSmallIntegerField(verbose_name='纪周')
    veins = models.PositiveSmallIntegerField(verbose_name='纪脉')
    point = models.PositiveSmallIntegerField(verbose_name='纪点')
    dimen = models.PositiveSmallIntegerField(verbose_name='纪维')

    class Meta:
        verbose_name = verbose_name_plural = "纪元"
