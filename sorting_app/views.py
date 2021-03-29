from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import PostForm, GenerateForm
from .models import Post
from .utilits import *


def response_info(request):
    all_results = Post.objects.order_by('-id')
    return render(request, 'sorting_app/result.html', {'results': all_results[:5]})


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
            form.start_list = start_list
            form.title = request.FILES['file']
            form.save()
            algorithm_type = alg_types[form.algorithm_type]
            context = {
                'results': [Post.objects.last()],
                'algorithm_type': algorithm_type,

            }
            return render(request, 'sorting_app/result.html', context)
    else:
        form = PostForm()
    return render(request, 'sorting_app/post.html', {'form': form})
