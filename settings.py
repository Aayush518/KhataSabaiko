# settings.py

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import credentials

# You can define your fonts and colors here
bg = '#94ffd6'  # or your desired background color
# styles.py

bg = '#94ffd6'
medium_lined = ('Imprint MT Shadow', 55, 'underline')
tree_font = ('Georgia', 20)
tiny_font = ('Times New Roman', 20)

# ...

class SettingsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg)
        self.controller = controller

        Label(self, text="Settings", fg="dark blue", font=medium_lined, bg=bg).pack()

        Label(self, text="New Username:", font=tree_font, bg=bg).pack()
        self.new_username = Entry(self, font=tree_font)
        self.new_username.pack()

        Label(self, text="New Password:", font=tree_font, bg=bg).pack()
        self.new_password = Entry(self, font=tree_font, show="*")
        self.new_password.pack()

        Button(self, text="Save", font=tiny_font, bg='green', fg='white', bd=4, relief=GROOVE, command=self.apply_changes).pack()
        Button(self, text="Back", font=tiny_font, bg='gray', fg='white', bd=4, relief=GROOVE, command=lambda: controller.show_frame("LockScreen")).pack()

    def apply_changes(self):
        new_username = self.new_username.get()
        new_password = self.new_password.get()

        if new_username and new_password:
            credentials.update_credentials(new_username, new_password)
            credentials.save_credentials()  # Save the updated credentials
            messagebox.showinfo("Success", "Credentials updated successfully!")
        else:
            messagebox.showerror("Error", "Both fields are required.")