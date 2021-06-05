from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea


# 片断是内容的初始形态
class Stage(models.Model):
    MATURITY_START = 1
    MATURITY_DRAFT = 2
    MATURITY_WRITING = 3
    MATURITY_REDACT = 4
    MATURITY_FINAL = 5
    MATURITY_ITEMS = (
        (MATURITY_START, '开始'),
        (MATURITY_DRAFT, '草稿'),
        (MATURITY_WRITING, '撰写'),
        (MATURITY_REDACT, '编辑校对'),
        (MATURITY_FINAL, '定稿'),
    )
    title = models.CharField(max_length=200, verbose_name="标题")
    content = models.TextField(verbose_name="内容", default="")
    author = models.ManyToManyField(User, verbose_name="作者")
    maturity = models.PositiveSmallIntegerField(
        default=MATURITY_START,
        choices=MATURITY_ITEMS,
        verbose_name="阶段")
    version = models.IntegerField(verbose_name="版本", default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "片断"
        ordering = ['-id']
    
    def __str__(self) -> str:
        return self.title


class StageForm(ModelForm):
    class Meta:
        model = Stage
        fields = ['title', 'content']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control form-control-sm'}),
            'content': Textarea(attrs={'class': 'form-control form-control-sm', 'rows': 5}),
        }
