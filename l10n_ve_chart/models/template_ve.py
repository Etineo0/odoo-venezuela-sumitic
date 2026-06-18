# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import models, _
from odoo.addons.account.models.chart_template import template

class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @template("ve")
    def _get_ve_template_data(self):
        return {
            "name": _("Venezuela"),
            "code_digits": "7",
            "account_account": {
                # CUENTA OBLIGATORIA PARA EVITAR EL KEYERROR
                "account_110104": {
                    "name": "PAGOS PENDIENTES POR CONCILIAR",
                    "code": "110104",
                    "account_type": "asset_current", 
                    "reconcile": True,
                },
                # Tus otras cuentas...
                "sumitic_ve_110301": {"name": "CLIENTES NACIONALES BS", "code": "110301", "account_type": "asset_receivable", "reconcile": True},
                "sumitic_ve_210101": {"name": "PROVEEDORES NACIONALES BS", "code": "210101", "account_type": "liability_payable", "reconcile": True},
                "sumitic_ve_410101": {"name": "VENTAS NACIONALES", "code": "410101", "account_type": "income", "reconcile": False},
                "sumitic_ve_510101": {"name": "COMPRAS NACIONALES", "code": "510101", "account_type": "expense", "reconcile": False},
            },
            "property_account_receivable_id": "sumitic_ve_110301",
            "property_account_payable_id": "sumitic_ve_210101",
            "property_account_expense_categ_id": "sumitic_ve_510101",
            "property_account_income_categ_id": "sumitic_ve_410101",
        }

    @template("ve", "res.company")
    def _get_ve_res_company(self):
        return {
            self.env.company.id: {
                "account_fiscal_country_id": False,
                "bank_account_code_prefix": "1113",
                "cash_account_code_prefix": "1111",
                "transfer_account_code_prefix": "1129003",
            },
        }
