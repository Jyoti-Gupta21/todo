def get_todo(filepath="todos.txt"):
    # doc-string
    """Read a text file and return the list of to-do items"""
    
    with open(filepath,'r') as file_local:
            todos_local=file_local.readlines()
            return todos_local
        

def write_todo(todos_arg, filepath="todos.txt"):
    """Write the to-do item list in the text file"""
    with open(filepath,'w') as file:
            file.writelines(todos_arg)