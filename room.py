from os import stat
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class RoomBooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")

        # =============================== Variables ===============================
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()
        # =============================== Variables ===============================

        # =============================== Title ===============================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=(
            "times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)
        # =============================== Title ===============================

        # =============================== Logo ===============================
        img2 = Image.open(
            r"C:\Users\fizas\OneDrive\Desktop\Hotel Management System\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbimg.place(x=5, y=4, width=100, height=40)
        # =============================== Logo ===============================

        # =============================== Label Frame ===============================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Booking Details", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)
        # =============================== Label Frame ===============================

        # =============================== Labels and Entries ===============================
        # Customer Contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(labelframeleft, width=20, textvariable=self.var_contact, font=(
            "arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        # Fetch Data Button
        btnFetchData = Button(labelframeleft, text="Fetch Data", command=self.fetchContact, font=(
            "arial", 8, "bold"), bg="black", fg="gold", width=8)
        btnFetchData.place(x=345, y=4)

        # Check_in Date
        Check_in_date = Label(labelframeleft, text="Check In Date", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        Check_in_date.grid(row=1, column=0, sticky=W)

        txtCheck_in_date = ttk.Entry(labelframeleft, width=29, textvariable=self.var_checkin, font=(
            "arial", 13, "bold"))
        txtCheck_in_date.grid(row=1, column=1)

        # Check_out date
        Check_out_date = Label(labelframeleft, text="Check Out date", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        Check_out_date.grid(row=2, column=0, sticky=W)

        txtCheck_out_date = ttk.Entry(labelframeleft, width=29, textvariable=self.var_checkout, font=(
            "arial", 13, "bold"))
        txtCheck_out_date.grid(row=2, column=1)

        # Room Type
        label_RoomType = Label(labelframeleft, text="Room Type", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        # Connect to database
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomType from details")
        ide = my_cursor.fetchall()


        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=(
            "arial", 12, "bold"), width=27, state="readonly")
        combo_RoomType["value"] = (ide)
        combo_RoomType.current(0)

        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

        # txtRoomAvailable = ttk.Entry(labelframeleft, width=29, textvariable=self.var_roomavailable, font=(
        #     "arial", 13, "bold"))
        # txtRoomAvailable.grid(row=4, column=1)

        # Connect to database
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select RoomNo from details")
        rows = my_cursor.fetchall()

        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=(
            "arial", 12, "bold"), width=27, state="readonly")
        combo_RoomNo["value"] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, text="Meal", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft, width=29, textvariable=self.var_meal, font=(
            "arial", 13, "bold"))
        txtMeal.grid(row=5, column=1)

        # No of days
        lblNoOfDays = Label(labelframeleft, text="No of Days", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, width=29, textvariable=self.var_noofdays, font=(
            "arial", 13, "bold"))
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = Label(labelframeleft, text="Paid Tax", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)

        txtPaidTax = ttk.Entry(labelframeleft, width=29, textvariable=self.var_paidtax, font=(
            "arial", 13, "bold"))
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(labelframeleft, text="Sub Total", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtSubTotal = ttk.Entry(labelframeleft, width=29, textvariable=self.var_actualtotal, font=(
            "arial", 13, "bold"))
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(labelframeleft, text="Total Cost", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)

        txtTotalCost = ttk.Entry(labelframeleft, width=29, textvariable=self.var_total, font=(
            "arial", 13, "bold"))
        txtTotalCost.grid(row=9, column=1)
        # =============================== Labels and Entries ===============================

        # =============================== Bill Button ===============================
        # Bill
        btnBill = Button(labelframeleft, text="Bill", command=self.total, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)
        # =============================== Bill Button ===============================

        # =============================== Buttons ===============================
        btn_frame = LabelFrame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        # Add
        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        # Update
        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        # Delete
        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        # Reset
        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        # =============================== Buttons ===============================

        # =============================== Right Side Image ===============================
        img3 = Image.open(
            r"C:\Users\fizas\OneDrive\Desktop\Hotel Management System\hotel images\bed.jpg")
        img3 = img3.resize((420, 300), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lbimg.place(x=860, y=55, width=420, height=300)
        # =============================== Right Side Image ===============================

        # =============================== Table Frame Search System ===============================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=(
            "arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, text="Search By", font=(
            "arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()

        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=(
            "arial", 12, "bold"), width=24, state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current(0)

        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()

        txtSearch = ttk.Entry(Table_Frame, width=24, textvariable=self.txt_search, font=(
            "arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        # Search Button
        btnSearch = Button(Table_Frame, text="Search", command=self.search,font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=2)

        # Show All Button
        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data,font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=2)
        # =============================== Table Frame Search System ===============================

        # =============================== Show Data Table ===============================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=852, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, columns=(
            "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="NoOfDays")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        # Call get_cursor function
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.fetch_data()
        # =============================== Show Data Table ===============================

    # =============================== Add data to database function ===============================
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                # Connect to database
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get()
                ))

                conn.commit()

                # Call fetch data funcion
                self.fetch_data()

                conn.close()

                messagebox.showinfo(
                    "Success", "Room Booked", parent=self.root)

            except Exception as es:
                messagebox.showwarning(
                    "Warning", "Something went wrong:{str(es)}", parent=self.root)
    # =============================== Add data to database function ===============================

    # =============================== Fetch data from database function ===============================
    def fetch_data(self):
        # Connect to database
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.room_table.delete(
                *self.room_table.get_children())

            for i in rows:
                self.room_table.insert("", END, values=i)

            conn.commit()
            conn.close()
    # =============================== Fetch data from database function ===============================

    # =============================== get_cursor function ===============================
    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    # =============================== get_cursor function ===============================

    # =============================== Update data from database function ===============================
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please Enter Mobile Number", parent=self.root)
        else:
            # Connect to database
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update room set check_in=%s, check_out=%s, roomtype=%s, Room=%s, meal=%s, noOfdays=%s where Contact=%s", (
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get(),
                    self.var_contact.get()
                ))

            conn.commit()

            # Call fetch data funcion
            self.fetch_data()

            conn.close()

            messagebox.showinfo(
                "Update", "Room Details has been Updated Successfully", parent=self.root)
    # =============================== Update data from database function ===============================

    # =============================== Delete data from database function ===============================
    def mDelete(self):
        mDelete = messagebox.askyesno(
            "Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()

            # Another methhod to run query
            query = "delete from room where Contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return

        conn.commit()

        # Call fetch data funcion
        self.fetch_data()

        conn.close()
    # =============================== Delete data from database function ===============================

    # =============================== Reset data function ===============================
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_roomavailable.set(""),
        self.var_meal.set(""),
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
    # =============================== Reset data function ===============================

    # =============================== All Data Fetch ===============================
    def fetchContact(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please Enter Contact Number", parent=self.root)
        else:
            # Connect to database
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            query = ("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "Contact Not Found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=400, height=155)

                # ============== Name ==============
                lblName = Label(showDataframe, text="Name:", font=(
                    "arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl1 = Label(showDataframe, text=row, font=(
                    "arial", 12, "bold"))
                lbl1.place(x=130, y=0)
                # ============== Name ==============

                # ============== Gender ==============
                # Connect to database
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="management")
                my_cursor = conn.cursor()
                query = ("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataframe, text="Gender:", font=(
                    "arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataframe, text=row, font=(
                    "arial", 12, "bold"))
                lbl2.place(x=130, y=30)
                # ============== Gender ==============

                # ============== Email ==============
                # Connect to database
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="management")
                my_cursor = conn.cursor()
                query = ("select Email from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataframe, text="Email:", font=(
                    "arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataframe, text=row, font=(
                    "arial", 12, "bold"))
                lbl3.place(x=130, y=60)
                # ============== Email ==============

                # ============== Nationality ==============
                # Connect to database
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="management")
                my_cursor = conn.cursor()
                query = ("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataframe, text="Nationality:", font=(
                    "arial", 12, "bold"))
                lblEmail.place(x=0, y=90)

                lbl3 = Label(showDataframe, text=row, font=(
                    "arial", 12, "bold"))
                lbl3.place(x=130, y=90)
                # ============== Nationality ==============

                # ============== Address ==============
                # Connect to database
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="management")
                my_cursor = conn.cursor()
                query = ("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataframe, text="Address:", font=(
                    "arial", 12, "bold"))
                lblEmail.place(x=0, y=120)

                lbl3 = Label(showDataframe, text=row, font=(
                    "arial", 12, "bold"))
                lbl3.place(x=130, y=120)
                # ============== Address ==============
    # =============================== All Data Fetch ===============================

    # =============================== Search function ===============================
    def search(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()

        # my_cursor.execute("select * from customer where " + str(
        #     self.search_var.get()) + "LIKE '%" + str(self.txt_search.get())+"%'")

        my_cursor.execute("select * from room where " + str(
            self.search_var.get()) + "=" + str(self.txt_search.get()))

        # Fetch data from table
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.room_table.delete(
                *self.room_table.get_children())

            for i in rows:
                self.room_table.insert("", END, values=i)

            conn.commit()
        conn.close()
    # =============================== Search function ===============================

    # =============================== Bill function ===============================
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()

        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")

        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = float(300)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f" % ((q5)*0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double"):
            q1 = float(400)
            q2 = float(700)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f" % ((q5)*0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = float(700)
            q2 = float(1000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f" % ((q5)*0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Single"):
            q1 = float(200)
            q2 = float(1000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f" % ((q5)*0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Double"):
            q1 = float(400)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f" % ((q5)*0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Luxury"):
            q1 = float(800)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f" % ((q5)*0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            q1 = float(350)
            q2 = float(1200)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f" % ((q5)*0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            q1 = float(700)
            q2 = float(1500)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f" % ((q5)*0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif(self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury"):
            q1 = float(800)
            q2 = float(2000)
            q3 = float(self.var_noofdays.get())
            q4 = float(q1+q2)
            q5 = float(q3+q4)
            Tax = "Rs." + str("%.2f" % ((q5)*0.9))
            ST = "Rs." + str("%.2f" % ((q5)))
            TT = "Rs." + str("%.2f" % (q5+((q5)*0.09)))

            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)
    # =============================== Bill function ===============================


if __name__ == "__main__":
    root = Tk()
    obj = RoomBooking(root)
    root.mainloop()
