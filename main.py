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
        self.mainframe = Frame(parent)
        title_frame = Frame(self.mainframe)
        option_select_frame = Frame(self.mainframe)
        order_frame = Frame(self.mainframe)
        self.review_order_frame = Frame(parent)
        self.review_order_frame_child = Frame(self.review_order_frame)

        self.food_items = [["Pizza", 8.50], ["Burger", 12.50], ["Fries", 2.50] , ["Soda", 1.50] , ["Sausage Roll", 6.50]]

        option_select_list = []
        self.order_list = []
        self.count = 0
        title_frame.grid(row=0, column=0, sticky="nsew")
        title = Label(title_frame, text="Mr H's Shop", font=("Arial", 20)).pack()

        option_select_frame.grid(row=1, column=0, sticky="nsew")
        count = 0
        count2 = 0
        for food in self.food_items:
            option_select_list.append(Button(option_select_frame, text=food[0], command=lambda  m = count: self.add_to_order(m)).pack(fill=X,expand=True,padx=5,pady=5))
            count += 1

        self.mainframe.grid()
        order_frame.grid(row=2, column=0, sticky="nsew")
        order_button = Button(order_frame, text="Review Order", command = self.order).grid(row=0,column=1,sticky=NSEW,padx=5)
        self.total_price = Label(order_frame, text="Total Price: $0.00", font=("Arial", 20))
        self.total_price.grid(row=0,column=2,sticky=NSEW,padx=5)

    def add_to_order(self, count):
        print(count)
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
            self.count += 1
        Label(self.review_order_frame_child, text="Total Price: $" + str(self.total_price_calc())).grid(row=self.count + 1, column=0, sticky="nsew")
        Button(self.review_order_frame_child, text="Edit Order", command=self.back).grid(row=self.count + 1, column=1, sticky="nsew")
        Button(self.review_order_frame_child, text="Confirm Order", command=self.confirm).grid(row=self.count + 1, column=2, sticky="nsew")

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
        pass


if __name__ == '__main__':
    root = Tk()
    root.title("Shop")
    root.geometry("500x500")
    gui = Shop(root)
    root.mainloop()