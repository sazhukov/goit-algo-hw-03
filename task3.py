import re

def normalize_phone(phone_number: str) -> str:
    '''normalizes phone numbers to a standard format'''
    digits = re.sub(r'[^\d\+]', '', phone_number)
    
    if not digits.startswith('+'):
        digits = '+38' + digits.lstrip('38')

    return digits