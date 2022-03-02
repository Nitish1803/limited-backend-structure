# limited-backend-structure

## Description

A Limited back end structure for an eCommerce application. Allows users to fetch data from database of products and categories. Can be accessed and interacted with via an API client such as [Postman](https://www.postman.com/product/api-client/).

## Installation

1. Clone this repo. Install dependencies by running `pip install -r requirements.txt`.

## Usage

- Run `app.py` to start the program.

- Submit requests to any of the endpoints using an API client (like Postman).

- NOTE: Although the code to delete `data.db` is already added but if the file is not deleted after successful execution
        of the program then before re-running the program, delete `data.db` because database is populated everytime the
        application starts and the `seeder.py` is not intelligent enough to handle data redundancy.

## Routes

### /all_products
 - GET
 - GET returns products and associated category
 - product_id as a param can be used to fetch data for a specific product

Example response from GET:

![Product GET](./assets/all-products.png?raw=true)

Example response from GET with sorting:

![Product GET](./assets/all-products-with-sorting.png?raw=true)

Example response from GET with filtering:

![Product GET](./assets/all-products-with-filtering.png?raw=true)


### /all_categories
 - GET
 - GET returns available categories

![Category GET](./assets/all-categories.png?raw=true)
