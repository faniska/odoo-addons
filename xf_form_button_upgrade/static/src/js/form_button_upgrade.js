odoo.define('xf_form_button_upgrade.skip_is_valid', function (require) {
    "use strict";

    const form_widgets = require('web.form_widgets');
    const form_common = require('web.form_common');

    form_widgets.WidgetButton.include({
        on_click: function () {
            this.view.dataset.context.button_context = this.build_context().eval();
            this._super.apply(this, arguments);
        },
    });

    form_common.AbstractField.include({
        is_valid: function () {
            if (this.skip_is_valid()) {
                return true;
            }
            return this._super.apply(this, arguments);
        },

        skip_is_valid: function () {
            const button_context = this.view.dataset.context['button_context'];
            if ($.isEmptyObject(button_context)) {
                // false if button context is not set
                return false
            }
            if (!Array.isArray(button_context['skip_is_valid'])) {
                // false if button context does not contain the list of fields to skip
                return false
            }
            // check if the current field (this) or the "all" keyword is set to skip validation
            return button_context['skip_is_valid'].includes(this.name) || button_context['skip_is_valid'].includes('all')
        }
    })

});