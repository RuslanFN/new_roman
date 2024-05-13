from django.db.models.signals import post_migrate
from django.contrib.auth.models import User, Group
from django.core.files.base import ContentFile
from django.dispatch import receiver
from django.db.models import signals
from shop.models import Kant, Textile
from PIL import Image
from io import BytesIO

@receiver(post_migrate)
def create_superuser_on_startup(sender, **kwargs):
    if User.objects.filter(username='admin').exists():
        return
    User.objects.create_superuser('admin', '', 'qwe123')

@receiver(post_migrate)
def create_group_on_startup(sender, **kwargs):
    if not Group.objects.filter(name='moderator').exists():
        group = Group(name='moderator')
        group.save()
    if not User.objects.filter(username='moderator').exists():
        user = User.objects.create_user('moderator', '', 'qwe123')
        user.save()
        group = Group.objects.get(name='moderator')
        user.groups.add(group)
        

@receiver(post_migrate)
def create_modelobjects(sender, **kwargs):
    if not Textile.objects.filter(title="Ткань1"):
        image1 = BytesIO()
        Image.open('newroman/on_startup_media/Ткань1-мини.jpg').save(image1, format='JPEG')
        image2 = BytesIO()
        Image.open('newroman/on_startup_media/Ткань1.png').save(image2, format='PNG')
        Textile.objects.create(title='Ткань1', fabric_type='Хлопок', 
            image_textile=ContentFile(image1.getvalue(), name='Ткань1-мини.jpg'), 
            image_blind=ContentFile(image2.getvalue(), name='Ткань1.png'))
    if not Textile.objects.filter(title="Ткань2"):
        image1 = BytesIO()
        Image.open('newroman/on_startup_media/Ткань2-мини.jpg').save(image1, format='JPEG')
        image2 = BytesIO()
        Image.open('newroman/on_startup_media/Ткань2.png').save(image2, format='PNG')
        Textile.objects.create(title='Ткань2', fabric_type='Хлопок',
            image_textile=ContentFile(image1.getvalue(), name='Ткань2-мини.jpg'), 
            image_blind=ContentFile(image2.getvalue(), name='Ткань2.png'))
    if not Kant.objects.filter(title='Кант1'):
        image1 = BytesIO()
        Image.open('newroman/on_startup_media/Кант.png').save(image1, format='PNG')
        Kant.objects.create(title='Кант1', fabric_type='Бархат',
            image_textile=ContentFile(image1.getvalue(), name='Кант.png'), 
            image_blind=ContentFile(image1.getvalue(), name='Кант.png'))
    if not Kant.objects.filter(title='Кант2'):
        image1 = BytesIO()
        Image.open('newroman/on_startup_media/Кант2.png').save(image1, format='PNG')
        Kant.objects.create(title='Кант2', fabric_type='Бархат', 
            image_textile=ContentFile(image1.getvalue(), name='Кант2.png'), 
            image_blind=ContentFile(image1.getvalue(), name='Кант2.png'))