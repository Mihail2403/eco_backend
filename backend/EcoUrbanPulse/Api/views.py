from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .models import User, Complaint, News
import json

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try: 
            User.objects.get(login=data['username'])
        except:
            new_user = User.objects.create(
                login=data['username'],
                password=data['password'],
                permition_id_id=2
            )
            new_user.save()
            return JsonResponse({'status': 'good', 'user_id': new_user.id, 'user_name': new_user.login})
        
        return JsonResponse({'status': 'bad', 'message': 'User already registered'})
        

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
    try:
        old_user = User.objects.get(login=data['username'], password=data['password'])
        return JsonResponse(
                {
                    'status': 'good', 
                    'user_id': old_user.id,
                    'user_name': old_user.login
                }
            )
    except:
        return JsonResponse({'status': 'bad', 'message': 'User is not in db'})
    


@csrf_exempt
def auth_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try: 
            user_id = data['id']
            try:
                current_user= User.objects.get(id=user_id)
                return JsonResponse({'user_id': current_user.pk, 'user_name': current_user.login})
            except:
                return JsonResponse({'status': "bad"})
        except:
            return JsonResponse({'status': 'bad'})


@csrf_exempt
def get_complaint(request):
    list_data = []
    if request.method == 'POST':
        response_data = Complaint.objects.all()
        for resp_elem in response_data:
            list_data += {
                'cords': resp_elem.cords,
                'rate': resp_elem.rate,
                'text': resp_elem.text,
                'photo_path': resp_elem.photo,
                'ser_ud': resp_elem.user_id,
                'final_eval': resp_elem,
            }
        return JsonResponse({'data': list_data})


@csrf_exempt
def get_news(request):
    result = []
    if request.method == 'POST':
        news = News.objects.all()
        for new in news:
            result.append(
                {
                    'title': new.title,
                    'discription': new.discription,
                    'adress': new.adress
                }
            )
        return JsonResponse({'data': result})
            
@csrf_exempt
def addComplain(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            new_complain = Complaint.objects.create(
                user_id = User.objects.get(id=data['user_id']),
                cords = data['cords'],
                rate = 3,
                address = data['address']
            )
            new_complain.save()
            return JsonResponse({'status': 'good'})
        except:
            return JsonResponse({'status': 'bad'})