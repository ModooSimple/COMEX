{
    "name": "Withholding Taxes",
    "description": "Calculate withholding taxes by minimun base",
    "version": "12.0.1.0.0",
    "license": "AGPL-3",
    "author": "Modoo Simple",
    "website": "www.modoosimple.com",
    "depends": ["sale", "purchase", "account", "l10n_co_edi"],
    "data": [  
        "views/account_tax_view.xml",
        "views/sale_order_view.xml",
        "views/purchase_order_view.xml",
        "views/account_invoice_view.xml",
    ],
}