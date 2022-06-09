from tkinter import * 
root=Tk()
root.title("Geometry Error")

try :
    root.geometry("600")
    
except:
        print("Bad Geometry Error, only one dimension passed in geometry instead of 2")
        
        root.mainloop()