from django.db import models

# Create your models here.
class Tutorial (models.Model):
	title = models.TextField(null=False, blank=False, max_length=50)
	content = models.TextField(null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.title

	@property
	def terminals(self):
		return self.terminal_set.all()

class Terminal (models.Model):
	tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
	is_available = models.BooleanField(default=True)
	key = models.TextField(default="",null=False, blank=False)
	url = models.URLField(max_length=200,null=True, blank=True)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return "{0} - {1}".format(self.tutorial,self.key)

	# @property
	# def choices(self):
	# 	return self.choice_set.all()