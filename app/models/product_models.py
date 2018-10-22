from flask import Flask, jsonify, request, json


# app = Flask(__name__)

products = [
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

# product_id = 0

class Product():
    # def __init__(self):
        # self.products = []

        # self.products = [
        #     {
        #         'product_id' : 1,
        #         'product_name' : 'Ladies Bag',
        #         'model_no': 'LDBG1111',
        #         'product_category': 'Wardrobes',
        #         'unit_price': 45000,
        #         'product_quantity': 200
        #     },
        #     {
        #         'product_id' : 2,
        #         'product_name' : 'Chocolate',
        #         'model_no': 'FCH121',
        #         'product_category': 'Snacks',
        #         'unit_price': 7500,
        #         'product_quantity': 500 
        #     }
        # ]


    def create_a_product(self, product_id, product_name, model_no, product_category, unit_price, product_quantity):
        # self.product_id = len(products) + 1
        # self.product_name = product_name
        # self.model_no = model_no
        # self.product_category = product_category
        # self.unit_price = unit_price
        # self.product_quantity = product_quantity
        
        product={
            'product_id': self.product_id,
            'product_name':self.product_name,
            'model_no' : self.model_no,
            'product_category': self.product_category,
            'unit_price': self.unit_price,
            'product_quantity': self.product_quantity      
        }

        products.append(product)
        return jsonify(products)

    def get_all_products(self):
        if len(products) > 0:
            return products
        # return "nothing"

    def get_a_product(self, product_id):
        for product in products:
            if product['product_id'] == product_id:
                return product
            # return "nothing again"

