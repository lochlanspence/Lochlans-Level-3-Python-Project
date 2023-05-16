"""This file is the main file for the shop program. It allows the user to order items of a menu and choose for them to be delivered or picked up. It also allows the user to edit their order before confirming it."""
from tkinter import *
from tkinter import messagebox
import random


class Support:
    """Stores the name and price of an item in the shop for later use."""

    def __init__(self, name, price):
        """The function initialises the class and sets the name and price of the item."""
        self.name = name
        self.price = price


class Shop:
    """This class creates the main GUI for the page."""

    def __init__(self,parent):
        """This function initialises the class and creates the main GUI."""
        self.mainframe = Frame(parent)
        title_frame = Frame(self.mainframe)
        option_select_frame = Frame(self.mainframe)
        order_frame = Frame(self.mainframe)
        self.review_order_frame = Frame(parent)
        self.review_order_frame_child = Frame(self.review_order_frame)
        self.receipt_frame = Frame(parent)

        self.food_items = [["Pizza", 8.50], ["Burger", 12.50], ["Fries", 2.50] , ["Soda", 1.50] , ["Sausage Roll", 6.50]]

        self.FONT = ("Arial", 16)
        self.BOLDFONT = ("Arial", 16, "bold")
        option_select_list = []
        self.order_list = []
        self.count = 0
        title_frame.grid(row=0, column=0, sticky="nsew")
        title = Label(title_frame, text="Mr H's Shop", font=("Arial", 20)).pack()

        option_select_frame.grid(row=1, column=0, sticky="nsew")
        count = 0
        for food in self.food_items:
            option_select_list.append(Button(option_select_frame, text=food[0], command=lambda  m = count: self.add_to_order(m)).pack(fill=X,expand=True,padx=5,pady=5))
            count += 1

        self.mainframe.grid()
        order_frame.grid(row=2, column=0, sticky="nsew")
        order_button = Button(order_frame, text="Review Order", command = self.order).grid(row=0,column=1,sticky=NSEW,padx=5,pady=5)
        self.total_price = Label(order_frame, text="Total Price: $0.00", font=("Arial", 20))
        self.total_price.grid(row=0,column=2,sticky=NSEW,padx=5)

    def add_to_order(self, count):
        check = messagebox.askyesno("Confirm", "Are you sure you want to add " + self.food_items[count][0] + " to your order?")
        if check == True:
            self.order_list.append(Support(self.food_items[count][0], self.food_items[count][1]))
            self.update_total_price()
        else:
            pass

    def order(self):
        self.mainframe.grid_forget()
        self.review_order_frame.grid(row=0, column=0, sticky="nsew")
        self.review_order_frame_child.grid(row=0, column=0, sticky="nsew")
        for item in self.order_list:
            Label(self.review_order_frame_child, text=item.name + " $" + str(item.price)).grid(row=self.count, column=0, sticky="nsew")
            Button(self.review_order_frame_child, text="Remove Item", command=lambda m=item: self.remove(m)).grid(row=self.count, column=1, sticky="nsew", padx=5, pady=5)
            self.count += 1
        Label(self.review_order_frame_child, text="Total Price: $" + str(self.total_price_calc())).grid(row=self.count + 1, columnspan=2, sticky="nsew")
        Label(self.review_order_frame_child, text="Name:").grid(row=self.count + 2, columnspan=2, sticky="nsew")
        self.user_name = Entry(self.review_order_frame_child, fg="grey")
        self.user_name.bind("<FocusIn>", self.clear_entry_text)
        self.user_name.insert(0, "Please enter your name.")
        self.user_name.grid(row=self.count + 3, columnspan=2, sticky="nsew")
        Button(self.review_order_frame_child, text="Edit Order", command=self.back).grid(row=self.count + 4, column=0, sticky="nsew", padx=5, pady=5)
        Button(self.review_order_frame_child, text="Confirm Order", command=self.confirm).grid(row=self.count + 4, column=1, sticky="nsew", padx=5, pady=5)

    def remove(self, item):
        check = messagebox.askyesno("Confirm", "Are you sure you want to remove " + item.name + " from your order?")
        if check == True:
            self.order_list.remove(item)
            self.review_order_frame_child.destroy()
            self.review_order_frame_child = Frame(self.review_order_frame)
            self.order()
            self.update_total_price()
        else:
            return

    def back(self):
        self.review_order_frame.grid_forget()
        self.mainframe.grid(row=0, column=0, sticky="nsew")
        self.count = 0
        self.review_order_frame_child.grid_forget()
        self.review_order_frame_child = Frame(self.review_order_frame)
        self.update_total_price()


    def update_total_price(self):
        self.total_price.configure(text="Total Price: $" + str(self.total_price_calc()))

    def total_price_calc(self):
        total = 0
        for item in self.order_list:
            total += item.price
        return total

    def confirm(self):
        name = self.user_name.get().strip()
        if name == "" or name.isdigit():
            messagebox.showerror("Error", "Please enter a valid name.")
            self.user_name.delete(0, END)
            return
        check = messagebox.askyesno("Confirm", "Are you sure you want to confirm your order?")
        if check == True:
            self.count = 0
            self.review_order_frame_child.destroy()
            self.review_order_frame_child = Frame(self.review_order_frame)
            self.review_order_frame.grid_forget()
            self.receipt_frame.grid(row=0, column=0, sticky="nsew")
            Label(self.receipt_frame, text="Name:", font=(self.BOLDFONT)).grid(row=1, column=0, sticky="nsew")
            Label(self.receipt_frame, text=name).grid(row=2, column=0, sticky="nsew")
            Label(self.receipt_frame, text="Items:", font=(self.BOLDFONT)).grid(row=3, column=0, sticky="nsew")
            for item in self.order_list:
                Label(self.receipt_frame, text=item.name).grid(row=self.count + 4, column=0, sticky="nsew")
                self.count += 1
            Label(self.receipt_frame, text="Total Price: $" + str(self.total_price_calc()), font=(self.BOLDFONT)).grid(row=self.count + 5, column=0, sticky="nsew")
            Label(self.receipt_frame, text="Order Number: ").grid(row=self.count + 6, column=0, sticky="nsew")
            Label(self.receipt_frame, text=random.randint(100, 999), font=(self.BOLDFONT)).grid(row=self.count + 7, column=0, sticky="nsew")
            Button(self.receipt_frame, text="Place Another Order", command=self.wipe).grid(row=self.count + 8, column=0, sticky="nsew", padx=5, pady=5)
            self.update_total_price()
            self.order_list = []
            messagebox.showinfo("Success", "Your order has been confirmed. Thank you for shopping with us.")
        else:
            pass

    def clear_entry_text(self, event):
        self.user_name.delete(0, END)
        self.user_name.config(fg="black")
    
    def wipe(self):
        self.receipt_frame.grid_forget()
        self.mainframe.grid(row=0, column=0, sticky="nsew")
        self.count = 0
        self.review_order_frame_child.grid_forget()
        self.review_order_frame_child = Frame(self.review_order_frame)
        self.update_total_price()


if __name__ == '__main__':
    root = Tk()
    root.title("Shop")
    gui = Shop(root)
    root.mainloop()