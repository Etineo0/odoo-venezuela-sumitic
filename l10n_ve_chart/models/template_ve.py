from odoo import models, _
from odoo.addons.account.models.chart_template import template

class AccountChartTemplate(models.AbstractModel):
    _inherit = "account.chart.template"

    @template("ve")
    def _get_ve_template_data(self):
        # Esta estructura es la que espera el motor contable de Odoo
        return {
            "name": _("Venezuela"),
            "code_digits": "7",
            "account_account": {
                "sumitic_ve_110104": {
                    "name": "PAGOS PENDIENTES POR CONCILIAR",
                    "code": "110104",
                    "account_type": "asset_current", # REQUERIDO POR ENTERPRISE
                    "reconcile": True,
                },
                "sumitic_ve_110301": {"name": "CLIENTES NACIONALES BS", "code": "110301", "account_type": "asset_receivable", "reconcile": True},
                "sumitic_ve_210101": {"name": "PROVEEDORES NACIONALES BS", "code": "210101", "account_type": "liability_payable", "reconcile": True},
            },
            "property_account_receivable_id": "sumitic_ve_110301",
            "property_account_payable_id": "sumitic_ve_210101",
        }
