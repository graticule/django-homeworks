from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type = request.GET.get('sort', None)
    phones = list(Phone.objects.all())
    if sort_type == 'name':
        phones = sorted(phones, key=lambda x: x.name)
    elif sort_type == 'min_price':
        phones = sorted(phones, key=lambda x: x.price)
    elif sort_type == 'max_price':
        phones = sorted(phones, key=lambda x: x.price, reverse=True)
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    if phone:
        phone = phone[0]
    context = {'phone': phone}
    return render(request, template, context)
