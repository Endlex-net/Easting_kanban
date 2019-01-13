from django.apps.registry import apps
if not apps.loading:
    import os
    os.environ['DJANGO_SETTINGS_MODULE'] = 'starvation.settings'
    import django
    django.setup()

from datetime import timedelta

from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.hashers import (
    make_password,
)

from utils import common_utils


def get_now():
    return timezone.now()


def get_today():
    return timezone.now().date()


def get_datetime_before_days(days=0):
    dt = get_now() - timezone.timedelta(days=days)

    return dt


def get_midnight_after_days(days=1):
    dt = get_now() + timezone.timedelta(days=days)
    dt = timezone.localtime(dt)
    dt = dt.replace(hour=23, minute=59, second=59)
    return dt.astimezone(timezone.utc)


def calc_slaughtered_time(birthday=None, days=300):
    if birthday is None:
        birthday = timezone.now()
    return birthday + timezone.timedelta(days=days)


def get_today_start(dt=None):
    if dt is None:
        dt = get_now()
    dt = timezone.localtime(dt)
    dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    return dt.astimezone(timezone.utc)


def get_this_year_month():
    today = get_today()
    return today.isoformat()[:-3]


def get_this_week_start():
    now = timezone.localtime(get_now())
    weekday = now.isoweekday()
    if weekday != 1:
        dt = now - timedelta(days=weekday - 1)
    else:
        dt = None
    return get_today_start(dt)


def get_next_week_start():
    return get_this_week_start() + timedelta(days=7)


def make_hashed_password(password):
    return make_password(common_utils.hash_password(password))


def get_distinct_username(prefix=''):
    username = prefix + common_utils.get_uuid()
    if User.objects.filter(username=username).exists():
        return get_distinct_username(prefix)
    return username


def create_user(password, **kwargs):
    username = get_distinct_username()
    user = User.objects.create_user(
        username=username,
        password=password,
        **kwargs
    )
    return user


if __name__ == '__main__':
    pass
