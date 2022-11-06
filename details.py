from os import stat
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+230")

        # =============================== Title ===============================
        lbl_title = Label(self.root, text="DETAILS", font=(
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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)
        # =============================== Label Frame ===============================

        # =============================== Labels and Entries ===============================
        # Floor
        lbl_floor = Label(labelframeleft, text="Floor", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor=StringVar()

        entry_floor = ttk.Entry(labelframeleft, width=20,  textvariable=self.var_floor,font=(
            "arial", 13, "bold"))
        entry_floor.grid(row=0, column=1, sticky=W)

        # Room No
        lbl_RoomNo = Label(labelframeleft, text="Room No", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_roomNo = StringVar()

        entry_RoomNo = ttk.Entry(labelframeleft, width=20,  textvariable=self.var_roomNo,font=(
            "arial", 13, "bold"))
        entry_RoomNo.grid(row=1, column=1, sticky=W)

        # Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        self.var_roomType = StringVar()

        entry_RoomType = ttk.Entry(labelframeleft, width=20,  textvariable=self.var_roomType,font=(
            "arial", 13, "bold"))
        entry_RoomType.grid(row=2, column=1, sticky=W)

        # =============================== Labels and Entries ===============================

        # =============================== Buttons ===============================
        btn_frame = LabelFrame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        # Add
        btnAdd = Button(btn_frame, text="Add",  command=self.add_data,font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        # Update
        btnUpdate = Button(btn_frame, text="Update",  command=self.update,font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        # Delete
        btnDelete = Button(btn_frame, text="Delete",  command=self.mDelete,font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        # Reset
        btnReset = Button(btn_frame, text="Reset",  command=self.reset,font=(
            "arial", 11, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)
        # =============================== Buttons ===============================

        # =============================== Table Frame Search System ===============================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=(
            "arial", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame, columns=(
            "floor", "roomno", "roomtype"), xscrollcommand=scroll_x, yscrollcommand=scroll_y)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomtype", text="Room Type")
       
        self.room_table["show"] = "headings"

        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomtype", width=100)

        self.room_table.pack(fill=BOTH, expand=1)

        # Call get_cursor function
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Call fetch data funcion
        self.fetch_data()
        # =============================== Table Frame Search System ===============================

    # =============================== Add data to database function ===============================
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomType.get() == "":
            messagebox.showerror(
                "Error", "All Fields are Required", parent=self.root)
        else:
            try:
                # Connect to database
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="root", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)", (
                    self.var_floor.get(),
                    self.var_roomNo.get(),
                    self.var_roomType.get()
                ))

                conn.commit()

                # Call fetch data funcion
                self.fetch_data()

                conn.close()

                messagebox.showinfo(
                    "Success", "New Room Added Successfully", parent=self.root)

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
        my_cursor.execute("select * from details")
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

        self.var_floor.set(row[0]),
        self.var_roomNo.set(row[1]),
        self.var_roomType.set(row[2]),
    # =============================== get_cursor function ===============================

    # =============================== Update data from database function ===============================
    def update(self):
        if self.var_floor.get() == "":
            messagebox.showerror(
                "Error", "Please Enter Room Number", parent=self.root)
        else:
            # Connect to database
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update details set Floor=%s, RoomType=%s where RoomNo=%s", (
                    self.var_floor.get(),
                    self.var_roomType.get(),
                    self.var_roomNo.get()
                ))

            conn.commit()

            # Call fetch data funcion
            self.fetch_data()

            conn.close()

            messagebox.showinfo(
                "Update", "New Room Details has been Updated Successfully", parent=self.root)
    # =============================== Update data from database function ===============================

    # =============================== Delete data from database function ===============================
    def mDelete(self):
        mDelete = messagebox.askyesno(
            "Hotel Management System", "Do you want to delete this room details?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="root", database="management")
            my_cursor = conn.cursor()

            # Another methhod to run query
            query = "delete from details where RoomNo=%s"
            value = (self.var_roomNo.get(),)
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
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_roomType.set(""),
    # =============================== Reset data function ===============================


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
