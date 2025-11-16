# new = [ 1, 2, 4, 6, 7]
# newEven = []

# for index in range(len(new)):
#     if new[index] % 2 == 0:
#         newEven.append(new[index] ** 2)

# print(newEven) # 4, 16, 36


# fruits = [ "apple", "banana", "cherry"]

# # for i in range(len(fruits)):
# #     print(fruits[i])

# for fruit in fruits:
#     print(fruit)


# numList = [1, 5, 67, 78, 84]
# total = 0
# print(numList)
# for num in numList:
#     # print(f" Total before addition: {total} ")
#     # print(f"{total} + {num} = {total + num}")
#     total += num
    
# print(total)


# nameList = ["shuvo hossen", "sultana islam isha", "samad islam"]

# #Shuvo Hossen

# for name in nameList:
#     print(name.title())
    

# newList = [1, 5, 9, 13, 6, 8, 15, 20, 23, 35, 49]
# newNum = []


# for num in  newList:
#     if num % 5 == 0:
#         continue 
#     newNum.append(num)

# print(newNum)

# newList = [1, 5, 9, 13, 15, 20, 23, 35, 49]
# numList = []

# for num in newList:
#     if num == 20:
#         break
#     print(num)


    # 1.....100
    # num % 3 == 0 -> print(Fizz)
    # num % 5 == 0 -> print(Buzz)
    # num%3 ==0 and num % 5 == 0-> print(FizzBuzz)
    # print(num) 
    
for i in range(1,101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
