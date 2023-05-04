"""This file is the main file for the shop program. It allows the user to order items of a menu and choose for them to be delivered or picked up. It also allows the user to edit their order before confirming it."""
from tkinter import *
from tkinter import messagebox


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
        title_frame = Frame(parent)
        option_select_frame = Frame(parent)
        order_frame = Frame(parent)
        confirm_item_add_frame = Frame(parent)

        food_items = [["Pizza", 8.50], ["Burger", 12.50], ["Fries", 2.50] , ["Soda", 1.50] , ["Sausage Roll", 6.50]]

        option_select_list = []
        self.order_list = []
        title_frame.grid(row=0, column=0, sticky="nsew")
        title = Label(title_frame, text="Mr H's Shop", font=("Arial", 20)).pack()

        option_select_frame.grid(row=1, column=0, sticky="nsew")
        count = 0
        count2 = 0
        for food in food_items:
            if count == 3:
                count = 0
                count2 += 1
            option_select_list.append(Button(option_select_frame, text=food[0], command=lambda: self.add_to_order(food[0], food[1])).grid(row=count,column=count2,sticky=NSEW,padx=5))
            count+=1
        

        order_frame.grid(row=2, column=0, sticky="nsew")
        edit_order =Button(order_frame, text="Edit Order", command=lambda: self.edit_order()).grid(row=0,column=0,sticky=NSEW,padx=5)
        order_button = Button(order_frame, text="Order", command=lambda: self.order()).grid(row=0,column=1,sticky=NSEW,padx=5)
        self.total_price = Label(order_frame, text="Total Price: $0.00", font=("Arial", 20))
        self.total_price.grid(row=0,column=2,sticky=NSEW,padx=5)

    def add_to_order(self, name, price):
        check = messagebox.askyesno("Confirm", "Are you sure you want to add " + name + " to your order?")
        if check == True:
            self.order_list.append(Support(name, price))
            self.update_total_price()
        else:
            pass

    def edit_order(self):
        pass

    def order(self):
        pass

    def update_total_price(self):
        self.total_price.configure(text="Total Price: $" + str(self.total_price_calc()))

    def total_price_calc(self):
        total = 0
        for item in self.order_list:
            total += item.price
        return total



if __name__ == '__main__':
    root = Tk()
    root.title("Shop")
    gui = Shop(root)
    root.mainloop()