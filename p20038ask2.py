def fibonacci(n):
    a=1
    b=1
    s=0
    import random
    if n==1 or n==2:
        print("Ο όρος της ακολουθίας Fibonacci που δώσατε δεν είναι πρώτος αριθμός" )
    else:
      for i in range(2,n,1):
       c=a+b
       a=b
       b=c
      for i in range(0,20,1):
         n=random.randint(1,100)
         if((n**c)%c==n%c):
            s=s+1
      if (s==20):
       print("Ο όρος της ακολουθίας Fibonacci που δώσατε είναι πρώτος αριθμός")
      else:
       print("Ο όρος της ακολουθίας Fibonacci που δώσατε δεν είναι πρώτος αριθμός")

n=int(input("Δώσε τον n όρο της ακολουθίας Fibonacci: "))
while n<=0:
    print("Μη έγκυρη τιμή!")
    n=int(input("Ξαναδώσε τον n όρο της ακολουθίας Fibonacci: "))    
fibonacci(n)
