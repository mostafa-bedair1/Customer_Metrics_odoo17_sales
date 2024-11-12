{
    'name': 'Customer Metrics Module',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Dashboard for Customer Sales Metrics',
    'description': 'Provides a dashboard view of top customers based on sales metrics.',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_metrics_view.xml',
    ],
    'installable': True,
    'application': True,
}
