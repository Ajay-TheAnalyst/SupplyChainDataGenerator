from generators.products import generate_products
from generators.customers import generate_customers
from generators.suppliers import generate_suppliers
from generators.warehouses import generate_warehouses
from generators.orders import generate_orders
from generators.order_items import generate_order_items

print("====================================")
print(" Supply Chain Data Generator ")
print("====================================")

generate_products()
generate_customers()
generate_suppliers()
generate_warehouses()
generate_orders()
generate_order_items()

print("====================================")
print("All datasets generated successfully!")
print("====================================")