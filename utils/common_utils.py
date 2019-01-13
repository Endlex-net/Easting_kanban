import time
import string
import hashlib
import shortuuid
from datetime import (
    date,
    datetime,
    timedelta,
)

from utils import constants

strptime = datetime.strptime


def to_date(the_date_str):
    the_date = strptime(the_date_str, constants.DATE_TPL)
    return the_date.date()


def add_one_day(the_date):
    if not isinstance(the_date, date):
        the_date = to_date(the_date)
    return the_date + timedelta(days=1)


def hash_password(raw_password):
    raw_password = raw_password.encode('utf-8')
    return hashlib.sha256(raw_password).hexdigest()[::2]


def generate_header():
    cur = int(time.time())
    expire = str(cur + 30)
    key = hashlib.sha256(
        f'starvation{cur}'.encode('utf-8')).hexdigest()[::4] + expire
    return {'Authentication': key}


def get_uuid(length=10, letters_only=False):
    alphabet = None
    if letters_only:
        alphabet = list(string.letters)
    return shortuuid.ShortUUID(alphabet).random(length=length)


if __name__ == '__main__':
    pass
