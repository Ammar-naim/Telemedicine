from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import *
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
import base64
from django.core.files.base import ContentFile
from datetime import datetime

@csrf_exempt		
def registerDoctor(request):
  body = request.body.decode('utf-8')
  body=json.loads(body)
  email=body['email']
  username=body['username']
  first_name=body['first_name']
  last_name=body['last_name']
  father_name=body['father_name']
  country=body['country']
  city=body['city']
  password=body['password']
  age=body['age']
  address=body['address']
  profile_photo=body['profile_photo']
  profile_photo_data = ContentFile(base64.b64decode(profile_photo), name='i.jpg')
  cover_photo=body['cover_photo']
  cover_photo_data = ContentFile(base64.b64decode(cover_photo), name='i.jpg')
  phone=body['phone']
  whats_phone=body['whats_phone']
  points=10000
  
  gender=body['gender']
  marital_status=body['marital_status']
  children_number=body['children_number']
  current_work=body['current_work']
  previous_work=body['previous_work']
  current_address=body['current_address']
  previous_address=body['previous_address']
  weight=body['weight']
  height=body['height']
  is_smoker=body['is_smoker']  
  cigaretes_number = body['cigaretes_number']  
  alcoholic = body['alcoholic']  
  Hookah = body['Hookah']  
  is_sensitive_from_medicine=body['is_sensitive_from_medicine']  
  sensitivy_medicines=body['sensitivy_medicines']  
  is_sensitive_from_bugs=body['is_sensitive_from_bugs']  
  is_sensitive_from_illnesses=body['is_sensitive_from_illnesses']  
  sensitivity_illnesses_names=body['sensitivity_illnesses_names'] 
  sugar=body['sugar']
  pressure=body['pressure']
  heart=body['heart'] 
  corona=body['corona'] 
  smallpox=body['smallpox'] 
  other_previous_illnesses=body['other_previous_illnesses'] 
  tonsils=body['tonsils'] 
  appendix=body['appendix'] 
  bitterness=body['bitterness'] 
  other_previous_surgeries=body['other_previous_surgeries']
  blood_type=body['blood_type'] 
  blood_donation_number=body['blood_donation_number'] 
  blood_getting_number=body['blood_getting_number'] 
  analysis_names=body['analysis_names'] 
  family_diseases=body['family_diseases']
  previous_medicenes=body['previous_medicenes']
  current_medicines=body['current_medicines']
  analysis_names=body['current_medicines']
  analysis_names_images=body['analysis_names_images']#null
  X_Ray_Images=body['X_Ray_Images']#null
  cv=models.CharField(max_length=20,null=True)
  university=models.CharField(max_length=20,null=True)
  college_id=body['college_id']
  college=College.objects.get(id=college_id)
  specialty_id= body['specialty_id'] 
  specialty=Specialty.objects.get(id=specialty_id)
  graduation_year=models.CharField(max_length=20,null=True)
  doctor_days=body['doctor_days']#list 
  doctor_languages=body['doctor_languages']#list for
  doctor_jobs=body['doctor_jobs']#list for
  doctor_certificate=body['doctor_certificate']#list for
  
  try:
    d=Doctor(email=email,username=username,first_name=first_name,last_name=last_name,father_name=father_name,country=country,city=city,password=password,age=eage,address=address,profile_photo=profile_photo_data,cover_photo=cover_photo_data,phone=phone,whats_phone=whats_phone,points=points,specialty=specialty,college=college)
    d.save()
  for im in analysis_names_images:
	  image_data = ContentFile(base64.b64decode(im), name='i.jpg')
	  cm=MedicalAnalysisImages(agent=d,image=image_data)
	  cm.save()
  for im in X_Ray_Images:
	  image_data = ContentFile(base64.b64decode(im), name='i.jpg')
	  cm=XRayImages(agent=d,image=image_data)
	  cm.save()
  for day_obj in doctor_days:
    day=day_obj['day'] 
    period_start_am=day_obj['period_start_am']
    period_end_am=day_obj['period_end_am']
    period_start_pm=day_obj['period_start_pm']
    period_end_pm=day_obj['period_end_pm']
    o=DoctorDays(doctor=d,day=day,period_start_am=period_start_am,period_end_am=period_end_am,period_start_pm=period_start_pm,period_end_pm=period_end_pm)
    o.save()
	#3 for
    return JsonResponse({'res':'ok'})
  except Exception as e:
    print(e)
    return JsonResponse({'res':'error'})

