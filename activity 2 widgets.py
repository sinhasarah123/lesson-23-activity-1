from cProfile import label
from tkinter import *
from datetime import date
root=Tk()
root.title("widgets demo")
root.geometry("400x300")
lbl=Label(text="Hello!",fg='white',bg="#0091e4",height=1,width=300)
name_label=Label(text="full name:",bg="#e12c93")
name_entry=Entry()
def display():
    name=name_entry.get()
    global Message
    message="welcome\n todays date is "+str(date.today())
    greet="hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
text_box=Text(root,height=10,width=50)
btn=Button(root,text="submit",command=display)
lbl.pack()
name_label.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()