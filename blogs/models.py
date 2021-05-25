from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    
    class Meta:
        verbose_name = verbose_name_plural = '分类'
    
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, '正常'),
        (STATUS_DELETE, '删除')
    )
    
    name = models.CharField(max_length=20, verbose_name='分类名称')
    status = models.PositiveSmallIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name='状态')
    is_nav = models.BooleanField(default=False, verbose_name='是否为导航')
    owner = models.ForeignKey(User, verbose_name='作者')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

