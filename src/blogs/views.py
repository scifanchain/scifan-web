from django.shortcuts import render, get_object_or_404
from .models import Category, Post
import markdown


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    context.update(Category.get_navs())  # 获取导航
    return render(request, 'blogs/list.html', context=context)

def lists(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.lastes_posts()

    context = {
        'category': category,
        'tag':tag,
        'post_list': post_list,
    }
    context.update(Category.get_navs()) #获取导航

    return render(request, 'blogs/list.html', context=context)

def detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.content = markdown.markdown(post.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',  # 语法高亮拓展
        'markdown.extensions.toc'  # 自动生成目录
    ])  # 修改blog.content内容为html
    return render(request, 'blogs/detail.html', {'post':post})
