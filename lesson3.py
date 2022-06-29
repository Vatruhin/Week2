# num1 = int(input('num1 = '))
# num2 = int(input('num2 = '))
# if num1 > num2:
#     print(f'{num1} > {num2}')
# elif num1 < num2:
#     print(f'{num1} < {num2}')

# num1 = int(input('num 1: '))
# num2 = int(input('num 2: '))
# operator = input("operator: ")
# if operator == "+":
#     print(num1+num2)
# elif operator == "-":
#     print(num1-num2)
# elif operator == "*":
#     print(num1*num2)
# elif operator == "/":
#     print(num1/num2)

# lists = [1, 2, 5]
# if 3 in lists:
#     print("its here")
# else:
#     print("oops")

# lists = [18, 19, 21, 27, 29]
# if 18 in lists and 21 in lists:
#     print("its here")

# lists = [18, 19, 21, 27, 29]
# if 18 in lists or 20 in lists:
#     print("its here")

# lists = list(range(1, 1001))
# lists_new = []
# for i in lists:
#     if (i%3)==0 and (i%5)==0 and (i%15)==0:
#         lists_new.append(i)
# print(lists_new)

# temp = float(input('Your temperature : '))
# question = input('Is it C or F? : ')
# if question == "C":
#     print("Its ", temp * 1.8 + 32, "in Fahrenheit")
# elif question == "F":
#     print("Its", (temp - 32)/1.8, "in Celcius")

# temp = float(input('Your temperature : '))
# if temp < -273.15:
#     print('Its cant be true')
# elif temp == -273.15:
#     print('Its equal to absolute zero!')
# elif -273.15 <= temp < 0:
#     print('Its lower then freezing point!')
# elif temp == 0:
#     print('Its freezing point!')
# elif 0 < temp < 100:
#     print('Its normal temperature')
# elif temp == 100:
#     print('Its boiling point!')
# elif temp > 100:
#     print('Its grater then boiling point!')

# year = int(input("Input a year : "))
# if (year % 4) == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Yes")
#     print('yes')
# else:
#     print("No")

# num1 = int(input('enter a numb : '))
# for i in range(1, 11):
#     print(i * num1)