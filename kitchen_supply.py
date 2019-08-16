# Shlok Wadhwa, Project, CIS345 T/Th 10:30-11:45

# Doing all the imports.
from tkinter import *
from tkinter import ttk, messagebox
from account_classes import Customer
from product_classes import Product, Attachment
import json
import csv
import datetime

# declring and initializing variables before use.
edit_mode = False
buy_mode = False
edit_index = 0
product_list = []
cart_productlist = []
cart_index = 0
cart_list = []
# cart_sum = 0
x = 0
index = 0
counter = 0
accnum_list = []
balance_list = []
listcust = []
cust_emp_list = []


def open_products():
    """Function to open the json file containing all products"""
    try:
        with open('products.json', 'r') as fp:
            data = json.load(fp)
            for l in data['products']:
                if 'materialtype' in l.keys():
                    line = Attachment(l['prodid'], l['materialtype'], l['desc'], l['quantity'], l['price'], l['id'])

                else:
                    line = Product(l['prodid'], l['desc'], l['quantity'], l['price'])
                products_listbox.insert(END, line)
                product_list.append(line)

        messagebox.showinfo(title='Products Loaded', message='Products Loaded. Press Ok to continue.')
    except IOError:
        messagebox.showinfo(title='Error', message='Error Loading the file. Please check your file and try again.')


