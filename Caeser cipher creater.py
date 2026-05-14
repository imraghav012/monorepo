#A-Z = 65-90
#a-z = 97-122

code = input('enter a code:')
shift = int(input('shift by:'))

for i in code:
    if i == ' ' or i is int:
        print(i, end = '')
        continue
    else:
        if 65 <= ord(i) and ord(i) <= 90:
            i = chr(ord(i)+shift)
            if ord(i) > 90:
                while ord(i) > 90:
                    i = chr(ord(i)-26)
        elif 97 <= ord(i) and ord(i) <= 122:
            i = chr(ord(i)+shift)
            if ord(i) > 122:
                while ord(i) > 122:
                    i = chr(ord(i)-26)
        else:
            print(i, end = '')
            continue
        
    print(i, end = '')
