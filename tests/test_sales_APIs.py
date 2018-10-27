import json

import unittest

from app import app

from app.routes.sales_routes import *



class Base(unittest.TestCase):
    """Base class for tests. 

    This class defines a common `setUp` 
    method that defines attributes which 
    are used in the various tests.
    """

    def setUp(self):
        self.app_client = app.test_client()

    # def test_get_empty_sales_list(self):
        # get_request = self.app_client.get("/api/v1/sales")
        # response = json.loads(get_request.data.decode())
        # self.assertEqual(response['message'], 'No sales have been added yet')
        # self.assertEqual(get_request.status_code, 204)

class Endpoints(Base):
    """
    Tests all aspects of endpoints

    Tests include: creating a sale record, getting all sale records,
    getting a particular sale record.  
    """
    def test_get_all_sales(self):
        sale = {
                "sales_id" : 1,
                "attendant_name" : "Mary",
                "no_of_products": 200,
                "total_profit": 450000
        }
        post_request = self.app_client.post("/api/v1/sales",
                                 content_type='application/json',
                                 data=json.dumps(sale)
                    )
        get_request = self.app_client.get("/api/v1/sales")
        self.assertEqual(get_request.status_code, 200)
    
    
    def test_get_sale(self):
        sale = {
                "sales_id" : 2,
                "attendant_name" : "Mary",
                "no_of_products": 200,
                "total_profit": 450000
        }
        post_request = self.app_client.post("/api/v1/sales",
                                 content_type='application/json',
                                 data=json.dumps(sale)
                    )
        self.assertEqual(post_request.status_code, 201)
        get_request = self.app_client.get('/api/v1/sales/2')
        self.assertEqual(get_request.status_code, 200)


    def test_create_sale(self):
        sale = {
                "sales_id" : 1,
                "attendant_name" : "Mary",
                "no_of_products": 200,
                "total_profit": 450000
        }
        post_request = self.app_client.post("/api/v1/sales",
                                 content_type='application/json',
                                 data=json.dumps(sale)
                    )
        self.assertEqual(post_request.status_code, 201)

class MethodsReturnType(Base):
    """
    Tests all aspects of non existent output

    Tests include: retrieving a non existent sale record
    """
    def test_get_non_existent_sale_record(self):
        get_request = self.app_client.get("/api/v1/sales/9")
        response = json.loads(get_request.data.decode())
        self.assertEqual(response['message'], 'There is no sale record matching that ID')
        self.assertEqual(get_request.status_code, 404)

class Set(Base):
    """
    Tests all aspects of setting attributes

    Tests include: setting attributes of wrong type, 
    setting attributes outside their constraints, setting empty attributes.
    """
    def test_attendant_name_required(self):
        sale = {
                'sales_id' : 1,
                'attendant_name' : "",
                'no_of_products': 200,
                'total_profit': 450000
        }
        post_request = self.app_client.post("/api/v1/sales",
                                        content_type='application/json',
                                        data=json.dumps(sale))
        response = json.loads(post_request.data.decode())
        self.assertIn("Attendant Name is required", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_attendant_name_chars(self):
        sale = {
                'sales_id' : 1,
                'attendant_name' : "12345",
                'no_of_products': "200",
                'total_profit': 450000
        }
        post_request = self.app_client.post("/api/v1/sales",
                                        content_type='application/json',
                                        data=json.dumps(sale))
        response = json.loads(post_request.data.decode())
        self.assertIn("Attendant Name must be letters", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_number_of_products_required(self):
        sale = {
                'sales_id' : 1,
                'attendant_name' : "Mary",
                'no_of_products': "",
                'total_profit': 450000
        }
        post_request = self.app_client.post("/api/v1/sales",
                                        content_type='application/json',
                                        data=json.dumps(sale))
        response = json.loads(post_request.data.decode())
        self.assertIn("Number of products is required", response['message'])
        self.assertEqual(post_request.status_code, 400)    

    def test_number_of_products_int(self):
        sale = {
                'sales_id' : 1,
                'attendant_name' : 'Mary',
                'no_of_products': "200",
                'total_profit': 450000
        }
        post_request = self.app_client.post("/api/v1/sales",
                                        content_type='application/json',
                                        data=json.dumps(sale))
        response = json.loads(post_request.data.decode())
        self.assertIn("Number of products must be a number", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_total_profit_required(self):
        sale = {
                'sales_id' : 1,
                'attendant_name' : "Mary",
                'no_of_products': 88
        }
        post_request = self.app_client.post("/api/v1/sales",
                                        content_type='application/json',
                                        data=json.dumps(sale))
        response = json.loads(post_request.data.decode())
        self.assertIn("Total profit is required", response['message'])
        self.assertEqual(post_request.status_code, 400)

    def test_total_profit_int(self):
        sale = {
                'sales_id' : 1,
                'attendant_name' : "Mary",
                'no_of_products': 88,
                'total_profit' : "Ninety"
        }
        post_request = self.app_client.post("/api/v1/sales",
                                        content_type='application/json',
                                        data=json.dumps(sale))
        response = json.loads(post_request.data.decode())
        self.assertIn("Total profit must be a number", response['message'])
        self.assertEqual(post_request.status_code, 400)  

if __name__ == ('__main__'):
    unittest.main()