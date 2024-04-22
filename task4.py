from datetime import datetime, timedelta
from typing import List, Dict

def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    '''returns a list of everyone whose birthday is 7 days ahead including the current day.'''
    today = datetime.today().date()
    upcoming_birthdays=[]
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year+1)
               
        if birthday_this_year.weekday() == 5:
            birthday_this_year += timedelta(days = 2)
        if birthday_this_year.weekday() == 6:
            birthday_this_year += timedelta(days = 1)
            
        days_to_birthday = (birthday_this_year - today).days
        
        if days_to_birthday <=7:
            upcoming_birthdays.append({
                "name" : user["name"],
                "congratulation_date" : birthday_this_year.strftime("%Y.%m.%d") 
            })
    return upcoming_birthdays
    