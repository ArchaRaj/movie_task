from . import views
from django.urls import path
app_name='web_app'

urlpatterns = [
    path('',views.index,name="index"),
    path('movie/<int:id>',views.details,name="details"),
    path('insert/',views.insert,name="insert"),
    path('update/<int:id>/',views.update,name="update"),
    path('delete/<int:id>/',views.delete,name="delete")

]