from cv_app.models import Person, Interest, WorkExperience, Education
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = ('email', 'firstName', 'lastName', 'description')


class InterestSerializer(serializers.ModelSerializer):
	class Meta:
		model = Interest
		fields = ('interest', 'person')

class WorkExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = WorkExperience
		fields = ('job', 'company', 'period', 'description', 'person')

class EducationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Education
		fields = ('school', 'course', 'period', 'person')