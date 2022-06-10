from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout


def index(request):
    return render(request, 'webpages/index.html')


def about(request):
    context = {
        'title': 'About US',
    }
    return render(request, 'webpages/about.html', context=context)


def handler404(request, exception):
    context = {
        'error_no': 404,
        'error_detail': 'Page Not Found'
    }
    return render(request, 'webpages/404.html', context)


def handler500(request):
    context = {
        'error_no': 500,
        'error_detail': 'Server Error'
    }
    return render(request, 'webpages/404.html', context)


def handler400(request, exception):
    context = {
        'error_no': 400,
        'error_detail': 'Bad Request'
    }
    return render(request, 'webpages/404.html', context)


def handler403(request, exception):
    context = {
        'error_no': 403,
        'error_detail': 'Permission Denied'
    }
    return render(request, 'webpages/404.html', context)


def my_logout(request):
    logout(request)
    return redirect('home')


def about(request):
    context = {
        'title': 'About US',
    }
    return render(request, 'webpages/about.html', context=context)
