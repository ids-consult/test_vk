# -*- coding: utf-8 -*-
#################################################################################
from datetime import date
from odoo import api,fields,models,_
from odoo.tools import formatLang

class SaleOrder(models.Model):
    _inherit = "sale.order"

    my_custom_name = fields.Char(string="Test name")
