from generators.suppliers import generate_suppliers
from generators.products import generate_products
from generators.customers import generate_customers
from generators.warehouses import generate_warehouses
from generators.orders import generate_orders
from generators.order_items import generate_order_items
from generators.inventory import generate_inventory
from generators.inventory_transactions import generate_inventory_transactions
from generators.purchase_orders import generate_purchase_orders
from generators.purchase_order_items import generate_purchase_order_items
from generators.returns import generate_returns

print("====================================")
print(" Supply Chain Data Generator ")
print("====================================")

generate_suppliers()
generate_products()
generate_customers()
generate_warehouses()
generate_orders()
generate_order_items()
generate_inventory()
generate_inventory_transactions()
generate_purchase_orders()
generate_purchase_order_items()
generate_returns()



print("====================================")
print("All datasets generated successfully!")
print("====================================")