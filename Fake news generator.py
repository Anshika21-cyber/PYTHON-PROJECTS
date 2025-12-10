import random
choice="yes"
l=[]
while choice=="yes":
   name=["Rohit Sharma" ,"Ananya" , "krish" ,"Narender Modi" , "Suhani" ,"Ironman"]
   other=["with enemies", "with dog","with 5 year old child","with wife"]
   places=["Park" ,"Auditorium", "Hall", "Ground","Shopping Mall", "Research center"]
   things=["playing" , "doing exercise" ,"fighting" ,"dancing " ,"Flying" ,"cooking"]



   NAME=random.choice(name)
   PLACES=random.choice(places)
   THINGS=random.choice(things)
   
   OTHERS=random.choice(other)

   line=f"{NAME} is {THINGS} {OTHERS} in {PLACES}"

   print("BREAKING NEWS ! \n", line)
   l.append(line)
   choice=input("\n Do you want another news(yes/no)").strip().lower()
   if choice=="no":
      break
   else:
      continue
   
print("Thanks ")
print("\n All generated news are:\n",l)

