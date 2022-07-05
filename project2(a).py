a=0
b=1
n=int(input("Enter how mmany times you want to generate a series :"))
print("Fibonacci series:")
print(" ",a," ",b,end="")
for i in range (n):
  c=a+b
  a=b
  b=c
  print(" ",c,end="")
