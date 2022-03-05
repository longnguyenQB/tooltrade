import tkinter as tk
from tkinter import *
import tkinter.ttk as exTK
import pandas as pd
import numpy as np
from PIL import Image, ImageTk


        
def main():
    root = tk.Tk()
    root.geometry("750x800")
    root.iconbitmap('icon.ico')
    root.title("Trade")
    root.configure(bg="#0B0A33")
    
    error_frame = Frame(root,padx=5, width=400, height=20 )
    error_frame.grid(row= 9, column=0, padx=0, pady=5, columnspan = 2)
    
    def clear_error_frame():
        for widget in error_frame.winfo_children():
            widget.destroy()

    # load = Image.open("background.png")
    # render = ImageTk.PhotoImage(load)
    # img = Label(root, image = render)
    # img.place(x=0,y=0)

    box = Text(root, padx = 5,width=105, height=80, font= ("Arial", 10))
    box.grid(row= 11)
    
    def clear():
        box.delete(1.0, END)
    
    
    def trade(status, number_token, price):
        if status == "Mua":
            resul_text = ''
            for j in np.arange(5, 20, 5): 
                price_sell = (number_token*price*1.004)/((number_token-j)*0.998)
                resul_text += f"Nếu muốn lời {j} token thì mua {number_token} ở giá {price} và bán {number_token-j} ở giá {price_sell}\n"
            box.insert(END,resul_text)   
                    
        if  status == "Bán":
            resul_text = ''
            for j in np.arange(5, 20, 5): 
                price_buy = (number_token*price*0.996)/((number_token+j)*1.002)
                resul_text += f"Nếu muốn lời {j} token thì bán {number_token} ở giá {price} và mua {number_token+j} ở giá {price_buy}\n"
            box.insert(END,resul_text)
                
    def trade_detail():
        
        number_token_input = 0
        price_input = 0
        
        try:
            number_token_input = float(number_token.get())
        except ValueError:
            clear_error_frame()
            label_error = Label(error_frame, text ="Nhập sai thông tin,số lượng muốn trade phải là số", fg="#FFFFFF", bd = 0, bg="#0B0A33")
            label_error.config(font=("Arial", 15))
            label_error.grid(column=0, row=9, padx=5, pady=5)
        
        try:
            price_input = float(price.get())
        except ValueError:
            clear_error_frame()
            label_error = Label(error_frame, text ="Nhập sai thông tin, giá muốn trade phải là số", fg="#FFFFFF", bd = 0, bg="#0B0A33")
            label_error.config(font=("Arial", 15))
            label_error.grid(column=0, row=9, padx=5, pady=5)
        if (number_token_input != 0) & (price_input !=0):
            trade(status.get(), number_token_input, price_input )
            
            
    

    # frame = tk.Frame(root, bg="white")
    # frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    label_status = Label(root, text = "Bạn muốn trade mua hay bán? ")
    label_status.grid(column=0, row=0, padx=5, pady=5)
    status = exTK.Combobox(root, width= 20, font= "Times 30 bold", values=('Mua', 'Bán'), state='readonly')
    status.grid(column=0,row=1, padx=5, pady=5)
    status.current(0)
    # status.focus()
    
    label_number_token = Label(root, text = "Nhập số lượng token muốn trade: ")
    label_number_token.grid(column=0, row=2, padx=5, pady=5)
    number_token= Entry(root, font= "Times 30 bold")
    number_token.grid(column=0, row=3, padx=5, pady=5)
    
    label_price = Label(root, text = "Nhập giá muốn trade: ")
    label_price.grid(column=0, row=4, padx=5, pady=5)
    price= Entry(root, font= "Times 30 bold")
    price.grid(column=0, row=5, padx=5, pady=5)


    trade_button = Button(root, text= "Trade", command= trade_detail)
    trade_button.grid(column=0, row=7, padx=5, pady=5)
    clear_button = Button(root, text= "Clear", command= clear)
    clear_button.grid(column=0, row=8, padx=5, pady=5)
    # Hàm thay đổi config theo giây
    # root.after(100, setText)


    root.mainloop()

if __name__ == "__main__":

    main()