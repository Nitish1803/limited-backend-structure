from src import db
from src.models import *


MOBILES_DUMMY_DATA = [
    [
        [1, "Samsung Galaxy S20 FE", "Fan Edition for Galaxy S20", "img", "ABC Electronics", 1000, "USA"],
        [1, 1]
    ],
    [
        [2, "Apple iPhone 13", "Latest smartphone by Apple", "img", "XYZ Electronics", 1500, "USA"],
        [1, 2]
    ]
]

LAPTOPS_DUMMY_DATA = [
    [
        [11, "Asus TUF Dash F15", "Beast from Asus", "img", "ABC Electronics", 10000, "China"],
        [2, 11]
    ],
    [
        [12, "Apple Macbook Air", "Beast from Apple", "img", "XYZ Electronics", 15000, "USA"],
        [2, 12]
    ]
]


def add_dummy_data():
    """
    Helper to dummy data to DB
    """
    # Add dummy data for mobiles
    db.session.add(Category(1, "Mobiles"))
    for val in MOBILES_DUMMY_DATA:
        db.session.add(Product(*val[0]))
        db.session.add(ProductCategory(*val[1]))
    db.session.commit()

    # Add dummy data for laptops
    db.session.add(Category(2, "Laptops"))
    for val in LAPTOPS_DUMMY_DATA:
        db.session.add(Product(*val[0]))
        db.session.add(ProductCategory(*val[1]))
    db.session.commit()
