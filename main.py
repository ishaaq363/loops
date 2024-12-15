
# for i in range(1,11,2):
#          print(i)

# for i in range(11,2):
#          print(i)

# str="coding"  

# for i in str:
#      print(i)

# number=int(input("enter number"))
# for i in range(1,11):
#     print(number , "*",i,"=",number*i)
         
# sumofnormalno=sum(range(1,11))
# print(sumofnormalno)

num = int(input("Enter number to be verified :"))

flag = False

if num > 1:
    
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break


if flag:
    print(num, "is not a prime No. Ishaaq sir") 

else:
      print(num, "Is prime a No. Ishaaq sir")       