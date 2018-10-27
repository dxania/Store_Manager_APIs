import json
from flask import jsonify

products = []
            # {
            #     'product_id' : 1,
            #     'product_name' : 'Ladies Bag',
            #     'model_no': 'LDBG1111',
            #     'product_category': 'Wardrobes',
            #     'unit_price': 45000,
            #     'product_quantity': 200
            # },
            # {
            #     'product_id' : 2,
            #     'product_name' : 'Chocolate',
            #     'model_no': 'FCH121',
            #     'product_category': 'Snacks',
            #     'unit_price': 7500,
            #     'product_quantity': 500 
            # }

class Product():
    """Products class defining 
    the product models
    """
    def __init__(self, product_id, product_name, model_no, product_category, unit_price, product_quantity):
        self.product_id = len(products) + 1
        self.product_name = product_name
        self.model_no = model_no
        self.product_category = product_category
        self.unit_price = unit_price
        self.product_quantity = product_quantity

        
    def create_a_product(self):
        
        product={
            "product_id": self.product_id,
            "product_name" : self.product_name,
            "model_no" : self.model_no,
            "product_category": self.product_category,
            "unit_price": self.unit_price,
            "product_quantity": self.product_quantity      
        }

        products.append(product)
        return jsonify({"Product successfully created":product})

    @staticmethod
    def get_all_products():
        """Model to get and 
        return all products
        """
        if len(products) > 0:
            return jsonify({"Products": products})
 
    @staticmethod
    def get_a_product(product_id):
        """Model to get and return 
        a particular product
        """
        for product in products:
            if product['product_id'] == product_id:
                return jsonify(product)



