import os
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from .utilits import *
from intetics.settings import BASE_DIR
from .forms import PostForm
from .models import Post


def index(request):
    file_name = Post.objects.last().__str__()
    file = os.path.join(BASE_DIR, 'media/', file_name)
    start_list = read_file(file)

    res = algorithms[Post.objects.last().algorithm_type](start_list)
    sort_list = res[0]
    time_to_sort = res[1]
    context = {
        'start_list': read_file(file),
        'sort_list': sort_list,
        'time_to_sort': time_to_sort,
        'post': file_name[6:],
        'type': algorithms[Post.objects.last().algorithm_type].__name__,
    }
    return render(request, template_name='sorting_app/home.html', context=context)


class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'sorting_app/post.html'
    success_url = reverse_lazy('home')


def handle_uploaded_file(f):
    with open(os.path.join(BASE_DIR, 'media/temp/new_f.txt'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    # return read_file(destination)


def upload_file(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            form = form.save(commit=False)
            handle_uploaded_file(request.FILES['file'])                             # form.file
            start_list = read_file(os.path.join(BASE_DIR, 'media/temp/new_f.txt'))

            result = algorithms[form.algorithm_type](start_list)
            form.sorted_list = result[0]
            form.time_to_sort = result[1]
            form.save()
            # return redirect(reverse('home'))
            context = {

            }
            return render(request, 'sorting_app/result.html', {'info': Post.objects.last()})
    else:
        form = PostForm()
    return render(request, 'sorting_app/post.html', {'form': form})


def response_info(request):
    resp = Post.objects.last()
    return render(request, 'sorting_app/result.html', {'info': resp})

