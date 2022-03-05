import tkinter as tk
from tkinter import *
import tkinter.ttk as exTK
import pandas as pd
import numpy as np
from PIL import Image, ImageTk


df = pd.read_csv("trade.csv")
df_fix = pd.read_csv("trade_fix.csv")
df = df.drop(['Unnamed: 0'], axis=1)

def check_df():
    print(df[-1:])

        
def main():
    root = tk.Tk()
    root.geometry("750x800")
    root.iconbitmap('icon.ico')
    root.title("Trade")
    root.configure(bg="#0B0A33")
    
    # load = Image.open("background.png")
    # render = ImageTk.PhotoImage(load)
    # img = Label(root, image = render)
    # img.place(x=0,y=0)

    box = Text(root, padx = 5,width=105, height=80, font= ("Arial", 10))
    box.grid(row= 11)
    def clear():
        box.delete(1.0, END)
    
    
    def trade_sell(price_sell):

        resul_text = ''
        for price_buy in np.arange(price_sell , price_sell-0.05, -0.0001)[1:]:
            for j in np.arange(5, 20, 5): 
                number_token_sell = (j*price_buy*1.002/(price_sell*0.996-price_buy*1.002))
                if (number_token_sell < 1000) & (number_token_sell > 0):
                    resul_text += f"Nếu muốn lời {j} token thì bán {number_token_sell} token ở giá {price_sell} và mua {number_token_sell+j} ở giá {price_buy}\n"
        box.insert(END,resul_text)
        
            
    def trade_buy(price_buy):
        resul_text = ''
        for price_sell in np.arange(price_buy , price_buy + 0.05, 0.001)[1:]:
            for j in np.arange(5, 20, 5): 
                number_token_buy = (j*price_sell*0.998/(price_sell*0.998-price_buy*1.004))
                if (number_token_buy < 1000) & (number_token_buy >0):
                    resul_text += f"Nếu muốn lời {j} token thì mua {number_token_buy} token ở giá {price_buy} và bán {number_token_buy-j} ở giá {price_sell}\n"
        box.insert(END,resul_text)
    def trade():
            
        try:
            price_trade = float(price.get())
        except :
            label_error = Label(root, text ="Nhập sai thông tin, giá muốn trade phải là số")
            label_error.grid(column=0, row=6, padx=5, pady=5)
            
        if status.get() == "Mua":
            trade_buy(price_trade)
            
        elif status.get() == "Bán":
            trade_sell(price_trade)
            
            
    

    # frame = tk.Frame(root, bg="white")
    # frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

    label_status = Label(root, text = "Bạn muốn trade mua hay bán? ")
    label_status.grid(column=0, row=0, padx=5, pady=5)
    status = exTK.Combobox(root, width= 20, font= "Times 30 bold", values=('Mua', 'Bán'), state='readonly')
    status.grid(column=0,row=1, padx=5, pady=5)
    status.current(0)
    # status.focus()
    
    label_price = Label(root, text = "Nhập giá muốn trade: ")
    label_price.grid(column=0, row=2, padx=5, pady=5)
    price= Entry(root, font= "Times 30 bold")
    price.grid(column=0, row=3, padx=5, pady=5)


    trade_button = Button(root, text= "Trade", command= trade)
    trade_button.grid(column=0, row=9, padx=5, pady=5)
    clear_button = Button(root, text= "Clear", command= clear)
    clear_button.grid(column=0, row=10, padx=5, pady=5)
    # Hàm thay đổi config theo giây
    # root.after(100, setText)


    root.mainloop()

if __name__ == "__main__":

    main()
