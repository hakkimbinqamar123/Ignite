from django.shortcuts import render, redirect
import stripe
from ignite.models import *
from django.contrib.auth.models import User, auth 
import stripe
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404




def home(request):
    return render(request, 'home.html')

def base(request):
    return render(request, 'base.html')

from django.db.models import Max

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        college = request.POST['college']
        id_card = request.FILES.get('id_card')
        event_ids = request.POST.getlist('event_ids')  # Use getlist() to retrieve multiple selected event IDs

        candidate_id = Student.objects.aggregate(Max('candidate_id'))['candidate_id__max']
        candidate_id = 1 if candidate_id is None else candidate_id + 1

        student = Student(
            candidate_id=candidate_id,
            username=username,
            email=email,
            phone=phone,
            password=password,
            college=college,
            id_card=id_card
        )

        if Student.objects.filter(email=email).exists():
            msg = {'msg1': 'Username already exists'}
            return render(request, 'registration.html', msg)
        else:
            student.save()
            student.events.set(event_ids)  # Associate the selected events with the student

        events = Event.objects.all()
        msg = 'Student registered successfully'
        return render(request, 'registration.html', {'msg': msg, 'events': events})
    else:
        events = Event.objects.all()
        return render(request, 'registration.html', {'events': events})


def result_upload(request):
    if request.method == 'POST':
        j_id=request.session['j_id']
        event_id = request.POST.get('event_id')
        event=Event.objects.get(event_id=event_id)
        candidate_id = request.POST.get('candidate_id')

        position = request.POST.get('position')
        grade = request.POST.get('grade')
        judge = Judge.objects.get(j_id=j_id)
        # up_result = Result.objects.get(event_id=event_id)
        R = Result(event_id=event, candidate_id=candidate_id, position=position, grade=grade,j_id=judge)
        R.save()
        msg='Result Uploaded Succesfully!'
        up_result =Event.objects.all()
        all={'msg':msg,'up_result':up_result}
        return render(request, 'result_upload.html',all)
    else:
        up_result =Event.objects.all()
        return render(request, 'result_upload.html', {'up_result': up_result})


def events(request):
    details = Event.objects.all()
    return render(request, 'events.html', {'details':details })


def product_details(request):
    return render(request, 'product-details.html')

def stud_prod_details(request):
    return render(request, 'stud_prod_details.html')



def stud_base(request):
    return render(request, 'stud_base.html')

def stud_events(request):
    details = Event.objects.all()
    return render(request, 'stud_events.html', {'details':details })

def stud_results(request):
    details = Event.objects.all()
    return render(request, 'stud_results.html', {'details':details })

