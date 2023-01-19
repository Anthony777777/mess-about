from datetime import date
birthdate = int(input("What year were you born?"))
def age(birthdate):
    today = date.today()
    return today.year - birthdate

print (age(birthdate))