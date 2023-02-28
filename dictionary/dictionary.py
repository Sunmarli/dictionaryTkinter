
from module1 import *
from tkinter import *
from tkinter import ttk 
import tkinter as tk 
import random

eng=[]
rus=[]
eng=loe_failist("eng.txt")
rus=loe_failist("rus.txt")
connect(rus,eng)


root = tk.Tk()
root.title("Main Window") 
root.geometry("400x200")

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("Eng to Rus") 
    new_window.geometry("300x200") 
    photo = tk.PhotoImage(file="image.png")
    entry = tk.Entry(new_window,font="Tahoma 14")
    entry.pack()
    buttonImg = tk.Button(new_window, image=photo) 
    buttonImg.image = photo
    def on_entry_return(event):
        user_input = entry.get() 

        if user_input in eng:
            ind = eng.index(user_input) 
            label.configure(text=rus[ind],font="Tahoma 16")
        else:
            label.configure(text="Word not found, add Eng-Rus translation")
            new_word_entry = tk.Entry(new_window)
            new_word_entry.pack()
            new_translation_entry = tk.Entry(new_window)
            new_translation_entry.pack()
            submit_button = tk.Button(new_window, text="Add", command=lambda: add_new_word(new_word_entry.get(), new_translation_entry.get()))
            submit_button.pack()
        entry.delete(0, tk.END)
        def add_new_word(new_word, new_translation):
            eng.append(new_word)
            rus.append(new_translation)
            with open("eng.txt", "a", encoding="utf-8") as eng_file:
                eng_file.write(new_word + "\n")
            with open("rus.txt", "a", encoding="utf-8") as rus_file:
                rus_file.write(new_translation + "\n")
            new_word_entry.destroy()
            new_translation_entry.destroy()
            submit_button.destroy()
            label.configure(text="New word added to dictionary",font="Tahoma 16") 

    buttonImg.bind("<Button-1>", on_entry_return) 
    buttonImg.pack()   
    label = tk.Label(new_window)
    label.pack()

def open_new_window2():
    new_window2 = tk.Toplevel(root)
    new_window2.title("Rus to Eng") 
    new_window2.geometry("300x200") 
    photo = tk.PhotoImage(file="image.png")
    entry = tk.Entry(new_window2,font="Tahoma 14")
    entry.pack()
    buttonImg = tk.Button(new_window2, image=photo) 
    buttonImg.image = photo
    def on_entry_return(event):
        user_input = entry.get() 

        if user_input in rus:
            ind = rus.index(user_input) 
            label.configure(text=eng[ind],font="Tahoma 16")
        else:
            label.configure(text="Word not found, add Eng-Rus translation")
            new_word_entry = tk.Entry(new_window2)
            new_word_entry.pack()
            new_translation_entry = tk.Entry(new_window2)
            new_translation_entry.pack()
            submit_button = tk.Button(new_window2, text="Add", command=lambda: add_new_word(new_word_entry.get(), new_translation_entry.get()))
            submit_button.pack()
        entry.delete(0, tk.END)
        def add_new_word(new_word, new_translation):
            rus.append(new_word)
            eng.append(new_translation)
            with open("rus.txt", "a", encoding="utf-8") as rus_file:
                rus_file.write(new_word + "\n")
            with open("eng.txt", "a", encoding="utf-8") as eng_file:
                eng_file.write(new_translation + "\n")
            new_word_entry.destroy()
            new_translation_entry.destroy()
            submit_button.destroy()
            label.configure(text="New word added to dictionary",font="Tahoma 16") 

    buttonImg.bind("<Button-1>", on_entry_return) 
    buttonImg.pack()   
    label = tk.Label(new_window2)
    label.pack() 

