from flask import Flask, jsonify, request

#sales list to hold dummy sale records
sales = [{
            'sales_id' : 1,
            'attendant_name' : 'Mary',
            'no_of_products': 200,
            'total_profit': 450000
        },
        {
            'sales_id' : 2,
            'attendant_name' : 'Daizy',
            'no_of_products': 20,
            'total_profit': 100000
        }
]

#Sales class that holds the sales models
class Sales():
    # def __init__(self):

    #     self.sales_id = 0

    #     self.sales = [
    #         {
    #             'sales_id' : 1,
    #             'attendant_name' : 'Mary',
    #             'no_of_products': 200
    #             'total_profit': 450000
    #         },
    #         {
    #             'sales_id' : 2,
    #             'attendant_name' : 'Daizy',
    #             'no_of_products': 20
    #             'total_profit': 100000
    #         }
    #     ]


    def create_sale(self, sales_id, attendant_name, no_of_pdts, total_profit):

        self.sales_id = self.sales_id + 1
        self.attendant_name = attendant_name
        self.no_of_pdts = no_of_pdts
        self.total_profit = total_profit

        sale={
            'sales_id': self.sales_id + 1,
            'attendant_name':request.json['attendant_name'],
            'no_of_pdts' : request.json['no_of_pdts'],
            'total_profit' : request.json['total_profit']
        }

        sales.append(sale)
        return jsonify(sales)

    #function to get and return all sales records
    def get_all_sales(self):
        if len(sales) > 0:
            return sales

    #funnction to get and return a particular sale record
    def get_sale(self, sales_id):
        for sale in sales:
            if sale['sales_id'] == sales_id:
                return sale


