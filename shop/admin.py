from django.contrib import admin

# Register your models here.
from .models import *

class adminCategory(admin.ModelAdmin):
    list_display = ["name", "id"]

admin.site.register(Technology)
admin.site.register(Collection, adminCategory)
admin.site.register(Product)
admin.site.register(Category, adminCategory)
admin.site.register(Contact_us_text)
admin.site.register(Owner_Email)
admin.site.register(FAQ)
admin.site.register(Video)

