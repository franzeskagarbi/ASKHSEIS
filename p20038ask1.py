array=[]
pl=0
athroisma=0
mo=0
import random
for n in range(0,100,1):
 dimension= int(input("Δώσε διάσταση: "))
 while dimension<=0:
     print("Μη έγκυρα δεδομένα!")
     dimension=int(input("Ξαναδώσε δίασταση: "))
 rows=dimension
 cols=dimension
 theseis=dimension*dimension
 gemisma=theseis//2
 if theseis<=9:
     pass
 else:
  for i in range(0,rows,1):
      array.append([])
      for j in range(0,cols,1):
          array[i].append([])
  for i in range(0,gemisma-1,1):
      number1=random.randint(0,dimension-1)
      number2=random.randint(0,dimension-1)
      while array[number1][number2]==1:
          number1=random.randint(0,dimension-1)
          number2=random.randint(0,dimension-1)               
      array[number1][number2]=1
  for i in range(0,rows,1):
    for j in range(0,cols-3,1):
        if array[i][j]==array[i][j+1]==array[i][j+2]==array[i][j+3]==1:
            pl=pl+1
  for j in range(0,cols,1):
    for i in range(0,rows-3,1):
        if array[i][j]==array[i+1][j]==array[i+2][j]==array[i+3][j]==1:
            pl=pl+1
  for i in range(0,rows-3,1):
     for j in range(0,cols-3,1):
       if i==j:
           if array[i][j]==array[i+1][j+1]==array[i+2][j+2]==array[i+3][j+3]==1:
              pl=pl+1
       if i+j== dimension +1:
          if array[i][j]==array[i+1][j-1]==array[i+2][j-2]==array[i+3][j-3]==1:
              pl=pl+1
  athroisma=pl+athroisma
mo=athroisma/100
print("Ο μέσος όρος είναι" ,mo)
