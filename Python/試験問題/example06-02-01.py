#p157

import tkinter as tk
import tkinter.messagebox as tmsg


def ButtonClick():
    b=int(editbox1.get())
    if b>=0 and b<=100:
        res = "OK"
    else:
        res = "DAME"
    tmsg.showinfo("TEST Title",res)


root = tk.Tk()


#p159
root.geometry("800x800")

#162
root.title("TK Lesson")
label1 = tk.Label(root, text = "x=20,y=20", font=("Times", 20))
label1.place(x = 20, y = 20)

label2 = tk.Label(root, text = "x=200,y=50", font=("Arial", 15))
label2.place(x = 200, y = 50)

label3 = tk.Label(root, text = "TOKYO SCHOOL OF BUSINESS", font=("CAMPUS PERSONAL USE", 40))
label3.place(x = 10, y = 100)


editbox1=tk.Entry(width=10)
editbox1.place(x=10,y=200)


button1 = tk.Button(root, text = "CHECK", font=("Times", 10), command=ButtonClick)
button1.place(x = 90, y = 195)





root.mainloop()





