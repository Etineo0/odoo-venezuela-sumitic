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

        Localización contable para Venezuela compatible con Odoo 19,
        desarrollada y mantenida por Sumitic C.A.

        Homologación contable adaptada a los requerimientos del SENIAT
        y las prácticas contables venezolanas vigentes.

        Este módulo provee:
        - Plan de cuentas de 7 dígitos basado en prácticas venezolanas
        - Grupos de impuestos: IVA 0%, 8%, 16%, 31%
        - Impuestos de venta y compra configurados con cuentas correctas
        - Configuración de cuentas por defecto de la compañía
        - Cuenta transitoria para transferencias bancarias
    """,
    "license": "LGPL-3",
    "depends": [
        "account", "accountant"
    ],
}
