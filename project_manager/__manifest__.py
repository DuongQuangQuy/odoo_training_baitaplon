{
    'name': "Project_manager",
    'version': '14.0.1',
    'depends': ['base','mail',],
    'author': "Enmasys",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'view/user.xml',
        'view/product_study.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}