def open_new_window3():
    global eng, rus
    new_window3 = tk.Toplevel(root)
    new_window3.title("Control yourself")
    new_window3.geometry("300x300") 
    prompt_label = tk.Label(new_window3, text="")
    entry_var = tk.StringVar()
    entry_widget = tk.Entry(new_window3, textvariable=entry_var)
    random_word = random.choice(eng) 
    prompt_label.config(text=f"What is the Russian translation of '{random_word}'?") 
    
    counter = 0
    correct_count = 0
    total_count = 0
    def check():
        nonlocal random_word, counter, correct_count, total_count
        user_translation = entry_var.get().strip().lower()
        ind = eng.index(random_word)

        if user_translation == rus[ind]:
            prompt_label.config(text="Correct!")
            correct_count += 1
        else:
            prompt_label.config(text=f"Incorrect. The correct answer is '{rus[ind]}'.")
        total_count += 1
        accuracy = correct_count / total_count * 100
        prompt_label.config(text=f"You got {correct_count} out of {total_count} correct ({accuracy:.2f}%).")

        counter += 1
        if counter >= 5:
            submit_button.config(state="disabled")
        else:
            random_word = random.choice(eng)
            prompt_label.config(text=f"What is the Russian translation of '{random_word}'?")
            entry_var.set("")
    
    submit_button = tk.Button(new_window3, text="Next", command=lambda: check())
    submit_button.pack()
    
    prompt_label.pack()
    entry_widget.pack()
    
    new_window3.mainloop()

def open_new_window4():
    global eng, rus
    new_window3 = tk.Toplevel(root)
    new_window3.title("Control yourself")
    new_window3.geometry("300x300") 
    prompt_label = tk.Label(new_window3, text="")
    entry_var = tk.StringVar()
    entry_widget = tk.Entry(new_window3, textvariable=entry_var)
    random_word = random.choice(eng) 
    prompt_label.config(text=f"What is the Russian translation of '{random_word}'?") 
    def check():
        for i in range(4):
            random_word = random.choice(eng) 
            prompt_label.config(text=f"What is the Russian translation of '{random_word}'?") 
        entry_var.set("")
        user_translation = entry_var.get().strip().lower()
        ind=eng.index(random_word)
        correct_count = 0
        total_count = 0
        if user_translation == rus[ind]:
            prompt_label.config(text="Correct!")
            correct_count += 1
        else:
            prompt_label.config(text=f"Incorrect. The correct answer is '{rus[ind]}'.")
        total_count += 1

        #accuracy = correct_count / total_count * 100
        #prompt_label.config(text=f"You got {correct_count} out of {total_count} correct ({accuracy:.2f}%).")
    submit_button = tk.Button(new_window3, text="Next", command=lambda: check())
    prompt_label.pack(pady=10)
    entry_widget.pack(pady=10)
    submit_button.pack(pady=10)






# create the button that opens the new window
button1 = tk.Button(root, text="Select",font="Tahoma 16",fg="#1c4226",bg="#aee8be",width=10, heigh=1,relief=RAISED, command=open_new_window) 
button2 = tk.Button(root, text="Select",font="Tahoma 16",fg="#1c4226",bg="#aee8be",width=10, heigh=1,relief=RAISED, command=open_new_window2) 
button3 = tk.Button(root, text="Select",font="Tahoma 16",fg="#1c4226",bg="#aee8be",width=10, heigh=1,relief=RAISED, command=open_new_window3) 

lbl=Label(root, text="Welcome to dictionary!",font="Arial 20",bg="#f0e4c7")
lbl2=Label(root, text="Eng to Rus",font="Arial 20",bg="#f0e4c7")
lbl3=Label(root, text="Rus to Eng",font="Arial 20",bg="#f0e4c7")
lbl4=Label(root, text="Controll yourself",font="Arial 20",bg="#f0e4c7")
lbl.grid(row=0, column=0,  columnspan=2) 
lbl2.grid(row=1, column=0, sticky="E", padx=5, pady=5) 
button1.grid(row=1, column=1, sticky="W")
lbl3.grid(row=2, column=0, sticky="E", padx=5, pady=5) 
button2.grid(row=2, column=1, sticky="W")
lbl4.grid(row=3, column=0, sticky="E", padx=5, pady=5) 
button3.grid(row=3, column=1, sticky="W")

root.mainloop()
