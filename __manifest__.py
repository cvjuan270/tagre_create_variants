# -*- coding: utf-8 -*-
{
    'name': "Crea Variantes",

    'summary': """
        Al duplicar productos con atributos dinámicos, no crea las variantes.
        Con esta extension """,


    'author': "Juan Collado V.",
    'website': "https://tagre.app",

    'category': 'Sales',
    'version': '0.1',
    'license': 'AGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sales_team'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
    ],
}
