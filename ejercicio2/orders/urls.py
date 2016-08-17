from django.conf.urls import url
from . import views

app_name = 'orders'
urlpatterns = [
    #Main Menu url
    url(r'^$', views.IndexView.as_view(), name='index'),
    #Order Completed Grouped By Month
    url(r'^ordersPerMonth/$', views.OrdersCompletedMonthView.as_view(), name='ordersPerMonth'),
    #Average Orders By User
    url(r'^averageOrders/$', views.AverageOrdersCountView.as_view(), name='averageOrders'),
    #Ammount of Orders for Each item in last month
    url(r'^lastMonthCount/$', views.SalesAmmountView.as_view(), name='lastMonthCount'),

]
