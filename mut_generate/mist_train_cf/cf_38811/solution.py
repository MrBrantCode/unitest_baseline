"""
QUESTION:
Implement a `PosOrderKey` class with a method `create_order_key` that takes a dictionary as input and returns a string representing a unique order key. If the input dictionary contains the key "source" with value "Alipay", the method should use the `from_alipay_dict` method to create the order key. Otherwise, it should use a default method. The `from_alipay_dict` method should create the order key based on the value provided in the input dictionary.

The input dictionary is expected to contain the keys "source" and "order_id". The `create_order_key` method should return a string in the format "AlipayOrder<order_id>" for Alipay inputs and "DefaultOrder<order_id>" for other inputs.
"""

def pos_order_key(input_dict):
    if input_dict.get("source") == "Alipay":
        return f"AlipayOrder{input_dict['order_id']}"
    else:
        return f"DefaultOrder{input_dict['order_id']}"