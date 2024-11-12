from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model_create_multi
    def create(self, vals_list):
        records = super(SaleOrder, self).create(vals_list)
        records._update_customer_metrics()
        return records

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        self._update_customer_metrics()
        return res

    def _update_customer_metrics(self):
        for order in self:
            if order.partner_id:
                # Check if a CustomerMetrics record exists for the customer
                customer_metrics = self.env['res.partner.customer_metrics'].search([
                    ('customer_id', '=', order.partner_id.id)
                ], limit=1)

                if not customer_metrics:
                    # Create a new Customer_ Metrics record _if it does not exist
                    customer_metrics = self.env['res.partner.customer_metrics'].create({
                        'customer_id': order.partner_id.id
                    })

                # Recalculate the fields by compute methods
                    customer_metrics._compute_total_sales()
                    customer_metrics._compute_order_count()
