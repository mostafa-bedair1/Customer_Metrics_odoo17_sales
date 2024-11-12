BreadcrumbsCustomer_Metrics_odoo17_sales
Task Overview:
1. Create a New Model and Compute Field

Define a new model called res.partner.customer_metrics that will store customer metrics, linked to the existing res.partner model.

This model  include:
A Many2one field to res.partner called customer_id.
A computed field total_sales that calculates the sum of amount_total from sale.order records associated with each customer.
A computed field order_count to store the count of orders each customer has placed.

2. Top Customers Method
Inside the res.partner.customer_metrics model, write a method called get_top_customers. This method should:

Retrieve the top 5 customers based on their total_sales values.
Return a list of dictionaries, each containing the customer’s name, total sales, and order count.

3. XML View for Top Customers Dashboard

Create a new XML file to define a dashboard view that displays the top 5 customers, including their total sales and order count.

Use an Odoo kanban or tree view to display this data in a structured format.
