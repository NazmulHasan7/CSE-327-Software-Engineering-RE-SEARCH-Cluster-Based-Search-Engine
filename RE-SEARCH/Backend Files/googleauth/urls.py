
from django.contrib import admin
from django.urls import base, path,include
from django.views.generic import TemplateView
from API import views
import base_app

urlpatterns = [
    path('', TemplateView.as_view(template_name="base/index.html")),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('cluster/', include('base_app.urls')),
    path('api/', include('API.urls')),
    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment/', base_app.views.testpayment, name='payment'),
]
