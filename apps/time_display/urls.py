from django.conf.urls import url
import views

urlpatterns = [

    url(r'^time_display$', views.index)

]