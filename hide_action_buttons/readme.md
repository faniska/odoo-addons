### Steps to start use ###
1. Install the module
2. Add computable boolean field named as "hide_action_buttons" for model
3. Implement computation by your business process
4. Insert the field "hide_action_buttons" in the form view of the model

Code example:
### python ###
```python
from odoo import models, fields, api
class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    # Step 2 - example code
    hide_action_buttons = fields.Boolean('Hide Action Buttons', compute='_compute_hide_action_buttons')
    
    # Step 3 - example code
    @api.multi
    @api.depends('state')
    def _compute_hide_action_buttons(self):
        for order in self:
            if order.state == 'draft':
                # Show Create/Edit buttons on draft
                order.hide_action_buttons = False
            elif order.state == 'done':
                # Hide Create/Edit buttons if order is done
                order.hide_action_buttons = True
```
### xml view ###
```xml
<!-- Step 4 - code example -->
<record id="purchase_order_form_inherited" model="ir.ui.view">
    <field name="name">purchase.order.inherited</field>
    <field name="model">purchase.order</field>
    <field name="inherit_id" ref="purchase.purchase_order_form"/>
    <field name="arch" type="xml">
    <data>
        <header position="inside">
            <field name="hide_action_buttons" invisible="True"/>
        </header>
    </data>
    </field>
</record>
```
