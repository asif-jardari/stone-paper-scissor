import tkinter as tk
from tkinter import ttk
import random
window = tk.Tk()
window.title("stone-paper-scissor game")
window.geometry("400x600")

#creating grid
for i in range(2):
    window.columnconfigure(i,weight=1)
for i in range(3):
    window.rowconfigure(i,weight=1)
result_var = tk.StringVar()
buttonvar = tk.StringVar()
def fc():
    user_input=buttonvar.get()
    my_list = ["stone","paper","scissor"]
    result = random.choice(my_list)
    if (user_input == result):
        result_var.set("MATCH DRAW!")
    elif(user_input == "stone" and result == "scissor"):
        result_var.set("YOU WIN")
    elif(user_input == "scssior" and result == "paper"):
        result_var.set("YOU WIN")
    elif(user_input == "paper" and result == "stone"):
        result_var.set("YOU WIN")
    else:
        result_var.set("YOU LOSS")
    

#creating entry
entry_w = ttk.Entry(window,textvariable=result_var)
entry_w.grid(row=0,column=0,sticky="ewns",columnspan=2)
#creating button
button_stone = ttk.Button(window,text="STONE",command=lambda : buttonvar.set("stone"))
button_paper = ttk.Button(window,text="PAPER",command=lambda: buttonvar.set("paper"))
button_scissor = ttk.Button(window,text="SCISSOR",command=lambda : buttonvar.set("scissor"))
button_start = ttk.Button(window,text="START",command=fc)


button_stone.grid(row=1,column=0,sticky="ewns")
button_paper.grid(row=1,column=1,sticky="ewns")
button_scissor.grid(row=2,column=0,sticky="ewns")
button_start.grid(row=2,column=1,sticky="ewns")





window.mainloop()
