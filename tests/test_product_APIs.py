import json

import unittest

from app import app

from app.models.product_models import *

from app.routes.product_routes import *



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

    def test_get_all_products(self):
        response = self.app_client.get("/api/v1/products")
        self.assertEqual(response.status_code, 200)

    def test_get_a_product(self):
        result = self.app_client.get('/api/v1/products/1')
        self.assertEqual(result.status_code, 200)

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


if __name__ == ('__main__'):
    unittest.main()