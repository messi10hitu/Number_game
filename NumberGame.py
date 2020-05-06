import random

print("--------Number game----------")
start = 0
end = 30
comp_number = random.randint(0, 30)
while True:
    usernumber = int(input("enter the number:"))
    if usernumber == comp_number:
        print("your number is correct")
        break
    elif usernumber > comp_number:
        end = comp_number
        midpoint = (start + end / 2)
        print(midpoint)
        if midpoint > usernumber:
            print("your number is high")
        else:
            print("your number is too high")
    elif usernumber < comp_number:
        end = usernumber
        midpoint = (start + end / 2)
        print(midpoint)
        if midpoint < comp_number:
            print("your number is low")
        else:
            print("your number is too low")

    else:
        print("invalid")
