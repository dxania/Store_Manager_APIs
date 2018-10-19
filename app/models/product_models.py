from flask import Flask, jsonify, request


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
        # product_id = self.product_id + 1
        # data = request.get_json()
        # product = {
        #     "product_id" : product_id,
        #     "product_name" : data['product_name'],
        #     "model_no" : data['model_no'],
        #     "product_category" : data['product_category'],
        #     "unit_price" : data['unit_price'],
        #     "product_quantity" : data['product_quantity']

        # }
        self.product_id += self.product_id
        self.product_name = product_name
        self.model_no = model_no
        self.product_category = product_category
        self.unit_price = unit_price
        self.product_quantity = product_quantity

        product={
            'product_id': self.product_id + 1,
            'product_name':request.json['product_name'],
            'model_no' : request.json['model_no'],
            'product_category':request.json['product_category'],
            'unit_price': request.json['unit_price'],
            'product_quantity': request.json['product_quantity']      
        }

        # created_products = a_product.create_a_product(product_id, product_name, model_no, product_category, unit_price, product_quantity)
        # if created_products:
        #     return products.append(request.get_json()), 201
        # return "nothing added"

        
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

