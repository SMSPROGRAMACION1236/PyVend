from src.views.sales import Sales
from src.views.inventory import Inventary


def open_sales_view():
    sales = Sales()
    sales.mainloop()


def open_inventory_view():
    inventory = Inventary()
    inventory.mainloop()

