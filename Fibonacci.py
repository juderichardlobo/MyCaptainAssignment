
#Input Block 
fibonacci = int(input("How many numbers in the fibonacci sequence do you want? "))
n1, n2 = 0, 1
#by default these have to be ur first two terms because it is fibonacci
count = 0
#will initialize count positive


#Condition Block
#Since fibonacci operates only in positive, we need to ensure it doesnt accept negative non integers
if fibonacci <= 0:
   print("Please enter a value that is both positive and an integer")
elif fibonacci == 1:
   print("The Fibonacci sequence is solitary and hence by arithmetic law is ",fibonacci,":")
   print(n1)
else:
   print("The Fibonacci sequence thus identified is :")
   while count < fibonacci:
       print(n1)
       last = n1 + n2
       #this will update the values
       n1 = n2
       n2 = last
       count += 1
       #this will accept until the final value is within the fibonacci range

   print("The values mentioned above conclude the list of fibonacci numbers up and until : ",fibonacci,)
