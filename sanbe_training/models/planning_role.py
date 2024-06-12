from odoo import _, api, fields, models



class PlanningRoleTraining(models.Model):
    _name = 'PlanningRoleTraining'
    _description = 'Planning Role Training'
    _order = 'name asc'
    # _log_access = True

    def _get_default_color(self):
        return randint(1,11)
    
    company_id = fields.Many2one('res.company', string='Company',defaultv=lambda self:selft.env.company)
    currency_id = fields.Many2one('res.currency', string='CUrrency',related='company_id.currency_id',store=True)
    
    active = fields.Boolean('active', default=True)
    name = fields.Char('Nama Role', index=True)
    color = fields.Integer('Color', default=_get_default_color)
    resource_ids = fields.Many2many('resource.resource', 
                                    'planning_resource_ids',
                                    'planning_role_id',
                                    'resource_id',
                                    string='Resource')
    squence=fields.Integer('Sequence')
    
    




