from datetime import datetime

def get_days_from_today(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)
    delta = today - date_obj
    return delta.days  