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
	qte_6_titre = fields.Char( string="Palier 6")
	qte_7_titre = fields.Char( string="Palier 7")
	qte_8_titre = fields.Char( string="Palier 8")
	
	qte_1 = fields.Char( string="Prix 1")
	qte_2 = fields.Char( string="Prix 2")
	qte_3 = fields.Char( string="Prix 3")
	qte_4 = fields.Char( string="Prix 4")
	qte_5 = fields.Char( string="Prix 5")
	qte_6 = fields.Char( string="Prix 6")
	qte_7 = fields.Char( string="Prix 7")
	qte_8 = fields.Char( string="Prix 8")

class ProductTemplate(models.Model):
	_inherit = 'product.template'

	qte_1_titre = fields.Char( string="Palier 1", related='product_variant_ids.qte_1_titre')
	qte_2_titre = fields.Char( string="Palier 2", related='product_variant_ids.qte_2_titre')
	qte_3_titre = fields.Char( string="Palier 3", related='product_variant_ids.qte_3_titre')
	qte_4_titre = fields.Char( string="Palier 4", related='product_variant_ids.qte_4_titre')
	qte_5_titre = fields.Char( string="Palier 5", related='product_variant_ids.qte_5_titre')
	qte_6_titre = fields.Char( string="Palier 6", related='product_variant_ids.qte_6_titre')
	qte_7_titre = fields.Char( string="Palier 7", related='product_variant_ids.qte_7_titre')
	qte_8_titre = fields.Char( string="Palier 8", related='product_variant_ids.qte_8_titre')
	
	qte_1 = fields.Char( string="Prix 1", related='product_variant_ids.qte_1')
	qte_2 = fields.Char( string="Prix 2", related='product_variant_ids.qte_2')
	qte_3 = fields.Char( string="Prix 3", related='product_variant_ids.qte_3')
	qte_4 = fields.Char( string="Prix 4", related='product_variant_ids.qte_4')
	qte_5 = fields.Char( string="Prix 5", related='product_variant_ids.qte_5')
	qte_6 = fields.Char( string="Prix 6", related='product_variant_ids.qte_6')
	qte_7 = fields.Char( string="Prix 7", related='product_variant_ids.qte_7')
	qte_8 = fields.Char( string="Prix 8", related='product_variant_ids.qte_8')

class ProductPublicCategory(models.Model):
	_inherit = 'product.public.category'

	tblCatQte1	= fields.Char( string="Titre qte 1")
	tblCatQte2	= fields.Char( string="Titre qte 2")
	tblCatQte3	= fields.Char( string="Titre qte 3")
	tblCatQte4	= fields.Char( string="Titre qte 4")
	tblCatQte5	= fields.Char( string="Titre qte 5")
	tblCatQte6	= fields.Char( string="Titre qte 6")
	tblCatQte7	= fields.Char( string="Titre qte 7")
	tblCatQte8  = fields.Char( string="Titre qte 8")
	tblCatRem	= fields.Char( string="Remarque")
	tblCatPrix	= fields.Char( string="Tarif")
	tblCatLivraison	 = fields.Char( string="Livraison")
	tblCatCondition	 = fields.Char( string="Condition")
	tblCatDelai	 = fields.Char( string="Délai")
	tblCatCont1	 = fields.Char( string="Contenu 1")
	tblCatCont2  = fields.Char( string="Contenu 2")
	tblCatCont3  = fields.Char( string="Contenu 3")
	tblCatCol1	= fields.Char( string="Titre col 1")
	tblCatCol2	= fields.Char( string="Titre col 2")
	tblCatCol3	= fields.Char( string="Titre col 3")
	tblCatCol4	= fields.Char( string="Titre col 4")
	tblCatCol5  = fields.Char( string="Titre col 5")


