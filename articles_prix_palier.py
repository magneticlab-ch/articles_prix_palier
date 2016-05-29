# -*- coding: utf-8 -*-
from openerp import models, fields
from openerp import api

class ProductProduct(models.Model):
	_inherit = 'product.product'

	qte_1_titre = fields.Char( string="Palier 1")
	qte_2_titre = fields.Char( string="Palier 2")
	qte_3_titre = fields.Char( string="Palier 3")
	qte_4_titre = fields.Char( string="Palier 4")
	qte_5_titre = fields.Char( string="Palier 5")
	
	qte_1 = fields.Char( string="Prix 1")
	qte_2 = fields.Char( string="Prix 2")
	qte_3 = fields.Char( string="Prix 3")
	qte_4 = fields.Char( string="Prix 4")
	qte_5 = fields.Char( string="Prix 5")

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	qte_1_titre = fields.Char( string="Palier 1", related='product_variant_ids.qte_1_titre')
	qte_2_titre = fields.Char( string="Palier 2", related='product_variant_ids.qte_2_titre')
	qte_3_titre = fields.Char( string="Palier 3", related='product_variant_ids.qte_3_titre')
	qte_4_titre = fields.Char( string="Palier 4", related='product_variant_ids.qte_4_titre')
	qte_5_titre = fields.Char( string="Palier 5", related='product_variant_ids.qte_5_titre')
	
	qte_1 = fields.Char( string="Prix 1", related='product_variant_ids.qte_1')
	qte_2 = fields.Char( string="Prix 2", related='product_variant_ids.qte_2')
	qte_3 = fields.Char( string="Prix 3", related='product_variant_ids.qte_3')
	qte_4 = fields.Char( string="Prix 4", related='product_variant_ids.qte_4')
	qte_5 = fields.Char( string="Prix 5", related='product_variant_ids.qte_5')