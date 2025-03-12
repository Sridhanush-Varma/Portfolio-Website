import random
print("Welcome to a small game of gambling!")
bet=input(print("Enter the bet type (T/N)"))
#T=type of number
#N=Specific number
#anyhting other than that is all in
money=1000

if bet()=="T":
   T=input(print("Enter odd or even"))
   if T()=="odd":
       O=1,3,5
       O="Odd"
       print("Confirmed")
   else:
           E=2,4,6
           E="Even"
           print("Confirmed")

elif bet()=="N":
    N=input(print("Enter a specific number"))

else:
    T=input(print("Enter odd or even"))
    if T()=="odd":
        O=1,3,5
        O="Odd"
        print("Confirmed")
    else:
        E=2,4,6
        E="Even"
        print("Confirmed")
        N=input(print("Enter a specific number"))

roll_dice = input("Do you wanna roll the dice? : ")

if roll_dice == "yes" or "y":
   posiblle_results = [1, 2, 3, 4, 5, 6]
   result = random.choice(posiblle_results)
   print("Result of dice rolling is : " + str(result))
else:
    print("Try again later")