from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea
from common.choices import Maturity


# 片断是内容的初始形态
class Doc(models.Model):
    title = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(verbose_name="内容", default="")
    author = models.ManyToManyField(User, verbose_name="作者")
    maturity = models.PositiveSmallIntegerField(
        default=Maturity.MATURITY_START,
        choices=Maturity.choices,
        verbose_name="阶段")
    version = models.IntegerField(verbose_name="版本", default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "片断"
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.title


class DocForm(ModelForm):
    class Meta:
        model = Doc
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-sm'}),
            'content': Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 5}),
        }
