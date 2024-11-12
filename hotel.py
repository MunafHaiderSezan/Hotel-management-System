import tkinter as tk
from PIL import Image, ImageTk
from customer import Cust_Win

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        # ==================================== 1st img ========================================================
        img1 = Image.open(r"C:\Users\munaf\Pictures\Hotel Management System\Hotel Management System\1633410403702hotel-images\hotel images\hotel1.png")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = tk.Label(self.root, image=self.photoimg1, bd=4, relief=tk.RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        # ===================================== logo ===========================================================
        img2 = Image.open(r"C:\Users\munaf\Pictures\Hotel Management System\Hotel Management System\1633410403702hotel-images\hotel images\logohotel1.png")
        img2 = img2.resize((230, 140), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lbl_logo = tk.Label(self.root, image=self.photoimg2, bd=4, relief=tk.RIDGE)
        lbl_logo.place(x=0, y=0, width=230, height=140)

        # ==================================== title ============================================================
        lbl_title = tk.Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=tk.RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # ==================================== main Frame ========================================================
        main_frame = tk.Frame(self.root, bd=4, relief=tk.RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # ===================================== menu ==============================================================
        lbl_menu = tk.Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=tk.RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ==================================== button ==========================================================
        btn_frame = tk.Frame(main_frame, bd=4, relief=tk.RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = tk.Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0)

        room_btn = tk.Button(btn_frame, text="ROOM", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0)

        details_btn = tk.Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0)

        report_btn = tk.Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0)

        logout_btn = tk.Button(btn_frame, text="LOGOUT", width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0)

        # ====================================== right side image =============================================
        img3 = Image.open(
            r"C:\Users\munaf\Pictures\Hotel Management System\Hotel Management System\1633410403702hotel-images\hotel images\slide3.jpg")
        img3 = img3.resize((1310, 590), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg3 = tk.Label(main_frame, image=self.photoimg3, bd=4, relief=tk.RIDGE)
        lblimg3.place(x=230, y=0, width=1310, height=590)

        # ======================================= down images ==================================================
        img4 = Image.open(
            r"C:\Users\munaf\Pictures\Hotel Management System\Hotel Management System\1633410403702hotel-images\hotel images\myh.jpg")
        img4 = img4.resize((230, 210), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg4 = tk.Label(main_frame, image=self.photoimg4, bd=4, relief=tk.RIDGE)
        lblimg4.place(x=0, y=225, width=230, height=210)

        img5 = Image.open(
            r"C:\Users\munaf\Pictures\Hotel Management System\Hotel Management System\1633410403702hotel-images\hotel images\khana.jpg")
        img5 = img5.resize((230, 190), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg5 = tk.Label(main_frame, image=self.photoimg5, bd=4, relief=tk.RIDGE)
        lblimg5.place(x=0, y=440, width=230, height=190)


        def cust_details(self):
            self.new_window= tk.Toplevel(self.root)
            self.app=Cust_Win(self.new_window)

    # Main execution


if __name__ == "__main__":
    root = tk.Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()