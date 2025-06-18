
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView


class LogoutViewAllowGet(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('orders.urls')),
    path('api/', include('orders.api_urls')),
    # <--- Adicione esta linha!
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', LogoutView.as_view(next_page='/'),
         name='logout'),  # para /logout/
    
    
    
]
