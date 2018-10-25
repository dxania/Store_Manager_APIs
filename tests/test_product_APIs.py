import json

import unittest

from app import app



class Tests(unittest.TestCase):
    product = { 'product_id' : 1,
                'product_name' : 'Ladies Bag',
                'model_no': 'LDBG1111',
                'product_category': 'Wardrobes',
                'unit_price': 45000,
                'product_quantity': 200
    }

    def setUp(self):
        self.app_client = app.test_client()

    def test_get_a_product(self):
        result = self.app_client.get('/api/v1/products/1')
        self.assertEqual(result.status_code, 200)

    # def test_get_all_products(self):
        # post_request = self.app_client.post("/api/v1/products", 
        #                               content_type='application/json',
                                        # data=json.dumps({ 'product_id' : 9,
                                                #           'product_name' : 'Ladies Shoes',
                                                #           'model_no': 'LDSH1111',
                                                #           'product_category': 'Wardrobes',
                                                #           'unit_price': 100000,
                                                #           'product_quantity': 260
                                                #         })
        # get_request = self.app_client.get('/api/v1/products')
        # self.assertEqual(get_request.status_code, 200)

    
    # def test_get_all_products(self):
    #     self.app_client.get("/api/v1/products")
    #     reply = json.loads(get_request.data)
    #     self.assertEqual(reply["message"], "All products")
        # self.assertEqual(get_request.status_code, 200)



    def test_create_a_product(self):
        response = self.app_client.post("/api/v1/products",
                                 content_type='application/json',
                                 data=json.dumps({  'product_id' : 9,
                                                    'product_name' : 'Ladies Shoes',
                                                    'model_no': 'LDSH1111',
                                                    'product_category': 'Wardrobes',
                                                    'unit_price': 100000,
                                                    'product_quantity': 260
                                                })
                    )
        self.assertEqual(response.status_code, 201)

    # def test_get_empty_list(self):
    #     get_request = self.app_client.get("/api/v1/products")
    #     self.assertEqual(get_request.status_code, 204)

    def test_get_non_existent_product(self):
        get_request = self.app_client.get("/api/v1/products/9")
        response = json.loads(get_request.data.decode())
        self.assertEqual(response['message'], 'There is no product matching that ID')
        self.assertEqual(get_request.status_code, 404)

    def test_unit_price_int(self):
        product = {
                    "product_id" : 9,
                    "product_name" : "Ladies Shoes",
                    "model_no": "LDSH1111",
                    "product_category": "Wardrobes",
                    "unit_price": "100000",
                    "product_quantity": 260
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product Price is required and must be an integer", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_quantity_int(self):
        product = {
                    "product_id" : 9,
                    "product_name" : "Ladies Shoes",
                    "model_no": "LDSH1111",
                    "product_category": "Wardrobes",
                    "unit_price": 10000,
                    "product_quantity": "260"
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product Quantity is required and must be an integer", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_product_name_string(self):
        product = {
                    "product_id" : 9,
                    "product_name" : "",
                    "model_no": "LDSH1111",
                    "product_category": "Wardrobes",
                    "unit_price": 10000,
                    "product_quantity": 260
        }
        post_request = self.app_client.post("/api/v1/products",
                                        content_type='application/json',
                                        data=json.dumps(product))
        response = json.loads(post_request.data.decode())
        self.assertIn("Product Name is required and should be letters", response['message'])
        self.assertEqual(post_request.status_code, 400)

if __name__ == ('__main__'):
    unittest.main()