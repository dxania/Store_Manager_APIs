from flask import Flask, jsonify, request


class Sales():
    """Sales class defining 
    the sales models
    """
    def __init__(self):
        self.sales = []

    #     self.sales = [
    #         {
    #             'sales_id' : 1,
    #             'attendant_name' : 'Mary',
    #             'no_of_products': 200,
    #             'total_profit': 450000
    #         },
    #         {
    #             'sales_id' : 2,
    #             'attendant_name' : 'Daizy',
    #             'no_of_products': 20,
    #             'total_profit': 100000
    #         }
    #     ]


    def create_sale(self, sales_id, attendant_name, no_of_products, total_profit):
        """Model to create a sale record"""
        self.sales_id = len(self.sales) + 1
        self.attendant_name = attendant_name
        self.no_of_products = no_of_pdts
        self.total_profit = total_profit

        sale={
            "sales_id": self.sales_id,
            "attendant_name":attendant_name,
            "no_of_products" : no_of_products,
            "total_profit" : total_profit
        }

        self.sales.append(sale)
        return jsonify(self.sales)


    def get_all_sales(self):
        """Model to get and return 
        all sales records
        """
        if len(self.sales) > 0:
            return "The sales"

    
    def get_sale(self, sales_id):
        """Model to get and return 
        a particular sale record
        """
        for sale in self.sales:
            if sale['sales_id'] == sales_id:
                return "The sale"


