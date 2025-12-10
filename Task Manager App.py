def Tasks():
     print("_________________________________________WELCOME TO TASK MANAGEMENT APP______________________________________________")
     print("Enter all the tasks you want to add to the queue:")
     tasks=input().split()
     n=len(tasks)
     print(f"Your have total a total of {n} number of tasks for today")
     show_tasks(tasks)
     return tasks

def show_tasks(tasks):
     for index,i in enumerate(tasks ,start=1):
          print(f"your {index} task is {i}" )


def update_task(tasks):
     print("Enter the task you want to update::")
     prev_task=input()
     print(f"\n Enter the task you want to do in replacement of {prev_task}::")
     updated_task=input()
     if prev_task in tasks:
          idx = tasks.index(prev_task)
          tasks[idx] = updated_task
     else:
        print(f"Task '{prev_task}' not found.")

     print("-----------Your updated list is-----------\n")
     show_tasks(tasks)



def delete_task(tasks):
     print("\n Enter the task you want to delete::")
     delete=input()
     if delete in tasks:
         tasks.remove(delete)
     else:
        print(f"Task '{delete}' not found.")

     show_tasks(tasks)

def add_task(tasks):
    add=input("Write the task you want to add to the queue:").split()
    tasks.extend(add)
    print("---------New list----------")
    show_tasks(tasks)

def main():
     tasks=Tasks()
     while True:
          print("...............Do you want any changes like \n 1.Add \n2.Delete \n3.Update \n 4.want to see tasks or exit............")
          choice=input().strip().lower()
          if choice=="add" :
               add_task(tasks)
          elif choice=="update" :
               update_task(tasks)
          elif choice=="delete":
               delete_task(tasks)
          elif choice=="want to see tasks":
               show_tasks(tasks)
          else:
               print("Exiting the program.........")
               exit()
        
main()