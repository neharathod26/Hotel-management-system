from os import times
from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from customer import Cust_Win
from room import RoomBooking
from details import DetailsRoom


class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x860+0+0")

    
