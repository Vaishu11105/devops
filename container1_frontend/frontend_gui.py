from tkinter import *
from tkinter import messagebox
import requests

class App:

    def __init__(self):
        self.root = Tk()
        self.root.title("Login/Register")
        self.root.geometry("400x500")
        self.root.configure(bg="#34495e")
        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear_gui()

        Label(self.root, text="Login asap", font=("Arial", 20, "bold"), bg="#34495e", fg="#aab7b8").pack(pady=20)

        Label(self.root, text="Email:", bg="#34495e", fg="white").pack(pady=5)
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack()

        Label(self.root, text="Password:", bg="#34495e", fg="white").pack(pady=5)
        self.password_input = Entry(self.root, show="*", width=30)
        self.password_input.pack()

        Button(self.root, text="Login", command=self.perform_login, width=15).pack(pady=15)
        Button(self.root, text="Register", command=self.register_gui, width=15).pack()

    def register_gui(self):
        self.clear_gui()

        Label(self.root, text="Register", font=("Arial", 20, "bold"), bg="#34495e", fg="#aab7b8").pack(pady=20)

        Label(self.root, text="Email:", bg="#34495e", fg="white").pack(pady=5)
        self.email_input = Entry(self.root, width=30)
        self.email_input.pack()

        Label(self.root, text="Password:", bg="#34495e", fg="white").pack(pady=5)
        self.password_input = Entry(self.root, show="*", width=30)
        self.password_input.pack()

        Label(self.root, text="Confirm Password:", bg="#34495e", fg="white").pack(pady=5)
        self.confirm_password_input = Entry(self.root, show="*", width=30)
        self.confirm_password_input.pack()

        Button(self.root, text="Register", command=self.perform_registration, width=15).pack(pady=15)
        Button(self.root, text="Back to Login", command=self.login_gui, width=15).pack()

    def clear_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()
        if not email or not password:
            messagebox.showinfo("Error", "Fill all details")
            return

        try:
            response = requests.post("http://c1_backend:5000/login", json={"email": email, "password": password})
            data = response.json()
            messagebox.showinfo("Info", data["message"])
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def perform_registration(self):
        email = self.email_input.get()
        password = self.password_input.get()
        confirm_password = self.confirm_password_input.get()
        if not email or not password or not confirm_password:
            messagebox.showinfo("Error", "Fill all details")
            return

        try:
            response = requests.post("http://c1_backend:5000/register", json={
                "email": email,
                "password": password,
                "confirm_password": confirm_password
            })
            data = response.json()
            messagebox.showinfo("Info", data["message"])
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    App()
