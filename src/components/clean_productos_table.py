def clean_product_table(table):
    for item in table.get_children():
        table.delete(item)