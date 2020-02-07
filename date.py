#get dates only from datetime
def date_parser(dates):
   return [i.split()[0]for i in dates]

dates = ['2019-11-29 12:50:54',
         '2019-11-29 12:46:53',
         '2019-11-29 12:46:10',
         '2019-11-29 12:33:36',
         '2019-11-29 12:17:43',
         '2019-11-29 11:28:40']

print(date_parser(dates))