from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('contact/', views.Contact.as_view(), name='contact'),
    path('pies/', views.Pies.as_view(), name='pies'),
    path('order/', views.Order.as_view(), name='order'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)