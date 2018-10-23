from flask import Flask, jsonify, request, json



class Product():
    def __init__(self):

        self.products = []

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
        self.product_id = len(self.products) + 1
        self.product_name = product_name
        self.model_no = model_no
        self.product_category = product_category
        self.unit_price = unit_price
        self.product_quantity = product_quantity

        product={
            "product_id": self.product_id,
            "product_name" : product_name,
            "model_no" : model_no,
            "product_category": product_category,
            "unit_price": unit_price,
            "product_quantity": product_quantity      
        }
        self.products.append(product)
        return jsonify(self.products)

    def get_all_products(self):
        if len(self.products) > 0:
            # return self.products
            return "The products"

    def get_a_product(self, product_id):
        for product in self.products:
            if product['product_id'] == product_id:
                # return product
                return "The product"

