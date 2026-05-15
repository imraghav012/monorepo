string = input('What do you want to test?')

string = string.upper()

string = string.replace(' ','')

if string == string[::-1]:
    print("It's a palindrome")
else:
    print("It's not a palindrome")
