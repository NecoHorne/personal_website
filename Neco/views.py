from django.shortcuts import render, redirect, render_to_response
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse

from Neco.models import Post
from .forms import ContactForm
from django.template import RequestContext


# Create your views here.

def index(request):
    return render(request, 'Neco/index.html')


def about(request):
    return render(request, 'Neco/about.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(contact_name,
                                     content,
                                     contact_email,
                                     ['necohorne@gmail.com'],
                                     reply_to=[contact_email],
                                     )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('/thanks')
    return render(request, 'Neco/contact.html', {'form': form})


def thanks(request):
    return render(request, 'Neco/thanks.html')


def education(request):
    return render(request, 'Neco/education.html')


def work(request):
    return render(request, 'Neco/work.html')


def portfolio(request):
    posts = Post.objects.order_by('-created_at').all()[:10]

    context = {
        'posts': posts
    }

    return render(request, 'Neco/portfolio.html', context)


def handler404(request):
    return render(request, '404.html', {}, status=404)


def handler500(request):
    return render(request, '500.html', {}, status=500)