# -*- coding: utf-8 -*-
{
    'name': 'Cốc Giấy Việt',
    'version': '1',
    'category': 'Cocgiayviet.com',
    'live_test_url': '#',
    'summary': '#',
    'author': 'Lv Quy',
    'company': '#',
    'website': 'https://cocgiayviet.com',
    'depends': ['base_setup','website'],
    'data': [
        #data

        # security
        # report
        # views
        'views/custom_footer.xml',
        # 'views/header.xml',
        'views/custom_style_heading.xml',
    ],

    'assets': {
        'web.assets_backend': [
            'cocgiay_vietcocviet.png/static/src/css/style.css'
        ],
        'web._assets_primary_variables': [
        ],
    },

    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
}
