from django.contrib import admin
from django.core.exceptions import RequestAborted
from django.urls import reverse
from django.utils.html import format_html
from .adminforms import PostAdminForm

from blogs.adminforms import PostAdminForm
from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'created_time')
    fields =('name', 'status', 'is_nav')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


# 自定义过滤器只显示登录用户分类
class CateboryOwnerFilter(admin.SimpleListFilter):
    title = "分类过滤器"
    parameter_name = "owner_category"

    def lookups(self, request, model_admin) -> list[tuple[int, str]]:
        return Category.objects.filter(owner=request.user).values_list('id', 'name')
    
    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=self.value())
        return queryset


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title','category', 'owner', 'status', 'created_time', 'operator')
    list_display_links = []
    list_filter = [CateboryOwnerFilter] # 使用自定义过滤器
    search_fields = ['title', 'category__name']
    actions_on_top = True
    actions_on_bottom = True
    save_on_top = True
    fields = (
        ('title', 'category'),
        'desc',
        'status',
        'content',
        'tag',
    )
    filter_vertical = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blogs_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PostAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
