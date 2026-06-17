# odoo-venezuela-sumitic

**Localización venezolana para Odoo 19** — desarrollada y mantenida por **Sumitic C.A.**

Homologación contable adaptada a los requerimientos del SENIAT y las prácticas contables venezolanas vigentes, compatible con **Odoo 19 / Odoo.sh**.

---

## Módulos incluidos

### `l10n_ve_chart` — Plan de Cuentas Venezuela

- **Plan de cuentas** de 7 dígitos (267 cuentas), basado en prácticas venezolanas
- **Grupos de IVA**: 0%, 8%, 16%, 31%
- **Impuestos** de venta y compra para cada alícuota
- Configuración de cuentas por defecto (cobros, pagos, diferencial cambiario, POS, cuenta puente)

```
l10n_ve_chart/
├── __manifest__.py
├── __init__.py
├── models/
│   └── template_ve.py        # @template "ve"
├── data/template/
│   ├── account.account.csv   # 267 cuentas
│   ├── account.tax.group.csv # Grupos IVA
│   └── account.tax.csv       # Impuestos IVA
└── demo/demo_company.xml
```

---

## Instalación en Odoo.sh

### Opción A — Repositorio de terceros (recomendada para Odoo.sh)

1. En el panel de **Odoo.sh → Settings → Repositories**, agrega:
   ```
   https://github.com/Etineo0/odoo-venezuela-sumitic
   ```
2. Selecciona la rama `main`.
3. Odoo.sh detectará los módulos automáticamente.
4. Ve a **Apps**, busca *Venezuela - Plan de Cuentas* e instálalo.

### Opción B — Submódulo Git

```bash
cd /ruta/a/tu/proyecto-odoo
git submodule add https://github.com/Etineo0/odoo-venezuela-sumitic.git addons/odoo-venezuela-sumitic
git commit -m "add: localización venezolana Sumitic"
git push
```

### Uso

Al crear una nueva compañía, selecciona **Venezuela** como país → el plan de cuentas se aplicará automáticamente desde el asistente de configuración de contabilidad.

---

## Compatibilidad

| Versión Odoo | Estado |
|---|---|
| 19.0 | ✅ Soportado |
| 18.0 | ✅ Compatible (mismo API) |
| 17.0 | ✅ Compatible (mismo API) |
| 16.0 o anterior | ❌ API distinto |

---

## Créditos

- Plan de cuentas base: **Binaural C.A.** (https://binauraldev.com/)
- Adaptación y mantenimiento Odoo 19: **Sumitic C.A.**
- Licencia: LGPL-3
