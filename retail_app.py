from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox as tsmg
import time
import webbrowser
import pandas as pd
from openpyxl import load_workbook

# ------------Software Size, Shape, Title
root = Tk()
root.geometry("1300x700+0+0")
root.maxsize(1350, 700)
root.title("RNK food products")

#######################################################################################################################

#---------Login button function
def log_in():
    if userentry.get() == "Aadarsh" and passwordentry.get() == "xyz":
        #------Pic of user who loged in
        # login_Photo_Log1 = PhotoImage(file="")
        # login_pic1 = Label(root, image=login_Photo_Log1)
        # login_pic1.place(x=600, y=230)
        #------Name of user who loged in
        # login_n1 = Label(root, text="Mr.Kishor", font="Georgia 15 bold")
        # login_n1.place(x=680, y=250)
        home_page()

    elif userentry.get() == "Leap" and passwordentry.get() == "leap":
        home_page()

    else:
        tsmg.showerror("Invalid Login", "Please! try again")

#######################################################################################################################
#-----------------------Home page and Other Functions

def home_page():

    #Clearing login_page
    user.place_forget()
    password.place_forget()
    userentry.place_forget()
    passwordentry.place_forget()
    pic.place_forget()
    b.place_forget()
    c.place_forget()

    # ------------------Billing System
    def billing():
        gmail.place_forget()
        employe.place_forget()
        bill.place_forget()
        list.place_forget()
        active_details.place_forget()
        headline_txt.pack_forget()
        headline_frame.pack_forget()
        clock.pack_forget()
        lastline_frame.pack_forget()
        rights_txt.pack_forget()
        f3.pack_forget()

        root.title(" Billing System")

        # Function For Text Area
        def welcome_soft():
            txt.delete('1.0', END)
            txt.insert(END, "                                    Welcome To RNK Store's Retail\n")
            txt.insert(END, f"\nBill No. : {str(c_bill_no.get())}")
            txt.insert(END, f"\nCustomer Name : {str(cus_name.get())}")
            txt.insert(END, f"\nPhone No. : {str(c_phone.get())}")
            txt.insert(END, f"\nAddress : {str(address.get())}")
            txt.insert(END, "\n=====================================================================")
            txt.insert(END, "\n                    Product                            Qty                 Price        "
                            "      Total")
            txt.insert(END, "\n=====================================================================")

        # Function to clear the bill area
        def clearing():
            txt.delete('1.0', END)

        # Add Product name , qty and price to bill area
        def bill_area():

            # =================Total Food Prices
            total_food_prices = (
                    (qitem1.get() * pitem1.get()) +
                    (qitem2.get() * pitem2.get()) +
                    (qitem3.get() * pitem3.get()) +
                    (qitem4.get() * pitem4.get()) +
                    (qitem5.get() * pitem5.get()) +
                    (qitem6.get() * pitem6.get()) +
                    (qitem7.get() * pitem7.get()) +
                    (qitem8.get() * pitem8.get())
            )
            total_food.set("Rs. " + str(total_food_prices))

            welcome_soft()
            if qitem1.get() != " ":
                txt.insert(END,
                           f"\n          1.{item1.get()}                {qitem1.get()}                   {pitem1.get()}"
                           f"                   {(qitem1.get() * pitem1.get())}")
            if qitem2.get() != 0:
                txt.insert(END,
                           f"\n          2.{item2.get()}                {qitem2.get()}                   {pitem2.get()}"
                           f"                   {(qitem2.get() * pitem2.get())}")
            if qitem3.get() != 0:
                txt.insert(END,
                           f"\n          3.{item3.get()}                {qitem3.get()}                   {pitem3.get()}"
                           f"                   {(qitem3.get() * pitem3.get())}")
            if qitem4.get() != 0:
                txt.insert(END,
                           f"\n          4.{item4.get()}                {qitem4.get()}                   {pitem4.get()}"
                           f"                   {(qitem4.get() * pitem4.get())}")
            if qitem5.get() != 0:
                txt.insert(END,
                           f"\n          5.{item5.get()}                {qitem5.get()}                   {pitem5.get()}"
                           f"                   {(qitem5.get() * pitem5.get())}")
            if qitem6.get() != 0:
                txt.insert(END,
                           f"\n          6.{item6.get()}                {qitem6.get()}                   {pitem6.get()}"
                           f"                   {(qitem6.get() * pitem6.get())}")
            if qitem7.get() != 0:
                txt.insert(END,
                           f"\n          7.{item7.get()}                {qitem7.get()}                   {pitem7.get()}"
                           f"                   {(qitem7.get() * pitem7.get())}")
            if qitem8.get() != 0:
                txt.insert(END,
                           f"\n          8.{item8.get()}                {qitem8.get()}                   {pitem8.get()}"
                           f"                   {(qitem8.get() * pitem8.get())}")

            txt.insert(END, "\n=====================================================================")
            txt.insert(END, f"\n                                                                                       "
                            f"            Total : Rs. {total_food_prices}")

        def printing():
            pass

        def exiting():
            # clearing all the frame of bill
            title.pack_forget()
            fram.place_forget()
            F2.place_forget()
            F3.place_forget()
            F4.place_forget()
            Frame2.place_forget()
            Frame_2.place_forget()

            # getting all the home widget
            headline_frame.pack(fill=BOTH)
            headline_txt.pack(fill=BOTH)
            f3.pack(fill=BOTH, pady=3)
            clock.pack(fill=BOTH)
            bill.place(x=510, y=350)
            gmail.place(x=50, y=200)
            employe.place(x=50, y=450)
            active_details.place(x=950, y=450)
            list.place(x=950, y=200)
            lastline_frame.pack(fill=BOTH, side=BOTTOM)
            rights_txt.pack(fill=BOTH, side=BOTTOM)

        ##############################################################################################################
        # ====================Variables========================#
        cus_name = StringVar()
        c_phone = StringVar()
        c_bill_no = StringVar()
        address = StringVar()
        # Seting Value to variable
        c_bill_no.set("0001")

        item1 = StringVar()
        item2 = StringVar()
        item3 = StringVar()
        item4 = StringVar()
        item5 = StringVar()
        item6 = StringVar()
        item7 = StringVar()
        item8 = StringVar()
        #    self.item9 = StringVar()

        pitem1 = DoubleVar()
        pitem2 = DoubleVar()
        pitem3 = DoubleVar()
        pitem4 = DoubleVar()
        pitem5 = DoubleVar()
        pitem6 = DoubleVar()
        pitem7 = DoubleVar()
        pitem8 = DoubleVar()

        qitem1 = IntVar()
        qitem2 = IntVar()
        qitem3 = IntVar()
        qitem4 = IntVar()
        qitem5 = IntVar()
        qitem6 = IntVar()
        qitem7 = IntVar()
        qitem8 = IntVar()

        total_food = StringVar()

        # ===================================
        bg_color = "dim Grey"
        fg_color = "white"
        lbl_color = 'white'

        # Title of App
        title = Label(root, text="RNK Billing System", bd=12, relief=GROOVE, fg=fg_color, bg=bg_color,
                      font=("times new roman", 30, "bold"), pady=6)
        title.pack(fill=X)

        # ==========Customers Frame==========#
        fram = LabelFrame(root, text="Customer Details", font=("time new roman", 12, "bold"), fg="gold", bg=bg_color,
                          relief=GROOVE, bd=10)
        fram.place(x=0, y=80, width=1350)

        # ===============Customer Name===========#
        cname_lbl = Label(fram, text="Customer Name", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold"))
        cname_lbl.grid(row=0, column=0, padx=10, pady=5)
        cname_en = Entry(fram, bd=8, relief=GROOVE, textvariable=cus_name)
        cname_en.grid(row=0, column=1, ipady=4, ipadx=30, pady=5)

        # =================Customer Phone==============#
        cphon_lbl = Label(fram, text="Phone No", bg=bg_color, fg=fg_color,
                          font=("times new roman", 15, "bold"))
        cphon_lbl.grid(row=0, column=2, padx=20)
        cphon_en = Entry(fram, bd=8, relief=GROOVE, textvariable=c_phone)
        cphon_en.grid(row=0, column=3, ipady=4, ipadx=30, pady=5)

        # ====================Customer Bill No==================#
        cbill_lbl = Label(fram, text="Bill No.", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
        cbill_lbl.grid(row=0, column=4, padx=20)
        cbill_en = Entry(fram, bd=8, relief=GROOVE, textvariable=c_bill_no)
        cbill_en.grid(row=0, column=5, ipadx=1, ipady=4, pady=5)

        # =================Address==============#
        cadd_lbl = Label(fram, text="Address", bg=bg_color, fg=fg_color, font=("times new roman", 15, "bold"))
        cadd_lbl.grid(row=0, column=6, padx=20)
        cadd_en = Entry(fram, bd=8, relief=GROOVE, textvariable=address)
        cadd_en.grid(row=0, column=7, ipady=4, ipadx=40, pady=5)

        # ==================Food Frame=====================#
        Frame2 = LabelFrame(root, text='Products', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                            font=("times new roman", 13, "bold"))
        Frame2.place(x=0, y=162, width=275, height=538)

        # ===========Frame Content
        # ===========Item1
        item1_lbl = Label(Frame2, font=("times new roman", 20, "bold"), fg=lbl_color, bg=bg_color, text="Item1")
        item1_lbl.grid(row=0, column=0, padx=10, pady=13)

        itemchoosen1 = ttk.Combobox(Frame2, width=12, font=("times new roman", 15), textvariable=item1)

        itemchoosen1['values'] = ("RNK Bhuja 400g          ",
                                  "RNK Bhuja 200g          ",
                                  "Sada Bhuja 200g         ",
                                  "Sada Bhuja 150g         ",
                                  "Soya Bean 5kg           ",
                                  "Soya Bean 200g          ",
                                  "Soya Flaker 400g        ",
                                  "M.D. Soya Bean 15kg(bag)",
                                  "Darsan Basean 500g      ",
                                  "Darsan Basean 200g      ",
                                  "Tiger Basean 500g       ",
                                  "Tiger Basean 450        ",
                                  "RNK Cups                ",
                                  "RNK Rings               ",
                                  "RNK Chees Balls         ",
                                  "Haldi 200g              ",
                                  "Mirchi 200g             ",
                                  "Dahaniya 200g           ")

        itemchoosen1.grid(column=1, row=0)

        # =======Item2
        item2_lbl = Label(Frame2, font=("times new roman", 20, "bold"), fg=lbl_color, bg=bg_color, text="Item2")
        item2_lbl.grid(row=1, column=0, padx=10, pady=13)

        itemchoosen2 = ttk.Combobox(Frame2, width=12, font=("times new roman", 15), textvariable=item2)

        itemchoosen2['values'] = ("RNK Bhuja 400g          ",
                                  "RNK Bhuja 200g          ",
                                  "Sada Bhuja 200g         ",
                                  "Sada Bhuja 150g         ",
                                  "Soya Bean 5kg           ",
                                  "Soya Bean 200g          ",
                                  "Soya Flaker 400g        ",
                                  "M.D. Soya Bean 15kg(bag)",
                                  "Darsan Basean 500g      ",
                                  "Darsan Basean 200g      ",
                                  "Tiger Basean 500g       ",
                                  "Tiger Basean 450        ",
                                  "RNK Cups                ",
                                  "RNK Rings               ",
                                  "RNK Chees Balls         ",
                                  "Haldi 200g              ",
                                  "Mirchi 200g             ",
                                  "Dahaniya 200g           ")
        itemchoosen2.grid(column=1, row=1)

        # ========Item3
        item3_lbl = Label(Frame2, font=("times new roman", 20, "bold"), fg=lbl_color, bg=bg_color, text="Item3")
        item3_lbl.grid(row=2, column=0, padx=10, pady=13)

        itemchoosen3 = ttk.Combobox(Frame2, width=12, font=("times new roman", 15), textvariable=item3)
        itemchoosen3['values'] = ("RNK Bhuja 400g          ",
                                  "RNK Bhuja 200g          ",
                                  "Sada Bhuja 200g         ",
                                  "Sada Bhuja 150g         ",
                                  "Soya Bean 5kg           ",
                                  "Soya Bean 200g          ",
                                  "Soya Flaker 400g        ",
                                  "M.D. Soya Bean 15kg(bag)",
                                  "Darsan Basean 500g      ",
                                  "Darsan Basean 200g      ",
                                  "Tiger Basean 500g       ",
                                  "Tiger Basean 450        ",
                                  "RNK Cups                ",
                                  "RNK Rings               ",
                                  "RNK Chees Balls         ",
                                  "Haldi 200g              ",
                                  "Mirchi 200g             ",
                                  "Dahaniya 200g           ")
        itemchoosen3.grid(column=1, row=2)

        # ========Item4
        item4_lbl = Label(Frame2, font=("times new roman", 20, "bold"), fg=lbl_color, bg=bg_color, text="Item4")
        item4_lbl.grid(row=3, column=0, padx=10, pady=13)

        itemchoosen4 = ttk.Combobox(Frame2, width=12, font=("times new roman", 15), textvariable=item4)
        itemchoosen4['values'] = ("RNK Bhuja 400g          ",
                                  "RNK Bhuja 200g          ",
                                  "Sada Bhuja 200g         ",
                                  "Sada Bhuja 150g         ",
                                  "Soya Bean 5kg           ",
                                  "Soya Bean 200g          ",
                                  "Soya Flaker 400g        ",
                                  "M.D. Soya Bean 15kg(bag)",
                                  "Darsan Basean 500g      ",
                                  "Darsan Basean 200g      ",
                                  "Tiger Basean 500g       ",
                                  "Tiger Basean 450        ",
                                  "RNK Cups                ",
                                  "RNK Rings               ",
                                  "RNK Chees Balls         ",
                                  "Haldi 200g              ",
                                  "Mirchi 200g             ",
                                  "Dahaniya 200g           ")
        itemchoosen4.grid(column=1, row=3)

        # ============Item5
        item5_lbl = Label(Frame2, font=("times new roman", 20, "bold"), fg=lbl_color, bg=bg_color, text="Item5")
        item5_lbl.grid(row=4, column=0, padx=10, pady=13)

        itemchoosen5 = ttk.Combobox(Frame2, width=12, font=("times new roman", 15), textvariable=item5)
        itemchoosen5['values'] = ("RNK Bhuja 400g          ",
                                  "RNK Bhuja 200g          ",
                                  "Sada Bhuja 200g         ",
                                  "Sada Bhuja 150g         ",
                                  "Soya Bean 5kg           ",
                                  "Soya Bean 200g          ",
                                  "Soya Flaker 400g        ",
                                  "M.D. Soya Bean 15kg(bag)",
                                  "Darsan Basean 500g      ",
                                  "Darsan Basean 200g      ",
                                  "Tiger Basean 500g       ",
                                  "Tiger Basean 450        ",
                                  "RNK Cups                ",
                                  "RNK Rings               ",
                                  "RNK Chees Balls         ",
                                  "Haldi 200g              ",
                                  "Mirchi 200g             ",
                                  "Dahaniya 200g           ")
        itemchoosen5.grid(column=1, row=4)

        # ============Item6
        item6_lbl = Label(Frame2, font=("times new roman", 20, "bold"), fg=lbl_color, bg=bg_color, text="Item6")
        item6_lbl.grid(row=5, column=0, padx=10, pady=13)

        itemchoosen6 = ttk.Combobox(Frame2, width=12, font=("times new roman", 15), textvariable=item6)
        itemchoosen6['values'] = ("RNK Bhuja 400g          ",
                                  "RNK Bhuja 200g          ",
                                  "Sada Bhuja 200g         ",
                                  "Sada Bhuja 150g         ",
                                  "Soya Bean 5kg           ",
                                  "Soya Bean 200g          ",
                                  "Soya Flaker 400g        ",
                                  "M.D. Soya Bean 15kg(bag)",
                                  "Darsan Basean 500g      ",
                                  "Darsan Basean 200g      ",
                                  "Tiger Basean 500g       ",
                                  "Tiger Basean 450        ",
                                  "RNK Cups                ",
                                  "RNK Rings               ",
                                  "RNK Chees Balls         ",
                                  "Haldi 200g              ",
                                  "Mirchi 200g             ",
                                  "Dahaniya 200g           ")
        itemchoosen6.grid(column=1, row=5)

        # ============Item7
        item7_lbl = Label(Frame2, font=("times new roman", 20, "bold"), fg=lbl_color, bg=bg_color, text="Item7")
        item7_lbl.grid(row=6, column=0, padx=10, pady=13)

        itemchoosen7 = ttk.Combobox(Frame2, width=12, font=("times new roman", 15), textvariable=item7)
        itemchoosen7['values'] = ("RNK Bhuja 400g          ",
                                  "RNK Bhuja 200g          ",
                                  "Sada Bhuja 200g         ",
                                  "Sada Bhuja 150g         ",
                                  "Soya Bean 5kg           ",
                                  "Soya Bean 200g          ",
                                  "Soya Flaker 400g        ",
                                  "M.D. Soya Bean 15kg(bag)",
                                  "Darsan Basean 500g      ",
                                  "Darsan Basean 200g      ",
                                  "Tiger Basean 500g       ",
                                  "Tiger Basean 450        ",
                                  "RNK Cups                ",
                                  "RNK Rings               ",
                                  "RNK Chees Balls         ",
                                  "Haldi 200g              ",
                                  "Mirchi 200g             ",
                                  "Dahaniya 200g           ")
        itemchoosen7.grid(column=1, row=6)
        itemchoosen7.current()

        # ============Item8
        item8_lbl = Label(Frame2, font=("times new roman", 20, "bold"), fg=lbl_color, bg=bg_color, text="Item8")
        item8_lbl.grid(row=7, column=0, padx=10, pady=13)

        itemchoosen8 = ttk.Combobox(Frame2, width=12, font=("times new roman", 15), textvariable=item8)
        itemchoosen8['values'] = ("RNK Bhuja 400g          ",
                                  "RNK Bhuja 200g          ",
                                  "Sada Bhuja 200g         ",
                                  "Sada Bhuja 150g         ",
                                  "Soya Bean 5kg           ",
                                  "Soya Bean 200g          ",
                                  "Soya Flaker 400g        ",
                                  "M.D. Soya Bean 15kg(bag)",
                                  "Darsan Basean 500g      ",
                                  "Darsan Basean 200g      ",
                                  "Tiger Basean 500g       ",
                                  "Tiger Basean 450        ",
                                  "RNK Cups                ",
                                  "RNK Rings               ",
                                  "RNK Chees Balls         ",
                                  "Haldi 200g              ",
                                  "Mirchi 200g             ",
                                  "Dahaniya 200g           ")
        itemchoosen8.grid(column=1, row=7)

        # ==================Quantity Frame=====================#
        Frame_2 = LabelFrame(root, text='Quantity', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                             font=("times new roman", 13, "bold"))
        Frame_2.place(x=275, y=162, width=225, height=538)

        # ===========Frame Content
        item1_en = Entry(Frame_2, bd=8, relief=GROOVE, textvariable=qitem1)
        item1_en.grid(row=0, column=1, padx=30, pady=13, ipady=2)

        # =======s
        item2_en = Entry(Frame_2, bd=8, relief=GROOVE, textvariable=qitem2)
        item2_en.grid(row=1, column=1, pady=13, padx=20, ipady=2)

        # =======
        item3_en = Entry(Frame_2, bd=8, relief=GROOVE, textvariable=qitem3)
        item3_en.grid(row=2, column=1, pady=13, padx=20, ipady=2)

        # ========
        item4_en = Entry(Frame_2, bd=8, relief=GROOVE, textvariable=qitem4)
        item4_en.grid(row=3, column=1, padx=20, pady=13, ipady=2)

        # ============
        item5_en = Entry(Frame_2, bd=8, relief=GROOVE, textvariable=qitem5)
        item5_en.grid(row=4, column=1, padx=20, pady=13, ipady=2)

        # =======
        item6_en = Entry(Frame_2, bd=8, relief=GROOVE, textvariable=qitem6)
        item6_en.grid(row=5, column=1, padx=20, pady=13, ipady=2)

        # ========
        item7_en = Entry(Frame_2, bd=8, relief=GROOVE, textvariable=qitem7)
        item7_en.grid(row=6, column=1, padx=20, pady=13, ipady=2)

        # =======
        item8_en = Entry(Frame_2, bd=8, relief=GROOVE, textvariable=qitem8)
        item8_en.grid(row=7, column=1, padx=20, pady=13, ipady=2)

        # ==================Price=====================#

        F2 = LabelFrame(root, text="Price", bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F2.place(x=500, y=162, width=260, height=538)

        # ===========Frame Content
        item1_en = Entry(F2, bd=8, relief=GROOVE, textvariable=pitem1)
        item1_en.grid(row=0, column=0, padx=25, pady=13, ipady=2)
        item1_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rs.")
        item1_lbl.grid(row=0, column=1, ipady=5, ipadx=5)

        # =======
        item2_en = Entry(F2, bd=8, relief=GROOVE, textvariable=pitem2)
        item2_en.grid(row=1, column=0, padx=10, pady=13, ipady=2)
        item2_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rs.")
        item2_lbl.grid(row=1, column=1, padx=10, pady=13)

        # =======
        item3_en = Entry(F2, bd=8, relief=GROOVE, textvariable=pitem3)
        item3_en.grid(row=2, column=0, padx=10, pady=13, ipady=2)
        item3_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rs.")
        item3_lbl.grid(row=2, column=1, padx=10, pady=13)

        # =======
        item4_en = Entry(F2, bd=8, relief=GROOVE, textvariable=pitem4)
        item4_en.grid(row=3, column=0, padx=10, pady=13, ipady=2)
        item4_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rs.")
        item4_lbl.grid(row=3, column=1, padx=10, pady=13)

        # =======
        item5_en = Entry(F2, bd=8, relief=GROOVE, textvariable=pitem5)
        item5_en.grid(row=4, column=0, padx=10, pady=13, ipady=2)
        item5_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rs.")
        item5_lbl.grid(row=4, column=1, padx=10, pady=13)

        # =======
        item6_en = Entry(F2, bd=8, relief=GROOVE, textvariable=pitem6)
        item6_en.grid(row=5, column=0, padx=10, pady=13, ipady=2)
        item6_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rs.")
        item6_lbl.grid(row=5, column=1, padx=10, pady=13)

        # =======
        item7_en = Entry(F2, bd=8, relief=GROOVE, textvariable=pitem7)
        item7_en.grid(row=6, column=0, padx=10, pady=13, ipady=2)
        item7_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rs.")
        item7_lbl.grid(row=6, column=1, padx=10, pady=13)

        # =======
        item8_en = Entry(F2, bd=8, relief=GROOVE, textvariable=pitem8)
        item8_en.grid(row=7, column=0, padx=10, pady=13, ipady=2)
        item8_lbl = Label(F2, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Rs.")
        item8_lbl.grid(row=7, column=1, padx=10, pady=13)

        # ===================Bill Aera================#
        F3 = Label(root, bd=10, relief=GROOVE)
        F3.place(x=760, y=162, width=595, height=400)
        # ===========
        bill_title = Label(F3, text="Bill List", font=("Lucida", 13, "bold"), bd=7, relief=GROOVE)
        bill_title.pack(fill=X)

        # ============
        scroll_y = Scrollbar(F3, orient=VERTICAL)
        txt = Text(F3, yscrollcommand=scroll_y.set, font=("Lucida", 10, "bold"))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=txt.yview)
        txt.pack(fill=BOTH, expand=1)

        # ===========Buttons Frame=============#
        F4 = LabelFrame(root, text='Bill Menu', bd=10, relief=GROOVE, bg=bg_color, fg="gold",
                        font=("times new roman", 13, "bold"))
        F4.place(x=760, y=555, width=590, height=145)

        # ===================
        cosm_lbl = Label(F4, font=("times new roman", 15, "bold"), fg=lbl_color, bg=bg_color, text="Total Food")
        cosm_lbl.grid(row=0, column=0, pady=10)
        cosm_en = Entry(F4, bd=8, relief=GROOVE, textvariable=total_food)
        cosm_en.grid(row=0, column=1, ipady=2, ipadx=5)

        # ====================
        # total_btn = Button(F4, text="Total", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
        #                    relief=GROOVE, command=total)
        # total_btn.grid(row=0, column=2, ipadx=20, padx=40)

        # ====================
        genbill_btn = Button(F4, text="Generate Bill", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                             relief=GROOVE, command=bill_area)
        genbill_btn.grid(row=1, column=0, padx=10, pady=10, ipadx=20)

        # ========================
        clear_btn = Button(F4, text="Clear", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                           relief=GROOVE, command=clearing)
        clear_btn.grid(row=1, column=1, ipadx=20)

        # ======================
        exit_btn = Button(F4, text="Exit", bg=bg_color, fg=fg_color, font=("lucida", 12, "bold"), bd=7,
                          relief=GROOVE, command=exiting)
        exit_btn.grid(row=1, column=2, ipadx=20)

        # ======================Printing bUTTON

        #   print_btn = Button(F4 , text = "Print" ,bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,
        #   relief = GROOVE,command = self.print)
        #  print_btn.grid(row = 0 , column = 3)

        root.mainloop()

#######################################################################################################################

    # -----------------Gmail
    def g_mail():
        mail = webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")
        return mail

#######################################################################################################################

    # -------------------Employee details
    def employees():
        # Clearing the home page
        gmail.place_forget()
        employe.place_forget()
        bill.place_forget()
        list.place_forget()
        active_details.place_forget()
        headline_txt.pack_forget()
        headline_frame.pack_forget()
        clock.pack_forget()
        lastline_frame.pack_forget()
        rights_txt.pack_forget()
        f3.pack_forget()
        root.title("Employees Details")
        hide1 = Label(root, text="              ", font="Georgia 40 bold", borderwidth=10)
        hide1.place(x=600, y=230)

        headline = Label(root, text="EMPLOYEE DETAILS:", font="Georgia 40 bold", bg="white", borderwidth=10)
        headline.place(x=50, y=20)

        # ---------Saving the details in Excel
        def do():
            emp_data = pd.DataFrame({'Name': [employee_nameentry.get()], 'phone': [phoneentry.get()],
                                     'email': [emailentry.get()], 'address': [addressentry.get()],
                                     'birth': [birthentry.get()],
                                     'father_name': [fatherentry.get()], 'post': [postentry.get()],
                                     'salary': [salaryentry.get()], 'proof': [proofentry.get()]})

            writer = pd.ExcelWriter('Employeedetails.xlsx', engine='openpyxl')
            writer.book = load_workbook('Employeedetails.xlsx')
            writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
            reader = pd.read_excel(r'Employeedetails.xlsx', engine='openpyxl')
            emp_data.to_excel(writer, 'Employeedetails', index=False, header=False, startrow=len(reader) + 1)
            writer.close()
            tsmg.showinfo("Details", "Employee Details Submitted")

        # -----------Back to Home Page
        def back2():
            # clearing all the widget
            headline.place_forget()
            employee_name.place_forget()
            employee_id.place_forget()
            phone.place_forget()
            email.place_forget()
            address.place_forget()
            birth.place_forget()
            father.place_forget()
            proof.place_forget()
            post.place_forget()
            salary.place_forget()
            employee_nameentry.place_forget()
            employee_identry.place_forget()
            phoneentry.place_forget()
            emailentry.place_forget()
            addressentry.place_forget()
            birthentry.place_forget()
            fatherentry.place_forget()
            proofentry.place_forget()
            postentry.place_forget()
            salaryentry.place_forget()
            f1.grid_forget()
            b1.place_forget()
            b2.place_forget()
            b3.place_forget()
            pic.place_forget()
            hide1.place_forget()

            # getting all the home widget
            headline_frame.pack(fill=BOTH)
            headline_txt.pack(fill=BOTH)
            f3.pack(fill=BOTH, pady=3)
            clock.pack(fill=BOTH)
            bill.place(x=510, y=350)
            gmail.place(x=50, y=200)
            employe.place(x=50, y=450)
            active_details.place(x=950, y=450)
            list.place(x=950, y=200)
            lastline_frame.pack(fill=BOTH, side=BOTTOM)
            rights_txt.pack(fill=BOTH, side=BOTTOM)

        def clear():
            employee_nameentry.delete(0, END)
            employee_identry.delete(0, END)
            phoneentry.delete(0, END)
            emailentry.delete(0, END)
            emailentry.delete(0, END)
            addressentry.delete(0, END)
            birthentry.delete(0, END)
            fatherentry.delete(0, END)
            proofentry.delete(0, END)
            postentry.delete(0, END)
            salaryentry.delete(0, END)

        employee_name = Label(root, text="Employee_Name:", font="georgia 15 bold")
        employee_id = Label(root, text="Employee_id:", font="georgia 15 bold")
        phone = Label(root, text="Phone:", font="georgia 15 bold")
        email = Label(root, text="Email:", font="georgia 15 bold")
        address = Label(root, text="Address:", font="georgia 15 bold")
        birth = Label(root, text="Date Of Birth:", font="georgia 15 bold")
        father = Label(root, text="Fathers Name:", font="georgia 15 bold")
        proof = Label(root, text="Proof:", font="georgia 15 bold")
        post = Label(root, text="Post:", font="georgia 15 bold")
        salary = Label(root, text="Salary:", font="georgia 15 bold")

        employee_name.place(x=63, y=150)
        employee_id.place(x=100, y=200)
        phone.place(x=165, y=250)
        email.place(x=170, y=300)
        address.place(x=150, y=350)
        birth.place(x=95, y=400)
        father.place(x=90, y=450)
        proof.place(x=175, y=500)
        post.place(x=185, y=550)
        salary.place(x=165, y=600)

        employee_namevalue = StringVar() or IntVar()
        employee_idvalue = StringVar() or IntVar()
        phonevalue = StringVar() or IntVar()
        emailvalue = StringVar() or IntVar()
        addressvalue = StringVar() or IntVar()
        birthvalue = StringVar() or IntVar()
        fathervalue = StringVar() or IntVar()
        proofvalue = StringVar() or IntVar()
        postvalue = StringVar() or IntVar()
        salaryvalue = StringVar() or IntVar()

        employee_nameentry = Entry(root, textvariable=employee_namevalue, font="Georgia 15", borderwidth=5)
        employee_identry = Entry(root, textvariable=employee_idvalue, font="Georgia 15", borderwidth=5)
        phoneentry = Entry(root, textvariable=phonevalue, font="Georgia 15", borderwidth=5)
        emailentry = Entry(root, textvariable=emailvalue, font="Georgia 15", borderwidth=5)
        addressentry = Entry(root, textvariable=addressvalue, font="Georgia 15", borderwidth=5)
        birthentry = Entry(root, textvariable=birthvalue, font="Georgia 15", borderwidth=5)
        fatherentry = Entry(root, textvariable=fathervalue, font="Georgia 15", borderwidth=5)
        proofentry = Entry(root, textvariable=proofvalue, font="Georgia 15", borderwidth=5)
        postentry = Entry(root, textvariable=postvalue, font="Georgia 15", borderwidth=5)
        salaryentry = Entry(root, textvariable=salaryvalue, font="Georgia 15", borderwidth=5)

        employee_nameentry.place(x=300, y=150)
        employee_identry.place(x=300, y=200)
        phoneentry.place(x=300, y=250)
        emailentry.place(x=300, y=300)
        addressentry.place(x=300, y=350)
        birthentry.place(x=300, y=400)
        fatherentry.place(x=300, y=450)
        proofentry.place(x=300, y=500)
        postentry.place(x=300, y=550)
        salaryentry.place(x=300, y=600)

        f1 = Frame(root, borderwidth=2)
        f1.grid()

        photo_home = PhotoImage(file="home_button_pic.png")
        photoimage_home = photo_home.subsample(5, 5)

        b1 = Button(root, text="Submit", borderwidth=7, font="Georgia 10 bold", width=9, height=3, bg="light grey",
                    command=do)
        b2 = Button(root, text="Clear", command=clear, borderwidth=7, font="Georgia 10 bold", width=9, height=3,
                    bg="light grey")
        b3 = Button(root, image=photoimage_home, command=back2, borderwidth=5, font="Georgia 10 bold", width=50,
                    height=35, bg="light grey")
        b1.place(x=630, y=510)
        b2.place(x=630, y=600)
        b3.place(x=1290, y=10)

        Photo_Log = PhotoImage(file="e_pic.png")
        pic = Label(root, image=Photo_Log)
        pic.place(x=780, y=50)

        root.mainloop()

#######################################################################################################################

    # ------------------Pending Orders, to_do_list System
    def order():
        # Clearing Home Page
        gmail.place_forget()
        employe.place_forget()
        bill.place_forget()
        list.place_forget()
        active_details.place_forget()
        headline_txt.pack_forget()
        headline_frame.pack_forget()
        clock.pack_forget()
        lastline_frame.pack_forget()
        rights_txt.pack_forget()
        f3.pack_forget()
        hide2 = Label(root, text="              ", font="Georgia 40 bold", borderwidth=10)
        hide2.place(x=600, y=230)

        root.title("RNK To_Do_List")

        # Headlines and frame of title
        f1 = Frame(root, borderwidth=7, bg="dim grey", relief=GROOVE, pady=5, padx=5)
        f1.pack(fill="x")
        hl = Label(f1, text="RNK Order: The Client Order's", fg="white", font="Georgia 32", bg="dim grey")
        hl.pack(fill="x")

        def back1():
            # clearing alll the list widget
            f1.pack_forget()
            hl.pack_forget()
            store_name.place_forget()
            address.place_forget()
            phone.place_forget()
            date.place_forget()
            store_nameentry.place_forget()
            addressentry.place_forget()
            phoneentry.place_forget()
            dateentry.place_forget()
            scroll.pack_forget()
            text.place_forget()
            txt_label.place_forget()
            open.place_forget()
            save_order.place_forget()
            print_details.place_forget()
            clear_all.place_forget()
            line.place_forget()
            b3.place_forget()
            hide2.place_forget()


            # getting all the home widget
            headline_frame.pack(fill=BOTH)
            headline_txt.pack(fill=BOTH)
            f3.pack(fill=BOTH, pady=3)
            clock.pack(fill=BOTH)
            bill.place(x=510, y=350)
            gmail.place(x=50, y=200)
            employe.place(x=50, y=450)
            active_details.place(x=950, y=450)
            list.place(x=950, y=200)
            lastline_frame.pack(fill=BOTH, side=BOTTOM)
            rights_txt.pack(fill=BOTH, side=BOTTOM)

        def save():
            files = [('Text Document', '*.txt')]
            filedialog.asksaveasfile(filetypes=files, defaultextension=files)

        def openfile():
            filedialog.askopenfilename()

        def clear():
            text.delete('1.0', END)
            store_nameentry.delete(0, END)
            addressentry.delete(0, END)
            phoneentry.delete(0, END)

        store_name = Label(root, text="Store_Name: ", font="georgia 15 bold")
        address = Label(root, text="Address: ", font="georgia 15 bold")
        phone = Label(root, text="Phone: ", font="georgia 15 bold")
        date = Label(root, text="Date:", font="georgia 15 bold")

        store_name.place(x=50, y=100)
        address.place(x=500, y=100)
        phone.place(x=890, y=100)
        date.place(x=908, y=150)

        store_namevalue = StringVar() or IntVar()
        addressvalue = StringVar() or IntVar()
        phonevalue = StringVar() or IntVar()
        datevalue = StringVar() or IntVar()

        store_nameentry = Entry(root, textvariable=store_namevalue, font="Georgia 15", borderwidth=5)
        addressentry = Entry(root, textvariable=addressvalue, font="Georgia 15", borderwidth=5)
        phoneentry = Entry(root, textvariable=phonevalue, font="Georgia 15", borderwidth=5)
        dateentry = Entry(root, textvariable=datevalue, font="Georgia 15", borderwidth=5)

        store_nameentry.place(x=200, y=100)
        addressentry.place(x=600, y=100)
        phoneentry.place(x=980, y=100)
        dateentry.place(x=980, y=150)

        # # Scrolll bar
        scroll = Scrollbar(root)
        scroll.pack(fill=BOTH, side=RIGHT)

        # Text for to do list
        text = Text(root, font="Georgia 15", width=50, height=15, borderwidth=6, yscrollcommand=scroll.set)
        text.place(x=100, y=240)

        txt_label = Label(root, text="Order's: ", fg="Black", font="georgia 20 bold")
        txt_label.place(x=350, y=200)

        open = Button(root, text="Open", font="Georgia 15 bold", fg="black", bg="Light grey", borderwidth=6, height=2,
                      width=15, command=openfile)
        open.place(x=970, y=350)
        save_order = Button(root, text="Save", font="Georgia 15 bold", fg="black", bg="Light grey", borderwidth=6,
                            height=2, width=15, command=save)
        save_order.place(x=970, y=260)
        print_details = Button(root, text="Print", font="Georgia 15 bold", fg="black", bg="Light grey", borderwidth=6,
                               height=2, width=15)
        print_details.place(x=970, y=440)
        clear_all = Button(root, text="Clear", font="Georgia 15 bold", fg="black", bg="Light grey", borderwidth=6,
                           height=2, width=15, command=clear)
        clear_all.place(x=970, y=530)

        line = Label(root, text="========================================================================", fg="Black",
                     font="georgia 20 bold")
        line.place(x=0, y=650)

        photo_home = PhotoImage(file="home_button_pic.png")
        photoimage_home = photo_home.subsample(5, 5)

        b3 = Button(root, image=photoimage_home, command=back1, borderwidth=5, font="Georgia 10 bold", width=50,
                    height=35, bg="light grey")
        b3.place(x=1285, y=80)

        root.mainloop()

#######################################################################################################################

    # -------------------Headline Frame and Text on Home Page
    headline_frame = Frame(root, borderwidth=10, relief=GROOVE, bg="black")
    headline_frame.pack(fill=BOTH)
    headline_txt = Label(headline_frame, text="RNK FOOD PRODUCTS Pvt Ltd.", font="Georgia 50 bold", fg="red",
                         bg="White")
    headline_txt.pack(fill=BOTH)


    # --------------------Clock
    def my_watch():
        x = time.strftime("Date : %Y-%m-%d, Time : %H:%M:%S, Day : %A")
        clock.config(text=x)
        clock.after(200, my_watch)


    f3 = Frame(root, borderwidth=2, bg="BLack")
    f3.pack(fill=BOTH, pady=3)
    clock = Label(f3, font="times 30 bold", fg="black")
    clock.pack(fill=BOTH)

    my_watch()

    # ------------------Copyrights Frame and Text
    lastline_frame = Frame(root, borderwidth=1, relief=SUNKEN, bg="black")
    lastline_frame.pack(fill=BOTH, side=BOTTOM)
    rights_txt = Label(lastline_frame, text="©Copyrights The Leap. All Rights Reserved", font="Georgia 15 bold",
                       fg="white", bg="black")
    rights_txt.pack(fill=BOTH, side=BOTTOM)

    photo = PhotoImage(file="mail_pic.png")
    photoimage = photo.subsample(3, 3)

    photo1 = PhotoImage(file="to_do_list_pic.png")
    photoimage1 = photo1.subsample(3, 3)

    photo2 = PhotoImage(file="employees_pic.png")
    photoimage2 = photo2.subsample(2, 2)

    photo3 = PhotoImage(file="active_details_pic.png")
    photoimage3 = photo3.subsample(2, 2)

    photo4 = PhotoImage(file="bill_pic.png")
    photoimage4 = photo4.subsample(2, 2)

    # -------------------Bill button
    bill = Button(root, text="BILL", image=photoimage4, font="Georgia 30 bold", fg="black", bg="white", borderwidth=10,
                  height=160, width=330, compound=TOP, command=billing)
    bill.place(x=510, y=350)

    # -------------------Gmail button
    gmail = Button(root, text="Gmail", image=photoimage, font="Georgia 30 bold", fg="black", bg="white", borderwidth=10,
                   height=160, width=330, compound=LEFT, command=g_mail)
    gmail.place(x=50, y=200)

    # -------------------Employee button
    employe = Button(root, text="Employees", image=photoimage2, font="Georgia 30 bold", fg="black", bg="white",
                     borderwidth=10, height=160, width=330, compound=TOP, command=employees)
    employe.place(x=50, y=450)

    # ----------------------Active button
    active_details = Button(root, text="Active details", image=photoimage3, font="Georgia 30 bold", fg="black",
                            bg="white", borderwidth=10, height=160, width=330, compound=TOP)
    active_details.place(x=950, y=450)

    # ---------------------Oredr Button
    list = Button(root, text="To_do_list", image=photoimage1, font="Georgia 30 bold", fg="black", bg="white",
                  borderwidth=10, height=160, width=330, compound=LEFT, command=order)
    list.place(x=950, y=200)
    root.mainloop()

#######################################################################################################################


user = Label(root, text=" User Name:", font="Georgia 30 bold")
password = Label(root, text=" Password:", font="Georgia 30 bold")
user.place(x=275, y=320)
password.place(x=300, y=380)

uservalve = StringVar()
passwordvalue = StringVar()

userentry = Entry(root, textvariable=uservalve, font="Georgia 25", borderwidth=5)
passwordentry = Entry(root, textvariable=passwordvalue, show="*", font="Georgia 25", borderwidth=5)
userentry.place(x=580, y=320)
passwordentry.place(x=580, y=380)

Photo_Log = PhotoImage(file="login_pic.png")
pic = Label(root, image=Photo_Log)
pic.place(x=580, y=50)

photo_log = PhotoImage(file="login_button pic.png")
photoimage_log = photo_log.subsample(4, 4)

b = Button(root, text="Login", image=photoimage_log, borderwidth=10, fg="black", font="Georgia 25", command=log_in,
           compound=LEFT)
b.place(x=500, y=500)
c = Button(root, text="Cancel", borderwidth=10, fg="black", font="Georgia 25")
c.place(x=760, y=500)

root.update()
root.mainloop()
