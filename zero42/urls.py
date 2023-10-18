from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', SignUp.as_view(), name='signup'),
    path('', FavoritesList.as_view(), name='home'),
    path('update/<int:id>', UpdateUser.as_view(), name='update'),
    path('delete/<int:id>', DeleteUser.as_view(), name='delete')
]
