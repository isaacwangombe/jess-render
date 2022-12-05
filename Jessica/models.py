from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Tools(models.Model):
	name = models.CharField(max_length =30)
	def __str__(self):
		return self.name

	class Meta:
			verbose_name_plural  =  "Tools"

	@classmethod
	def get_all(cls):
		items = cls.objects.all()
		return items

class Models(models.Model):
	name = models.CharField(max_length =30)
	def __str__(self):
		return self.name

	class Meta:
			verbose_name_plural  =  "Models"  



	@classmethod
	def get_all(cls):
		items = cls.objects.all()
		return items


class Projects(models.Model):
	name = models.CharField(max_length =100)
	image = CloudinaryField('image')
	details = models.TextField(max_length =1000)
	highlighted = models.BooleanField()
	github = models.CharField(max_length =150, blank=True, null=True)
	date = models.DateField(auto_now_add=False) 
	tools = models.ManyToManyField(Tools , blank=True)
	models = models.ManyToManyField(Models, blank=True)


	def __str__(self):
			return self.name

	class Meta:
			verbose_name_plural  =  "Projects"  


	@classmethod
	def get_all(cls):
		projects = cls.objects.all().order_by('-id')
		return projects


	@classmethod
	def get_id(cls, id):
		projects = cls.objects.get(id=id)
		return projects


	@classmethod
	def filter_model(cls, models):
		projects = cls.objects.filter(models=models)
		return projects


	@classmethod
	def filter_tool(cls, tools):
		projects = cls.objects.filter(tools=tools)
		return projects




RATING = (
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),

)

class Comments(models.Model):
	name = models.CharField(max_length =30)
	email = models.EmailField(max_length =30, blank=True,null=True)
	comment = models.TextField(max_length =1000, default = "Great Project")
	rating = models.IntegerField(choices=RATING, default=1)
	date = models.DateField(auto_now_add=True) 
	project = models.ForeignKey(Projects, on_delete=models.CASCADE)

	def __str__(self):
		return str(f"name-{self.name}, date- {self.date}")

	class Meta:
			verbose_name_plural  =  "Comments"  


	@classmethod
	def get_all(cls):
		comments = cls.objects.all()
		return comments

	@classmethod
	def filter_project(cls, project):
		projects = cls.objects.filter(project__name=project)
		return projects
