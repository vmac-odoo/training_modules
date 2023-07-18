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
    "data": [
        "security/motorcycle_registry_groups.xml",
        "security/ir.model.access.csv",
        "views/motorcycle_registry_menu.xml",
    ],
    "demo": [
        "demo/motorcycle_demo.xml",
    ],
    "application": True,
    "installable": True,
}
