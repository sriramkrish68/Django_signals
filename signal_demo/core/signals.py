# Question NO:1
# By default are django signals executed synchronously or asynchronously?


# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# import time

# @receiver(post_save, sender=User)
# def user_created_log(sender, instance, created, **kwargs):
#     if created:
#         start = time.time()
#         print(f"New user '{instance.username}' created. Logging this...")
#         time.sleep(3)  # Adding Delay
#         print("User Added")
#         end = time.time()
#         print(f"⏱ Total time: {end - start:.2f} seconds")

#Test in Shell 
# User.objects.create_user(username='Amar', password='12345') 



# Question No : 2

# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.contrib.auth.models import User
# from .models import BlogPost
# import threading

# @receiver(post_save, sender=BlogPost)
# def user_created_log(sender, instance, created, **kwargs):
#     print(f"Signal thread ID: {threading.get_ident()}")


# Test in Shell :
# import threading
# print(threading.get_ident())
# BlogPost.objects.create(title="python", content="Hello world") 



# Question no : 3

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BlogPost
from django.db import connection

@receiver(post_save, sender=BlogPost)
def transaction_check(sender, instance, **kwargs):
    print(f"Inside signal - Is inside DB transaction? {connection.in_atomic_block}")


#Test in shell

# from django.db import transaction
# from core.models import BlogPost

# with transaction.atomic():
#     BlogPost.objects.create(title="Inside Transaction", content="Checking atomic block")

