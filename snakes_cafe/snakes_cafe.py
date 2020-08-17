def welcome():
    print(
    """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************

    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears

    """
)
welcome()

menu_list = ['Wings', 'Cookies', 'Spring Rolls', 'Salmon', 'Steak', 'Meat Tornado', 'A Literal Garden', 'IceCream', 'Cake', 'Pie', 'Coffee', 'Tea', 'UnicornTears']


counter = []

while True:
    order_name = input("> ")
    if order_name == "quit":
        break
    elif order_name.capitalize() in menu_list:
        counter.append(order_name)
        order_number = counter.count(order_name) 
        print(f"**{order_number} order of {order_name.capitalize()} have been added to your meal**")
    else:
        print("wrong input!! Try again")