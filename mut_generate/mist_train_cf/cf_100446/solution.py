"""
QUESTION:
Create a function called `recommend_laptop` that recommends laptops based on a customer's budget and requirements. The function should take four parameters: `budget`, `processor_speed`, `ram`, and `storage`. It should return a list of laptops that meet the customer's requirements, sorted by price. The laptops should have a processor speed greater than or equal to `processor_speed`, RAM greater than or equal to `ram`, storage greater than or equal to `storage`, and a price less than or equal to `budget`.
"""

def recommend_laptop(budget, processor_speed, ram, storage):
  """
  Recommends laptops based on a customer's budget and requirements.

  Args:
    budget (int): The customer's budget.
    processor_speed (float): The required processor speed.
    ram (int): The required RAM.
    storage (int): The required storage.

  Returns:
    list: A list of laptops that meet the customer's requirements, sorted by price.
  """

  laptops = [
    {"brand": "Acer", "model": "Aspire 5", "processor_speed": 2.1, "ram": 8, "storage": 256, "price": 499},
    {"brand": "Dell", "model": "Inspiron 15", "processor_speed": 2.3, "ram": 4, "storage": 500, "price": 549},
    {"brand": "HP", "model": "Pavilion 15", "processor_speed": 2.5, "ram": 8, "storage": 512, "price": 599},
    {"brand": "Lenovo", "model": "IdeaPad 3", "processor_speed": 2.4, "ram": 4, "storage": 128, "price": 399},
    {"brand": "ASUS", "model": "VivoBook 15", "processor_speed": 2.2, "ram": 8, "storage": 256, "price": 479}
  ]
  
  recommended_laptops = [laptop for laptop in laptops 
                        if laptop["processor_speed"] >= processor_speed 
                        and laptop["ram"] >= ram 
                        and laptop["storage"] >= storage 
                        and laptop["price"] <= budget]
  
  return sorted(recommended_laptops, key=lambda k: k['price'])