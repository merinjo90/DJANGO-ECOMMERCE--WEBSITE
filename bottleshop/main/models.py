from django.db import models

# Create your models here.


# Banner
class Banner(models.Model):
    img=models.ImageField(upload_to="banner_img/")
    alt_text=models.CharField(max_length=300)

    def __str__(self):
        return self.alt_text

#Category
class Category(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="cat_imgs/")

    def __str__(self):
        return self.title

#Brand
class Brand(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="brand_imgs/")

    def __str__(self):
        return self.title

#color
class Color(models.Model):
    title=models.CharField(max_length=100)
    color_code=models.CharField(max_length=100)

    def __str__(self):
        return self.title


#Size
class Size(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title


#Product Model
class Product(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to="product_imgs/")
    slug=models.CharField(max_length=400)
    detail=models.TextField()
    specs=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    status=models.BooleanField(default=True)

#Prduct Attribute
class ProductAttribute(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    size=models.ForeignKey(Size,on_delete=models.CASCADE)
    price=models.PositiveIntegerField(default=0)

    def __str__(self):
         return self.product.title