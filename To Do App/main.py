def task():
    tasks=[]
    print("WELCOME TO THE TO-D0 LIST")
    task_name = input("Enter Today's Task : ")
    tasks.append(task_name)

    # Total Tasks are ???
    print(f"All Tasks are: {str(tasks)}")
    
    while True:
        try:
            operation = int(input("Choose the following : \n 1-Add \n 2-Delete \n 3-View \n 4-Exit \n You choose : "))
            if operation == 1:
                add = input("Enter task you want to add = ")
                tasks.append(add)
                print(f"Task '{add}' has been successfully added.")
            
            elif operation == 2:
                del_val = input("Which task you want to delete = ")
                if del_val in tasks:
                    ind = tasks.index(del_val)
                    del tasks[ind]
                    print(f"Task '{del_val}' has been deleted.")
                else:
                    print("Task not found.")
            elif operation == 3:
                print(f"Total tasks = {tasks}")
            elif operation == 4:
                print("Closing the program....")
                break
            else:
                print("Invalid Input. Please choose options between 1 to 4.")
        except ValueError:
            print("Invalid Input. Please enter a valid number.")

task()





           