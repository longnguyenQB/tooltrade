import tkinter as tk
from tkinter import *
import tkinter.ttk as exTK
import pandas as pd
from PIL import Image, ImageTk
from trade import main as m
from insert import insert as i
from trade_detail import main as o

def open_trade():
    m()    
def open_insert():
    i()    
def open_trade_detail():
    o()
def main():
    root = tk.Tk()
    root.geometry("900x600")
    root.title("Trade menu")
    root.configure(bg="#CD1076")
    root.iconbitmap('icon.ico')
    
    
    load = Image.open("trade.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(root, image = render)
    img.place(x=0,y=0)

    name = Label(root, text="Trading", fg="#FFFFFF", bd = 0, bg="#04082d")
    name.config(font=("Aquire", 50))
    name.grid(column = 0, padx=10, pady=10, columnspan = 2)

    #Label check
    name = Label(root, text="Dữ liệu hiện tại: ", fg="#FFFFFF", bd = 0, bg="#040838")
    name.config(font=("Arial", 30))
    name.grid(row = 5, column = 0, padx=10, pady=10, columnspan = 2)

    

        
    def clear_tree():
        my_tree.delete(*my_tree.get_children())   
    def clear_frame():
        for widget in my_frame.winfo_children():
            widget.destroy()
    # Create frame
    my_frame = Frame(root,padx=5, width=900, height=300 )
    my_frame.grid(row= 12, column=0, padx=0, pady=5, columnspan = 2)
    # Create treeview
    my_tree = exTK.Treeview(my_frame)
    
    df = pd.read_csv("trade.csv")
    df = df.drop(['Unnamed: 0'], axis=1)
    # clear old tree
    clear_tree()
    # setup new tree view
    my_tree["columns"] = list(df.columns)
    my_tree["show"] = "headings"
    # loop thru columns
    for column in my_tree["columns"]:
        if column in ["number_token", "number_token_sell", "number_token_buy"]:
            my_tree.column(column, width =110, stretch=True)
        else: 
            my_tree.column(column, width =70, stretch=True)
        my_tree.heading(column, text=column)
    # put data in tree view
    df_rows = df[-5:].to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("", "end", values=row)
    my_tree.grid(row= 12, column=0, padx=0, pady=5, columnspan = 2)
    
    def open_file():
        
        # Create frame
        my_frame = Frame(root,padx=5, width=900, height=300 )
        my_frame.grid(row= 12, column=0, padx=0, pady=5, columnspan = 2)
        # Create treeview
        my_tree = exTK.Treeview(my_frame)
        clear_frame()
        df = pd.read_csv("trade.csv")
        df = df.drop(['Unnamed: 0'], axis=1)
        # setup new tree view
        my_tree["columns"] = list(df.columns)
        my_tree["show"] = "headings"
        # loop thru columns
        for column in my_tree["columns"]:
            if column in ["number_token", "number_token_sell", "number_token_buy"]:
                my_tree.column(column, width =110, stretch=True)
            else: 
                my_tree.column(column, width =70, stretch=True)
            my_tree.heading(column, text=column)
        # put data in tree view
        df_rows = df[-5:].to_numpy().tolist()
        for row in df_rows:
            my_tree.insert("", "end", values=row)

        my_tree.grid(row= 12, column=0, padx=0, pady=5, columnspan = 2)
    
    check_button = Button(root, text= "Check", command = open_file)
    check_button.grid(column = 0, row = 1, padx=10,pady=10, columnspan = 2)
    trade_button = Button(root, text= "Trade by price", command= open_trade)
    trade_button.grid(column = 0, row = 2,padx=10,pady=10, columnspan = 2)
    trade_button = Button(root, text= "Trade by number token", command= open_trade_detail)
    trade_button.grid(column = 0, row = 3,padx=10,pady=10, columnspan = 2)
    insert_button = Button(root, text= "Insert", command= open_insert)
    insert_button.grid(column = 0, row = 4,padx=10,pady=10, columnspan = 2)
    # Hàm thay đổi config theo giây
    # root.after(100, setText)


    root.mainloop()

if __name__ == "__main__":

    main()
