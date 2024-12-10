from tkinter import *
from datetime import date
root=Tk()
root.title("getting Started with Widgets")
root.geometry("400x300")
lbl=Label(text="Hey there",fg="white",bg="black",height=1,width=300)
namelbl=Label(text="full name",bg="blue")
nameentry=Entry()
def display():
    name=nameentry.get()
    global message
    message="Wellcome to the website \nTodays date is:"
    greet="hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)
btn=Button(text="Begin",command=display,fg="lightblue",bg="dark blue",height=1)
lbl.pack()
namelbl.pack()
nameentry.pack()
btn.pack()
text_box.pack()
root.mainloop()

