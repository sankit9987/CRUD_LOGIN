from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('form',views.form,name="form"),
    path('search',views.search,name="search"),
    path('delete<int:id>',views.delete,name="delete"),
    path('edit<int:id>',views.edit,name="edit"),
    path('signup',views.user_sign,name="signup"),
    path('logout',views.user_logout,name="logout"),
    path('login',views.user_login,name="login"),
]
