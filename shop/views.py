from django.shortcuts import render
from .models import *
from .utils import *
from rest_framework import viewsets
from .serializers import *


# Create your views here.

class ProductView(viewsets.ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()

class TechnologyView(viewsets.ModelViewSet):
    serializer_class = TechnologiesSerializer
    queryset = Technology.objects.all()

class CollectionView(viewsets.ModelViewSet):
    serializer_class = CollectionsSerializer
    queryset = Collection.objects.all()

class CategoryView(viewsets.ModelViewSet):
    serializer_class = CategoriesSerializer
    queryset = Category.objects.all()


class FaqView(viewsets.ModelViewSet):
    serializer_class = FaqsSerializer
    queryset = FAQ.objects.all()

def index(request):
    tools = Collection.objects.values()
    cards = {
        "tools" : tools
    }    
    return render(request, "index.html", cards)


def video(request):
    v = Video.objects.all()
    cards = {
        "videos" : v
    }    
    return render(request, "video-page.html", cards)


def contact(request):
    obj = Contact_us_text.objects.all()[0]
    if request.method == "POST":
        
        msg = f"""
            NAME : {request.POST["name"]}
            EMAIL : {request.POST["email"]}
            SUB : {request.POST["sub"]}
            MSG: 
                {request.POST["msg"]}
        """
        isDone = send_email_to_owner(sub=f"[CONTACT-US] : {request.POST['sub']}", msg=msg)
        return render(request, "contact-us.html", {"SEND": isDone, "msg": obj})

    return render(request, "contact-us.html", {"msg": obj})

def represent(request):
    return render(request, "represent-us.html")


def tools(request, param):
    obj = Product.objects.all()
    cards = {
        "is_search": False,
        "search": "",
        "products": obj,
        "param": param
    }
    return render(request, "tools.html", cards)

def tools_all(request):
    obj = Product.objects.all()
    cards = {
        "products": obj,
        "is_search": True,
        "search": request.GET["search"],
        "param": 'all-products'
    }
    return render(request, "tools.html", cards)

def technology(request):  
    obj = Technology.objects.values()
    
    cards = {
        "cards" : obj
    }
    
    return render(request, "technology.html", cards)

def about(request):
    return render(request, "about-deetec.html")

def faqs(request):
    objects = FAQ.objects.all()
    return render(request, "faqs.html", {"faqs": objects})

def find_dealer(request):
    return render(request, "map.html")

def want_quote(request):
    obj = Contact_us_text.objects.all()[0]
    if request.method == "POST":
        
        msg = f"""
            NAME : {request.POST["fname"]} {request.POST["lname"]}
            EMAIL : {request.POST["email"]}
            TELEPHONE : {request.POST["telephone"]}
            MSG: 
                {request.POST["special_instruction"]}
        """
        isDone = send_email_to_owner(sub=f"[WANT-QUOTE]", msg=msg)
        return render(request, "want_quote.html", {"SEND": isDone, "msg": obj})

    return render(request, "want_quote.html", {"msg": obj})    

def product(request, param):
    p = Product.objects.get(id=param)
    attrsName = list(filter( lambda x : str(x).startswith("attributesName") , p.__dir__()))[1:]
    attrsName = list(map( lambda x : getattr(p, x) , attrsName))
    attrs = list(filter( lambda x : str(x).startswith("attributes") and not str(x).startswith("attributesName") , p.__dir__()))[1:]
    attrs = list(map( lambda x : getattr(p, x) , attrs))
    return render(request, "product.html", {"product": p, "attr" : zip(attrsName,attrs)})


