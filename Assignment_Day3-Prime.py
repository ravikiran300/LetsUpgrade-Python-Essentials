#2)Using for loop please print all the prime numbers between 1- 200 using FOR LOOP AND RANGE function.

lower = 1
upper = 200

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):

   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
