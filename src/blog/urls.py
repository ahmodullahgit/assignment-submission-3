from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('<slug:slug>/', views.single_view, name='single'),
    path('category/<slug:slug>/', views.categories, name='categories')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)