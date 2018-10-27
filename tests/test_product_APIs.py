# import json

# import unittest

import json

import unittest

from app import app

from app.routes.product_routes import *



class Base(unittest.TestCase):
    """Base class for tests. 

    This class defines a common `setUp` 
    method that defines attributes which 
    are used in the various tests.
    """

    def setUp(self):
        self.app_client = app.test_client()


class Endpoints(Base):
    """
    Tests all aspects of endpoints

    Tests include: creating a product, getting all products,
    getting a particular product.  
    """
    def test_get_all_products(self):
        product = {
                "product_id" : 9,
                "product_name" : "Ladies Shoes",
                "model_no": "LDSH1111",
                "product_category": "Wardrobes",
                "unit_price": 100000,
                "product_quantity": 260
        }
        post_request = self.app_client.post("/api/v1/products",
                                 content_type='application/json',
                                 data=json.dumps(product)
                    )
        get_request = self.app_client.get("/api/v1/products")
        self.assertEqual(get_request.status_code, 200)
    
    def test_get_product(self):
        # product = {
        #         "product_id" : 1,
        #         "product_name" : "Ladies Shoes",
        #         "model_no": "LDSH1111",
        #         "product_category": "Wardrobes",
        #         "unit_price": 100000,
        #         "product_quantity": 260
        # }
        # post_request = self.app_client.post("/api/v1/products",
        #                          content_type='application/json',
        #                          data=json.dumps(product)
        #             )
        # self.assertEqual(post_request.status_code, 201)
        get_request = self.app_client.get("/api/v1/products/1")
        self.assertEqual(get_request.status_code, 200)
    
    def test_create_product(self):
        product = {
                "product_id" : 9,
                "product_name" : "Ladies Shoes",
                "model_no": "LDSH1111",
                "product_category": "Wardrobes",
                "unit_price": 100000,
                "product_quantity": 260
        }
        response = self.app_client.post("/api/v1/products",
                                 content_type='application/json',
                                 data=json.dumps(product)
                    )
        self.assertEqual(response.status_code, 201)

class MethodsReturnType(Base):
    """
    Tests all aspects of non existent output

    Tests include: retrieving a non existent product record
    """
    # def test_get_empty_list(self):
    #     get_request = self.app_client.get("/api/v1/products")
    #     response = json.loads(get_request.data.decode())
    #     self.assertEqual('There are no products in the store', response["message"])
    #     self.assertEqual(get_request.status_code, 204)

    def test_get_non_existent_product_record(self):
        get_request = self.app_client.get("/api/v1/products/9999")
        # response = json.loads(get_request.data.decode())
        # self.assertEqual(response['message'], 'There is no product matching that ID')
        self.assertEqual(get_request.status_code, 204)

class Set(Base):
    """
    Tests all aspects of setting attributes

    Tests include: setting attributes of wrong type, 
    setting attributes outside their constraints, setting empty attributes.
    """
    def test_product_name_required(self):
        product = {
                "product_id" : 9,
                "product_name" : "",
                "model_no": 'LDSH1111',
                "product_category": "Wardrobes",
                "unit_price": 100000,
                "product_quantity": 260
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product Name is required", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_product_name_chars(self):
        product = {
                "product_id" : 9,
                "product_name" : "66",
                "model_no": "LDSH1111",
                "product_category": "Wardrobes",
                "unit_price": 100000,
                "product_quantity": 260
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product Name must be letters", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_model_no_equired(self):
        product = {
                "product_id" : 9,
                "product_name" : "Crisps",
                "model_no": "",
                "product_category": "Food",
                "unit_price": 1000,
                "product_quantity": 260
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product Model number is required", response['message'])
        self.assertEqual(post_request.status_code, 400)    

    def test_category_required(self):
        product = {
                "product_id" : 9,
                "product_name" : "Crisps",
                "model_no": "we1453",
                "product_category": "",
                "unit_price": 1000,
                "product_quantity": 260
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product Category is required", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_unit_price_required(self):
        product = {
                "product_id" : 9,
                "product_name" : "Crisps",
                "model_no": "we1453",
                "product_category": "Food",
                "product_quantity": 260
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product Price is required", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_unit_price_int(self):
        product = {
                "product_id" : 9,
                "product_name" : "Crisps",
                "model_no": "we1453",
                "product_category": "Food",
                "unit_price": "1000",
                "product_quantity": 260
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product Price must be a number", response['message'])
        self.assertEqual(post_request.status_code, 400)

    
    def test_product_quantity_required(self):
        product = {
                "product_id" : 9,
                "product_name" : "Crisps",
                "model_no": "we1453",
                "product_category": "Food",
                "unit_price": 1000
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product quantity is required", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_product_quantity_int(self):
        product = {
                "product_id" : 9,
                "product_name" : "Crisps",
                "model_no": "we1453",
                "product_category": "Food",
                "unit_price": 1000,
                "product_quantity": "260"
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product quantity must be a number", response['message'])
        self.assertEqual(post_request.status_code, 400)  

if __name__ == ('__main__'):
    unittest.main()