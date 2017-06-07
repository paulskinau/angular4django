from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles import views
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from django.conf.urls import url, include


from .robotview import RobotView

urlpatterns = [
    url(r'^robot/$', RobotView.as_view()),
    url(r'^docs/', include_docs_urls(title='My API title')),

]