num = int(input("Enter an integer: "))
if num % 2 == 0:
    # 3. Display result for even
    print("The number is even.")
else:
    print("The number is odd.")
total = 0
for i in range(1, 51):
    total += i  
print("The sum of integers from 1 to 50 is:", total)
