"""LitReviews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from feed.views import feed, create_ticket, create_review, create_ticket_and_review, edit_ticket, edit_review
from authentication.views import LoginPage, SignupPage, logout_user

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication App related
    path('', LoginPage.as_view(), name='login'),
    path('signup/', SignupPage.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),

    # Feed App related
    path('feed/', feed, name='feed'),
    path('create-ticket/', create_ticket, name='create_ticket'),
    path('edit-ticket/<int:ticket_id>/', edit_ticket, name='edit_ticket'),

    path('create-review/<int:ticket_id>/', create_review, name='create_review'),
    path('create-review/', create_ticket_and_review, name='create_ticket_and_review'),
    path('edit-review/<int:review_id>/', edit_review, name='edit_review'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
