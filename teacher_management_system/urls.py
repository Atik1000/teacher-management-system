from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import HomePageView

urlpatterns = [
    path('management/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('auth/', include('customauth.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('question/', include('question.urls')),
    path('seatplan/', include('seatplan.urls')),
    path('teacher/', include('teacher_profile.urls')),  
]

# Serve media files in development environment
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
