from django.db import models

# Create your models here.


class Technology(models.Model):
    left_heading = models.TextField(blank=False)
    left_description = models.TextField(blank=False)
    left_logo = models.ImageField(blank=False, upload_to="shop/images/")

    right_heading = models.TextField(blank=False)
    right_description = models.TextField(blank=False)
    right_logo = models.ImageField(blank=False, upload_to="shop/images/")

class Contact_us_text(models.Model):
    success_msg = models.TextField(default="")
    failure_msg = models.TextField(default="")

class Owner_Email(models.Model):
    email = models.TextField(default="")

    def __str__(self):
        return self.email


class Category(models.Model):
    name = models.TextField(blank=False)

    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.TextField(blank=False)
    url = models.TextField(blank=False)
    desc = models.TextField(blank=False)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.TextField(default="")
    answer = models.TextField(default="")


    def __str__(self):
        return self.question


class Collection(models.Model):
    name = models.TextField(blank=False, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    heading = models.TextField(default="", blank=True, null=True)
    desc = models.TextField(default="", blank=True, null=True)
    description1 = models.TextField(blank=True, null=True)
    description2 = models.TextField(blank=True, null=True)
    description3 = models.TextField(blank=True, null=True)
    description4 = models.TextField(blank=True, null=True)
    description5 = models.TextField(blank=True, null=True)
    description6 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.TextField(blank=False, default="")
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    attributesName1 = models.CharField(max_length=80, blank=True, null= True, default="")
    attributes1 = models.TextField(blank=True, null= True, default="")
    attributesName2 = models.CharField(max_length=80, blank=True, null= True, default="")
    attributes2 = models.TextField(blank=True, null= True, default="")
    attributesName3 = models.CharField(max_length=80, blank=True, null= True, default="")
    attributes3 = models.TextField(blank=True, null= True, default="")
    attributesName4 = models.CharField(max_length=80, blank=True, null= True, default="")
    attributes4 = models.TextField(blank=True, null= True, default="")
    attributesName5 = models.CharField(max_length=80, blank=True, null= True, default="")
    attributes5 = models.TextField(blank=True, null= True, default="")
    attributesName6 = models.CharField(max_length=80, blank=True, null= True, default="")
    attributes6 = models.TextField(blank=True, null= True, default="")
    attributesName7 = models.CharField(max_length=80, blank=True, null= True, default="")
    attributes7 = models.TextField(blank=True, null= True, default="")
    attributesName8 = models.CharField(max_length=80, blank=True, null= True, default="")
    attributes8 = models.TextField(blank=True, null= True, default="")
    total = models.TextField(default="", blank=True)

    def save(self, *args, **kwargs):
        self.set_total()
        super().save(args, kwargs)

    def __str__(self):
        return self.name
        

    def set_total(self):
        s = self.name
        s += self.collection.name
        s += self.collection.category.name
        s += self.attributesName1
        s += self.attributesName2
        s += self.attributesName3
        s += self.attributes1
        s += self.attributes2
        s += self.attributes3
        self.total = s