"""AlmacenLosYuYitos URL Configuration

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
from LosYuYitos.models import Proveedor, Pedido
from django import urls
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from django.views.generic import edit
from LosYuYitos.views import agregarProveedor,listarProveedor,modificarProveedor,eliminar_proveedor,\
     registroUsuario, listarUsuarios, eliminar_usuario, agregar_cliente, listar_clientes,modificar_cliente, eliminar_cliente,editar_usuario,\
     editar_password, agregarProducto, listarProducto, modificar_producto, eliminar_producto,agregar_pedido,eliminar_pedido,listarPedido,modificar_pedido,agregar_venta,\
     modificar_venta,listarVenta,eliminar_venta,Pdf
from LosYuYitos import views

urlpatterns = [
    path('pdf/',Pdf.as_view(), name='pdf'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', auth_views.LoginView.as_view()),
    path('inicio', auth_views.LoginView.as_view()),
    path('agregarproveedor/' ,agregarProveedor, name="agregar-proveedor"),
    path('listarproveedor/' ,listarProveedor, name="listar-proveedor"),
    path('modificarproveedor/<id>/' ,modificarProveedor, name="modificar-proveedor"),
    path('eliminarproveedor/<id>/' ,eliminar_proveedor, name="eliminar-proveedor"),
    path('registro/', registroUsuario, name="registro-usuario"),
    path('listarusuarios/', listarUsuarios, name="listar-usuarios"),
    path('eliminarusuario/<id>/' ,eliminar_usuario, name="eliminar-usuario"),
    path('agregarcliente/' ,agregar_cliente, name="agregar-cliente"),
    path('listarcliente/' ,listar_clientes, name="listar-cliente"),
    path('modificarclienter/<id>/' ,modificar_cliente, name="modificar-cliente"),
    path('eliminarcliente/<id>/' ,eliminar_cliente, name="eliminar-cliente"),
    path('modificarusuario/<id>/' ,editar_usuario, name="editar-usuario"),
    path('modificarpassword/<id>/' ,editar_password, name="editar-password"),
    path('agregarproducto/' , agregarProducto, name="agregar-producto"),
    path('listarproductos/' , listarProducto, name="listar-productos"),
    path('modificarproducto/<id>/' , modificar_producto, name="modificar-productos"),
    path('eliminarproducto/<id>/' , eliminar_producto, name="eliminar-producto"),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="registration/RecuperarPassword.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="registration/RecuperarPasswordEnviado.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="registration/RecuperarPasswordForm.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="registration/RecuperarPasswordCompletado.html"), 
        name="password_reset_complete"),
    
    path('agregarpedido/<id>' , agregar_pedido, name="agregar-pedido"),
    path('crearpedido/' , views.DetallePedidoCreateView.as_view(), name="agregar-detalle-pedido"),
    path('eliminarpedido/<id>/' ,eliminar_pedido, name="eliminar-pedido"),
    path('listarpedido/' ,listarPedido, name="listar-pedido"),
    path('modificarpedido/<id>/' ,modificar_pedido, name="modificar-pedido"),
    path('agregarventa/' ,agregar_venta, name="agregar-venta"),
    path('crearventa/' , views.DetalleVentaCreateView.as_view(), name="agregar-detalle-venta"),
    path('modificarventa/<id>/' ,modificar_venta, name="modificar-venta"),
    path('listarventa/' ,listarVenta, name="listar-venta"),
    path('eliminarventa/<id>/' ,eliminar_venta, name="eliminar-venta")

]
