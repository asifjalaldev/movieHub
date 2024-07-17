from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import UserProfile
from django.dispatch import receiver

# custom_data=Signal(providing_args=['extra_data'])

@receiver(post_save, sender=User)
def post_create_User(sender,instance, created, **kwargs):

    if created:
        # when new user created , also create its profile
        user_profile=UserProfile.objects.create(user=instance, address='House no 123')
        user_profile.save()

        print(f'User Profile created!++++++++++++ address: {user_profile.address}')
    else: # user updated
        # print(f'updated fields : {update_fields}')
        print(f'kwargs updated field: {kwargs.get("update_fields")}')
        # if update_fields is not None and 'first_name' in update_fields:
            # print('first name is changed @@@@@@@@@@@@')
        print('user updated : ', instance.username)
    for key, val in kwargs.items():
        print(f'kwargs dict data: key -> {key}, val -> {val}')
