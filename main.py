# functions
def add_task(prompt):
    print(("**" * 6) + "Task Added!" + ("**" * 6))   
    return todo_list.append(prompt)  

def view_task():
    counter = 0
    for task in todo_list:
        counter += 1
        print(f'{counter}. {task}')
    return

def del_task(i):
    print(("**" * 4) + "Task removed!" + ("**" * 4))  
    return todo_list.pop(i)

def seperator():
    return print('=' * 30)

def intro():
    seperator()
    print("To-Do List")
    seperator()
    
# init list
todo_list = []

# intro
intro()

# run program
display = True
while display:   
    # option inputs        
    print('1. Add\n2. View\n3. Remove\n4. Exit')
    seperator()
    option = int(input('Enter your number: '))
    seperator()

    # option handlings
    if option == 1:
        prompt = str(input('Input the task you would like to add.\n- '))
        add_task(prompt)
    elif option == 2:
        print('')
        view_task()
        print('')
        seperator()
    elif option == 3:
        inp = int(input('Which task would you like to remove?\n- '))
        inp_index = inp - 1
        seperator()
        del_task(inp_index)
    elif option == 4:
        display = False
    else:
        print('Invalid Input, Please try again.') 
else:
        print('Closing...')