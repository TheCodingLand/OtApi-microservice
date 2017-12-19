#List folders for objec
folders = { 'Events' : '' , 'Tickets' : '' }

def generate():
    for folder in folders:
        fields = getAllFields(folder)
        #write a json file on listing all the fields possible with name and type for objects
        
        
