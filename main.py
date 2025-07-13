
# functions
def add_task(prompt):
    print(("=" * 6) + "Task Added!" + ("=" * 6))   
    return todo_list.append(prompt)  

def view_task():    
    return print(todo_list)

def del_task(i):
    print(("=" * 4) + "Task removed!" + ("=" * 4))  
    return todo_list.pop(i)

def library():
    pass

def seperator():
    return print('=' * 30)

# init list
todo_list = ['1','2','3']

# intro
print("To-Do List")
seperator()
    
# run program
while True:    
    # option inputs        
    print('1. Add\n2. View\n3. Remove\n4. Library\n5. Exit')
    seperator()
    option = int(input('Enter your number: '))
    seperator()
    
    # option handlings
    if option == 1:
        prompt = input(str('Input the task you would like to add.\n- '))
        add_task(prompt)
    elif option == 2:
        view_task()
    elif option == 3:
        inp = int(input('Which task would you like to remove?\n- '))
        inp_index = inp - 1
        seperator()
        del_task(inp_index)
    elif option == 4:
        print('This option will create a library for tasks to be displayed in the terminal.')
        seperator()
    elif option == 5:
        break
    else:
        print('Invalid Input, Please try again.')