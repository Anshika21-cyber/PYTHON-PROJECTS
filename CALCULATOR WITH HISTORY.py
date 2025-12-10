HISTORY_FILE="HISTORY.txt"
def show_history():
    file= open("HISTORY.txt","r")
    lines=file.readlines()
    if(len(lines)==0):
        print("N0 HISTORY FOUND!")
    else:
        for i in reversed(lines):
            print(i)
            print("\n")

    file.close()

def clear_history():
    file= open("HISTORY.txt","w")
    file.close()
    print("HISTORY CLEARED!")

def exit():
    print("GOODBYE! HAVE A NICE DAY.")

def save_to_history(user_input,result):
    file= open("HISTORY.txt","a")
    file.write(user_input + "=" +  str(result) )
    file.close()

def calculate(user_input):
    eqn=user_input.split()
    if len(eqn)!=3:
        print("INVALID INPUT.Enter in this format--->A+B(e.g. 3+5)")
    else:
        num1=float(eqn[0])
        num2=float(eqn[2])
        op= eqn[1]
    if op=="+":
        result=num1+num2
    elif op=="-":
        result=num1-num2 
    elif op=="*":
        result=num1*num2
    elif op=="/":
           if num2==0:
               print(" SORRY! Cannot divide by 0")
           else:
               result=num1+num2
    elif op=="%":
           if num2==0:
               print(" SORRY! Cannot divide by 0")
           else:
               result=num1%num2
    else:
        print("INVALID input.Choose from (+ _ * % / )")

    if result==int(result):
        result=int(result)
        print("result:",result)
        save_to_history(user_input,result)


def main ():

    print("----------SIMPLE CALCULATOR-------------")
    while True:
       user_input=input("Enter CALCULATION(+ - * % /) or command history,clear, exit:")
       if user_input=="history":
           show_history()
       elif user_input=="clear":
           clear_history()
       elif user_input=="exit":
           exit()
       else:
           calculate(user_input)
    #    else:
     
    
    #        print("INVALID ENTER.")

main()



    