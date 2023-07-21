from odoo import models, fields, api


class Product(models.Model):
    _inherit = "product.template"

    detailed_type = fields.Selection(
        selection_add=[
            ("motorcycle", "Motorcycle"),
        ],
        ondelete={"motorcycle": "set product"},
    )

    horse_power = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    battery_capacity = fields.Char()
    charge_time = fields.Float()
    moto_range = fields.Float(string="Range")
    curb_weight = fields.Float()
    make = fields.Char()
    model = fields.Char()
    launch_date = fields.Date()
    year = fields.Integer()

    def _detailed_type_mapping(self):
        type_mapping = super()._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping