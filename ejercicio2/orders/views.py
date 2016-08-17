from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.db import connection
from datetime import datetime, timedelta
from django.db.models import Count

from orders.models import UserProfile, Order

class IndexView(generic.TemplateView):
    template_name = "orders/index.html"


class OrdersCompletedMonthView(generic.ListView):
    template_name = 'orders/ordersPerMonth.html'
    context_object_name = 'orders_completed_month'

    def get_queryset(self):
        truncate_date = connection.ops.date_trunc_sql('month', 'date_created')
        return Order.objects.filter(state='SUCCESSFUL').extra({'month':truncate_date})

class AverageOrdersCountView(generic.ListView):
    template_name = 'orders/averageOrders.html'
    context_object_name = 'average'

    def get_queryset(self):
        avg = []
        users = UserProfile.objects.annotate(total_orders=Count('order'), successful_orders=Count(Case(When(order__state='SUCCESSFUL', then=1))))
        for x in range(users.count()):
            avg[x][0] = users[x].id
            avg[x][1] = users[x].name
            avg[x][2] = users[x].gender
            if users[x].total_orders is not 0:
                avg[x][3] = users[x].successful_orders / users[x].total_orders
        return avg

class SalesAmmountView(generic.ListView):
    template_name = 'orders/lastMonthCount.html'
    context_object_name = 'sales_ammount'

    def get_queryset(self):
        orders_count = {'laptops':0, 'camaras':0, 'minicomponentes':0}
        last_month = datetime.today() - timedelta(days=30)
        orders = Order.objects.filter(date_created__gte=last_month).annotate(num_laptops=Count('laptop'), num_camaras=Count('cámara'), num_minicomp=Count('minicomponente'))
        for x in range(orders.count()):
            orders_count['laptops'] = orders_count['laptops'] + orders[x].num_laptops
            orders_count['camaras'] = orders_count['camaras'] + orders[x].num_camaras
            orders_count['minicomponentes'] = orders_count['minicomponentes'] + orders[x].num_minicomp

        return orders_count
