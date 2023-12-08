from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import json
from django.contrib.auth import logout as auth_logout


@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Check if the user is an admin
            is_admin = user.is_staff and user.is_superuser

            # Prepare the response data
            response_data = {
                "username": user.username,
                "status": True,
                "message": "Login successful!",
                "is_admin": is_admin  # Include the admin status in the response
                # Add more data as needed
            }

            return JsonResponse(response_data, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, the account is inactive."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, check the username or password."
        }, status=401)

@csrf_exempt
def register(request):
    try:
        data = json.loads(request.body)

        username = data.get("username")
        password1 = data.get("password1")
        password2 = data.get("password2")
        is_admin = data.get("is_admin", False)  # Defaulting to False if not provided

        if not (username and password1 and password2):
            return JsonResponse({'status': 'failed', 'message': 'Incomplete data provided'})

        if password1 != password2:
            return JsonResponse({'status': 'failed', 'message': 'Passwords do not match'})

        new_user = User.objects.create_user(username=username, password=password1)
        
        # Check and set admin role
        if is_admin:
            new_user.is_staff = True
            new_user.is_superuser = True  # Optional for full admin privileges
            new_user.save()

        return JsonResponse({"status": "success"}, status=200)
    except Exception as e:
        print(e)
        return JsonResponse({"status": "error"}, status=401)
    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)
    