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
        self.root.geometry("1295x580+230+220")

        # ===================================== variable ===========================================================
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # ==================================== title ============================================================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ===================================== logo ===========================================================
        img2 = Image.open(
            r"C:\Users\munaf\Documents\GitHub\Hotel-management-System\1633410403702hotel-images\hotel images\logohotel1.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_logo = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lbl_logo.place(x=5, y=2, width=100, height=40)

        # ======================================== labelFrame =============================================================
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # ========================================= labels and entries ======================================================
        # custRef
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("times new roman", 18, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        enty_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, state="readonly",
                             font=("times new roman", 13, "bold"))
        enty_ref.grid(row=0, column=1)

        # cust name
        lbl_cname = Label(labelframeleft, font=("arial", 12, "bold"), text="Customer Name:", padx=2, pady=6)
        lbl_cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, font=("arial", 13, "bold"), width=29)
        txtcname.grid(row=1, column=1)

        # mother name
        lbl_mname = Label(labelframeleft, font=("arial", 12, "bold"), text="Mother Name:", padx=2, pady=6)
        lbl_mname.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(labelframeleft, textvariable=self.var_mother, font=("arial", 13, "bold"), width=29)
        txtmname.grid(row=2, column=1)

        # gender combo box
        lbl_gender = Label(labelframeleft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6)
        lbl_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft,
                                    textvariable=self.var_gender,
                                    font=("arial", 12, "bold"),
                                    width=27,
                                    state="readonly")

        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # postcode
        lblPostCode = Label(labelframeleft, font=("arial", 12, "bold"), text="PostCode:", padx=(2), pady=(6))
        lblPostCode.grid(row=(4), column=(0), sticky=W)

        txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post, font=("arial", 13, "bold"), width=(29))
        txtPostCode.grid(row=(4), column=(1))

        # mobile number
        lblMobile = Label(labelframeleft, font=("arial", 12, "bold"), text="Mobile:", padx=(2), pady=(6))
        lblMobile.grid(row=(5), column=(0), sticky=W)

        txtMobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, font=("arial", 13, "bold"), width=(29))
        txtMobile.grid(row=(5), column=(1))

        # email
        lblEmail = Label(labelframeleft, font=("arial", 12, "bold"), text="Email:", padx=(2), pady=(6))
        lblEmail.grid(row=(6), column=(0), sticky=W)

        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, font=("arial", 13, "bold"), width=(29))
        txtEmail.grid(row=(6), column=(1))

        # nationality
        lblNationality = Label(labelframeleft, font=("arial", 12, "bold"), text="Nationality:", padx=(2), pady=(6))
        lblNationality.grid(row=(7), column=(0), sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"),
                                         width=(27), state="readonly")
        combo_Nationality["value"] = ("Bangladeshi", "Indian", "American", "British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=(7), column=(1))

        # ID proof type combo box
        lblIdProof = Label(labelframeleft, font=("arial", 12, "bold"), text="Id Proof Type:", padx=(2), pady=(6))
        lblIdProof.grid(row=(8), column=(0), sticky=W)

        combo_id = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=(27),
                                state="readonly")
        combo_id["value"] = ["National ID CARD", "Passport", "Driving License", "Birth Certificate"]
        combo_id.current(0)
        combo_id.grid(row=(8), column=(1))

        # ID number
        lblIdNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="Id Number:", padx=(2), pady=(6))
        lblIdNumber.grid(row=(9), column=(0), sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number, font=("arial", 13, "bold"), width=(29))
        txtIdNumber.grid(row=(9), column=(1))

        # address
        lblAddress = Label(labelframeleft, font=("arial", 12, "bold"), text="Address:", padx=(2), pady=(6))
        lblAddress.grid(row=(10), column=(0), sticky=W)

        txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address, font=("arial", 13, "bold"), width=(29))
        txtAddress.grid(row=(10), column=(1))

        # ======================================== buttons =============================================================
        btn_frame = Frame(labelframeleft, borderwidth=(2), relief=(RIDGE))
        btn_frame.place(x=(0), y=(400), width=(412), height=(40))

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold",
                        width=(10))
        btnAdd.grid(row=(0), column=(0), padx=(1))

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 12, "bold"), bg="black",
                           fg="gold",
                           width=(10))
        btnUpdate.grid(row=(0), column=(1), padx=(1))

        btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="black",
                           fg="gold",
                           width=(10))
        btnDelete.grid(row=(0), column=(2), padx=(1))

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12, "bold"), bg="black",
                          fg="gold",
                          width=(10))
        btnReset.grid(row=(0), column=(3), padx=(1))

        # =========================================== table frame search system ====================================================
        Table_Frame = LabelFrame(self.root, borderwidth=(2),
                                 relief=(RIDGE),
                                 text="View Details And Search System",
                                 font=("times new roman", 12, "bold"),
                                 padx=(2))
        Table_Frame.place(x=(435),
                          y=(50),
                          width=(860),
                          height=(490))

        lblSearchBy = Label(Table_Frame,
                            font=("arial", 12, "bold"),
                            text="Search By:",
                            bg="red",
                            fg="white")
        lblSearchBy.grid(row=(0),
                         column=(0),
                         sticky=W,
                         padx=(2))

        self.search_variable = StringVar()
        combo_Search = ttk.Combobox(Table_Frame,
                                    textvariable=self.search_variable,
                                    font=("arial", 12, "bold"),
                                    width=24,
                                    state="readonly")

        combo_Search["value"] = ["Mobile", "Passport", "Reference"]
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame,
                              textvariable=self.txt_search,
                              font=("arial", 13, "bold"),
                              width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame,
                           text="Search",
                           command=self.search,
                           font=("arial", 12, "bold"),
                           bg="black",
                           fg="gold",
                           width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame,
                            text="Show All",
                            command=self.fetch_data,
                            font=("arial", 12, "bold"),
                            bg="black",
                            fg="gold",
                            width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # ============================================= Show Data Table ============================================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table,
                                                column=["ref", "name", "mother", "gender", "post", "mobile", "email",
                                                        "nationality", "idproof", "idnumber", "address"],
                                                xscrollcommand=scroll_x.set,
                                                yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No ")
        self.Cust_Details_Table.heading("name", text="Name ")
        self.Cust_Details_Table.heading("mother", text="Mother Name ")
        self.Cust_Details_Table.heading("gender", text="Gender ")
        self.Cust_Details_Table.heading("post", text="PostCode ")
        self.Cust_Details_Table.heading("mobile", text="Mobile ")
        self.Cust_Details_Table.heading("email", text="Email ")
        self.Cust_Details_Table.heading("nationality", text="Nationality ")
        self.Cust_Details_Table.heading("idproof", text="Id Proof ")
        self.Cust_Details_Table.heading("idnumber", text="Id Number ")
        self.Cust_Details_Table.heading("address", text="Address ")

        # Show headings only
        self.Cust_Details_Table["show"] = "headings"

        # Set column widths
        columns_widths = [100] * 11
        for i in range(len(columns_widths)):
            self.Cust_Details_Table.column(i, width=columns_widths[i])

        self.Cust_Details_Table.pack(fill=BOTH, expand=True)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if not (self.var_mobile.get() and self.var_mother.get()):
            messagebox.showerror("Error", "All fields are required ", parent=self.root)
            return

        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="2024", database="customer")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    self.var_ref.get(),
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
                )
            )
            conn.commit()
            messagebox.showinfo("Success", "Customer has been added.", parent=self.root)
            conn.close()
            self.fetch_data()  # Make sure to call self.fetch_data() with 'self.'

        except Exception as es:
            messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

        def fetch_data(self):
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="2024", database="customer")
                my_cursor = conn.cursor()
                my_cursor.execute("SELECT * FROM customer")

                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                    for i in rows:
                        self.Cust_Details_Table.insert("", END, value=i)

                conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while fetching data: {str(e)}", parent=self.root)

        def get_cursor(self, event=None):
            cursor_row = self.Cust_Details_Table.focus()
            content = self.Cust_Details_Table.item(cursor_row)
            row_content = content['values']

            # Set the variables with the selected row's data
            self.var_ref.set(row_content[0])
            self.var_cust_name.set(row_content[1])
            self.var_mother.set(row_content[2])
            self.var_gender.set(row_content[3])
            self.var_post.set(row_content[4])
            self.var_mobile.set(row_content[5])
            self.var_email.set(row_content[6])
            self.var_nationality.set(row_content[7])
            self.var_id_proof.set(row_content[8])
            self.var_id_number.set(row_content[9])
            self.var_address.set(row_content[10])

        def update(self):
            if not (self.var_mobile.get()):
                messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
                return

            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="2024", database="customer")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    """UPDATE customer SET Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s,
                    Nationality=%s, Idproof=%s, Idnumber=%s, Address=%s WHERE Ref=%s""",
                    (
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
                        self.var_ref.get()
                    )
                )

                conn.commit()
                self.fetch_data()
                conn.close()

                messagebox.showinfo("Update", "Customer details have been updated successfully.", parent=self.root)
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while updating: {str(e)}", parent=self.root)

        def mDelete(self):
            mDelete = messagebox.askyesno(
                "Hotel Management System",
                "Do you want to delete this customer?",
                parent=self.root
            )

            if mDelete:
                try:
                    conn = mysql.connector.connect(host="localhost", username="root", password="2024",
                                                   database="customer")
                    my_cursor = conn.cursor()

                    query = """DELETE FROM customer WHERE Ref=%s"""
                    value = (self.var_ref.get(),)  # Make sure to pass a tuple
                    my_cursor.execute(query, value)

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred while deleting: {str(e)}", parent=self.root)

        def reset(self):
            for var in [self.var_ref, self.var_cust_name, self.var_mother, self.var_gender, self.var_post,
                        self.var_mobile, self.var_email, self.var_nationality, self.var_id_proof,
                        self.var_id_number, self.var_address]:
                var.set("")

            x = random.randint(1000, 9999)
            self.var_ref.set(str(x))

        def search(self):
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="2024", database="customer")
                my_cursor = conn.cursor()

                search_by = self.search_variable.get()
                search_text = self.txt_search.get()

                if search_by == "Mobile":
                    query = "SELECT * FROM customer WHERE Mobile LIKE %s"
                    value = (f"%{search_text}%",)
                elif search_by == "Passport":
                    query = "SELECT * FROM customer WHERE Idnumber LIKE %s"
                    value = (f"%{search_text}%",)
                else:
                    query = "SELECT * FROM customer WHERE Name LIKE %s"
                    value = (f"%{search_text}%",)

                my_cursor.execute(query, value)
                rows = my_cursor.fetchall()

                if len(rows) != 0:
                    self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                    for i in rows:
                        self.Cust_Details_Table.insert("", END, value=i)

                conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred while searching: {str(e)}", parent=self.root)

                # Main function to run the application
            if __name__ == "__main__":
                root = Tk()
                obj = Cust_Win(root)
                root.mainloop()