"""
setup structure
- create menu
- add tasks by appending to lists
- view tasks display tasks with a loop
- remove/complete tasks
- implement exit
- error handling
"""

def add_task(prompt):   
    return todo_list.append(prompt)

def view_task():    
    return print(todo_list)

def del_task(i):
    pass

def library():
    pass

todo_list = ['1','2','3']
while True:    
    print('1. Add\n2. View\n3. Remove\n')
    option = int(input('Enter your number: '))
    
    if option == 1:
        prompt = input(str('Input the task you would like to add.\n'))
        add_task(prompt)
    elif option == 2:
        view_task()
    elif option == 3:
        # inp = input(int('Which task would you like to remove?\n'))
        # del_task(inp)
        print('This option will remove a task.')
    elif option == 4:
        print('This option will library a task.')
    elif option == 5:
        break
    else:
        print('Invalid Input, Please try again.')