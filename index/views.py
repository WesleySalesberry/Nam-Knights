from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

from index.models import AssistanceRequest, MembershipRequest

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about.html')

def request_assistance(request):
    return render(request, 'forms/assistance.html')

# @csrf_exempt  # use if CSRF token not passed (prefer avoiding this!)
def submit_assistance_request(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            AssistanceRequest.objects.create(
                name=data['name'],
                email=data['email'],
                phone_number=data['phone_number'],
                street_address=data['street_address'],
                city=data['city'],
                state=data['state'],
                zip_code=data['zip_code'],
                assistance_description=data.get('assistance_description', ''),
                comment=data.get('comment', '')
            )
            return JsonResponse({'message': 'Success'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

def request_to_join(request):
    return render(request, 'forms/join.html')


def submit_membership_request(request):
    if request.method == "POST":
        data = json.loads(request.body)
        try:
            MembershipRequest.objects.create(
                name=data['name'],
                email=data['email'],
                phone=data['phone'],
                street_address=data['street_address'],
                city=data['city'],
                state=data['state'],
                zip_code=data['zip_code'],
                motorcycle_make=data['motorcycle_make'],
                motorcycle_model=data['motorcycle_model'],
                military_service=data['military_service'],
                military_branch=data.get('military_branch', ''),
                comment=data.get('comment', '')
            )
            return JsonResponse({"message": "Success"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=405)