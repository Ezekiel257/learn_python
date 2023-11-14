def my_func():
    print("This is my first function")

#my_func()

def check_prime_number(num):
    number = int(num)
    condition = 0
    count = 2
    iteration = 0

    # Go through a number of iterations where the iteration
    # is less than or equal to half of our initial number
    while iteration <= number / 2:
        if number % count == 0:
            print(f"Condition met at iteration = {iteration}")
            condition = 1
            break
        iteration += 1

    if condition == 0:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

#check_prime_number(35)
#check_prime_number(40)
#check_prime_number(45)
#check_prime_number(50)
#check_prime_number(55)

#defining arguements 
def total_calc(bill_amount,tip_perc=10):
  total = bill_amount*(1 + 0.01*tip_perc)
  total = round(total,2)
  print(f"Please pay ${total}")

#total_calc(150)
#total_calc(200, 15)
#total_calc(165, 7.5)
#total_calc(20)

#adding * to specify infinite
def add_num(*args):
    final_num = 0
    print(f"Type of arguement is: {type(args)}")
    
    for num in args:
        final_num += num

    return final_num

#print(add_num(1,3,5,7.23))

#print("Using the sum function instead", sum([1,2,3,4,5]))

#using key word arguments in functions
def calc_num(num1, num2=0, num3=0):
    final_num = num1+ num2 - num3
    return final_num

#print(calc_num(5, num3=2))

#utilizing return value
def my_var_sum(*args):
  sum = 0
  for arg in args:
    sum += arg
  return sum

#my_var_sum(12)

#function scope
def calc_num(num1, **kwargs):
    num2 = kwargs.get("num2")
    num3 = kwargs.get("num3")
    final_num = 0

    for k,v in kwargs.items():
        final_num += v
    return final_num

#print(calc_num(1, num3=2, num2=7, num4=3, num5=6))

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
protein = ["chicken", "babe", "whey"]
#my_function(fruits)
my_function(protein)

#recursion function
#which means a defined function can call itself.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


