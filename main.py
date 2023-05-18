"""This file is the main file for the shop program. It allows the user to order items of a menu and choose for them to be delivered or picked up. It also allows the user to edit their order before confirming it."""
from tkinter import *
from tkinter import messagebox
import random


class Support:
    """Stores the name and price of an item in the shop for later use."""

    def __init__(self, name, price):
        """This function initialises the class and stores the name and price of an item in the shop."""
        self.name = name
        self.price = price


class Shop:
    """This class creates the main GUI for the page."""

    def __init__(self, parent):
        """This function initialises the class and creates the main GUI."""
        # Create frames
        self.mainframe = Frame(parent)
        title_frame = Frame(self.mainframe)
        option_select_frame = Frame(self.mainframe)
        order_frame = Frame(self.mainframe)
        self.review_order_frame = Frame(parent)
        self.review_order_frame_child = Frame(self.review_order_frame)
        self.receipt_frame = Frame(parent)
        # Create variables and lists
        self.food_items = [["Sushi (Japan)", 20], ["Peking Duck (China)", 40], ["Goulash (Hungary)", 10], ["Moussaka (Greece)", 15], ["Pad Thai (Thailand)", 8], ["Tacos (Mexico)", 3], ["Churros (Spain)", 5], ["Wiener Schnitzel (Austria)", 20], ["Lobster Roll (United States)", 25], ["Haggis (Scotland)", 15], ["Tiramisu (Italy)", 8], ["Feijoada (Brazil)", 12], ["Espresso (Italy)", 3], ["Margarita (Mexico)", 10], ["Mojito (Cuba)", 12], ["Champagne (France)", 50], ["Tequila (Mexico)", 6], ["Sangria (Spain)", 8], ["Gin and Tonic (England)", 7], ["Matcha Latte (Japan)", 5]]
        self.order_option = ""
        option_select_list = []
        self.order_list = []
        self.count = 0
        title_frame.grid(row=0, column=0, sticky="nsew")
        Label(title_frame, text="World's Delicacies", font=("Arial", 20)).pack()
        option_select_frame.grid(row=1, column=0, sticky="nsew")
        count = 0
        # Create Constants
        self.FONT = ("Arial", 16)
        self.BOLDFONT = ("Arial", 16, "bold")
        # Create buttons and labels for main menu
        for food in self.food_items:
            option_select_list.append(Button(option_select_frame, text=food[0], command=lambda m=count: self.add_to_order(m)).pack(fill=X, expand=True, padx=5, pady=5))
            count += 1
        self.mainframe.grid()
        order_frame.grid(row=2, column=0, sticky="nsew")
        self.order_button=Button(order_frame, text="Review Order", command=self.order)
        self.order_button.grid(row=0, column=1, sticky=NSEW, padx=5, pady=5)
        self.total_price = Label(order_frame, text="Total Price: $0.00", font=self.BOLDFONT)
        self.total_price.grid(row=0, column=2, sticky=NSEW, padx=5)
        # Disable order button so user can't order and empty order
        self.order_button.configure(state=DISABLED)

    def add_to_order(self, count):
        """This function adds the selected item to the order list."""
        # Ask user to confirm order
        check = messagebox.askyesno("Confirm", "Are you sure you want to add " + self.food_items[count][0] + " to your order?")
        # If user confirms, add item to order list and enable order button
        if check is True:
            self.order_list.append(Support(self.food_items[count][0], self.food_items[count][1]))
            self.order_button.configure(state=NORMAL)
            self.update_total_price()
        # If user cancels, do nothing
        else:
            pass

    def order(self):
        """This function creates the order GUI."""
        # Clear order GUI
        self.clear_order_details()
        self.mainframe.grid_forget()
        self.review_order_frame.grid(row=0, column=0, sticky="nsew")
        self.review_order_frame_child.grid(row=0, column=0, sticky="nsew")
        # Creates labels and buttons for order GUI and displays them
        for item in self.order_list:
            Label(self.review_order_frame_child, text=item.name + " $" + str(item.price), font=self.BOLDFONT).grid(row=self.count, column=0, sticky="nsew")
            Button(self.review_order_frame_child, text="Remove Item", command=lambda m=item: self.remove(m)).grid(row=self.count, column=1, sticky="nsew", padx=5, pady=5)
            self.count += 1
        # Creates Labels and buttons for better usability and visual appeal
        Label(self.review_order_frame_child, font=self.BOLDFONT, text="Total Price: $" + str(self.total_price_calc())).grid(row=self.count + 1, columnspan=2, sticky="nsew")
        Label(self.review_order_frame_child, text="Name:", font=self.BOLDFONT).grid(row=self.count + 2, columnspan=2, sticky="nsew")
        self.user_name = Entry(self.review_order_frame_child, fg="grey")
        self.user_name.bind("<FocusIn>", self.clear_entry_text)
        self.user_name.insert(0, "Please enter your name.")
        self.user_name.grid(row=self.count + 3, columnspan=2, sticky="nsew")
        self.dine_in_button = Button(self.review_order_frame_child, text="Dine In", font=self.BOLDFONT, command=self.have_here)
        self.dine_in_button.grid(row=self.count + 4, column=0, sticky="nsew", padx=5, pady=5)
        self.takeaway_button = Button(self.review_order_frame_child, text="Take Away", font=self.BOLDFONT, command=self.takeaway)
        self.takeaway_button.grid(row=self.count + 4, column=1, sticky="nsew", padx=5, pady=5)
        # Spacing text
        Label(self.review_order_frame_child, text="-----------------------------------").grid(row=self.count + 5, columnspan=2, sticky="nsew")
        Button(self.review_order_frame_child, text="Edit Order", font=self.BOLDFONT, command=self.back).grid(row=self.count + 6, column=0, sticky="nsew", padx=5, pady=5)
        Button(self.review_order_frame_child, text="Confirm Order", font=self.BOLDFONT, command=self.confirm).grid(row=self.count + 6, column=1, sticky="nsew", padx=5, pady=5)

    def clear_order_details(self):
        """This function clears the order GUI."""
        # Clear order GUI and reset variables by checking for how many widgets (Labels, buttons, etc.) are in the frame and destroying them
        for widget in self.review_order_frame_child.winfo_children():
            widget.destroy()
        self.count = 0
        self.review_order_frame.grid_forget()
        self.review_order_frame_child = Frame(self.review_order_frame)

    def have_here(self):
        """This function sets the order option to dine in."""
        self.order_option = "Dine In"
        # Disable dine in button and enable takeaway button
        self.dine_in_button.configure(state=DISABLED)
        self.takeaway_button.configure(state=NORMAL)

    def takeaway(self):
        """This function sets the order option to take away."""
        self.order_option = "Take Away"
        # Disable takeaway button and enable dine in button
        self.takeaway_button.configure(state=DISABLED)
        self.dine_in_button.configure(state=NORMAL)

    def remove(self, item):
        """This function removes the selected item from the order list."""
        # Ask user to confirm removal
        check = messagebox.askyesno("Confirm", "Are you sure you want to remove " + item.name + " from your order?")
        # If user confirms, remove item from order list and update order GUI
        if check is True:
            self.order_list.remove(item)
            self.review_order_frame_child = Frame(self.review_order_frame)
            self.order()
            self.update_total_price()
            # If order list is empty, disable order button and return user to main menu
            if self.order_list == []:
                messagebox.showinfo("Empty", "Your order is empty. You have been returned to the main menu.")
                self.order_button.configure(state=DISABLED)
                self.review_order_frame.grid_forget()
                self.review_order_frame_child.grid_forget()
                self.mainframe.grid(row=0, column=0, sticky="nsew")
        # If user cancels, do nothing
        else:
            return

    def back(self):
        """This function returns the user to the main menu."""
        self.review_order_frame.grid_forget()
        self.mainframe.grid(row=0, column=0, sticky="nsew")
        self.count = 0
        self.review_order_frame_child.grid_forget()
        self.review_order_frame_child = Frame(self.review_order_frame)
        self.update_total_price()

    def update_total_price(self):
        """This function updates the total price label."""
        # Update total price label
        self.total_price.configure(text="Total Price: $" + str(self.total_price_calc()))

    def total_price_calc(self):
        """This function calculates the total price of the order."""
        total = 0
        # Calculate total price of order
        for item in self.order_list:
            total += item.price
        return total

    def confirm(self):
        """This function confirms the order and creates the receipt GUI."""
        # Check if user has entered a name and selected an order option
        name = self.user_name.get().strip()
        if name == "Please enter your name." or name.isdigit() or name == "":
            messagebox.showerror("Error", "Please enter a valid name.")
            # If user has not entered a name, clear entry box
            if name == "Please enter your name.":
                return
            else:
                self.user_name.delete(0, END)
                return
        # If user has not selected an order option, display error message
        if self.order_option == "":
            messagebox.showerror("Error", "Please select an order option.")
            return
        # Ask user to confirm order
        check = messagebox.askyesno("Confirm", "Are you sure you want to confirm your order?")
        # If user confirms, create receipt GUI
        if check is True:
            self.count = 0
            self.review_order_frame_child.destroy()
            self.review_order_frame_child = Frame(self.review_order_frame)
            self.review_order_frame.grid_forget()
            self.receipt_frame.grid(row=0, column=0, sticky="nsew")
            Label(self.receipt_frame, text="World's Delicacies", font=("Arial", 20)).grid(row=0, column=0, sticky="nsew")
            Label(self.receipt_frame, text=self.order_option, font=(self.FONT)).grid(row=1, column=0, sticky="nsew")
            Label(self.receipt_frame, text="Name:", font=(self.BOLDFONT)).grid(row=2, column=0, sticky="nsew")
            Label(self.receipt_frame, text=name).grid(row=3, column=0, sticky="nsew")
            Label(self.receipt_frame, text="Items:", font=(self.BOLDFONT)).grid(row=4, column=0, sticky="nsew")
            for item in self.order_list:
                Label(self.receipt_frame, text=item.name).grid(row=self.count + 5, column=0, sticky="nsew")
                self.count += 1
            Label(self.receipt_frame, text="Total Price: $" + str(self.total_price_calc()), font=(self.BOLDFONT)).grid(row=self.count + 6, column=0, sticky="nsew")
            Label(self.receipt_frame, text="Order Number: ").grid(row=self.count + 7, column=0, sticky="nsew")
            # Generate random order number
            Label(self.receipt_frame, text=random.randint(100, 999), font=(self.BOLDFONT)).grid(row=self.count + 8, column=0, sticky="nsew")
            Button(self.receipt_frame, text="Place Another Order", command=self.wipe).grid(row=self.count + 9, column=0, sticky="nsew", padx=5, pady=5)
            self.update_total_price()
            self.order_list = []
            # Display success message
            messagebox.showinfo("Success", "Your order has been confirmed. Thank you for shopping with us.")
        else:
            pass

    def clear_entry_text(self, event):
        """This function clears the entry box when the user clicks on it."""
        self.user_name.delete(0, END)
        self.user_name.config(fg="black")

    def wipe(self):
        """This function wipes the receipt GUI and returns the user to the main menu."""
        self.order_button.configure(state=DISABLED)
        self.receipt_frame.grid_forget()
        self.order_option = ""
        self.mainframe.grid(row=0, column=0, sticky="nsew")
        self.count = 0
        self.review_order_frame_child.grid_forget()
        self.review_order_frame_child = Frame(self.review_order_frame)
        self.update_total_price()

if __name__ == '__main__': # Run program
    root = Tk()
    root.title("Shop")
    gui = Shop(root)
    root.mainloop()
