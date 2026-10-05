# Named function without input and without return
#declaration
# def printHelloWorld():
#     print("Hello World")
# #calling
# printHelloWorld()

#adding 2 numbers
#defining or declaration
# def addTwo():
#     a=10
#     b=20
#     sum=a+b
#     print("sum of 2 numbers =",sum)
# #calling
# addTwo()

#write the code to display the smallest number from given number
# def smallNum():
#     a=10
#     b=20
#     c=30
#     if a<b and a<c:
#         print(a,"is smallest number")
#     elif b<a and b<c:
#         print(b,"is smallest number")
#     else:
#         print(c,"is smallest number")
# #calling
# smallNum()


# named function with input and without return
# def displayName(name):
#     print(name)
# displayName("Hero")

# write the logic to check given number is even or odd
# def checkEven(n):
#     if n%2==0:
#         print(n,"is even")
#     else:
#         print(n,"is odd")
# checkEven(4)

# avg of three numbers
# def avgOfThree(n1,n2,n3):
#     avg=(n1+n2+n3)/3
#     print(f"avg of {n1},{n2} and {n3} avg={avg}")
# avgOfThree(13,10,14)

#named function without input and with return
# def displayName():
#     name="Hero"
#     return name
# myName = displayName()
# print(myName)

# def findFactorial():
#     n=5
#     fact=1
#     for i in range(1,n+1,1):
#      fact=fact*i
#     return fact
# factorial=findFactorial()
# print(factorial)

# write the code to return the sum of even numbers in range of 1 to 10
# def sumOfEven():
#   for i in range(1,11,1):
#     sum=0
#     if i%2==0:
#         sum=sum+i
#     return sum
#   sumEven=sumOfEven()
#   print(sumEven)


# named function with input and with return
# def displayName(myName):
#     return myName
# name=displayName("Hero")
# print("My name is ",name)


#------------------FUNCTIONS TASKS---------------------
# WITHOUT INPUT AND WITHOUT RETURN
# 1. even or odd
# def evenOdd():
#     n=10
#     if n%2==0:
#         print("Even")
#     else:
#         print("Odd")
# evenOdd()

# 2. positive,negative or zero
# def checkNum():
#     n=-5
#     if n>0:
#         print("Positive")
#     elif n<0:
#         print("Negative")
#     else:
#         print("Zero")
# checkNum()

# 3. Largest of 2 numbers
# def largest():
#     a=30
#     b=40
#     if a>b:
#         print(a)
#     else:
#         print(b)
# largest()

#4. Find the largest number of three numbers
# def largeNum():
#     a=35
#     b=40
#     c=50
#     if a>b and a>c:
#         print(a)
#     elif b>a and b>c:
#         print(b)
#     else:
#         print(c)
# largeNum()

# 5.check number prime or not
# def checkPrime():
#     n=17
#     count=0
#     for i in range(1,n+1,1):
#         if n%i==0:
#             count= count+1
#     if count==2:
#         print("Prime")
#     else:
#         print("Not Prime")
# checkPrime()

# 6.check whether number is palindrome or not
# def palindrome():
#     n=121
#     for i in range(1,n+1,1):
#         original=n
#         reverse=0
#         while n>0:
#             ld=n%10
#             reverse=reverse*10+ld
#             n=n//10
#     if original==reverse:
#         print("Palindrome")
#     else:
#         print("Not a Palindrome")
# palindrome()


# 7. find armstrong number from 1 to 1000
# def armstrong():
#     for i in range(1,1001,1):
#         n=i
#         sum=0
#         while n>0:
#             digit=n%10
#             sum=sum+digit**3
#             n=n//10
#         if sum==i:
#             print(i)
# armstrong()

# 8. find perfect number 1 to 1000
# def perfectNum():
#     for j in range(1,1001,1):
#         sum=0
#         for i in range(1,j,1):
#             if j%i==0:
#                 sum=sum+i
#         if sum==j:
#             print(i)
# perfectNum()

# 9. find prime factors of a number
# def primeFactors():
#     n=84
#     for j in range(2,n+1,1):
#         count=0
#         for i in range(1,j+1,1):
#             if j%i==0:
#                 count=count+1
#         if n%j==0 and count==2:
#             print(j)
# primeFactors()

