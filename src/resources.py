import ast, json
from flask_restful import Resource
from flask import request, Response
from sqlalchemy import asc, desc, tuple_
from src.models import *


class AllProducts(Resource):
    """
    AllProducts - This is the main API. It includes required sorting and filtering,
                  Same API can be used to fetch an individual product's details 
                  (using filter on product_id).
    """
    def get(self):
        """
        Get()
        """
        try:
            # Sorting Mechanism
            sort_by = request.args.get('sort_by', 'category_id')
            sort_order = request.args.get('sort_order', 'asc')
            if sort_by in ['category_id', 'category_name']:
                sort_column = getattr(Category, sort_by)
            else:
                sort_column = getattr(Product, sort_by)
            sort_direction = desc if sort_order == 'desc' else asc

            # Filtering Mechanism
            filter_by = ast.literal_eval(request.args.get('filter_by', 'None'))
            if filter_by:
                filter_map = {}
                for k,v in filter_by.items():
                    if k in ['category_id', 'category_name']:
                        filter_column = getattr(Category, k)
                    else:
                        filter_column = getattr(Product, k)
                    filter_map.update({filter_column:v})

            # Query Data
            if filter_by:
                itemData = Product.query.join(ProductCategory, Product.product_id == ProductCategory.product_id) \
                .add_columns(Product.product_id, Product.product_name, Product.price, Product.description, Product.image, ProductCategory.category_id, Product.vendor, Product.admissible_region) \
                .filter(tuple_(*filter_map.keys()).in_([tuple(filter_map.values())])) \
                .join(Category, Category.category_id == ProductCategory.category_id) \
                .order_by(sort_direction(sort_column)) \
                .all()
            else:
                itemData = Product.query.join(ProductCategory, Product.product_id == ProductCategory.product_id) \
                .add_columns(Product.product_id, Product.product_name, Product.price, Product.description, Product.image, ProductCategory.category_id, Product.vendor, Product.admissible_region) \
                .join(Category, Category.category_id == ProductCategory.category_id) \
                .order_by(sort_direction(sort_column)) \
                .all()

            # Format and Return Data
            resultData = []
            for record in itemData:
                itemObject = {
                    'category_id': record.category_id,
                    'product_id': record.product_id,
                    'product_name': record.product_name,
                    'price': float(record.price),
                    'description': record.description,
                    'image':  record.image,
                    'vendor': record.vendor,
                    'admissible_region': record.admissible_region
                }
                resultData.append(itemObject)
            return resultData
        except Exception as e:
            resp = {
                "error_code": 500,
                "error_msg": str(e)
            }
            return Response(json.dumps(resp), status=500, mimetype='application/json')


class AllCategories(Resource):
    """
    AllCategories - This API is used to display all the available categories.
                    It only supports sorting. No filtering is available because
                    the no. of columns is very less and it doesn't make sense to
                    add it.
    """
    def get(self):
        """
        Get()
        """
        try:
            # Sorting Mechanism
            sort_by = request.args.get('sort_by', 'category_id')
            sort_order = request.args.get('sort_order', 'asc')
            sort_direction = desc if sort_order == 'desc' else asc

            # Query Data
            itemData = Category.query.join(ProductCategory, Category.category_id == ProductCategory.category_id) \
            .join(Product, Product.product_id == ProductCategory.product_id) \
            .order_by(sort_direction(getattr(Category, sort_by))) \
            .distinct(Category.category_id) \
            .all()

            # Format and Return Data
            resultData = []
            for record in itemData:
                itemObject = {
                    'category_id': record.category_id,
                    'category_name': record.category_name,
                }
                resultData.append(itemObject)
            return resultData
        except Exception as e:
            resp = {
                "error_code": 500,
                "error_msg": str(e)
            }
            return Response(json.dumps(resp), status=500, mimetype='application/json')
