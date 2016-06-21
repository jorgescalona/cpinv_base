# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
#
#   jorgescalona@riseup.net   @jorgemustaine  https://github.com/jorgescalona
#
##############################################################################
{
        "name" : "cpinv_base",
        "version" : "0.0.1",
        "author" : "jorgescalona @jorgemustaine",
        "website" : "http://www.attakatara.wordpress.com",
        "category" : "Desconocida",
        "description": """ modulo para el control de inventarios de civil proyect
                           adaptación al mes de Mayo de 2016 """,
        "depends" : ['base', 'l10n_ve_dpt'],
        "init_xml" : [ ],
        "demo_xml" : [ ],
        "update_xml" : ['views/cpinv_view.xml', 'security/ir.model.access.csv', 'security/security.xml'],
        "installable": True,
        #"data":['security/security.xml','security/ir.model.access.csv'],
}
