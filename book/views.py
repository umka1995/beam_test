from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.http import JsonResponse
from .models import UserProfile, Product, Order, Notification
from .serializers import UserProfileSerializer, ProductSerializer, OrderSerializer, NotificationSerializer

def index(request):
    users = UserProfile.objects.all()
    return render(request, 'index.html', {'users': users})

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        new_user = UserProfile.objects.create(username=username, email=email)
        new_user.save()
        send_notification_to_other_users(new_user)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def send_notification_to_other_users(new_user):
    from asgiref.sync import async_to_sync
    from channels.layers import get_channel_layer

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notifications",
        {
            'type': 'send_notification',
            'notification': f'New user "{new_user.username}" has been created!'
        }
    )

class UserProfileViewSet(ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

