from odoo import fields, models

class AccountTax(models.Model):
    _inherit = 'account.tax'
    
    min_base = fields.Float(default=0, string="Base mínima")
    l10n_co_edi_type_name = fields.Char(string="Nombre tipo de valor", related="l10n_co_edi_type.name")