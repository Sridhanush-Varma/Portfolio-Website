import time
name=(input("Please enter your name:"))
print("Welcome!",name,"its's time for a little Quiz!")
time.sleep(1)
print("Well it's more like a test to check you're general knowledge")
time.sleep(2)
answer=input("Are you ready to play the Quiz ? (y/n):")
print("Tips: 1. All answers must be answered in lowercases")
print("2. The difficulty of the Quiz increases gradually")
time.sleep(1)
print("All the best!")
score=0
total_questions=5
 
if answer.lower()=="y":
   answer=input("Question 1: Which animal is known as the 'Ship of the Dessert ?")
   if answer.lower()=="camel":
       score+=1
       time.sleep(2)
       print("Correct Answer!!!")
   else:
       time.sleep(2)
       print("Wrong Answer :(")
   time.sleep(1)
   answer=input("Question 2: Which is the most exposed organ of a human body ?")
   if answer.lower()=="skin":
       score+=1
       time.sleep(2)
       print("Correct Answer!!!")
   else:
       time.sleep(2)
       print("Wrong Answer :(")
   time.sleep(1)
   answer=input("Question 3: Which planet is the hottest in our solar system ?")
   if answer.lower()=="venus":
       score+=1
       time.sleep(2)
       print("Correct Answer!!!")
   else:
       time.sleep(2)
       print("Wrong Answer :(")
   time.sleep(1)
   answer=input("Question 4: What's the world's smallest country ?")
   if answer.lower()=="vatican city":
       score+=1
       time.sleep(2)
       print("Correct Answer!!!")
   else:
       time.sleep(2)
       print("Wrong ANswer :(")
   time.sleep(1)
   answer=input("Question 5: Who invented computer ?")
   if answer.lower()=="charles babbage":
       score+=1
       time.sleep(2)
       print("Correct Answer!!!")
   else:
       time.sleep(2)
       print("Wrong Answer :(")
else:
    print("Please try again when you're free!!")
print("Congratulasions! You have successfully completed the Quiz!")
print("Total score:",score,"Total Questions:",total_questions,"Questions answered correctly:",score)
mark=(score/total_questions)*100
print("Marks obtained:",mark)
print("Goodbye!")