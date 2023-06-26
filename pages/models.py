from django.db import models

class userData(models.Model):
    user_name=models.CharField(max_length=100,verbose_name="Name")
    user_email=models.CharField(max_length=500,verbose_name="Email")
    user_phone=models.CharField(max_length=500,verbose_name="Phone")
    message=models.TextField(verbose_name="Message")
    user_image=models.ImageField()
    def __str__(self):
        return self.user_name

class Coffee(models.Model):
    Coffee_name=models.CharField(max_length=100,verbose_name="Name Of Coffe")
    Coffee_Type=models.CharField(max_length=100,verbose_name="Type Of Coffe")
    Coffee_description=models.CharField(max_length=500, verbose_name="Small Description")
    Coffee_price=models.IntegerField(default=0, verbose_name="Price")
    Coffee_image=models.ImageField(verbose_name="Image For Coffe")
    def __str__(self):
        return self.Coffee_name
class Blog(models.Model):
    blog_title=models.CharField(max_length=100)
    blog_publish_date=models.DateField()
    blog_description=models.TextField()
    blog_image=models.ImageField()

