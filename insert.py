from tkinter import *
import tkinter as tk
import tkinter.ttk as exTK
import pandas as pd
import numpy as np
from datetime import date,datetime, timedelta
from PIL import Image, ImageTk



def insert():
    
    def update_df():
        
        clear_error_frame()
        usdt = 22826
        
        price_insert = 0
        number_token_insert = 0
        try:
            price_insert = float(price.get())
        except :
            
            label_error = Label(error_frame, text ="Nhập sai thông tin, giá nhập vào phải là số", fg="#FFFFFF", bd = 0, bg="#0B0A33")
            label_error.config(font=("Arial", 20))
            label_error.grid(column=0, row=11, padx=5, pady=5, columnspan = 2)
        
        try:
            number_token_insert = float(number_token.get())
        except :

            label_error = Label(error_frame, text ="Nhập sai thông tin, số lượng token phải là số", fg="#FFFFFF", bd = 0, bg="#0B0A33")
            label_error.config(font=("Arial", 20))
            label_error.grid(column=0, row=11, padx=5, pady=5, columnspan = 2)
            
        if (price_insert >= 0) & (number_token_insert >=0):
            
            df = pd.read_csv("trade.csv")
            df = df.drop(['Unnamed: 0'], axis=1)
            
            day = datetime.now().strftime("%d/%m/%Y")
            hour = datetime.now().time().strftime("%X")
            
            if status.get() == "Bán":
                sell = 1
                buy = 0
            else :
                sell =0
                buy = 1
            
            if trade.get() == "Không":
                trade_insert = 0
            else:
                trade_insert = 1       

            if last.get() == "Không":
                last_insert = 0
            else:
                last_insert = 1   
            
            #________________________________________________________________________         
            
            # Update number_token and capital:
            if sell == 1 :
                number_token_update = df[-1:].number_token - number_token_insert 
            if buy == 1 :
                number_token_update = df[-1:].number_token + number_token_insert 
            
            # Caculator profit
            if trade_insert == 0:
                
                capital_update  = df[-1:].capital + number_token_insert*price_insert*usdt + number_token_insert*price_insert*usdt*0.002
                
                if last_insert == 1:
                    profit_day = df.number_token.tolist()[-1] - df.number_token.tolist()[0] - df.loc[(df.trade == 0) & (df.number_token_buy >0)].number_token_buy.sum() + df.loc[(df.trade == 0) & (df.number_token_sell >0)].number_token_sell.sum()
                else: 
                    profit_day = 0
                    
            elif trade_insert == 1:
                
                capital_update  = df[-1:].capital
                
                if last_insert == 1:
                    profit_day = number_token_update - number_token_insert - df.number_token.tolist()[0] - df.loc[(df.trade == 0) & (df.number_token_buy >0)].number_token_buy.sum() + df.loc[(df.trade == 0) & (df.number_token_sell >0)].number_token_sell.sum()
                else: 
                    profit_day = 0
                
            #Insert to csv file
            dca = capital_update / number_token_update
            df = df.append({'day': day,
                            'hour': hour,
                            "number_token": float(number_token_update),
                            "capital": float(capital_update),
                            "dca" : float(dca),
                            "number_token_sell": float(sell*number_token_insert) ,
                            "price_sell": float(sell*price_insert),
                            "number_token_buy": float(buy*number_token_insert),
                            "price_buy" : float(buy*price_insert),
                            "trade": float(trade_insert),
                            "profit_day": float(profit_day)
                            },
                            ignore_index=True)
            df.to_csv("trade.csv")
            label_error = Label(error_frame, text ="Nhập thành công!", fg="#FFFFFF", bd = 0, bg="#0B0A33")
            label_error.config(font=("Arial", 20))
            label_error.grid(column=0, row=11, padx=5, pady=5, columnspan = 2)
            open_file()
    
    
    
    root = tk.Tk()
    root.geometry("900x650")
    root.title("Insert")
    root.iconbitmap('icon.ico')
    root.configure(bg="#0B0A33")

    error_frame = Frame(root,padx=5, width=400, height=20 )
    error_frame.grid(row= 11, column=0, padx=0, pady=5, columnspan = 2)
    
    # load = Image.open("background.png")
    # render = ImageTk.PhotoImage(load)
    # img = Label(root, image = render)
    # img.place(x=0,y=0)
    
    label_status = Label(root, text = "Bạn muốn nhập thông tin mua hay bán? ")
    label_status.grid(column=0, row=0, pady = 5, padx = 5, sticky='E')
    status = exTK.Combobox(root, width= 20, font= "Times 10 bold", values=('Mua', 'Bán'), state='readonly')
    status.grid(column=1,row=0, pady = 5, padx = 50, sticky='W')
    status.current(0) 

    
    label_number_token = Label(root, text = "Nhập số lượng token:  ")
    label_number_token.grid(column=0, row=1, pady=5, padx = 5, sticky='E')
    number_token= Entry(root, font= "Times 10 bold")
    number_token.grid(column=1, row=1, pady=5, padx = 50, sticky='W')
    
    
    label_price = Label(root, text = "Nhập giá: ")
    label_price.grid(column=0, row=2, pady=5, padx = 5, sticky='E')
    price= Entry(root, font= "Times 10 bold")
    price.grid(column=1, row=2, pady=5, padx = 50, sticky='W')

        
    label_trade = Label(root, text = "Trade? ")
    label_trade.grid(column=0, row=3, pady=5, padx = 5, sticky='E')
    trade = exTK.Combobox(root, width= 20, font= "Times 10 bold", values=('Không', 'Có'), state='readonly')
    trade.grid(column=1,row=3, pady=5, padx = 50, sticky='W')
    trade.current(0)
    


    label_last = Label(root, text = "Có muốn tổng kết lãi trong ngày không? ")
    label_last.grid(column=0, row=4, pady=5,  padx = 5, sticky='E')
    last = exTK.Combobox(root, width= 20, font= "Times 10 bold", values=('Không', 'Có'), state='readonly')
    last.grid(column=1,row=4, pady=5, padx = 50, sticky='W')
    last.current(0)      

    # Create frame
    my_frame = Frame(root,padx=5, width=900, height=300 )
    my_frame.grid(row= 12, column=0, padx=0, pady=5, columnspan = 2)
    # Create treeview
    my_tree = exTK.Treeview(my_frame)
    
    # file open
    def open_file():
        
        # Create frame
        my_frame = Frame(root,padx=5, width=900, height=300 )
        my_frame.grid(row= 12, column=0, padx=0, pady=5, columnspan = 2)
        # Create treeview
        my_tree = exTK.Treeview(my_frame)
        
        df = pd.read_csv("trade.csv")
        df = df.drop(['Unnamed: 0'], axis=1)
        # clear old tree
        clear_frame()
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
        df_rows = df[-10:].to_numpy().tolist()
        for row in df_rows:
            my_tree.insert("", "end", values=row)

        my_tree.grid(row= 12, column=0, padx=0, pady=5, columnspan = 2)
    
    def clear_error_frame():
        for widget in error_frame.winfo_children():
            widget.destroy()
    def clear_frame():
        for widget in my_frame.winfo_children():
            widget.destroy()
        
    def drop1row():
        clear_error_frame()
        # Create frame
        my_frame = Frame(root,padx=5, width=900, height=300 )
        my_frame.grid(row= 12, column=0, padx=0, pady=5, columnspan = 2)
        # Create treeview
        my_tree = exTK.Treeview(my_frame)
        
        df = pd.read_csv("trade.csv")
        df = df.drop(['Unnamed: 0'], axis=1)
        # clear old tree
        clear_frame()
        df = pd.read_csv("trade.csv")
        df = df.drop(['Unnamed: 0'], axis=1)
        df =df.drop([len(df)-1])
        df.to_csv("trade.csv")
        
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
        df_rows = df[-10:].to_numpy().tolist()
        for row in df_rows:
            my_tree.insert("", "end", values=row)

        my_tree.grid(row= 12, column=0, padx=0, pady=5, columnspan = 2)
        
        label_error = Label(error_frame, text ="Xóa 1 hàng thành công!", fg="#FFFFFF", bd = 0, bg="#0B0A33")
        label_error.config(font=("Arial", 20))
        label_error.grid(column=0, row=11, padx=5, pady=5, columnspan = 2)
        

    trade_button = Button(root, text= "Insert", command= update_df, font= ("Aquire", 15))
    trade_button.grid(column=0, row=10, pady=10 ,columnspan = 2)
    drop_button =  Button(root, text= "Drop", command= drop1row, font= ("Aquire", 15))
    drop_button.grid(column=0, row=13, pady=10 ,columnspan = 2)
    # Hàm thay đổi config theo giây
    # root.after(100, setText)


    root.mainloop()

if __name__ == "__main__":

    insert()
