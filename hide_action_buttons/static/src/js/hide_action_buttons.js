odoo.define('hide_action_buttons.hide_action_buttons', function (require) {
    "use strict";
    let FormView = require('web.FormView');
    FormView.include({
        load_record: function (record) {
            if (record && this.$buttons) {
                if (record.hide_action_buttons) {
                    this.$buttons.find('.o_form_buttons_view').hide();
                } else {
                    this.$buttons.find('.o_form_buttons_view').show();
                }
            }
            return this._super(record);
        }
    });
});