@csrf_exempt		
def registerPharma(request):
  body = request.body.decode('utf-8')
  body=json.loads(body)
  email=body['email']
  username=body['username']
  first_name=body['first_name']
  last_name=body['last_name']
  father_name=body['father_name']
  country=body['country']
  city=body['city']
  password=body['password']
  age=body['age']
  address=body['address']
  profile_photo=body['profile_photo']
  profile_photo_data = ContentFile(base64.b64decode(profile_photo), name='i.jpg')
  cover_photo=body['cover_photo']
  cover_photo_data = ContentFile(base64.b64decode(cover_photo), name='i.jpg')
  phone=body['phone']
  whats_phone=body['whats_phone']
  points=10000

  gender=body['gender']
  marital_status=body['marital_status']
  children_number=body['children_number']
  current_work=body['current_work']
  previous_work=body['previous_work']
  current_address=body['current_address']
  previous_address=body['previous_address']
  weight=body['weight']
  height=body['height']
  is_smoker=body['is_smoker']  
  cigaretes_number = body['cigaretes_number']  
  alcoholic = body['alcoholic']  
  Hookah = body['Hookah']  
  is_sensitive_from_medicine=body['is_sensitive_from_medicine']  
  sensitivy_medicines=body['sensitivy_medicines']  
  is_sensitive_from_bugs=body['is_sensitive_from_bugs']  
  is_sensitive_from_illnesses=body['is_sensitive_from_illnesses']  
  sensitivity_illnesses_names=body['sensitivity_illnesses_names'] 
  sugar=body['sugar']
  pressure=body['pressure']
  heart=body['heart'] 
  corona=body['corona'] 
  smallpox=body['smallpox'] 
  other_previous_illnesses=body['other_previous_illnesses'] 
  tonsils=body['tonsils'] 
  appendix=body['appendix'] 
  bitterness=body['bitterness'] 
  other_previous_surgeries=body['other_previous_surgeries']
  blood_type=body['blood_type'] 
  blood_donation_number=body['blood_donation_number'] 
  blood_getting_number=body['blood_getting_number'] 
  analysis_names=body['analysis_names'] 
  family_diseases=body['family_diseases']
  previous_medicenes=body['previous_medicenes']
  current_medicines=body['current_medicines']
  analysis_names=body['current_medicines']
  analysis_names_images=body['analysis_names_images']#null
  X_Ray_Images=body['X_Ray_Images']#null
  
  try:
    d=Pharma(email=email,username=username,first_name=first_name,last_name=last_name,father_name=father_name,country=country,city=city,password=password,age=eage,address=address,profile_photo=profile_photo_data,cover_photo=cover_photo_data,phone=phone,whats_phone=whats_phone,points=points)
    d.save()
  for im in analysis_names_images:
    image_data = ContentFile(base64.b64decode(im), name='i.jpg')
    cm=MedicalAnalysisImages(agent=d,image=image_data)
    cm.save()
  for im in X_Ray_Images:
    image_data = ContentFile(base64.b64decode(im), name='i.jpg')
    cm=XRayImages(agent=d,image=image_data)
    cm.save()
			
	#previous_medicines for
    return JsonResponse({'res':'ok'})
  except Exception as e:
    print(e)
    return JsonResponse({'res':'error'})
	
