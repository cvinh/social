from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    show_aliases_mail_tracking = fields.Boolean(
        string="Show Aliases in Mail Tracking",
        default=False,
    )
