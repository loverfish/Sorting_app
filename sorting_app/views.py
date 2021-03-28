import os
from django.shortcuts import render, redirect
from django.urls import reverse

from intetics.settings import BASE_DIR
from .utilits import *
from .forms import PostForm, GenerateForm
from .models import Post


def handle_uploaded_file(f):
    with open(os.path.join(BASE_DIR, 'media/temp/new_f.txt'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


# def upload_file(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form = form.save(commit=False)
#             handle_uploaded_file(request.FILES['file'])                             # form.file
#             start_list = read_file(os.path.join(BASE_DIR, 'media/temp/new_f.txt'))
#             result = algorithms[form.algorithm_type](start_list)
#             form.sorted_list = result[0]
#             form.time_to_sort = result[1]
#             form.save()
#             algorithm_type = alg_types[form.algorithm_type]
#             context = {
#                 'info': Post.objects.last(),
#                 'start_list': read_file(os.path.join(BASE_DIR, 'media/temp/new_f.txt')),
#                 'start_name': request.FILES['file'],
#                 'algorithm_type': algorithm_type,
#
#             }
#             return render(request, 'sorting_app/result.html', context)
#     else:
#         form = PostForm()
#     return render(request, 'sorting_app/post.html', {'form': form})


def response_info(request):
    resp = Post.objects.last()
    return render(request, 'sorting_app/result.html', {'info': resp})


def generate_file(request):
    if request.method == 'POST':
        form = GenerateForm(request.POST)
        if form.is_valid():
            create_file(request.POST['title'] + '.txt', int(form.cleaned_data['quantity']))
            return redirect(reverse('upload_file'))
    else:
        form = GenerateForm()
    return render(request, 'sorting_app/generate_file.html', {'form': form})


def upload_file_class(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            handle_uploaded_file(request.FILES['file'])                             # form.file
            start_list = read_file(os.path.join(BASE_DIR, 'media/temp/new_f.txt'))
            array = start_list.copy()
            result = algorithms_class[form.algorithm_type]().sort(array)
            form.sorted_list = result[0]
            form.time_to_sort = result[1]
            form.save()
            algorithm_type = alg_types[form.algorithm_type]
            context = {
                'info': Post.objects.last(),
                'start_list': start_list,
                'start_name': request.FILES['file'],
                'algorithm_type': algorithm_type,

            }
            return render(request, 'sorting_app/result.html', context)
    else:
        form = PostForm()
    return render(request, 'sorting_app/post.html', {'form': form})
