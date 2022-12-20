from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from shop.models import *
from shop.forms import *

# home 
def home(request):
    # get request for car
    cars = Car.objects.filter(sold_out=0)
    feedbacks = Feedback.objects.all()

    paginator = Paginator(cars, 3)
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number)
    totalpage = page_obj.paginator.num_pages

    context = { 'car': page_obj, 
                'lastpage': totalpage,
                'totalpagelist': [n+1 for n in range(totalpage)],
                'feedbacks': feedbacks
            }

    # print(context)


    # Inquiry Form 
    if request.method == 'POST' and request.POST.get('inq_text', '') != '':
        if request.user.is_authenticated:
            inq = UserInquiry(request.POST) 
            if inq.is_valid():
                    instance = inq.save(commit=False)
                    instance.user_id = request.user
                    instance.save()
                    messages.success(request, 'We have got your query. will you connect soon!')
                    return redirect('home')
            else:
                messages.warning(request, 'plz, enter correct detials')
        else:
            return redirect('login')
            
        return redirect('home')


    # Post request for car search
    if request.method == 'POST' and request.POST.get('search', '') != '':
        print('post')
        search = request.POST['search']

        data = Car.objects.filter(car_name__icontains=search, sold_out=0)
        paginator = Paginator(data, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        totalpage = page_obj.paginator.num_pages

        context = { 'car': page_obj, 
                    'lastpage': totalpage,
                    'totalpagelist': [n+1 for n in range(totalpage)],
                    'feedbacks': feedbacks
                }

        # print(context)
    
    return render(request, 'home.html', context)

# 404 page
def error_404_view(request, exception):
    return render(request, '_404.html')