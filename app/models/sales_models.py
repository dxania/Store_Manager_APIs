from flask import Flask, jsonify, request


class Sales():
    def __init__(self):

        self.sales_id = 0

        self.sales = [
            {
                'sales_id' : 1,
                'attendant_name' : 'Mary',
                'no_of_pdts': 200
                'total_profit': 450000
            },
            {
                'sales_id' : 2,
                'attendant_name' : 'Daizy',
                'no_of_pdts': 20
                'total_profit': 100000
            }
        ]


    # def create_sale(self, sales_id, attendant_name, no_of_pdts, total_profit):

    #     self.sales_id += self.sales_id
    #     self.attendant_name = attendant_name
    #     self.no_of_pdts = no_of_pdts
    #     self.total_profit

    #     sale={
    #         'sales_id': self.sales_id + 1,
    #         'attendant_name':request.json['attendant_name'],
    #         'no_of_pdts' : request.json['no_of_pdts'],
    #         'total_profit' : request.json['total_profit']
    #     }

    #     self.sales.append(sale)
    #     return jsonify(self.sales)

    def get_all_sales(self):
        if len(self.sales) > 0:
            return self.sales


    def get_sale(self, sales_id):
        for sale in self.sales:
            if sale['sales_id'] == sales_id:
                return sale


