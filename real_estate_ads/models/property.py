from odoo import  field, models

class Property(models.Model):
    _name = "estate.property"

    name = field.Char(string="Name")
    description = field.Text(string="Descrription")
    postcode = field.Char(string="Post Code")
    date_availability = field.Date(string="Available From")
    expected_price = field.Float(string="Expected Price")
    selling_price = field.FLoad(string="Selling Price")
    bedrooms = field.Integer(string="Bedrooms")
    living_area = field.Integer(string="Living Area(sqm)")
    facades = field.Integer(string="Facades")
    garage = field.Boolean(string="Garage", default=False)
    garden = field.Boolean(string="Garden", default=False)
    garden_area = field.Integer(string="Garden area")
    garden_orientation = field.selection([('north', 'North'), ('south', 'south'), ('east', 'East'), ('west', 'West')], string="Garden Orientation", default='north')


