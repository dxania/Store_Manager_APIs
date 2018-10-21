import json

import unittest

from Store_Manager_APIs.app import app

from Store_Manager_APIs.app.models.sales_models import *

from Store_Manager_APIs.app.routes.sales_routes import *



class Tests(unittest.TestCase):
    sale = {
                'sales_id' : 1,
                'attendant_name' : 'Mary',
                'no_of_pdts': 200
                'total_profit': 450000
            }

    def setUp(self):
        self.app_client = app.test_client()

    def test_get_all_sales(self):
        response = self.app_client.get("/api/v1/sales")
        self.assertEqual(response.status_code, 200)

    def test_get_sale(self):
        result = self.app_client.get('/api/v1/sales/1')
        self.assertEqual(result.status_code, 200)

    # def test_create_sale(self):
    #     response = self.app_client.post("/api/v1/sales",
    #                              content_type='application/json',
    #                              data=json.dumps({ 
                                                        # 'sales_id' : 1,
                                                        # 'attendant_name' : 'Mary',
                                                        # 'no_of_pdts': 200
                                                        # 'total_profit': 450000
    #                                             })
    #                 )
    #     self.assertEqual(response.status_code, 201)


if __name__ == ('__main__'):
    unittest.main()