def open_customers():
    """Function to open and load all customers on the window."""
    global accnum_list, balance_list, listcust, cust_emp_list
    try:
        with open('customers.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader)
            for line in csv_reader:
                cust = Customer(line[0], line[1], line[2], line[3], line[4], line[5])
                listcust.append(cust)
                balance_list.append(cust.balance)
                cust_emp_list.append(cust.isemployee)
                accnum_list.append(cust.accnum)
            account['values'] = listcust
        messagebox.showinfo(title='Customers Loaded',
                            message='Customers Loaded in drop down list. Press Ok to continue.')
    except IOError:
        messagebox.showinfo(title='Error', message='Error Loading the file. Please check your file and try again.')


def normal_mode():
    """This is the customer mode, which launches when the program initially starts"""
    global cart_instructions, cart_listbox, buy_btn, total_lbl, total_tbx, cart_quantity_lbl, cart_quantity_tbx, image,\
        product_list
    cart_instructions.grid(row=6, column=6, columnspan=2)
    cart_listbox.grid(row=7, column=7, columnspan=3)
    buy_btn.grid(padx=10, pady=10, row=8, column=9, rowspan=2, columnspan=3)
    buy_con.set("Buy")
    total_lbl.grid(row=10, column=7)
    total_tbx.grid(row=10, column=8)
    cart_quantity_lbl.grid(row=11, column=7)
    cart_quantity_tbx.grid(row=11, column=8)
    image.grid(row=0, column=8, rowspan=4)
    emp_buy_btn.grid(row=16, column=4)
    pin_lbl.grid(row=12, column=7)
    pin_tbx.grid(row=12, column=8)
    delete_btn.grid_forget()
    emp_buy_btn.grid_forget()


def emp_mode():
    """This launches the employee mode which hides all other modes and
    lets employees add/delete or edit new products."""
    global cart_instructions, cart_listbox, buy_btn, total_lbl, total_tbx, cart_quantity_lbl, cart_quantity_tbx, image,\
        product_list
    cart_instructions.grid_forget()
    cart_listbox.grid_forget()
    buy_btn.grid_forget()
    total_lbl.grid_forget()
    total_tbx.grid_forget()
    cart_quantity_lbl.grid_forget()
    cart_quantity_tbx.grid_forget()
    image.grid(row=0, column=10, padx=50, pady=20)
    emp_buy_btn.grid(row=16, column=1)
    delete_btn.grid(row=16, column=2)
    pin_lbl.grid(row=16, column=4)
    pin_tbx.grid(row=16, column=5)
    move_right.grid_forget()
    move_left.grid_forget()
    final.grid_forget()


def add_product():
    """Function lets you add new products to the json file"""
    if pin.get() == '2233':
        add_newproduct = Product(id_tbx.get(), desc_tbx.get(), quantity_tbx.get(), price_tbx.get())
        products_listbox.insert(END, add_newproduct)
        product_list.append(add_newproduct)
    elif pin.get() != '2233':
        messagebox.showinfo(title='Incorrect Pin', message='Incorrect pin entered. Please try again')


def delete_product():
    """Lets employees delete products from the product list."""
    global product_list, delete_btn
    if pin.get() == '2233':
        delete_index = products_listbox.curselection()[0]
        products_listbox.delete(delete_index)
        product_list.pop(delete_index)
    elif pin.get() != '2233':
        messagebox.showinfo(title='Incorrect Pin', message='Incorrect pin entered. Please try again')


def save_products():
    """Lets users save products to the file after editing"""
    with open('products.json', 'w') as filePointer:
        list_list = list()
        for p in product_list:
            if isinstance(p, Product):
                list_list.append({'prodid': p.prodid, 'desc': p.desc, 'quantity': p.quantity, 'price': p.price})

            else:
                list_list.append({'prodid': p.prodid, 'desc': p.desc, 'quantity': p.quantity, 'price': p.price,
                                  'materialtype': p.materialtype, 'id': p.aid})

        json.dump({"products": list_list}, filePointer)


customer_list = [['acc_num', 'fname', 'lname', 'pin', 'balance', 'isemployee']]


def save_customer():
    """Lets users save customers after making edits and changing balances after purchases"""
    for c in listcust:
        customer_list.append([c.accnum, c.fname, c.lname, c.pin, c.balance, c.isemployee])
    with open("customers.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(customer_list)


def buy():
    """Checks whether the user has enough money and make purchases from the list of available products"""
    global listcust, product_list, cart_listbox, cart_list, counter
    purchase_balance = balance_list[account.current()]
    purchase_amt = total.get()
    buy_con.set("Continue")

    if int(purchase_balance) >= int(purchase_amt) and listcust[index].pin == pin.get():
        print(pin.get())
        new_balance = int(purchase_balance) - int(purchase_amt)
        listcust[index].balance = new_balance
        print(new_balance)
        cust_balance.set(new_balance)
        balance_list[account.current()] = new_balance
        print(balance_list[account.current()])
        total.set(0)
        print(cart_list)
        for c in cart_list:
            for p in product_list:
                if c.prodid == p.prodid:
                    new_p = int(p.quantity)
                    new_c = int(c.quantity)
                    new_p += new_c
                    print(new_p)
                    p.quantity = new_p
                    print(p.quantity)
                    quantity.set(p.quantity)
        current_time = datetime.datetime.now()
        final.grid(row=13, column=8)

        invoice = [['Description', 'Quantity', 'Price', 'Total Price', 'Date & Time']]
        for z in cart_list:
            invoice.append([z.desc, z.quantity, z.price, (int(z.quantity) * int(z.price)), listcust[account.current()],
                            current_time])
        with open('invoice.csv', 'w', newline='') as invoice_file:
            writer = csv.writer(invoice_file)
            writer.writerows(invoice)

        cart_listbox.delete(0, 'end')
        buy_btn.grid_forget()

    elif int(purchase_balance) < int(purchase_amt) or listcust[index].pin != pin.get():
        print('Insufficient funds')
        if int(purchase_balance) < int(purchase_amt):
            messagebox.showinfo(title='Insufficient Balance',
                                message='Insufficient balance to purchase products in cart.')
        else:
            messagebox.showinfo(title='Incorrect Pin', message='Incorrect pin entered. Please try again')


def current_balance(*args):
    """Checks for current balance of customers and updates it to the textbox for users to see."""
    global index
    print(account.current())
    index = account.current()
    cust_balance.set(balance_list[account.current()])
    account_num.set(accnum_list[account.current()])


def toggle_product(args):
    """Function to check and toggle entryboxes which lets employees edit product details"""
    global id_tbx, desc_tbx, quantity_tbx, price_tbx
    if not args:
        id_tbx['state'] = DISABLED
        desc_tbx['state'] = DISABLED
        quantity_tbx['state'] = DISABLED
        price_tbx['state'] = DISABLED
        materials_tbx['state'] = DISABLED
        materials.set('N/A')
        attachments_tbx['state'] = DISABLED
        attachments.set('N/A')
        order_quantity_tbx['state'] = NORMAL
        cart_quantity_tbx['state'] = NORMAL
    else:
        id_tbx['state'] = NORMAL
        desc_tbx['state'] = NORMAL
        price_tbx['state'] = NORMAL
        quantity_tbx['state'] = NORMAL
        materials_tbx['state'] = NORMAL
        attachments_tbx['state'] = NORMAL
        order_quantity_tbx['state'] = NORMAL
        materials_tbx['state'] = NORMAL
        materials.set('N/A')
        attachments_tbx['state'] = NORMAL
        attachments.set('N/A')
        order_quantity_tbx['state'] = NORMAL
        cart_quantity_tbx['state'] = NORMAL


def edit_product(event):
    """Checking for employee status and lets you edit products
    while non-employee status displays product details in entryboxes"""
    global edit_index, edit_mode, products_listbox, prod_id, description, quantity, price, product_list
    edit_index = products_listbox.curselection()[0]
    edit_prod = product_list[edit_index]
    if listcust[account.current()].balance == '0' and listcust[account.current()].pin == '2233':
        toggle_product(True)
        order_quantity_tbx['state'] = NORMAL
        move_right.grid(padx=10, pady=20, row=7, column=5)
        add_edit.set("Edit")

    else:
        toggle_product(False)
        move_right.grid(padx=10, pady=20, row=7, column=5)
        add_edit.set("Add")
    try:
        prod_id.set(edit_prod.prodid)
        description.set(edit_prod.desc)
        quantity.set(edit_prod.quantity)
        price.set(edit_prod.price)
        materials.set(edit_prod.materialtype)
        attachments.set(edit_prod.aid)
    except AttributeError:
        pass


def view_product(event):
    """Lets employees and customers view product details,
    by getting it from the product llist and adding to the entry boxes"""
    global cart_index, edit_mode, cart_listbox, prod_id, description, quantity, price, product_list
    try:
        cart_index = cart_listbox.curselection()[0]

    except IndexError:
        # if cart_listbox.curselection()[0] >= 0:
        #     pass
        # else:
        messagebox.showinfo(title="Alert Message", message="Select the product to view information!")
    view_prod = cart_list[cart_index]
    if listcust[account.current()].balance == '0' and listcust[account.current()].pin == '2233':
        toggle_product(True)
        order_quantity_tbx['state'] = NORMAL
    else:
        toggle_product(False)

    try:
        prod_id.set(view_prod.prodid)
        description.set(view_prod.desc)
        quantity.set(view_prod.quantity)
        price.set(view_prod.price)
        materials.set(view_prod.materialtype)
        attachments.set(view_prod.aid)
    except AttributeError:
        pass


cart_sum = 0


def order_total():
    """Calculates order total based on the cart list quantity and price"""
    global cart_sum, total_tbx, x, cart_list
    for c in cart_list:
        x = int(c.price) * int(c.quantity)
        print(x)
    cart_sum += x
    print(cart_sum)
    total_tbx['state'] = DISABLED
    total.set(cart_sum)
    if cart_sum < 0:
        messagebox.showinfo(title='Negative Balance', message='Your cart has a negative balance')


def move_right():
    """One of the most important function in the program. Checks for quantity available and entered quantity.
    if user is an Employee; changes button to "Edit" and verifies pin for changing product details.
    If user is a customer, it changes button to add to cart and checks for quantities"""
    global listcust, products_listbox, edit_mode, cart_listbox, cart_quantity_tbx, buy_btn, add_edit, product_list, \
        order_quantity_tbx, pin_tbx, buy_mode

    selection = products_listbox.curselection()[0]
    total.set(0)

    if listcust[account.current()].balance == '0' and listcust[account.current()].pin == '2233' and pin.get() == '2233':
        edit_mode = True
        new_product = Product(id_tbx.get(), desc_tbx.get(), quantity_tbx.get(), price_tbx.get())
        products_listbox.delete(selection)
        products_listbox.insert(selection, new_product)

        product_list.pop(selection)
        product_list.insert(selection, new_product)
    elif listcust[account.current()].balance == '0' and listcust[account.current()].pin == '2233' and pin.get() != '2233':
        messagebox.showinfo(title='Incorrect Pin', message='Incorrect pin entered. Please try again')

    elif product_list[selection].quantity - int(order_quantity.get()) >= 0:
        buy_mode = True
        cart_product = Product(id_tbx.get(), desc_tbx.get(), int(order_quantity_tbx.get()), int(price_tbx.get()))
        cart_listbox.insert(END, cart_product)
        cart_productlist.append(cart_product)
        cart_list.append(cart_product)
        calculate_quantity()

        order_total()
        buy_con.set("Buy")
        buy_btn.grid(padx=10, pady=10, row=8, column=9, rowspan=2, columnspan=3)
        move_left.grid(padx=10, pady=20, row=7, column=5, rowspan=5)

    elif int(order_quantity.get()) > int(quantity.get()):
        messagebox.showinfo(title='Excess Number of items',
                            message='You are trying to select more items than available')


def calculate_quantity():
    for c in cart_list:
        for p in product_list:
            if c.prodid == p.prodid:
                new_p = int(p.quantity)
                new_c = int(c.quantity)
                new_p -= new_c
                quantity.set(new_p)
                p.quantity = new_p


def move_left():
    """Implements the deleting functionality. Lets user delete the quantity they would like to delete.
    Implements another textbox, which lets you delete particular number of items from the cart"""
    global product_list, cart_list, cart_listbox, products_listbox, cart_quantity_tbx
    selection = cart_listbox.curselection()[0]
    print(product_list[selection])
    new_q = int(cart_quantity_tbx.get()) + int(quantity_tbx.get())
    quantity.set(new_q)
    alt_price = int(cart_quantity_tbx.get()) * int(price_tbx.get())
    new_price = int(total_tbx.get()) - alt_price
    print(new_price)
    total.set(new_price)
    if order_quantity.get == cart_quantity.get() or new_price == 0:
        cart_listbox.delete(selection)
    for c in cart_list:
        for p in product_list:
            if c.prodid == p.prodid:
                print(p.quantity)
                new_p = int(p.quantity)
                new_c = int(c.quantity)
                new_p += new_c
                print(new_p)
                p.quantity = new_q
                print(p.quantity)


# Making background and frame color variables for future use.
bg_color = 'dodger blue'
framecolor = 'cornsilk'

# Creating and initializing the window using Tk, setting background color and specifying window size
window = Tk()
window.config(bg=bg_color)
window.title("Kitchen Supply Order Management")
window.geometry('1150x800')

# Form data
acc_type = StringVar()
prod_id = StringVar()
description = StringVar()
quantity = StringVar()
price = StringVar()
cust_balance = StringVar()
materials = StringVar()
attachments = StringVar()
order_quantity = StringVar()
total = StringVar()
cart_quantity = StringVar()
pin = StringVar()
buy_con = StringVar()
account_num = StringVar()
add_edit = StringVar()

# Making label to make some space to fit in other GUI in a clean manner
Label(window, text=' ', background=bg_color).grid(row=0, column=0, padx=25, pady=25)

# Menu
menu_bar = Menu(window)
window.config(menu=menu_bar)

# adding commands to the menu
file_menu = Menu(menu_bar, tearoff=FALSE)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='Open Customer', command=open_customers)
file_menu.add_command(label='Open Products', command=open_products)
file_menu.add_command(label='Save Customer', command=save_customer)
file_menu.add_command(label='Save Product', command=save_products)
file_menu.add_command(label='Employee Mode', command=emp_mode)
file_menu.add_command(label='Customer Mode', command=normal_mode)
file_menu.add_command(label='Exit', command=window.quit)


# Frame and combo box
frame = Frame(window, bg=framecolor, width=500, height=150, borderwidth=1, relief=SUNKEN)
frame.grid(row=0, column=1, columnspan=3, pady=20)
frame.pack_propagate(0)

acc_type_label = Label(frame, text='Select Your Account', justify=LEFT, bg=framecolor,
                       font=("Helvetica", 30, "bold italic"))
acc_type_label.pack(anchor=NW)

balance = Entry(frame, bg=framecolor, textvariable=cust_balance, state=DISABLED, width=15)
balance.pack(side=RIGHT, pady=10)

acc_num = Entry(frame, bg=framecolor, state=DISABLED, textvariable=account_num ,width=15)
acc_num.pack(side=RIGHT, pady=10)


account = ttk.Combobox(frame, background=framecolor, state='readonly')
account.pack(side=LEFT, pady=20)
account.bind('<<ComboboxSelected>>', current_balance)


# Making instructions for product listbox and listbox
instructions = Label(window, text='(Double-Click to view information about a product)', background=bg_color,
                     font=("Helvetica", 20, "italic"))
instructions.grid(row=6, column=1, columnspan=2)
products_listbox = Listbox(window, width=50)
products_listbox.bind('<Double-Button-1>', edit_product)
products_listbox.grid(row=7, column=1, columnspan=3)

# Product ID
id_lbl = Label(window, text='ID:', background=bg_color, justify=LEFT)
id_lbl.grid(row=9, column=1, padx=5, pady=5)
id_tbx = Entry(window, textvariable=prod_id, width=30)
id_tbx.grid(row=9, column=2, columnspan=2)

# Product Description
desc_lbl = Label(window, text='Description:', background=bg_color, justify=LEFT)
desc_lbl.grid(row=10, column=1, padx=5, pady=5)
desc_tbx = Entry(window, textvariable=description, width=30)
desc_tbx.grid(row=10, column=2, columnspan=2)

# Quantity Available
quantity_lbl = Label(window, text='Quantity Available:', background=bg_color, justify=LEFT)
quantity_lbl.grid(row=11, column=1, padx=5, pady=5)
quantity_tbx = Entry(window, textvariable=quantity, width=30)
quantity_tbx.grid(row=11, column=2, columnspan=2)

# Price of product
price_lbl = Label(window, text='Price($):', background=bg_color, justify=LEFT)
price_lbl.grid(row=12, column=1, padx=5, pady=5)
price_tbx = Entry(window, textvariable=price, width=30)
price_tbx.grid(row=12, column=2, columnspan=2)

# Materials (For attachment)
materials_lbl = Label(window, text='Materials:', background=bg_color, justify=LEFT)
materials_lbl.grid(row=13, column=1, padx=5, pady=5)
materials_tbx = Entry(window, textvariable=materials, width=30)
materials_tbx.grid(row=13, column=2, columnspan=2)

# Attachment to ID
attachments_lbl = Label(window, text='Attachment to:', background=bg_color, justify=LEFT)
attachments_lbl.grid(row=14, column=1, padx=5, pady=5)
attachments_tbx = Entry(window, textvariable=attachments, width=30)
attachments_tbx.grid(row=14, column=2, columnspan=2)

# Order quantity the use wants
order_quantity_lbl = Label(window, text='Order Quantity:', background=bg_color, justify=LEFT)
order_quantity_lbl.grid(row=15, column=1, padx=5, pady=5)
order_quantity_tbx = Entry(window, textvariable=order_quantity, width=30)
order_quantity_tbx.grid(row=15, column=2, columnspan=2)

# Add to cart/ Edit button
move_right = Button(window, text='Add', background=bg_color, command=move_right, textvariable=add_edit)
move_right.grid(padx=10, pady=20, row=7, column=5)
move_right.grid_forget()

# Delete Button
move_left = Button(window, text='Delete Item', background=bg_color, command=move_left)
move_left.grid(padx=10, pady=20, row=7, column=5, rowspan=5)
move_left.grid_forget()

# Cart listbox and Cart instructions
cart_instructions = Label(window, text='Your Cart', background=bg_color, font=("Helvetica", 30, "bold italic"))
cart_instructions.grid(row=6, column=6, columnspan=2)
cart_listbox = Listbox(window, width=50)
cart_listbox.bind('<Double-Button-1>', view_product)
cart_listbox.grid(row=7, column=7, columnspan=3)

# Buy Button
buy_btn = Button(window, text='Buy', background=bg_color, textvariable=buy_con, command=buy)
buy_btn.grid(padx=10, pady=10, row=8, column=9, rowspan=2, columnspan=3)
buy_btn.grid_forget()

# Total price to be paid
total_lbl = Label(window, text='Total Price($):', background=bg_color, justify=LEFT)
total_lbl.grid(row=10, column=7)
total_tbx = Entry(window, width=20, textvariable=total)
total_tbx.grid(row=10, column=8)

# Delete quantity (used with delete button)
cart_quantity_lbl = Label(window, text='Delete-Quantity:', background=bg_color, justify=LEFT)
cart_quantity_lbl.grid(row=11, column=7)
cart_quantity_tbx = Entry(window, width=20, textvariable=cart_quantity)
cart_quantity_tbx.grid(row=11, column=8)

# Pin entrybox
pin_lbl = Label(window, text='Pin:', background=bg_color, justify=LEFT)
pin_lbl.grid(row=12, column=7)
pin_tbx = Entry(window, width=20, textvariable=pin)
pin_tbx.grid(row=12, column=8)

# Employee mode: Add product
emp_buy_btn = Button(window, text='Add Product', bg=bg_color, command=add_product)
emp_buy_btn.grid(row=16, column=4)
emp_buy_btn.grid_forget()

# Employee mode: Delete product
delete_btn = Button(window, text='Delete Product', bg=bg_color, command=delete_product)
delete_btn.grid(row=16, column=4)
delete_btn.grid_forget()

# Confirmation that product was successfully bought.
final = Label(window, bg=bg_color, text=f'Purchase Successful! Invoice Generated.\nHave a great day!',
              font=("Helvetica", 15, "bold italic"))
final.grid(row=13, column=8)
final.grid_forget()

# adding icon the the status bar
window.iconbitmap('icon.png')

# adding image to the screen as a label
image = Label(window, bitmap='logo.png')
image.grid(row=0, column=8, rowspan=4)


window.mainloop()

