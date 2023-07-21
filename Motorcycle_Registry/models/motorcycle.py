from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

vin_pattern = r"^[A-Z]{4}\d{2}[A-Z\d]{2}\d{6}$"


class MotorcycleRegistry(models.Model):
    _name = "motorcycle.registry"
    _description = "Motorcycle Registry"
    _rec_name = "registry_number"

    _sql_constraints = [
        ("check_unique_vin", "UNIQUE(vin)", "The VIN must be unique!"),
        (
            "check_unique_registry_number",
            "UNIQUE(registry_number)",
            "The Registry Number must be unique!",
        ),
    ]

    registry_number = fields.Char(
        string="Registry Number",
        required=True,
        default="MRN0000",
        copy=False,
        readonly=True,
    )
    vin = fields.Char(string="VIN", required=True)
    brand = fields.Char(compute="_compute_vin_relations")
    make = fields.Char(compute="_compute_vin_relations")
    model = fields.Char(compute="_compute_vin_relations")
    owner_id = fields.Many2one(
        string="Owner",
        comodel_name="res.partner",
        ondelete="restrict",
    )
    owner_name = fields.Char(related="owner_id.name", string="Name")
    owner_phone = fields.Char(related="owner_id.phone", string="Phone")
    owner_email = fields.Char(related="owner_id.email", string="Email")
    picture = fields.Binary(string="Picture")
    current_mileage = fields.Float(string="Current Mileage")
    license_plate = fields.Char(string="License Plate")
    certificate_title = fields.Binary(string="Certificate of Title")
    register_date = fields.Date(string="Register Date")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get("registry_number", ("MRN0000")) == ("MRN0000"):
                vals["registry_number"] = self.env["ir.sequence"].next_by_code(
                    "motorcycle.registry.number"
                )
        return super().create(vals_list)

    @api.constrains("vin")
    def _check_vin(self):
        for motorcycle_registry in self:
            if not bool(re.match(vin_pattern, str(motorcycle_registry.vin))):
                raise ValidationError(
                    """
                    The VIN Number requires the following pattern:\n
                        Make - 2 Capital Letters\n
                        Model - 2 Capital Letters\n
                        Year - 2 Digits\n
                        Battery Capacity - 2 Capital Letters or Numbers\n
                        Serial Number - 6 Digits        
                """
                )

    @api.constrains("license_plate")
    def _check_license_plate(self):
        for motorcycle_registry in self:
            license_plate_regex = r"^[A-Z]{1,4}\d{1,3}[A-Z]{0,2}$"
            if motorcycle_registry.license_plate and not bool(
                re.match(license_plate_regex, str(motorcycle_registry.license_plate))
            ):
                raise ValidationError(
                    """
                    The License Plate requires the following pattern:\n
                        1 - 4 Capital Letters\n
                        1 - 3 Digits\n
                        Optional 2 Capital Letters
                """
                )

    @api.depends("vin")
    def _compute_vin_relations(self):
        self.brand, self.make, self.model = "", "", ""
        for motorcycle_registry in self:
            if motorcycle_registry.vin and bool(
                re.match(vin_pattern, str(motorcycle_registry.vin))
            ):
                motorcycle_registry.brand = motorcycle_registry.vin[:2]
                motorcycle_registry.make = motorcycle_registry.vin[2:4]
                motorcycle_registry.model = motorcycle_registry.vin[4:6]
