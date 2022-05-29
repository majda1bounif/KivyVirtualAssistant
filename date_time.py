import datetime
from datetime import date


def date():
    now = datetime.datetime.now()
    current_date= now.strftime("%B %d %Y")
    return current_date

def time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
