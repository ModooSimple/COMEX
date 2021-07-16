from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

        
    @api.multi
    def calculate_rtefte(self):
        """
        Unlinks ReteFuente taxes from account invoice line if the sum of lines with same retefuente tax is not greater than min base
        """
        self.ensure_one()
        rtefte_taxes = self.invoice_line_ids.tax_ids.filtered(
            lambda l: l.l10n_co_edi.type.name == "ReteFuente"
        )
        for tax in rtefte_taxes:
            lines = self.invoice_line_ids.filtered(lambda l: tax.id in l.tax_ids.ids)
            subtotal = sum(lines.mapped('price_subtotal'))
            if subtotal < tax.min_base:
                [line.write({'tax_ids': [(3, tax.id, 0)]}) for line in lines]
            else: pass

        return True
