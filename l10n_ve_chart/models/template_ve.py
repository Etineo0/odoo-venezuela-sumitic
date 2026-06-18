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
                # Mapeo de tus cuentas desde el CSV
                "sumitic_ve_110101": {"name": "CAJA PRINCIPAL BS", "code": "110101", "account_type": "asset_cash", "reconcile": True},
                "sumitic_ve_110102": {"name": "BANCO NACIONAL BS", "code": "110102", "account_type": "asset_cash", "reconcile": True},
                "sumitic_ve_110103": {"name": "BANCO CUSTODIA USD", "code": "110103", "account_type": "asset_cash", "reconcile": True},
                "sumitic_ve_110104": {"name": "PAGOS PENDIENTES POR CONCILIAR", "code": "110104", "account_type": "asset_current", "reconcile": True},
                "sumitic_ve_110105": {"name": "TARJETAS POR COBRAR (PUNTO DE VENTA)", "code": "110105", "account_type": "asset_current", "reconcile": True},
                "sumitic_ve_110301": {"name": "CLIENTES NACIONALES BS", "code": "110301", "account_type": "asset_receivable", "reconcile": True},
                "sumitic_ve_110302": {"name": "CLIENTES NACIONALES USD", "code": "110302", "account_type": "asset_receivable", "reconcile": True},
                "sumitic_ve_110303": {"name": "ANTICIPOS A PROVEEDORES BS", "code": "110303", "account_type": "asset_current", "reconcile": True},
                "sumitic_ve_110304": {"name": "ANTICIPOS A PROVEEDORES USD", "code": "110304", "account_type": "asset_current", "reconcile": True},
                "sumitic_ve_110501": {"name": "IVA CREDITO FISCAL (16%)", "code": "110501", "account_type": "asset_current", "reconcile": True},
                "sumitic_ve_110502": {"name": "IVA CREDITO FISCAL (REDUCIDO 8%)", "code": "110502", "account_type": "asset_current", "reconcile": True},
                "sumitic_ve_110503": {"name": "IVA CREDITO FISCAL (SUNTUARIO 31%)", "code": "110503", "account_type": "asset_current", "reconcile": True},
                "sumitic_ve_110504": {"name": "RETENCIONES DE IVA ACUMULADAS", "code": "110504", "account_type": "asset_current", "reconcile": True},
                "sumitic_ve_110505": {"name": "RETENCIONES DE ISLR ACUMULADAS", "code": "110505", "account_type": "asset_current", "reconcile": True},
                "sumitic_ve_210101": {"name": "PROVEEDORES NACIONALES BS", "code": "210101", "account_type": "liability_payable", "reconcile": True},
                "sumitic_ve_210102": {"name": "ANTICIPOS DE CLIENTES BS", "code": "210102", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_210103": {"name": "ANTICIPOS DE CLIENTES USD", "code": "210103", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_210201": {"name": "IVA DEBITO FISCAL (16%)", "code": "210201", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_210202": {"name": "IVA DEBITO FISCAL (REDUCIDO 8%)", "code": "210202", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_210203": {"name": "IVA DEBITO FISCAL (SUNTUARIO 31%)", "code": "210203", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_210204": {"name": "IGTF POR ENTERAR (3%)", "code": "210204", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_210205": {"name": "RETENCIONES IVA POR ENTERAR", "code": "210205", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_210206": {"name": "RETENCIONES ISLR - HONORARIOS", "code": "210206", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_210207": {"name": "RETENCIONES ISLR - SERVICIOS", "code": "210207", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_210208": {"name": "CONTRIBUCION ESPECIAL DE PENSIONES", "code": "210208", "account_type": "liability_current", "reconcile": True},
                "sumitic_ve_310101": {"name": "CAPITAL SOCIAL", "code": "310101", "account_type": "equity", "reconcile": False},
                "sumitic_ve_310102": {"name": "RESULTADOS ACUMULADOS", "code": "310102", "account_type": "equity", "reconcile": False},
                "sumitic_ve_310103": {"name": "RESULTADO DEL EJERCICIO", "code": "310103", "account_type": "equity", "reconcile": False},
                "sumitic_ve_410101": {"name": "VENTAS NACIONALES (GRAVADAS)", "code": "410101", "account_type": "income", "reconcile": False},
                "sumitic_ve_410102": {"name": "VENTAS EXENTAS / EXONERADAS", "code": "410102", "account_type": "income", "reconcile": False},
                "sumitic_ve_410103": {"name": "GANANCIA POR DIFERENCIAL CAMBIARIO", "code": "410103", "account_type": "income", "reconcile": False},
                "sumitic_ve_510101": {"name": "COMPRAS NACIONALES (GRAVADAS)", "code": "510101", "account_type": "expense", "reconcile": False},
                "sumitic_ve_510102": {"name": "PERDIDA POR DIFERENCIAL CAMBIARIO", "code": "510102", "account_type": "expense", "reconcile": False},
                "sumitic_ve_510103": {"name": "GASTOS BANCARIOS E IGTF BANCARIO", "code": "510103", "account_type": "expense", "reconcile": False},
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
                "account_fiscal_country_id": False, # Corregido a False para evitar errores de ID base.ve
                "bank_account_code_prefix": "1113",
                "cash_account_code_prefix": "1111",
                "transfer_account_code_prefix": "1129003",
            },
        }
