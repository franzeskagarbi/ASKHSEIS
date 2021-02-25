def linetodict(x):
   pl=0
   for i in range(0,len(x),2):
         dictionary={x[i]:x[i+1]}
         pl=pl+1
   return pl

file=input("Δώσε το όνομα του λεξικού αρχείου: ")
maxi=0
rfile=open(file,"r")
for line in rfile:
   if (line == "\n"):
     maxi=0
   else:
      pl=0
      pl1=0
      pl2=0
      x=line.split()
      print(x)
      pl=linetodict(x)
      for word in line:
         if "[" in word :
            pl1=pl1+1
         if "{" in word :
            pl2=pl2+1
         if "[" in word :
            if "{" in word:
               pl=pl=+1
         if "{" in word :
            if "[" in word :
               pl=pl+1
      if pl1>=2 :
         pl=pl+1
      if pl2>=2:
         pl=pl+1
      if (pl>maxi):
         maxi=pl
print("Το μέγιστο βάθος είναι : ",maxi)
rfile.close()
