from datetime import datetime

date_str = '2024-03-11T02:26:18.671407'
our_date = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f')
print(our_date.strftime('%d.%m.%Y'))
