from odoo import models, fields, api

class OwlDashboard(models.TransientModel):
    _name = 'owl.dashboard'
    _description = 'Tablero OWL de Compras y Ventas'

    @api.model
    def get_dashboard_data(self):

        # --- VENTAS ---
        ventas = self.env['sale.order'].search([
            ('state', 'in', ['sale', 'done'])
        ])

        total_ventas = sum(orden.amount_total for orden in ventas)

        registros_ventas = [{
            'id': orden.id,
            'nombre': orden.name or '',
            'cliente': orden.partner_id.name or '',
            'total': orden.amount_total or 0,
            'fecha': str(orden.date_order) or '',
            'estado': orden.state or '',
        } for orden in ventas]

        # --- COMPRAS ---
        compras = self.env['purchase.order'].search([
            ('state', 'in', ['purchase', 'done'])
        ])

        total_compras = sum(orden.amount_total for orden in compras)

        registros_compras = [{
            'id': orden.id,
            'nombre': orden.name or '',
            'proveedor': orden.partner_id.name or '',
            'total': orden.amount_total or 0,
            'fecha': str(orden.date_order) or '',
            'estado': orden.state or '',
        } for orden in compras]

        # --- RESULTADO ---
        return {
            'total_ventas': total_ventas,
            'total_compras': total_compras,
            'ganancia': total_ventas - total_compras,
            'registros_ventas': registros_ventas,
            'registros_compras': registros_compras,
        }