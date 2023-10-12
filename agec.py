import datetime

date_format = "%Y-%m-%d"
current_date = datetime.date.today()
current_year = datetime.date.today().year
min_date = datetime.date(1, 1, 1)
#current_date_string = current_date.strftime(date_format)

birth_year = int (input('Enter the year you were born?\n'))
print (f"You are {current_year - birth_year} old \n")

birth_date_input = (input('Enter your the date of your birth (yyyy-mm-dd): \n'))
birth_date = datetime.datetime.strptime(birth_date_input, date_format).date()

if birth_date > min_date and birth_date < current_date :
  birthday_this_year = birth_date.replace (year=current_date.year)

  if birthday_this_year > current_date :
    count_days = birthday_this_year - current_date
  else :
    birthday_this_year = birth_date.replace (year=current_date.year+1)

  print (f"You have {birthday_this_year - current_date} days until your birthday")
else :
  print ("You entered wrong date")



