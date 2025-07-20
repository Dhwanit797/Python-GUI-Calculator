import tkinter as tk
from functools import partial

win = tk.Tk()

win.title("Calculator")

win.attributes("-fullscreen",True)

entry = tk.Entry(win,font=("Arial",16) , justify="right")
entry.grid(row=0,column=0,columnspan=4,sticky="nsew",padx=10,pady=10)

button = [
    ("7","8","9","/"),
    ("4","5","6","*"),
    ("1","2","3","-"),
    ("C","0","=","+")
]

def on_click(button_entry):
    current_entry = entry.get()

    if button_entry == "C":
        entry.delete(0,tk.END)

    elif button_entry == "=":
        try:
            result = eval(current_entry)
            entry.delete(0,tk.END)
            entry.insert(tk.END,str(result))
        except:
            entry.delete(0,tk.END)
            entry.insert(tk.END,"Invalid")

    else:
        entry.insert(tk.END,button_entry)


for r,row in enumerate(button,start=1):
    for c,text in enumerate(row):
        btn = tk.Button(win, text=text , font=("Arial",20),command=partial(on_click,text))
        btn.grid(row = r , column= c , sticky="nsew")

for i in range(5):
    win.grid_rowconfigure(i,weight=1)
    win.grid_columnconfigure(i,weight=1)

win.mainloop()