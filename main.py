# import modules.functions as functions
# from functions import get_todo, write_todo
from modules import functions

while True:
    # Get user input and strip space chars from it
    user_action=input("Type add, show, edit, complete or exit: ")
    user_action=user_action.strip()
    
    
    if user_action.startswith("add"):
        todo=user_action[4:]
        
        # file=open('todos.txt','r')
        # todos=file.readlines()
        # file.close()
        
        # with context manager---it automatically closes the file
        # with open('todos.txt','r') as file:
        #     todos=file.readlines()
        
        todos=functions.get_todo()
        
        todos.append(todo+'\n')
        
        # file=open('todos.txt','w')
        # file.writelines(todos)
        # file.close()
        
        functions.write_todo(todos)
    
    elif user_action.startswith("show"):
        # file=open('todos.txt','r')
        # todos=file.readlines()
        # file.close()
        
        # with open('todos.txt','r') as file:
        #     todos=file.readlines()

        todos=functions.get_todo()
        
        # new_todos=[item.strip('\n') for item in todos] -----list comprehension
        
        for index, item in enumerate(todos):
            item=item.strip('\n')
            row=f"{index+1}-{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number=int(user_action[5:])
            print(number)
            number=number-1
            
            todos=functions.get_todo()
            
            new_todo=input("Enter new todo: ")
            todos[number]=new_todo+'\n'
            
            functions.write_todo(todos)
            
        except ValueError:
            print("Your command is not valid!")
            continue
        
    elif user_action.startswith("complete"):
        try:
            number=int(int(user_action[9:]))
            
            todos=functions.get_todo()
            
            index=number-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)
            
            functions.write_todo(todos)
                
            message=f"todo {todo_to_remove} was removed from the list."
            print(message)
        
        except IndexError:
            print("There is no item with that number")
            continue
        
    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid Command!")
        
print("Bye!")