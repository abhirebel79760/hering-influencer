from django.shortcuts import render, redirect
from . models import Hiretuber
from django.contrib import messages
# Create your views here.

#first_name = models.models.CharField(max_length=50)
#last_name = models.CharField(max_length=50)
#tuber_id = models.IntegerField()
#tuber_name = models.CharField(max_length=50)
#city = models.CharField(max_length=50)
#phone = models.CharField(max_length=50)
#state = models.CharField(max_length=50)
# message = models.TextField(bla)
#user_id = models.IntegerField(blank=True)


def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

        # todo: do all check

        hiretuber = Hiretuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name,
                              city=city, phone=phone, email=email, state=state, message=message, user_id=user_id)
        hiretuber.save()

    messages.success(request, 'thanku for reaching out')
    return redirect('youtubers')
