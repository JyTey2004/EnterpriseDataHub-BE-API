# MockPRS API

## Description
This API will be able to fetch the data from the database and return the response in JSON format. This API is created using Python Flask and deployed in remote desktop for my instance. If the record is not found, the data will be inserted into the database and return the response in JSON format. 

## Overview
  1. Schema Creation which contains the EDH data using mysql to store the data.
     1. More configuration details in [app](app/__init__.py)
     2. Schema Creation Script [modals](app/modals)
     3. Modal Controller [controller](app/controllers)
     4. Server Routes [routes](app/routes) 
  2. API created using Python Flask to fetch the data from the database.
  3. API is deployed in remote desktop
  4. API is accessible via http://localhost:5000/v1/entity/<uen>
     1. More details below
  5. API is tested using Postman
     1. [Postman Test Files](Postman_Tests)

## Table of Contents
1. [Instructions & Configurations](#instructions)
2. [API Endpoint - POST](#api-endpoint---post)
3. [Testing](#testing)

### Instructions
1. Clone the repository
2. Create a virtual environment
    1. Install virtualenv `pip install virtualenv`
    2. Create a virtual environment `virtualenv venv`
    3. Activate the virtual environment `source venv/bin/activate`
3. Install the dependencies pip install -r requirements.txt
4. Update the database configuration in [app](app/__init__.py) if required
   1. `db_username = 'root'`
   2. `db_password = 'password$1'`
   3. `db_host = 'edh-mockdb'`
   4. `db_name = 'localhost'`
5. Run the application `python run.py`
6. Access the application via http://localhost:5000/v1/entity/<uen>
7. Also, you can access it via http://your-ip-address:5000/v1/entity/<uen>

### API Endpoint - POST
* http://localhost:5000/v1/entity/<uen>
  * Request Body - JSON:
    1. [LC - Sample Request File](Postman_Tests/Requests/201900001B.json)
    2. [BN - Sample Request File](Postman_Tests/Requests/87654321B.json)
  
  * Response Body - JSON:
    1. [LC - Sample Response File](Postman_Tests/Response/201900001B_response.json)
    2. [BN - Sample Response File](Postman_Tests/Response/87654321B_response.json)

### Testing
* Delete the existing tables and create a new tables with the same name and run the below command
  1. Press `Ctrl + C` to stop the application
  2. Go to mysql and delete all the tables
  3. Run `python run.py` 
  4. Continue inserting the data or test the api endpoints

* Test the API endpoints using Postman
  1. Import the [Postman Collection](Postman_Tests/MockServer.postman_collection.json)
  2. Run the collection
  3. Check the response body
  4. Check the response time
  5. Check the response status code
  6. Check the response headers
  7. Check the response body
