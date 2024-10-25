from odoo import  field, models

class Property(models.Model):
    _name = "estate.property"

    name = field.Char(string="Name")
    description = field.Text(string="Descrription")
    postcode = field.Char(string="Post Code")
    date_availability = field.Date(string="Available From")
    expected_price = field.Float(string="Expected Price")
    selling_price = field.FLoad(string="Selling Price")
