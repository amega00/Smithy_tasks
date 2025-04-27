import re
from datetime import datetime
pattern = re.compile(r'\d+')
text_card = 'Счет 35383033474447895560'

def get_mask_card_number(number_card: str) -> str:
    """Функция маскировки номера банковской карты"""
    mask_card = ""
    number_card = number_card.replace(" ", "")
    if len(number_card) == 16:
        mask_card = number_card[0:4] + " " + number_card[4:6] + "** **** " + number_card[-4:]
    else:
        return "Номер карты введен не верно. Попробуйте еще раз."
    return mask_card


numbers = (pattern.search(text_card).group())
print("Найденные числа:", numbers)
print("TXT:", re.search('Счет', text_card).group())
print(re.sub(pattern, get_mask_card_number(numbers), text_card))

now_date = '2024-03-11T02:26:18.671407'
print(datetime.strptime(now_date, "%Y-%m-%d%a%H:%M:%S.%f"))

