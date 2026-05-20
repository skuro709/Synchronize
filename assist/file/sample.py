# sample.py

import tkinter as tk

def main():
    root = tk.Tk()
    root.title("Hello GUI")
    root.geometry("300x150")

    label_hello = tk.Label(
        root, 
        text="Hello World", 
        font=("Arial", 18, "bold")
    )
    label_hello.pack(expand=True)

    label_credit = tk.Label(
        root, 
        text="Made by sk", 
        font=("Arial", 8, "italic"),
        fg="gray"
    )
    label_credit.pack(side="bottom", anchor="w", padx=5, pady=2)
    
    root.mainloop()
    
if __name__ == "__main__":
    main()