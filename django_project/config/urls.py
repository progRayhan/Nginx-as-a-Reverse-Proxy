from django.contrib import admin
from django.urls import path
from .views import GetProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://0.0.0.0:8001/profile/
    path('profile/', GetProfileView.as_view(), name="get-profile")
]
