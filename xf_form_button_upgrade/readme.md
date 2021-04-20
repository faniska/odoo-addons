### Steps to start use ###

1. Install the module
2. Add comma-separated list of fields to the "skip_is_valid" key of context for the button in form view
3. Also, you can use the "all" keyword to skip all fields like that:  ```context="{'skip_is_valid':['all']}"```

Code example:

### xml view ###

```xml
<!-- Step 4 - code example -->
<record id="purchase_order_form_inherited" model="ir.ui.view">
    <field name="name">purchase.order.inherited</field>
    <field name="model">purchase.order</field>
    <field name="inherit_id" ref="purchase.purchase_order_form"/>
    <field name="arch" type="xml">
        <data>
            <!-- If you need inherit existing button -->
            <button name="action_rfq_send" position="attributes">
                <attribute name="context">{'skip_is_valid':['company_id','currency_id']}</attribute>
            </button>
            <!-- When you add a new button -->
            <button name="print_quotation" string="Print RFQ" type="object"
                    states="draft" class="oe_highlight" groups="base.group_user"
                    context="{'skip_is_valid':['company_id','currency_id']}"/>
        </data>
    </field>
</record>
```