def stud_results1(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    r = Result.objects.filter(event_id=event)
    candidate_ids = [result.candidate_id for result in r]
    students = Student.objects.filter(candidate_id__in=candidate_ids)
    context = {'r': r, 'students': students, 'event': event}
    return render(request, 'stud_results1.html', context)




def stud_home(request):
    events = Event.objects.all()
    return render(request, 'stud_home.html', {'events': events})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        student = Student.objects.filter(email = email, password = password)
        judge=Judge.objects.filter(email = email, password = password)
        if student.filter(email = email, password = password).exists():
            for i in student:
                id = i.candidate_id
                request.session['candidate_id'] = id
                request.session['email'] = email
            return render(request, 'stud_home.html', )
        elif judge.filter(email = email, password = password).exists():
            for i in judge:
                j_id = i.j_id
               
                request.session['j_id'] = j_id
                request.session['email'] = email
                
            return render(request, 'judgehome.html', )            
        else:
            msg = 'invalid details'
            return render(request, 'login.html', {'msg':msg})
    return render(request, 'login.html')


def schedule(request):
     details = Event.objects.all()
    
     return render(request, 'schedule.html', {'details':details })


def results1(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    r = Result.objects.filter(event_id=event)
    candidate_ids = [result.candidate_id for result in r]
    students = Student.objects.filter(candidate_id__in=candidate_ids)
    context = {'r': r, 'students': students, 'event': event}
    return render(request, 'results1.html', context)



def results(request):
    details = Event.objects.all()
    return render(request, 'results.html', {'details':details })

def product_details(request,event_id):
   a = Event.objects.filter(event_id=event_id)
   return render(request, "product-details.html", {"a": a})

def stud_prod_details(request,event_id):
    b = Event.objects.filter(event_id=event_id)
    return render(request, "stud_prod_details.html", {"b": b})

def judgehome(request):
    return render(request, 'judgehome.html')

def contact(request):
    return render(request, 'contact.html')


    
    
def payment(request):
    event =  request.session['event_id'] 
    s_event = select_event.objects.filter(id=event)
    context = {'events': s_event}
    return render(request, 'payment.html', context)

import os
import stripe   

stripe.api_key = 'sk_test_51N3dNsSDXvHpuYeFhuGTdvMBDfPCTq4FO7TOxZyFfIYLpmyivp48GK3ygxcALJHcZlohtXQPc0WosuPo4WTVQxGK001Holj1nk' 
def confirm_payment(request):
    id =  request.session['event_id'] 
    cart_obj = select_event.objects.get(id=id)
    price = 200

    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'inr',
                'product_data': {
                    'name': cart_obj.event_name,
                },
                'unit_amount': price*100,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/pay_success',
        cancel_url='http://127.0.0.1:8000/pay_failure',
    )
     
    return redirect(session.url, code=303)


def stud_profile(request):
    candidate_id=request.session['candidate_id']
    stud = Student.objects.filter(candidate_id=candidate_id)
    events = Event.objects.all()
    return render(request, "stud_profile.html", {"stud": stud, "events":events})

def edit_stud_profile(request):
        if request.method == 'POST':
            candidate_id = request.session['candidate_id']
            events = Event.objects.all()
            up = Student.objects.get(candidate_id=int(candidate_id))

            username = request.POST.get('username')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            password = request.POST.get('password')
            college = request.POST.get('college')
           


            up.username = username
            up.phone = phone
            up.email = email
            up.password = password
            up.college = college
            up.save()
            stud=Student.objects.filter(candidate_id=int(candidate_id))
            context = {'msg': 'Student Details Updated','up':up,'stud':stud}
            return render(request, 'stud_profile.html',context)

        else:
            candidate_id = request.session['candidate_id']
            stud=Student.objects.filter(candidate_id=int(candidate_id))
            up = Student.objects.get(candidate_id=int(candidate_id))
            context={'up':up,'stud':stud}
            return render(request, 'edit_stud_profile.html',context)
        


def judge_base(request):
    return render(request, 'judge_base.html')

def judge_prod_details(request,event_id):
    b = Event.objects.filter(event_id=event_id)
    return render(request, "stud_prod_details.html", {"b": b})

def judge_profile(request):
    j_id=request.session['j_id']
    jud = Judge.objects.filter(j_id=j_id)
    return render(request, "judge_profile.html", {"jud": jud})

def edit_judge_profile(request):
    if request.method == 'POST':
            j_id = request.session['j_id']
            events = Event.objects.all()
            up = Judge.objects.get(j_id=int(j_id))

            username = request.POST.get('username')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            password = request.POST.get('password')
            qualification = request.POST.get('qualification')
            event = request.POST.get('events')


            up.username = username
            up.phone = phone
            up.email = email
            up.password = password
            up.qualification = qualification
            up.event = event
            up.save()
            jud=Judge.objects.filter(j_id=int(j_id))
            context = {'msg': 'Judge Details Updated','up':up,'jud':jud}
            return render(request, 'judge_profile.html',context)

    else:
            j_id = request.session['j_id']
            jud=Judge.objects.filter(j_id=int(j_id))
            up = Judge.objects.get(j_id=int(j_id))
            context={'up':up,'jud':jud}
            return render(request, 'edit_judge_profile.html',context)

def judge_results(request):
    details = Event.objects.all()
    return render(request, 'judge_results.html', {'details':details })

def judge_results1(request, event_id):
    event = get_object_or_404(Event, event_id=event_id)
    r = Result.objects.filter(event_id=event)
    candidate_ids = [result.candidate_id for result in r]
    students = Student.objects.filter(candidate_id__in=candidate_ids)
    context = {'r': r, 'students': students, 'event': event}
    return render(request, 'stud_results1.html', context)

def judge_events(request):
    details = Event.objects.all()
    return render(request, 'stud_events.html', {'details':details })

def logout_view(request):
    logout(request)
    return redirect('/')



def create_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            user = request.user
            notification = Notification(user=user, message=message)
            notification.save()
            return redirect('notification_list')  # Redirect to notification list view
    else:
        form = NotificationForm()
    
    return render(request, 'create_notification.html', {'form': form})

def notification_list(request):
    user = request.user
    notifications = Notification.objects.filter(user=user).order_by('-created_at')
    return render(request, 'notification_list.html', {'notifications': notifications})

def stud_home(request):
    notifications = Notification.objects.all()  # Fetch all notifications
    return render(request, 'stud_home.html', {'notifications': notifications})


