from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.utils import timezone
from myblog.models import Post
from myblog.forms import PostForm


def list_view(request):
    published = Post.objects.exclude(published_date__exact=None)
    posts = published.order_by('-published_date')
    context = {'posts': posts}

    return render(request, 'list.html', context)


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post}

    return render(request, 'detail.html', context)


def add_view(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.published_date = timezone.now()
            model_instance.save()
            return redirect('/')

    else:

        form = PostForm()

        return render(request, 'add_post.html', {'form': form})


