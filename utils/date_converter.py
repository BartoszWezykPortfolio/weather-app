import datetime

def date_format(timestamp: int) -> str:
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime('%d-%m-%Y')