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
from openerp import api, fields, models

class cp_inventario(models.Model):
    """inventario de equipos, herramientas y consumibles de civil proyect"""
    _name = 'cp.inventario'
    _rec_name = 'codigo'
    codigo = fields.Char('codigo', size=10, required=True, help='codigo del equipo, consumible o herramienta')
    marca_id = fields.Many2one('cp.marca', 'Marca', help='marca del equipo, consumible o herramienta')
    serial = fields.Char('serial', size=15, help='serial del equipo consumible o herramienta')
    parte = fields.Char('nro de parte', size=20, help='numero de parte del fabricante')
    descripcion = fields.Char('descripcion', size=200, help='descripción del item')
    proveedor_id = fields.Many2one('cp.provee', 'Proveedor', help='carga al proveedor del equipo, consumible o material')
    status_id = fields.Many2one('cp.status.bien', 'Status', required=True, help='se puede referir a: en almacen, prestamo, en obra')
    ubicacion = fields.Char('ubicacion', size=30, required=True, help='ubicación geográfica del equipo, consumible o herramienta')
    fecha_compra = fields.Datetime('fecha de compra', help='indica la fecha de compra del bien cosumible o herramienta')


class cp_marca(models.Model):
    """guarda las marcas de los fabricantes de los bienes adquieridos por civil proyect"""
    _name = 'cp.marca'
    _rec_name = 'marca'
    marca = fields.Char('marca', size=20, help='marca del fabricante del equipo, consumible o herramienta')


class cp_status_bien(models.Model):
    """clase contenedora del estatus de los bienes de civil proyect"""
    _name = 'cp.status.bien'
    _rec_name = 'status'
    status = fields.Char('status', size=20, required=True, help='almacena el status del equipo, consumible o bien de civil proyect')


class cp_provee(models.Model):
    """agenda de proveedores de civil proyect"""
    _name = 'cp.provee'
    _rec_name = 'proveedor'
    proveedor = fields.Char('proveedor', size=30, required=True, help='persona natural o jurídica ')
    direccion = fields.Char('direccion', size=150, help='direccion geografica del proveedor ')
    estado_id = fields.Many2one('estado', 'Estado', help='entidad federal donde se ubica el despacho del proveedor')
    municipio_id = fields.Many2one('municipio', 'Municipio', help='municipio de la ubicacion geografica')
    parroquia_id = fields.Many2one('parroquia', 'Parroquia', help='parroquia de la ubicación geográfica')
    contacto = fields.Char('persona de contacto', size=25, help='nombre de la persona de contacto')
    tel_fijo = fields.Char('telefono fijo', size=15, help='telefono fijo del despacho del proveedor')
    tel_cel = fields.Char('telefono movil', size=15, help='telefono movil de la persona de contacto')
    tel_otro = fields.Char('telefono otro', size=15, help='otro telefono de contacto')
    pagweb = fields.Char('pagina web', size=30, help='sitio web del proveedor')
    otro = fields.Char('info', size=100, help='cualquier otro comentario sobre el proveedor')


class estado(models.Model):
    """Tabla de Referencia de Estados (Geografico)"""
    _name = 'estado'
    _rec_name = 'estado'
    codigo = fields.Char('Codigo',size=3,required='True', help='Codigo del Estado')
    estado = fields.Char('Estado',size=30,required='True', help='Nombre del Estado')


class municipio(models.Model):
    """Tabla de Referencia de Municipios (Geografico)"""
    _name = 'municipio'
    _rec_name = 'municipio'
    codigo = fields.Char('Codigo',size=3,required='True', help='Codigo del Municipio')
    municipio = fields.Char('Municipio',size=30,required='True', help='Nombre del Municipio')
    estado_id = fields.Many2one('estado','Estado', help='Estado al cual pertenece el Municipio')


class cp_parroquias(models.Model):
    """Tabla de Referencia de Parroquias (Geografico)"""
    _name = 'parroquia'
    _rec_name = 'parroquia'
    codigo = fields.Char('Codigo',size=3,required='True', help='Codigo de Identificacion de la Parroquia')
    parroquia = fields.Char('Parroquia',size=30,required='True', help='Nombre de la Parroquia')
    municipio_id = fields.Many2one('municipio','Municipio', help='Municipio al cual pertenece la Parroquia')





