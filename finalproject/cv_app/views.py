from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
import datetime

from .models import Person, Interest, WorkExperience, Education
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import viewsets
from .serialize import PersonSerializer, InterestSerializer, WorkExperienceSerializer, EducationSerializer

# Create your views here.
class Home(View):
	def get(self, request, *args, **kwargs):
		person = Person.objects.all()
		interest = Interest.objects.all()
		workExperience = WorkExperience.objects.all()
		education = Education.objects.all()

		serialized1 = PersonSerializer(person, many=True)
		serialized2 = InterestSerializer(interest, many=True)
		serialized3 = WorkExperienceSerializer(workExperience, many=True)
		serialized4 = EducationSerializer(education, many=True)

		context = {'persons': serialized1.data, 'interest': serialized2.data, 'workExperience': serialized3.data, 'education': serialized4.data}
		return render(request, 'cv_app/index.html', context)
    	# education = Education.objects.filter(person = person._id)

# class UserView(APIView):
# 	def get(self, request):
# 		users = User.objects.all()
# 		serialized_account = UserSerializer(data=users, many=True)
# 		return JsonResponse(serialized_account.data)

# 	def post(self, request):
# 		data = JSONParser().parse(request)
# 		serializer = UserSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)

# class ProductView(APIView):
# 	def get(self, request):
# 		products = Product.objects.all()
# 		serialized_account = ProductSerializer(data=products, many=True)
# 		return JsonResponse(serialized_account.data)

# 	def post(self, request):
# 		data = JSONParser().parse(request)
# 		serializer = ProductSerializer(data=data) 
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)

# class CartView(APIView):
# 	def get(self, request):
# 		carts = Cart.objects.all()
# 		serialized_account = CartSerializer(data=carts, many=True)
# 		return JsonResponse(serialized_account.data)

# 	def post(self, request):
# 		data = JSONParser().parse(request)
# 		serializer = CartSerializer(data=data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return JsonResponse(serializer.data, status=201)
# 		return JsonResponse(serializer.errors, status=400)