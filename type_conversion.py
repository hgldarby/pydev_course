from datetime import datetime
birth_year = int(input('what year were you born'))

now = datetime.now()
age = now.year - birth_year
print(age)