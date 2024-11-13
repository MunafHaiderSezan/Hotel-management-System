from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector

class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer Management System")
        self.root.geometry("1300x600+0+0")

        # Variable declarations
        self.var_ref = StringVar()
        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar(value="Male")
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar(value="Bangladeshi")
        self.var_id_proof = StringVar(value="National ID CARD")
        self.var_id_number = StringVar()
        self.var_address = StringVar()

        # Title
        title = Label(self.root, text="Customer Management System", font=("times new roman", 30, "bold"), bg="black", fg="gold")
        title.pack(side=TOP, fill=X)

        # Frame for form
        form_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        form_frame.place(x=10, y=50, width=400, height=500)

        # Labels and Entry fields
        lbl_ref = Label(form_frame, text="Refer No", bg="white", font=("arial", 12, "bold"))
        lbl_ref.grid(row=0, column=0, padx=10, pady=10)
        txt_ref = Entry(form_frame, textvariable=self.var_ref, font=("arial", 12, "bold"), width=20)
        txt_ref.grid(row=0, column=1, padx=10, pady=10)

        lbl_name = Label(form_frame, text="Customer Name", bg="white", font=("arial", 12, "bold"))
        lbl_name.grid(row=1, column=0, padx=10, pady=10)
        txt_name = Entry(form_frame, textvariable=self.var_cust_name, font=("arial", 12, "bold"), width=20)
        txt_name.grid(row=1, column=1, padx=10, pady=10)

        lbl_mother = Label(form_frame, text="Mother Name", bg="white", font=("arial", 12, "bold"))
        lbl_mother.grid(row=2, column=0, padx=10, pady=10)
        txt_mother = Entry(form_frame, textvariable=self.var_mother, font=("arial", 12, "bold"), width=20)
        txt_mother.grid(row=2, column=1, padx=10, pady=10)

        lbl_gender = Label(form_frame, text="Gender", bg="white", font=("arial", 12, "bold"))
        lbl_gender.grid(row=3, column=0, padx=10, pady=10)
        combo_gender = ttk.Combobox(form_frame, textvariable=self.var_gender, font=("arial", 12, "bold"), width=18)
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=3, column=1, padx=10, pady=10)

        lbl_post = Label(form_frame, text="Post Code", bg="white", font=("arial", 12, "bold"))
        lbl_post.grid(row=4, column=0, padx=10, pady=10)
        txt_post = Entry(form_frame, textvariable=self.var_post, font=("arial", 12, "bold"), width=20)
        txt_post.grid(row=4, column=1, padx=10, pady=10)

        lbl_mobile = Label(form_frame, text="Mobile No", bg="white", font=("arial", 12, "bold"))
        lbl_mobile.grid(row=5, column=0, padx=10, pady=10)
        txt_mobile = Entry(form_frame, textvariable=self.var_mobile, font=("arial", 12, "bold"), width=20)
        txt_mobile.grid(row=5, column=1, padx=10, pady=10)

        lbl_email = Label(form_frame, text="Email", bg="white", font=("arial", 12, "bold"))
        lbl_email.grid(row=6, column=0, padx=10, pady=10)
        txt_email = Entry(form_frame, textvariable=self.var_email, font=("arial", 12, "bold"), width=20)
        txt_email.grid(row=6, column=1, padx=10, pady=10)

    lbl_nationality = Label(form_frame, text="Nationality", bg="white", font=("arial", 12, "bold"))
    lbl_nationality.grid(row=7, column=0, padx=10, pady=10)
    combo_nationality = ttk.Combobox(form_frame, textvariable=self.var_nationality, font=("arial", 12, "bold"),
                                     width=18)
    combo_nationality['values'] = ("Bangladeshi", "Indian", "Pakistani", "Others")
    combo_nationality.grid(row=7, column=1, padx=10, pady=10)

    lbl_id_proof = Label(form_frame, text="ID Proof", bg="white", font=("arial", 12, "bold"))
    lbl_id_proof.grid(row=8, column=0, padx=10, pady=10)
    combo_id_proof = ttk.Combobox(form_frame, textvariable=self.var_id_proof, font=("arial", 12, "bold"), width=18)
    combo_id_proof['values'] = ("National ID CARD", "Passport", "Driving License")
    combo_id_proof.grid(row=8, column=1, padx=10, pady=10)

    lbl_id_number = Label(form_frame, text="ID Number", bg="white", font=("arial", 12, "bold"))
    lbl_id_number.grid(row=9, column=0, padx=10, pady=10)
    txt_id_number = Entry(form_frame, textvariable=self.var_id_number, font=("arial", 12, "bold"), width=20)
    txt_id_number.grid(row=9, column=1, padx=10, pady=10)

    lbl_address = Label(form_frame, text="Address", bg="white", font=("arial", 12, "bold"))
    lbl_address.grid(row=10, column=0, padx=10, pady=10)
    txt_address = Entry(form_frame, textvariable=self.var_address, font=("arial", 12, "bold"), width=20)
    txt_address.grid(row=10, column=1, padx=10, pady=10)

    # Button Frame
    btn_frame = Frame(form_frame, bd=2, relief=RIDGE, bg="white")
    btn_frame.place(x=5, y=400, width=390)

    btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold",
                    width=10)
    btnAdd.grid(row=0, column=0, padx=1)

    btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold",
                       width=10)
    btnUpdate.grid(row=0, column=1, padx=1)

    btnDelete = Button(btn_frame, text="Delete", command=self.mDelete, font=("arial", 12, "bold"), bg="black",
                       fg="gold", width=10)
    btnDelete.grid(row=0, column=2, padx=1)

    btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold",
                      width=10)
    btnReset.grid(row=0, column=3, padx=1)

    # Table Frame
    table_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
    table_frame.place(x=420, y=50, width=860, height=500)

    # Scrollbars
    scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
    scroll_y = Scrollbar(table_frame, orient=VERTICAL)

    self.Cust_Details_Table = ttk.Treeview(table_frame, columns=(
    "Ref", "Name", "Mother", "Gender", "Post", "Mobile", "Email", "Nationality", "ID Proof", "ID Number", "Address"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
    scroll_x.pack(side=BOTTOM, fill=X)
    scroll_y.pack(side=RIGHT, fill=Y)

    scroll_x.config(command=self.Cust_Details_Table.xview)
    scroll_y.config(command=self.Cust_Details_Table.yview)

    self.Cust_Details_Table.heading("Ref", text="Ref")
    self.Cust_Details_Table.heading("Name", text="Name")
    self.Cust_Details_Table.heading("Mother", text="Mother")
    self.Cust_Details_Table.heading("Gender", text="Gender")
    self.Cust_Details_Table.heading("Post", text="Post")
    self.Cust_Details_Table.heading("Mobile", text="Mobile")
    self.Cust_Details_Table.heading("Email", text="Email")
    self.Cust_Details_Table.heading("Nationality", text="Nationality")
    self.Cust_Details_Table.heading("ID Proof", text="ID Proof")
    self.Cust_Details_Table.heading("ID Number", text="ID Number")
    self.Cust_Details_Table.heading("Address", text="Address")

    self.Cust_Details_Table['show'] = 'headings'
    self.Cust_Details_Table.pack(fill=BOTH, expand=1)

    def fetch_data(self):
        # Clear the current data in the table
        for row in self.Cust_Details_Table.get_children():
            self.Cust_Details_Table.delete(row)
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customer")
            rows = cursor.fetchall()
            for row in rows:
                self.Cust_Details_Table.insert('', END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")

    def update(self):
        if self.var_ref.get() == "" or self.var_cust_name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management")
                cursor = conn.cursor()
                cursor.execute(
                    "UPDATE customer SET name=%s, mother=%s, gender=%s, post=%s, mobile=%s, email=%s, nationality=%s, id_proof=%s, id_number=%s, address=%s WHERE ref=%s",
                    (self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(), self.var_post.get(),
                     self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(), self.var_id_proof.get(),
                     self.var_id_number.get(), self.var_address.get(), self.var_ref.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")

    def fetch_data(self):
        # Clear the current data in the table
        for row in self.Cust_Details_Table.get_children():
            self.Cust_Details_Table.delete(row)
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management")
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customer")
            rows = cursor.fetchall()
            for row in rows:
                self.Cust_Details_Table.insert('', END, values=row)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to {str(e)}")

    def update(self):
        if self.var_ref.get() == "" or self.var_cust_name.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management")
                cursor = conn.cursor()
                cursor.execute("UPDATE customer SET name=%s, mother=%s, gender=%s, post=%s, mobile=%s, email=%s, nationality=%s, id_proof=%s, id_number=%s, address=%s WHERE ref=%s",
                               (self.var_cust_name.get(), self.var_mother.get(), self.var_gender.get(), self.var_post.get(),
                                self.var_mobile.get(), self.var_email.get(), self.var_nationality.get(), self.var_id_proof.get(),
                                self.var_id_number.get(), self.var_address.get(), self.var_ref.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer updated successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")

    def mDelete(self):
        if self.var_ref.get() == "":
            messagebox.showerror("Error", "Enter the Reference number to delete")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="", database="hotel_management")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM customer WHERE ref=%s", (self.var_ref.get(),))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer deleted successfully")
            except Exception as e:
                messagebox.showerror("Error", f"Error due to {str(e)}")

    def reset(self):
        self.var_ref.set("")
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("Male")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nationality.set("Bangladeshi")
        self.var_id_proof.set("National ID CARD")
        self.var_id_number.set("")
        self.var_address.set("")
    def on_select(self, event):
        selected_row = self.Cust_Details_Table.focus()
        if selected_row:
            data = self.Cust_Details_Table.item(selected_row)
            row = data['values']

            self.var_ref.set(row[0])
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

    def run(self):
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.on_select)
        self.root.mainloop()

if __name__ == "__main__":
    root = Tk()
    app = Cust_Win(root)
    app.run()