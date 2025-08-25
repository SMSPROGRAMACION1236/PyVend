from src.views.new_product import NewProduct
from src.views.modify_product import ChangedProduct

def add_new_product():
    new_product = NewProduct()
    new_product.mainloop()

def modify_product(product_code, product_name, unit_price, stock):
    changed_product = ChangedProduct()
    changed_product.modify_product(product_code, product_name, unit_price, stock)
    changed_product.mainloop()
