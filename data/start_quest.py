import datetime

from data.config import DEBUG


def check_available():
    stamp = datetime.datetime.now().timestamp()
    if not bool(DEBUG):
        if stamp < 1668333600:
            return False
        else:
            return True
    else:
        return True
