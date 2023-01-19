user = int(input("enter a multiple checker?" ))
user2 = int(input("enter a multiple checker?" ))

def isMultiple(num, check_with):
    return num % check_with == 0;

if (isMultiple(user, user2) == True):
    print(str(user), "is multiple of", str(user2));
else:
    print(str(user), "is not multiple of ", str(user2));