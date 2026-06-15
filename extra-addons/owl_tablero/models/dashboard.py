from odoo import models, fields, api

class OwlDashboard(models.TransientModel):
    _name = 'owl.dashboard'
    _description = 'Tablero OWL de Compras y Ventas'

    @api.model
    def get_dashboard_data(self):

        ventas = self.env['sale.order'].search([
            ('state', 'in', ['sale', 'done'])
        ])

        total_ventas = sum(orden.amount_total for orden in ventas)
        num_ventas = len(ventas)
        ultima_venta = ventas[0].name if ventas else 'Sin órdenes'

        registros_ventas = [{
            'id': orden.id,
            'nombre': orden.name or '',
            'cliente': orden.partner_id.name or '',
            'total': orden.amount_total or 0,
            'fecha': str(orden.date_order) or '',
            'estado': orden.state or '',
        } for orden in ventas]

        compras = self.env['purchase.order'].search([
            ('state', 'in', ['purchase', 'done'])
        ])

        total_compras = sum(orden.amount_total for orden in compras)
        num_compras = len(compras)
        ultima_compra = compras[0].name if compras else 'Sin órdenes'

        registros_compras = [{
            'id': orden.id,
            'nombre': orden.name or '',
            'proveedor': orden.partner_id.name or '',
            'total': orden.amount_total or 0,
            'fecha': str(orden.date_order) or '',
            'estado': orden.state or '',
        } for orden in compras]

        ganancia = total_ventas - total_compras

        return {
            'total_ventas': total_ventas,
            'num_ventas': num_ventas,
            'ultima_venta': ultima_venta,
            'total_compras': total_compras,
            'num_compras': num_compras,
            'ultima_compra': ultima_compra,
            'ganancia': ganancia,
            'estado_ganancia': 'positivo' if ganancia >= 0 else 'negativo',
            'registros_ventas': registros_ventas,
            'registros_compras': registros_compras,
        }