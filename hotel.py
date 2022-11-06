from os import times
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from customer import Cust_Win
from room import RoomBooking
from details import DetailsRoom
from report import Report


class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x860+0+0")

        # =============================== First Image ===============================
        img1 = Image.open(
            r"C:\Users\fizas\OneDrive\Desktop\Hotel Management System\hotel images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lbimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lbimg.place(x=0, y=0, width=1550, height=140)

        # =============================== Logo ===============================
        img2 = Image.open(
            r"C:\Users\fizas\OneDrive\Desktop\Hotel Management System\hotel images\logohotel.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lbimg.place(x=0, y=0, width=230, height=140)

        # =============================== Title ===============================
        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=(
            "times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # Main Frame
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # =============================== Menu ===============================
        lbl_menu = Label(main_frame, text="MENU", font=(
            "times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # =============================== ButtonFrame ===============================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        # =============================== Buttons ===============================
        # Customer Details
        cust_btn = Button(btn_frame, text="CUSTOMER",command=self.cust_details,width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        cust_btn.grid(row=0, column=0, pady=1)

        # Room Booking
        room_btn = Button(btn_frame, text="ROOM", command=self.roombooking,width=22, font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        room_btn.grid(row=1, column=0, pady=1)

        # Room Booking Details
        details_btn = Button(btn_frame, text="ROOM DETAILS", width=22, command=self.details_room,font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        details_btn.grid(row=2, column=0, pady=1)

        report_btn = Button(btn_frame, text="REPORT", width=22, command=self.report,font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        report_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", width=22, command=self.logout,font=(
            "times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)
        # =============================== Buttons ===============================

        # =============================== Right Side Image ===============================
        img3 = Image.open(
            r"C:\Users\fizas\OneDrive\Desktop\Hotel Management System\hotel images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lbimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lbimg1.place(x=225, y=0, width=1310, height=590)
        # =============================== Right Side Image ===============================

        # =============================== Down Images ===============================
        img4 = Image.open(
            r"C:\Users\fizas\OneDrive\Desktop\Hotel Management System\hotel images\myh.jpg")
        img4 = img4.resize((230, 210), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lbimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lbimg1.place(x=0, y=225, width=230, height=210)


        img5 = Image.open(
            r"C:\Users\fizas\OneDrive\Desktop\Hotel Management System\hotel images\khana.jpg")
        img5 = img5.resize((230, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lbimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lbimg1.place(x=0, y=420, width=230, height=190)
        # =============================== Down Images ===============================

    # Customer details function
    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    # Room Booking details function
    def roombooking(self):
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)

    # Details room function
    def details_room(self):
        self.new_window = Toplevel(self.root)
        self.app = DetailsRoom(self.new_window)

    # Details room function
    def report(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self.new_window)

    # Logout
    def logout(self):
        self.root.destroy()



if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
