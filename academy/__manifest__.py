{
    'name': 'Odoo Academy',
    'version': '0.0.0.0.2',
    'summary': 'Import Products from CSV/Excel File, Import Products, Import Product and update Product, Odoo All Import Data',
    'description': """
        training for odoo custom modules
    """,
    'author': 'MagnaWave',
    'website': 'www.magnawavepemf.com',
    'category': 'Custome Modules',
    'depends': ['base'],
    'data': [
        'security/academy_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
    ],
    'demo': [
        'demo/course_demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'OPL-1',
}