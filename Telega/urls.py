"""Telega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from Telega import settings
from django.contrib import admin
from django.urls import path
from msg.views import main_view, ChatView
from user.views import logout_view, LogRegView, profile_view
from groupchat.views import GroupChatView, leave_group_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('logout/', logout_view),
    path('login/', LogRegView.as_view()),
    path('user/<int:id>/', ChatView.as_view()),
    path('user/<int:id>/profile', profile_view),
    path('group/<int:id>/', GroupChatView.as_view()),
    path('leave/<int:id>/', leave_group_view)
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
