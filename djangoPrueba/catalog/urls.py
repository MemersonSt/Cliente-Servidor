from django.urls import path, include #importamos el metodo path para crear las rutas
from rest_framework import routers #importamos el enrutador que nos permite crear las rutas de la api
from rest_framework.documentation import include_docs_urls
from catalog import views #importamos la vista de la api

router = routers.DefaultRouter()
router.register(r'Users', views.UserViews, 'Users')

urlpatterns = [
    path("login/sign/", include(router.urls)),
    path('docs/', include_docs_urls(title='API Django Prueba')),
]