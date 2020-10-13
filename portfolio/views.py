from django.shortcuts import render
import math

from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import timezone
from .forms import PostForm
from .forms import ContactForm

from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from .models import Post


def index(request):
    return render(request, 'html/index.html')

def modal(request):
    return render(request, 'html/modal.html')


def about(request):
    return render(request, 'html/about.html')


# def contact(request):
#    return render(request, 'contact.html')


def post(request):
    posts = Post.objects.all().order_by('-post_modifydate')
    paginator = Paginator(posts, 9)
    page = int(request.GET.get('page', 1))
    pages = paginator.get_page(page)
    page_range = 5  # 페이지 범위 지정 예 1, 2, 3, 4, 5 / 6, 7, 8, 9, 10
    current_block = math.ceil(int(page) / page_range)  # 해당 페이지가 몇번째 블럭인가
    start_block = (current_block - 1) * page_range
    end_block = start_block + page_range
    p_range = paginator.page_range[start_block:end_block]
    return render(request, 'html/post.html', {'posts': pages, 'p_range': p_range})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'html/post_detail.html', {'post': post})


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ksp6061@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "html/contact.html", {'form': form})