# 10. find the number with maximum factors from 1 to 100
# def maxFactors():
#     max_count=0
#     max_number=0
#     for j in range(1,101,1):
#         count=0
#         for i in range(1,j+1,1):
#             if j%i==0:
#                 count=count+1
#         if count>max_count:
#             max_count=count
#             max_number=i
#     print(max_number)
#     print(max_count)
# maxFactors()
#--------------------------------------------------------
# WITH INPUT AND WITHOUT RETURN

#1. find prime number
# def prime(n):
#     count=0
#     for i in range(1,n+1,1):
#           if n%i==0:
#                count=count+1
#     if count==2:
#          print("Prime")
#     else:
#          print("Not Prime")
# n=int(input("Enter a Number :"))
# prime(n)

# 2. check whether a number is palindrome
# def palindrome(n):
#     original=n
#     reverse=0
#     while n>0:
#         digit=n%10
#         reverse=reverse*10+digit
#         n=n//10
#     if original==reverse:
#         print("Palindrome")
#     else:
#         print(" not a Palidrome")
# n=int(input("Enter a number :"))
# palindrome(n)

# 3.find the factorial of a number
# def factorial(n):
#     fact=1
#     for i in range(1,n+1,1):
#         fact=fact*i
#     print(fact)
# n=int(input("Enter a Number :"))
# factorial(n)

# 4.find sum of digits of a number
# def digits_sum(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit
#         n=n//10
#     print(sum)
# n=int(input("Enter a Number :"))
# digits_sum(n)

# 5.check whether a number is armstrong or not
# def armstrong(n):
#     original=n
#     sum=0
#     while n>0:
#         digit=n%10
#         sum=sum+digit**3
#         n=n//10
#     if sum==original:
#         print("Armstrong")
#     else:
#         print("Not Armstrong")
# n=int(input("Enter a Number :"))
# armstrong(n)

# 6.find the reverse of a number
# def reverseNum(n):
#     reverse=0
#     while n>0:
#         digit=n%10
#         reverse=reverse*10+digit
#         n=n//10
#     print(reverse)
# n=int(input("Enter a Number :"))
# reverseNum(n)

# 7. find the sum of even digits in a number
# def evenDigits_sum(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         if digit%2==0:
#             sum=sum+digit
#         n=n//10
#     print(sum)
# n=int(input("Enter a Number :"))
# evenDigits_sum(n)

# 8.find product of digits of number
# def product_digits(n):
#     product=1
#     while n>0:
#         digit=n%10
#         product=product*digit
#         n=n//10
#     print(product)
# n=int(input("Enter a Number :"))
# product_digits(n)

# 9.find the largest digit in a number
# def largest_digit(n):
#     largest=0
#     while n>0:
#         digit=n%10
#         if digit>largest:
#             largest=digit
#         n=n//10
#     print(largest)
# n=int(input("Enter a Number :"))
# largest_digit(n)

# 10. find the smallest digit in a number
# def smallest_digit(n):
#     smallest=9
#     while n>0:
#         digit=n%10
#         if digit<smallest:
#             smallest=digit
#         n=n//10
#     print(smallest)
# n=int(input("Enter a Number :"))
# smallest_digit(n)
#--------------------------------------------------------------------------------
#WITHOUT INPUT AND WITH RETURN

# 1. find the square of a number
# def square():
#     n=6
#     return n*n
# result=square()
# print(result)

# 2. find the cube of a number
# def cube():
#     n=5
#     return n*n*n
# result=cube()
# print(result)

# 3. sum of first  n natural numbers
# def sum_Natural():
#     n=10
#     sum=0
#     for i in range(1,n+1,1):
#         sum=sum+i
#     return sum
# result=sum_Natural()
# print(result)

# 4. find the factorial of a number
# def factorial():
#     n=6
#     fact=1
#     for i in range(1,n+1,1):
#         fact=fact*i
#     return fact
# result=factorial()
# print(result)

# 5. find the reverse of a number
# def reverse_number():
#     n=1234
#     reverse=0
#     while n>0:
#         ld=n%10
#         reverse=reverse*10+ld
#         n=n//10
#     return reverse
# result=reverse_number()
# print(result)

