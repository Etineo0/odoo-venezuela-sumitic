from odoo import models, _
from odoo.addons.account.models.chart_template import template

class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @template("ve")
    def _get_ve_template_data(self):
        return {
            "name": _("Venezuela"),
            "code_digits": "7",
            # Es vital que 'account.account' sea la clave principal de los datos
            "account.account": {
                "sumitic_ve_110104": {
                    "name": "PAGOS PENDIENTES POR CONCILIAR",
                    "code": "110104",
                    "account_type": "asset_current", 
                    "reconcile": True,
                },
                "sumitic_ve_110301": {
                    "name": "CLIENTES NACIONALES BS", 
                    "code": "110301", 
                    "account_type": "asset_receivable", 
                    "reconcile": True
                },
            },
            "property_account_receivable_id": "sumitic_ve_110301",
            "property_account_payable_id": "sumitic_ve_210101",
        }

    @template("ve", "res.company")
    def _get_ve_res_company(self):
        return {
            self.env.company.id: {
                "account_fiscal_country_id": False,
                "bank_account_code_prefix": "1113",
            },
        }
