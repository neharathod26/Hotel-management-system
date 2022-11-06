from os import stat
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")

        # =============================== Variables ===============================
        # Generate random reference number
        self.ref_var = StringVar()
        x = random.randint(1000, 9999)
        self.ref_var.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()
        self.var_address = StringVar()
        # =============================== Variables ===============================

        # =============================== Title ===============================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=(
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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)
        # =============================== Label Frame ===============================

        # =============================== Labels and Entries ===============================
        # Customer Reference
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, width=29, textvariable=self.ref_var, font=(
            "arial", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)

        # Customer Name
        cname = Label(labelframeleft, text="Customer Name", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, width=29, textvariable=self.var_cust_name, font=(
            "arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # Mother Name
        lblmname = Label(labelframeleft, text="Mother Name", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(labelframeleft, width=29, textvariable=self.var_mother, font=(
            "arial", 13, "bold"))
        txtmname.grid(row=2, column=1)

        # Gender Combobox
        label_gender = Label(labelframeleft, text="Gender", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, font=(
            "arial", 12, "bold"), textvariable=self.var_gender, width=27, state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(1)

        combo_gender.grid(row=3, column=1)

        # Postcode
        lblPostCode = Label(labelframeleft, text="PostCode", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)

        txtPostCode = ttk.Entry(labelframeleft, width=29, textvariable=self.var_post, font=(
            "arial", 13, "bold"))
        txtPostCode.grid(row=4, column=1)

        # Mobile Number
        lblMobile = Label(labelframeleft, text="Mobile Number", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft, width=29, textvariable=self.var_mobile, font=(
            "arial", 13, "bold"))
        txtMobile.grid(row=5, column=1)

        # Email ID
        lblEmail = Label(labelframeleft, text="Email ID", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft, width=29, textvariable=self.var_email, font=(
            "arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)

        # Nationality Combobox
        lblNationality = Label(labelframeleft, text="Nationality", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=(
            "arial", 12, "bold"), width=27, state="readonly")
        combo_nationality["value"] = ("Indian", "Other")
        combo_nationality.current(0)

        combo_nationality.grid(row=7, column=1)

        # Id proof Combobox
        lblIdProof = Label(labelframeleft, text="ID Proof", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_id = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=(
            "arial", 12, "bold"), width=27, state="readonly")
        combo_id["value"] = ("AADHAR", "Driving License", "Passport")
        combo_id.current(0)

        combo_id.grid(row=8, column=1)

        # ID Number
        lblIdNumber = Label(labelframeleft, text="ID Number", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, width=29, textvariable=self.var_id_number, font=(
            "arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, text="Address", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)

        txtAddress = ttk.Entry(labelframeleft, width=29, textvariable=self.var_address, font=(
            "arial", 13, "bold"))
        txtAddress.grid(row=10, column=1)
        # =============================== Labels and Entries ===============================

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

        # =============================== Table Frame Search System ===============================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=(
            "arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, text="Search By", font=(
            "arial", 12, "bold"), bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()

        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=(
            "arial", 12, "bold"), width=24, state="readonly")
        combo_Search["value"] = ("Mobile", "Ref")
        combo_Search.current(0)

        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()

        txtSearch = ttk.Entry(Table_Frame, width=24, textvariable=self.txt_search, font=(
            "arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        # Search Button
        btnSearch = Button(Table_Frame, text="Search",command=self.search, font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=2)

        # Show All Button
        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data,font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=2)
        # =============================== Table Frame Search System===============================

        # =============================== Show Data Table ===============================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=852, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, columns=(
            "ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Ref No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother's Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile No")
        self.Cust_Details_Table.heading("email", text="Email ID")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="ID Proof")
        self.Cust_Details_Table.heading("idnumber", text="ID Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)

        # Call get_cursor function
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)

        # Call fetch data funcion
        self.fetch_data()
        # =============================== Show Data Table ===============================

    # =============================== Add data to database function ===============================
    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                # Connect to database
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.ref_var.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()

                ))

                conn.commit()

                # Call fetch data funcion
                self.fetch_data()

                conn.close()

                messagebox.showinfo(
                    "Success", "Customer has been Added", parent=self.root)

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
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())

            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()
            conn.close()
    # =============================== Fetch data from database function ===============================

    # =============================== get_cursor function ===============================
    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.ref_var.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_id_proof.set(row[8])
        self.var_id_number.set(row[9])
        self.var_address.set(row[10])
    # =============================== get_cursor function ===============================

    # =============================== Update data from database function ===============================
    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror(
                "Error", "Please Enter Mobile Number", parent=self.root)
        else:
            # Connect to database
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update customer set Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, IdProof=%s, IdNumber=%s, Address=%s where Ref=%s", (
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get(),
                    self.ref_var.get()
                ))

            conn.commit()

            # Call fetch data funcion
            self.fetch_data()

            conn.close()

            messagebox.showinfo(
                "Update", "Customer Details has been Updated Successfully", parent=self.root)
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
            query = "delete from customer where Ref=%s"
            value = (self.ref_var.get(),)
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
        # self.ref_var.set("")
        self.var_cust_name.set("")
        self.var_mother.set("")
        # self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        # self.var_nationality.set("")
        # self.var_id_proof.set("")
        self.var_id_number.set("")
        self.var_address.set("")

        # Generate random reference number
        x = random.randint(1000, 9999)
        self.ref_var.set(str(x))
    # =============================== Reset data function ===============================

    # =============================== Search function ===============================
    def search(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="root", database="management")
        my_cursor = conn.cursor()

        # my_cursor.execute("select * from customer where " + str(
        #     self.search_var.get()) + "LIKE '%" + str(self.txt_search.get())+"%'")

        my_cursor.execute("select * from customer where " + str(
            self.search_var.get()) + "=" + str(self.txt_search.get()))

        # Fetch data from table
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())

            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)

            conn.commit()
        conn.close()
    # =============================== Search function ===============================


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
