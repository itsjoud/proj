from django.db import models

# Create your models here.

class Customer(models.Model):
	name= models.CharField(max_length=200, null=True)
	phone= models.CharField(max_length=200, null=True)
	email= models.CharField(max_length=200, null=True)
	data_created= models.DateTimeField(auto_now_add=True, null=True)
	
	def __str__(self):
    		return self.name
	
class Tag(models.Model):
	name= models.CharField(max_length=200, null=True)
	
	def __str__(self):
    		return self.name

class Product(models.Model):
	CATEGORY = (
    ('Novel', 'Novel'),
    ('Journal', 'Journal'),
    ('Magazine', 'Magazine'),
    ('Article', 'Article'),
    ('Legal Case','Legal Case'),
    ('Blog','Blog'),
    ('Thesis','Thesis'),
    
)

	pic = models.ImageField(upload_to='static/images', null=True)
	title= models.CharField(max_length=200, null=True)
	SSBN= models.FloatField( null=True)
	author=models.CharField(max_length=200, null=True)
	tags=models.ManyToManyField(Tag)
	type= models.CharField(max_length=200, null=True, choices= CATEGORY)
	source=models.CharField(max_length=200, null=True, blank=True)
	price= models.FloatField(null=True)
	date_created= models.DateTimeField(auto_now_add=True, null=True) 

	def __str__(self):
    		return self.title




class Order (models.Model):
	STATUS= (
		('Reserved', 'Reserved'),
	  ('Available', 'Available'),
	 
	  )
	Customer=models.ForeignKey(Customer,null=True, on_delete=models.SET_NULL)
	Product=models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
	# Tag=models.ForeignKey(Tag,null=True, on_delete=models.SET_NULL)
	date_created= models.DateTimeField(auto_now_add=True, null=True)
	status= models.CharField( null=True,max_length=200,  choices= STATUS)

	def __str__(self):
    		return self.Product.title

# class Migration(migrations.Migration):

#     initial=True

#     dependencies=[]
#     operations=[
#         migrations.CreateModel(
#             name='Customer',
#             fields=[
#             (id = models.CharField(max_length=200, null=True)),
#             (name = models.CharField(max_length=200, null=True)),
#             (phone = models.CharField(max_length=200, null=True)),
#             (email = models.CharField(max_length=200, null=True)),
#             (date_created = models.DateTimeField(auto_now_add=True, null=True)),
#             ],
#         ),
#     ]
