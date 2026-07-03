from generators.products import generate_products
from generators.customers import generate_customers
from generators.suppliers import generate_suppliers
from generators.warehouses import generate_warehouses

print("====================================")
print(" Supply Chain Data Generator ")
print("====================================")

generate_products()
generate_customers()
generate_suppliers()
generate_warehouses()

print("====================================")
print("All datasets generated successfully!")
print("====================================")