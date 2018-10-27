from flask import Flask, jsonify, request


class Sales():
    """Sales class defining 
    the sales models
    """
    sales = []
        # {
        #     'sales_id' : 1,
        #     'attendant_name' : 'Mary',
        #     'no_of_products': 200,
        #     'total_profit': 450000
        # },
        # {
        #     'sales_id' : 2,
        #     'attendant_name' : 'Daizy',
        #     'no_of_products': 20,
        #     'total_profit': 100000
        # }
    # ]
    def __init__(self, sales_id, attendant_name, no_of_products, total_profit):
        self.sales_id = len(Sales.sales) + 1
        self.attendant_name = attendant_name
        self.no_of_products = no_of_products
        self.total_profit = total_profit
        
    def create_sale(self):
        """Model to create a sale record"""
        sale={
            "sales_id": self.sales_id,
            "attendant_name":self.attendant_name,
            "no_of_products" : self.no_of_products,
            "total_profit" : self.total_profit
        }
        Sales.sales.append(sale)
        return jsonify({"Sale record successfully created":sale})

    @staticmethod
    def get_all_sales():
        """Model to get and return 
        all sales records
        """
        if len(Sales.sales) > 0:
            return jsonify({"Sale records": Sales.sales})

    @staticmethod
    def get_sale(sales_id):
        """Model to get and return 
        a particular sale record
        """
        for sale in Sales.sales:
            if sale['sales_id'] == sales_id:
                return jsonify(sale)


