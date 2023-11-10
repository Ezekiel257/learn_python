#Collect an input, basically some random numbers
num = input("Enter Number:")
number = int(num)
condition = 0
count = 2
iteration = 0

#go through a number of iterations where the iteration is 
# less than or equal to our initial number
while iteration <= number/ 2:
    if number % count == 0:
        print(f"condition met at iteration = {iteration}")
        condition = 1
        break
    iteration += 1

if condition == 0:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")

#names = ["James", "Joseph", "john", "james", "John"]
#unique = set()
#for name in names:
#    if name.islower():
#        unique.add(name)
#        continue
#    unique.add(name.lower())
#print(unique)
