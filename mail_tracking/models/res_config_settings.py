from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    show_aliases_mail_tracking = fields.Boolean(
        related="company_id.show_aliases_mail_tracking",
        readonly=False,
    )
