#Print the first ArmStrong number in the range of 1042000 to 702648265 and exit the loop as soon as you encounter the first armstrong number. Use while loop
n = 1042000
while n <= 702648265:

    order = len(str(n))

    s=0

    num = n

    while num > 0:    

        digit = num % 10

        s += digit ** order

        num //= 10

    if n == s:

        print("The first armstrong number is :",n)

        break

    n += 1
