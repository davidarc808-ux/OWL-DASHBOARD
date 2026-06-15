/** @odoo-module **/

import { Component, useState, onWillStart } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

class OwlDashboard extends Component {
    static template = "owl_tablero.OwlDashboard";

    setup() {
        this.orm = useService("orm");

        this.state = useState({
            total_ventas: 0,
            num_ventas: 0,
            ultima_venta: '',
            total_compras: 0,
            num_compras: 0,
            ultima_compra: '',
            ganancia: 0,
            estado_ganancia: 'positivo',
            registros_ventas: [],
            registros_compras: [],
        });

        onWillStart(async () => {
            await this.cargarDatos();
        });
    }

    async cargarDatos() {
        const datos = await this.orm.call(
            "owl.dashboard",
            "get_dashboard_data",
            [],
            {}
        );

        this.state.total_ventas = datos.total_ventas;
        this.state.num_ventas = datos.num_ventas;
        this.state.ultima_venta = datos.ultima_venta;
        this.state.total_compras = datos.total_compras;
        this.state.num_compras = datos.num_compras;
        this.state.ultima_compra = datos.ultima_compra;
        this.state.ganancia = datos.ganancia;
        this.state.estado_ganancia = datos.estado_ganancia;
        this.state.registros_ventas = datos.registros_ventas;
        this.state.registros_compras = datos.registros_compras;
    }

    formatMoney(amount) {
        return new Intl.NumberFormat('es-MX', {
            style: 'currency',
            currency: 'MXN',
        }).format(amount);
    }
}

registry.category("actions").add("owl_tablero", OwlDashboard);