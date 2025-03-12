#As for the assignment, I had a similar idea to late book sumbmissions to library 
#but this program is more of an interface for police to interact to upload 
#the traffic disobident related charges and calculate it accordingly.
#H=No helmet charges
#T=Triple riding
#P=No parking
import time
H=500
T=800
P=1000
print("Welcome to Traffic Police Data Entry interface of HYPD")
vechile=input("Enter Vechile Type:")
answer=input("Please Enter the Offence Commited:")
if answer.upper()=="HTP":
    fine=H+T+P
elif answer.upper()=="HT":
    fine=H+T
elif answer.upper()=="TP":
    fine=T+P
elif answer.upper()=="PH":
    fine=P+H
elif answer.upper()=="H":
    fine=H
elif answer.upper()=="T":
    fine=T
else:
    fine=P
Processing="Processing....."
for char in Processing:
    print(char,end='') 
    time.sleep(0.2)
time.sleep(2)
print("\nThe total Fine/Challan of the",vechile,"is:",fine,"/- Rupees")
