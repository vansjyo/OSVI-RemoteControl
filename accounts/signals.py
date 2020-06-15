from django.contrib.auth import user_logged_in, user_logged_out
from django.dispatch import receiver
from accounts.models import LoggedInUser
from django.utils import timezone
from runcode.runcodefuncs import kill_stop_clear


@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    LoggedInUser.objects.get_or_create(user=kwargs.get('user'))
    request.user.logged_in_user.login_time = timezone.now()
    request.user.logged_in_user.save()


@receiver(user_logged_out)
def on_user_logged_out(sender, **kwargs):
    kill_stop_clear()
    LoggedInUser.objects.filter(user=kwargs.get('user')).delete()
