# -*- coding: utf-8 -*-

{
    "name": "Motorcycle Registry",
    "version": "1.0",
    "summary": "Manage Registration of Motorcycles",
    "description": """ 
        Motorcycle Registry
            -This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.
    """,
    "author": "vmac-odoo",
    "website": "https://github.com/vmac-odoo",
    "category": "Kawiil",
    "license": "OPL-1",
    "data": [
        "security/motorcycle_registry_groups.xml",
        "security/ir.model.access.csv",
        "data/motorcycle_registry_data.xml",
        "views/motorcycle_registry_menu.xml",
        "views/motorcycle_registry_views.xml",
        "views/motorcycle_inherit_product.xml",
        "views/motorcycle_web_templates.xml",
    ],
    "demo": [
        "demo/motorcycle_demo.xml",
        "demo/motorcycle_products_demo.xml"
    ],
    "depends": ["product", "stock", "website"],
    "application": True,
    "installable": True,
}
