def is_year_leap(year): 
    if year%4 == 0: 
        if year%100 ==0: 
            if year%400 ==0: 
                return True 
            else:
                return False 
        else: 
            return True
    else: 
        return False

def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [1 , 3 , 5 , 7 , 8 , 10 , 12]:
        return 31
    elif month in [4 , 6 , 9 , 11]:
        return 30

userYear = input("What Year:")
userMonth = input("What Month:")

days_in_month(userYear, userMonth)
