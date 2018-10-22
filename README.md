# Store_Manager_APIs

[![Build Status](https://travis-ci.org/dxania/Store_Manager_APIs.svg?branch=develop)]
(https://travis-ci.org/dxania/Store_Manager_APIs) 

[![Coverage Status](https://coveralls.io/repos/github/dxania/Store_Manager_APIs/badge.svg)](https://coveralls.io/github/dxania/Store_Manager_APIs)

[![Code Climate](https://codeclimate.com/github/codeclimate/codeclimate/badges/gpa.svg)](https://codeclimate.com/github/dxania/Store_Manager_APIs)


Set of API endpoints to be consumed by a store manager application


## Features
The Program offers the following set of endpoints:


  | EndPoint                   | Functionality                 | Notes                                  |
  | ---------------------------|-------------------------------|----------------------------------------|
  | GET /products              | Fetch all products            | Get all available products.            |
  | GET /products/[productId]  | Fetch a single product record | Get a specific product using the       |  |                                                               product’s id.                         |
  |  GET /sales                | Fetch all sale records        | Get all sale records.                  |
  |  GET /sales/[saleId]       | Fetch a single sale record    | Get a specific sale record using its id|
  |  POST /sales               | Create a sale order           | Create a sale record.                  |
  |  POST /products            | Create a product              | Create a product.                      |



## Getting started
These instructions will get you a copy of the program on your local machine for development and testing purposes. The instructions are tailored for uses of `LINUX OS` particularly `UBUNTU`

## Prerequisites
What things you will need to run the application

```
Python3
    version: 3.4.3
```
```
Pip for python3
    $ sudo apt-get install python3-pip
```
```
Flask to build the application
    version: 1.0.2
    $ pip install flask
```
```
Virtualenv to create a virtual environment
    version: 16.0.0
```
```
Pytest to perform tests
    version: 2.5.1
    $ pip install pytest -U
```
Alternatively, run `pip install -r requirements.txt` to install all the necessary tools

## Built With
[Flask](http://flask.pocoo.org/) -  microframework for Python

## Installing
To have a copy of the project on your machine, run the command below in your preferred directory:

``` 
git clone https://github.com/dxania/Store_Manager_APIs.git
```
After cloning, you will have a folder named `Store_Manager_APIs`

## How to use
1. Navigate to `Store_Manager_APIs`
2. Create a virtual environment by running:
``` python3 -m venv <name of virtualenvironment> ```
3. Activate the virtual environment
``` source <name of virtualenvironment>/bin/activate```
You should the name of the virtual environment placed right nefore your current path/directory in brackets()
4. Run the application
```export FLASK_APP=store_mgr.py``` then
```flask run```
5. Follow the instructions

## Testing
1. Run `pytest` in the directory of the project to run unit tests
2. Test with [Postman](https://www.getpostman.com/) by pasting the url [http://127.0.0.1:5000/api/v1/products](http://127.0.0.1:5000/api/v1/products) for Products or [http://127.0.0.1:5000/api/v1/sales](http://127.0.0.1:5000/api/v1/sales) for Sales into the url section and call the GET/POST methods accordingly. (For the POST requests, enter the data as raw application/json)

## Author
[Daizy Obura](https://github.com/dxania/)