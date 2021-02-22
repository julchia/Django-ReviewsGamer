from django.urls import path
from reviewsapp import views
from django.conf import settings
from django.contrib.auth.views import LoginView, logout_then_login
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from .views import SearchReview


urlpatterns = [
    path('', views.index, name='index'),
    path('reviews', views.reviews, name='reviews'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('upload', login_required(views.upload_review), name='upload'),
    path('search', views.index, name='search'),
    path('login', LoginView.as_view(template_name='reviewsapp/login.html'), name='login'),
    path('logout', logout_then_login, name='logout'),
    path('register', views.UserRegister.as_view(), name='register'),
    path('autocomplete', SearchReview.as_view(), name='autocomplete'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
