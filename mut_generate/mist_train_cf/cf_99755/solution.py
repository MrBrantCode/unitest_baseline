"""
QUESTION:
Create a function called `recommend_laptop` that takes four parameters: `budget`, `processor_speed`, `ram`, and `storage`. The function should return a list of dictionaries representing laptops that meet the specified requirements and are within the given budget. The laptops should be sorted by price in ascending order. Each laptop dictionary should contain the keys `brand`, `model`, `processor_speed`, `ram`, `storage`, and `price`. The function should assume that the list of available laptops is predefined.
"""

def recommend_laptop(budget, processor_speed, ram, storage):
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