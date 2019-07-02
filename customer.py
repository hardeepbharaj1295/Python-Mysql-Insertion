from tkinter import *
from tkinter import messagebox
import db.db


class Customer:

    def __init__(self):
        self.win = Tk()
        self.win.geometry("600x400")
        self.win.title("Data Insertion")

    def add_frame(self):
        self.frame = Frame(self.win, width=400, height=300)
        self.frame.place(x=0,y=0)

        self.label = Label(self.frame, text='Name')
        self.label.place(x=10, y=10)

        self.name = Entry(self.frame)
        self.name.place(x=80, y=10)

        self.label = Label(self.frame, text='Email')
        self.label.place(x=10, y=40)

        self.email = Entry(self.frame)
        self.email.place(x=80, y=40)

        self.label = Label(self.frame, text='Password')
        self.label.place(x=10, y=70)

        self.password = Entry(self.frame, show='*')
        self.password.place(x=80, y=70)

        self.button =Button(self.frame, text='SUBMIT', command=self.addcustomer)
        self.button.place(x=50, y=100)

        self.win.mainloop()

    def addcustomer(self):
        if self.name.get() == "":
            messagebox.showwarning("Alert!","Enter your name")
        elif self.email.get() == "":
            messagebox.showwarning("Alert!", "Enter your email")
        elif self.password.get() == "":
            messagebox.showwarning("Alert!", "Enter your password")
        else:
            data = (
                self.name.get(),
                self.email.get(),
                self.password.get()
            )
            res = db.db.add_customer(data)
            if res:
                messagebox.showinfo("Message","Add success")
            else:
                messagebox.showerror("Alert!","Something is wrong")



if __name__ == "__main__":
    x  = Customer()
    x.add_frame()