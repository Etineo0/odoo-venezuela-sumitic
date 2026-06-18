# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    "name": "Venezuela - Plan de Cuentas (Sumitic)",
    "version": "19.0.1.0.0",
    "author": "Sumitic C.A.",
    "website": "https://github.com/Etineo0/odoo-venezuela-sumitic",
    "icon": "/account/static/description/l10n.png",
    "countries": ["ve"],
    "category": "Accounting/Localizations/Account Charts",
    "description": """
        Plan de Cuentas para Venezuela — Sumitic C.A.
        ==============================================

        Localización contable para Venezuela compatible con Odoo 19.
    """,
    "license": "LGPL-3",
    "depends": [
        "account",
        "l10n_ve",           # CRUCIAL: Esto crea el registro 'base.ve'
        "account_accountant", # Necesario para las funciones de template
    ],
    "data": [
        "data/template/account.tax.group.csv",
        "data/template/account.tax.csv",
        "data/template/account.account.csv",
    ],
    "installable": True,
    "auto_install": False,
}
