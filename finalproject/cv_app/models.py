from django.db import models

# Create your models here.

class AbstractItem(models.Model):
	created_on = models.DateTimeField(auto_now_add = True)
	updated_on = models.DateTimeField(auto_now_add = True)

	class Meta:
		abstract = True

class Person(AbstractItem):
	email = models.EmailField()
	firstName = models.CharField(max_length = 50)
	lastName = models.CharField(max_length = 50)
	description = models.TextField()

	def __str__(self):
		return self.firstName + " " + self.lastName

class Interest(AbstractItem):
	interest = models.CharField(max_length = 150)
	person = models.ForeignKey('Person', on_delete=models.CASCADE, default=None)

class WorkExperience(AbstractItem):
	job = models.CharField(max_length = 100, default=None)
	company = models.CharField(max_length = 100, default=None)
	period = models.DateField(auto_now_add = False)
	description = models.TextField()
	person = models.ForeignKey('Person', on_delete=models.CASCADE)


class Education(AbstractItem):
	school = models.CharField(max_length = 100)
	course = models.CharField(max_length = 100, default=None, blank=True, null=True)
	period = models.DateField(auto_now_add = False)
	person = models.ForeignKey('Person', on_delete=models.CASCADE)