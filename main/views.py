from django.shortcuts import render
import datetime

# Create your views here.
def about_us(request):
    return render(request, 'about_us.html')

def date_now(request):
    date = datetime.datetime.now()
    context = {
        'date': date
    }
    return render(request, 'date_now.html', context)