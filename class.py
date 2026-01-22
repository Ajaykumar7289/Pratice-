# a = float(input("enter: "))
# b = float(input("enter: "))
# c = input("operator: ")
# ans = 0
# if(c=="+"):
#     ans = a+b
# elif(c=="-"):
#     ans = a-b
# elif(c=="*"):
#     ans = a*b
# elif(c=="/"):
#     ans = a/b
# # print(ans)

# a = int(input("enter: "))
# b = int(input("enter: "))
# c = int(input("enter: "))
# heighest = max(a,b,c)
# print(heighest)

# p = int(input("enter: "))
# t = int(input("enter: "))
# r = int(input("enter: "))
# intrest = (p*t*r)/100
# print(f"interest is {intrest} and total including intrest is {intrest+p}")
# s = input("enter: ")

# if(s=="password"):
#     print("access granted")
# else:
#     print("password invalid")

# a = int(input("Enter amount: "))

# if a >= 200 and (a%100==0 and a != 300):
#     print("Withdrawable")
# else:
#     print("Not withdrawable")


while True:
    hour = int(input("Enter time (1–24): "))
    if 1 <= hour <= 24:
        break
    print("Invalid time, please enter again")

if hour < 12:
    print("Good Morning")
elif hour < 16:
    print("Good Afternoon")
elif hour < 20:
    print("Good Evening")
else:
    print("Good Night")



