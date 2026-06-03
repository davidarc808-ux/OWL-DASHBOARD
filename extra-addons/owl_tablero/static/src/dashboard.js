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
            total_compras: 0,
            ganancia: 0,
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
        this.state.total_compras = datos.total_compras;
        this.state.ganancia = datos.ganancia;
        this.state.registros_ventas = datos.registros_ventas;
        this.state.registros_compras = datos.registros_compras;
    }
}

registry.category("actions").add("owl_tablero", OwlDashboard);