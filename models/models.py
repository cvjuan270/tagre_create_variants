import logging
from odoo import models
_logger = logging.getLogger(__name__)


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def create_variant_ids_0(self, log_warning=False):
        self.ensure_one()
        # combination = self._get_first_possible_combination()
        product_products = self.env['product.product'].search([('product_tmpl_id', '=', self.id)])
        combinations = self.env['product.template.attribute.value'].search([('product_tmpl_id', '=', self.id)])
        # filtrar combinaciones que tengan product.atrubute igual a color
        combinations = combinations.filtered(lambda c: c.attribute_id.id == 6)
        combination_indices = [item.combination_indices for item in product_products]
        combination_indices = ','.join(combination_indices)
        combination_indices = combination_indices.split(',')
        for combination in combinations:
            Product = self.env['product.product']
            if str(combination.id) in combination_indices:
                continue
            product_variant = self._get_variant_for_combination(combination)
            if product_variant:
                if not product_variant.active and self.has_dynamic_attributes() and self._is_combination_possible(
                        combination):
                    product_variant.active = True
                # return product_variant
                continue

            if not self.has_dynamic_attributes():
                if log_warning:
                    _logger.warning('The user #%s tried to create a variant for the non-dynamic product %s.' % (
                        self.env.user.id, self.id))
                # return Product
                continue
            # if not self._is_combination_possible(combination):
            #     if log_warning:
            #         _logger.warning(
            #             'The user #%s tried to create an invalid variant for the product %s.' % (self.env.user.id, self.id))
            #     # return Product
            #     continue
            variant = Product.sudo().create({
                'product_tmpl_id': self.id,
                'product_template_attribute_value_ids': [(6, 0, combination._without_no_variant_attributes().ids)]
            })
            print(variant.id, '|', variant.name, '|', variant.product_template_attribute_value_ids.name)