# 6. check whether the given number is perfect number or not
# def perfect():
#     n=28
#     sum=0
#     for i in range(1,n,1):
#         if n%i==0:
#             sum=sum+i
#     if sum==n:
#         return "perfect Number"
#     else:
#         return "not a perfect number"
# result=perfect()
# print(result)

# 7. check whether a number is armstrong 
# def armstrong():
#     n=153
#     original=n
#     sum=0
#     while n>0:
#         ld=n%10
#         sum=sum+ld**3
#         n=n//10
#     if sum==original:
#         return "Armstrong Number"
#     else:
#         return "Not an Armstrong Number"
# result=armstrong()
# print(result)

# 8. find the largest digit in a number
# def largest_digit():
#     n=583246
#     largest=0
#     while n>0:
#         digit=n%10
#         if digit>largest:
#             largest=digit
#         n=n//10
#     return largest
# result=largest_digit()
# print(result)

# 9. find the smallest digit
# def smallest_digit():
#     n=784277
#     smallest=9
#     while n>0:
#         digit=n%10
#         if digit<smallest:
#             smallest=digit
#         n=n//10
#     return smallest
# result=smallest_digit()
# print(result)

# 10. find sum of even digits in a number
# def even_digits_sum():
#     n=58346
#     sum=0
#     while n>0:
#         digit = n%10
#         if n%2==0:
#             sum=sum+digit
#         n=n//10
#     return sum
# result=even_digits_sum()
# print(result)
#--------------------------------------------------------------------------------------------
# WITH INPUT AND WITH RETURN

# 1. find the square of a number
# def square(n):
#     return n*n
# n=int(input("Enter a Number :"))
# result=square(n)
# print(result)

# 2. find the cube of a number
# def cube(n):
#     return n*n*n
# n=int(input("Enter a Number :"))
# result=cube(n)
# print(result)

# 3. find the sum of prime numbers upto N
# def sum_prime(n):
#     sum=0
#     for j in range(2,n+1,1):
#         count=0
#         for i in range(1,j+1,1):
#             if j%i==0:
#                 count=count+1
#         if count==2:
#             sum=sum+j
#     return sum
# n=int(input("Enter a Number :"))
# result=sum_prime(n)
# print(result)

# 4. find the GCD of two numbers
# def gcd(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a
# a=int(input("Enter a Number :"))
# b=int(input("Enter a Number :"))
# result=gcd(a,b)
# print(result)

# 5. find strong number
# def strong(n):
#     original=n
#     sum=0
#     while n>0:
#         digit=n%10
#         fact=1
#         for i in range(1,digit+1,1):
#             fact=fact*i
#         sum=sum+fact
#         n=n//10
#     if sum==original:
#         return "Strong Number"
#     else:
#         return "Not Strong Number"
# n=int(input("Enter a Number :"))
# result=strong(n)
# print(result)

# 6. count the no.of digits
# def count_digits(n):
#     count=0
#     while n>0:
#         count=count+1
#         n=n//10
#     return count
# n=int(input("Enter a Number :"))
# result=count_digits(n)
# print(result)

# 7. reverse a number
# def reverse_number(n):
#     reverse=0
#     while n>0:
#         digit=n%10
#         reverse=reverse*10+digit
#         n=n//10
#     return reverse
# n=int(input("Enter a Number :"))
# result=reverse_number(n)
# print(result)

# 8. sum of even digits
# def sum_even_digits(n):
#     sum=0
#     while n>0:
#         digit=n%10
#         if digit%2==0:
#             sum=sum+digit
#         n=n//10
#     return sum
# n=int(input("Enter a Number :"))
# result=sum_even_digits(n)
# print(result)

# 9. product of digits
# def product_digits(n):
#     product=1
#     while n>0:
#         digit=n%10
#         product=product*digit
#         n=n//10
#     return product
# n=int(input("Enter a Number :"))
# result=product_digits(n)
# print(result)

# 10. largest digit
# def largest_digit(n):
#     largest=0
#     while n>0:
#         digit=n%10
#         if digit>largest:
#             largest=digit
#         n=n//10
#     return largest
# n=int(input("Enter a Number :" ))
# result=largest_digit(n)
# print(result)