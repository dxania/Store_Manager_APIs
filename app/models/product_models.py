from flask import Flask, jsonify


# app = Flask(__name__)

# products = [
#     {
#         'product_id' : 1,
#         'product_name' : 'Ladies Bag',
#         'model_no': 'LDBG1111',
#         'category': 'Wardrobes',
#         'unit_price': 45000,
#         'quantity': 200
#     },
#     {
#         'product_id' : 2,
#         'product_name' : 'Chocolate',
#         'model_no': 'FCH121',
#         'category': 'Snacks',
#         'unit_price': 7500,
#         'quantity': 500 
#     }
# ]

# product_id = 0

class Product():
    def __init__(self):
        # self.products = []
        self.product_id = 0

        self.products = [
            {
                'product_id' : 1,
                'product_name' : 'Ladies Bag',
                'model_no': 'LDBG1111',
                'category': 'Wardrobes',
                'unit_price': 45000,
                'quantity': 200
            },
            {
                'product_id' : 2,
                'product_name' : 'Chocolate',
                'model_no': 'FCH121',
                'category': 'Snacks',
                'unit_price': 7500,
                'quantity': 500 
            }
        ]


    def create_a_product(self, product_id, product_name, model_no, product_category, unit_price, product_quantity):
        product = {
            product_id : self.product_id + 1,
            product_name : products['product_name'],
            model_no : products['model_no'],
            product_category : products['product_category'],
            unit_price : products['unit_price'],
            product_quantity : products['product_quantity']

        }
        
        self.products.append(product)
        return jsonify(self.products)

    def get_all_products(self):
        if len(self.products) > 0:
            return self.products
        # return "nothing"

    def get_a_product(self, product_id):
        for product in self.products:
            if product['product_id'] == product_id:
                return product
            # return "nothing again"

