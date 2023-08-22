{
    'name': "Project_study",
    'version': '14.0.1',
    'depends': ['base','mail','sale'],
    'author': "Enmasys",
    'category': 'Category',
    'description': """
    Description text,
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'view/Student.xml',
        'view/classroom.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}