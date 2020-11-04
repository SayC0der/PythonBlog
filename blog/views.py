from django.shortcuts import render, get_object_or_404
from .models import getpost, categories
from django.core.paginator import Paginator
from .sitemaps import blogsitemap
# Create your views here.

sitemaps = {
        'blogposts': blogsitemap
    }

def test(request):
    return render(request, 'blog/testemp.html')

def landpage(request):
    return render(request, 'blog/land.html')

def homepage(request):
    model = categories.objects.all()
    context = {'cat': model}
    return render(request, 'blog/categories.html', context=context)

def article(request):
    model = getpost.objects.all()
    paginator = Paginator(model, 3)  # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'articles': page_obj}
    return render(request, 'blog/index.html', context=context)

def article_det(request, id):
    subject = get_object_or_404(getpost, pk=id)
    context = {'article': subject}
    return render(request, 'blog/article.html', context=context)

def filto(request, id):
    model = get_object_or_404(categories, pk=id)
    context = {'farticle': model}
    return render(request, 'blog/filt.html', context=context)
