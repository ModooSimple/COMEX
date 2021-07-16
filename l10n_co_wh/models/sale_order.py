from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def calculate_rtefte(self):
        """
        Unlinks ReteFuente taxes from account invoice line if the sum of lines with same retefuente tax is not greater than min base
        """
        self.ensure_one()
        rtefte_taxes = self.order_line.tax_id.filtered(
            lambda l: l.l10n_co_edi.type.name == "ReteFuente"
        )
        for tax in rtefte_taxes:
            lines = self.order_line.filtered(lambda l: tax.id in l.tax_id.ids)
            subtotal = sum(lines.mapped('price_subtotal'))
            if subtotal < tax.min_base:
                [line.write({'tax_id': [(3, tax.id, 0)]}) for line in lines]
            else: pass

        return True    