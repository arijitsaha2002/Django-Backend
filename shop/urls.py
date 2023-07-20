from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from django.urls import include

router = routers.DefaultRouter()
router.register(r'products', views.ProductView, 'products')
router.register(r'collections', views.CollectionView, 'collections')
router.register(r'categories', views.CategoryView, 'categories')
router.register(r'faqs', views.FaqView, 'faqs')
router.register(r'technology', views.TechnologyView, 'technology')

urlpatterns = [
    path('', views.index, name="index"),
    path('contact-us', views.contact, name="contact-us"),
    path('represent-us', views.represent, name="represent-us"),
    path('tools/<str:param>/', views.tools, name='tools'),
    path('product/<int:param>/', views.product, name='product'),
    path('tools/', views.tools_all, name='tools'),
    path("technology", views.technology, name="technology"),
    path("about-deetec", views.about, name="about-deetec"),
    path("faqs", views.faqs, name="faqs"),
    path("promo-videos", views.video, name="promo-videos"),
    path("find-dealer", views.find_dealer, name="find-dealer"),
    path("want-quote", views.want_quote, name="want-quote"),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
