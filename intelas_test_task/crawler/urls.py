from django.urls import path

from .views import CrawlFormView

urlpatterns = [
    path('', CrawlFormView.as_view()),
]
