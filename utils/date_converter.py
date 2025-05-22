import datetime

def date_format(timestamp: int) -> str:
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime('%d-%m-%Y')

def time_format(time):
    if isinstance(time, datetime.timedelta):
        total_seconds = int(time.total_seconds())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return f'{hours:02d}:{minutes:02d}:{seconds:02d}'
    return time