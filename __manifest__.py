# -*- coding: utf-8 -*-
# © 2017 Diagram Software S.L.
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html


{
    "name": "Odoo pruebas",
    "version": "11.0.1.1",
    "author": "Diagram Software, S.L.",
    "category": "NubeaERP",
    "summary": "odoo_pruebas",
    "depends": [
        'mrp',
        'mrp_operations',
        'purchase',
        'project',
        'mrp_byproduct',
        'stock',
    ],
    "data": [
        'security/005176_security.xml',
        'security/ir.model.access.csv',
        'reports/generate_check_report.xml',
        'wizards/change_beam_bobbin.xml',
        'wizards/mrp_workorder_extra.xml',
        'views/mo_reports.xml',
        'views/product_family.xml',
        'views/product_base_code.xml',
        'views/product.xml',
        'views/project.xml',
        'datas/send_generate_check_report.xml',
        'datas/device_meters_line_type_data.xml',
        'datas/pay_off_negative_quant_cron.xml',
        'datas/procurement_data.xml',
        'datas/crons.xml',
    ],
    "installable": True,
}
