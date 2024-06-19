from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from content.views import CategoriesView, VideoViewSet
from customers.views import LoginView, LogoutView, RegisterView


urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('django-rq/', include('django_rq.urls')),
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
    path('content/', VideoViewSet.as_view()),
    path('categories/', CategoriesView.as_view())


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT, )
