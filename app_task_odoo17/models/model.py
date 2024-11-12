from odoo import models, fields, api


# parent="sale.sale_order_menu"
class CustomerMetrics(models.Model):
    _name = 'res.partner.customer_metrics'
    _description = 'Customer Sales Metrics'

    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    total_sales = fields.Float(string='Total Sales', compute='_compute_total_sales', store=True)
    order_count = fields.Integer(string='Order Count', compute='_compute_order_count', store=True)

    @api.depends('customer_id')
    def _compute_total_sales(self):
        for record in self:
            # Calculate total sales for the customer
            total = sum(
                self.env['sale.order'].search([('partner_id', '=', record.customer_id.id)]).mapped('amount_total'))
            record.total_sales = total

    @api.depends('customer_id')
    def _compute_order_count(self):
        for record in self:
            # Count the number of orders for the customer
            count = self.env['sale.order'].search_count([('partner_id', '=', record.customer_id.id)])
            record.order_count = count