@csrf_exempt		
def registerUser(request):
  body = request.body.decode('utf-8')
  body=json.loads(body)
  email=body['email']
  username=body['username']
  first_name=body['first_name']
  last_name=body['last_name']
  father_name=body['father_name']
  country=body['country']
  city=body['city']
  password=body['password']
  age=body['age']
  address=body['address']
  profile_photo=body['profile_photo']
  profile_photo_data = ContentFile(base64.b64decode(profile_photo), name='i.jpg')
  cover_photo=body['cover_photo']
  cover_photo_data = ContentFile(base64.b64decode(cover_photo), name='i.jpg')
  phone=body['phone']
  whats_phone=body['whats_phone']
  points=10000

  gender=body['gender']
  marital_status=body['marital_status']
  children_number=body['children_number']
  current_work=body['current_work']
  previous_work=body['previous_work']
  current_address=body['current_address']
  previous_address=body['previous_address']
  weight=body['weight']
  height=body['height']
  is_smoker=body['is_smoker']  
  cigaretes_number = body['cigaretes_number']  
  alcoholic = body['alcoholic']  
  Hookah = body['Hookah']  
  is_sensitive_from_medicine=body['is_sensitive_from_medicine']  
  sensitivy_medicines=body['sensitivy_medicines']  
  is_sensitive_from_bugs=body['is_sensitive_from_bugs']  
  is_sensitive_from_illnesses=body['is_sensitive_from_illnesses']  
  sensitivity_illnesses_names=body['sensitivity_illnesses_names'] 
  sugar=body['sugar']
  pressure=body['pressure']
  heart=body['heart'] 
  corona=body['corona'] 
  smallpox=body['smallpox'] 
  other_previous_illnesses=body['other_previous_illnesses'] 
  tonsils=body['tonsils'] 
  appendix=body['appendix'] 
  bitterness=body['bitterness'] 
  other_previous_surgeries=body['other_previous_surgeries']
  blood_type=body['blood_type'] 
  blood_donation_number=body['blood_donation_number'] 
  blood_getting_number=body['blood_getting_number'] 
  analysis_names=body['analysis_names'] 
  family_diseases=body['family_diseases']
  previous_medicenes=body['previous_medicenes']
  current_medicines=body['current_medicines']
  analysis_names=body['current_medicines']
  analysis_names_images=body['analysis_names_images']#null
  X_Ray_Images=body['X_Ray_Images']#null

  try:
    d=User(email=email,username=username,first_name=first_name,last_name=last_name,father_name=father_name,country=country,city=city,password=password,age=age,address=address,profile_photo=profile_photo_data,cover_photo=cover_photo_data,phone=phone,whats_phone=whats_phone,points=points)
    d.save()
  for im in analysis_names_images:
    image_data = ContentFile(base64.b64decode(im), name='i.jpg')
    cm=MedicalAnalysisImages(agent=d,image=image_data)
    cm.save()
  for im in X_Ray_Images:
    image_data = ContentFile(base64.b64decode(im), name='i.jpg')
    cm=XRayImages(agent=d,image=image_data)
    cm.save()
			
	#previous_medicines for
    return JsonResponse({'res':'ok'})
  except Exception as e:
    print(e)
    return JsonResponse({'res':'error'})
@csrf_exempt	

###############Login################

def loginUser(request):
  body=request.body.decode('utf-8')
  body=json.loads(body)
  username=body['username']
  password=body['password']
  
  try:
    u=User.objects.get(id=uid,password=password)
    ujs=model_to_dict(u)
    del ujs["password"]
    return JsonResponse({'res':'ok','data':ujs})
  except Exception as e:
    print(e)
    return JsonResponse({'res':'error'})
	
	
@csrf_exempt		
def loginDoctor(request):
  body=request.body.decode('utf-8')
  body=json.loads(body)
  username=body['username']
  password=body['password']
  
  try:
    d=Doctor.objects.get(id=uid,password=password)
    ujs=model_to_dict(u)
    del ujs["password"]
    return JsonResponse({'res':'ok','data':ujs})
  except Exception as e:
    print(e)
    return JsonResponse({'res':'error'})
	
	
@csrf_exempt		
def loginPharma(request):
  body=request.body.decode('utf-8')
  body=json.loads(body)
  username=body['username']
  password=body['password']

  try:
    p=Pharma.objects.get(id=uid,password=password)
    ujs=model_to_dict(u)
    del ujs["password"]
    return JsonResponse({'res':'ok','data':ujs})
  except Exception as e:
    print(e)
    return JsonResponse({'res':'error'})