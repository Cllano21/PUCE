import pandas as pd
import dash
from dash import dcc, html, Input, Output, State
import os

# Crear DataFrames con tus datos
datos_graduados = [
    ("2023", "Quito", "4014"),
    ("2023", "Ambato", "576"),
    ("2023", "Santo Domingo", "405"),
    ("2023", "Esmeraldas", "569"),
    ("2023", "Ibarra", "963"),
    ("2023", "Manabí", "924"),
    ("2023", "Nacional", "7451"),
]

datos_empleo = [
    ("2023", "Ambato", "Aún no consigo empleo desde mi graduación", "57"),
    ("2023", "Ambato", "Me tomó hasta 12 meses (un año) conseguir empleo", "31"),
    ("2023", "Ambato", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "8"),
    ("2023", "Ambato", "Me tomó hasta 24 meses (dos años) conseguir empleo", "3"),
    ("2023", "Ambato", "Me tomó hasta 6 meses conseguir empleo", "59"),
    ("2023", "Ambato", "Ya contaba con un empleo al momento de mi graduación", "164"),
    ("2023", "Esmeraldas", "Aún no consigo empleo desde mi graduación", "23"),
    ("2023", "Esmeraldas", "Me tomó hasta 12 meses (un año) conseguir empleo", "4"),
    ("2023", "Esmeraldas", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "2"),
    ("2023", "Esmeraldas", "Me tomó hasta 24 meses (dos años) conseguir empleo", "1"),
    ("2023", "Esmeraldas", "Me tomó hasta 6 meses conseguir empleo", "5"),
    ("2023", "Esmeraldas", "Ya contaba con un empleo al momento de mi graduación", "18"),
    ("2023", "Ibarra", "Aún no consigo empleo desde mi graduación", "53"),
    ("2023", "Ibarra", "Me tomó hasta 12 meses (un año) conseguir empleo", "26"),
    ("2023", "Ibarra", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "9"),
    ("2023", "Ibarra", "Me tomó hasta 24 meses (dos años) conseguir empleo", "1"),
    ("2023", "Ibarra", "Me tomó hasta 6 meses conseguir empleo", "41"),
    ("2023", "Ibarra", "Ya contaba con un empleo al momento de mi graduación", "95"),
    ("2023", "Quito", "Aún no consigo empleo desde mi graduación", "185"),
    ("2023", "Quito", "Me tomó hasta 12 meses (un año) conseguir empleo", "74"),
    ("2023", "Quito", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "21"),
    ("2023", "Quito", "Me tomó hasta 24 meses (dos años) conseguir empleo", "10"),
    ("2023", "Quito", "Me tomó hasta 6 meses conseguir empleo", "185"),
    ("2023", "Quito", "Ya contaba con un empleo al momento de mi graduación", "433"),
    ("2023", "Santo Domingo", "Aún no consigo empleo desde mi graduación", "29"),
    ("2023", "Santo Domingo", "Me tomó hasta 12 meses (un año) conseguir empleo", "7"),
    ("2023", "Santo Domingo", "Me tomó hasta 6 meses conseguir empleo", "15"),
    ("2023", "Santo Domingo", "Ya contaba con un empleo al momento de mi graduación", "22"),
    ("2023", "Manabí", "Aún no consigo empleo desde mi graduación", "38"),
    ("2023", "Manabí", "Me tomó hasta 12 meses (un año) conseguir empleo", "22"),
    ("2023", "Manabí", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "6"),
    ("2023", "Manabí", "Me tomó hasta 6 meses conseguir empleo", "36"),
    ("2023", "Manabí", "Ya contaba con un empleo al momento de mi graduación", "112"),
    ("2023", "Nacional", "Aún no consigo empleo desde mi graduación", "385"),
    ("2023", "Nacional", "Me tomó hasta 12 meses (un año) conseguir empleo", "164"),
    ("2023", "Nacional", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "46"),
    ("2023", "Nacional", "Me tomó hasta 24 meses (dos años) conseguir empleo", "15"),
    ("2023", "Nacional", "Me tomó hasta 6 meses conseguir empleo", "341"),
    ("2023", "Nacional", "Ya contaba con un empleo al momento de mi graduación", "844"),
]

# Crear DataFrames con la columna de año
df_graduados = pd.DataFrame(datos_graduados, columns=["Año", "SEDES", "Graduados"])
df_empleo = pd.DataFrame(datos_empleo, columns=["Año", "SEDES", "Conseguir empleo", "Participantes"])

# Convertir a numérico
df_graduados["Graduados"] = pd.to_numeric(df_graduados["Graduados"], errors="coerce")
df_empleo["Participantes"] = pd.to_numeric(df_empleo["Participantes"], errors="coerce")

# Obtener listas únicas para los dropdowns
años_disponibles = sorted(df_graduados["Año"].unique().tolist())
sedes_disponibles = sorted([s for s in df_empleo["SEDES"].unique().tolist() if s != "Nacional"], key=lambda x: x.lower())
sedes_disponibles_con_nacional = sedes_disponibles + ["Nacional"]

# App
app = dash.Dash(__name__)
server = app.server  # Necesario para despliegue en servidores como Heroku

app.layout = html.Div(style={
    "fontFamily": "Arial, sans-serif",
    "padding": "20px",
    "maxWidth": "1200px",
    "margin": "0 auto",
    "backgroundColor": "#f8f9fa"
}, children=[
    # Título
    html.H1("Análisis de Graduados y Empleo", style={
        "textAlign": "center",
        "color": "#1e3a8a",
        "marginBottom": "30px"
    }),
    
    # Controles de filtro
    html.Div(style={
        "display": "flex",
        "flexWrap": "wrap",
        "gap": "20px",
        "marginBottom": "30px",
        "alignItems": "flex-end"
    }, children=[
        # Dropdown para seleccionar año
        html.Div(style={"flex": "1", "minWidth": "200px"}, children=[
            html.Label("Seleccionar Año:", style={"fontWeight": "bold", "marginBottom": "5px"}),
            dcc.Dropdown(
                id="selector-anio",
                options=[{"label": año, "value": año} for año in años_disponibles],
                value=años_disponibles[0] if años_disponibles else None,
                clearable=False
            )
        ]),
        
        # Dropdown para seleccionar sede
        html.Div(style={"flex": "2", "minWidth": "250px"}, children=[
            html.Label("Seleccionar Sede:", style={"fontWeight": "bold", "marginBottom": "5px"}),
            dcc.Dropdown(
                id="selector-sedes",
                options=[{"label": sede, "value": sede} for sede in sedes_disponibles],
                value=sedes_disponibles[0] if sedes_disponibles else None,
                clearable=False
            )
        ]),
        
        # Botón para mostrar datos nacionales
        html.Div(style={"flex": "1", "minWidth": "150px"}, children=[
            html.Label("Vista Nacional:", style={"fontWeight": "bold", "marginBottom": "5px"}),
            html.Button(
                "Ver Nacional",
                id="boton-nacional",
                n_clicks=0,
                style={
                    "width": "100%",
                    "padding": "10px",
                    "backgroundColor": "#1e3a8a",
                    "color": "white",
                    "border": "none",
                    "borderRadius": "4px",
                    "cursor": "pointer",
                    "fontWeight": "bold"
                }
            )
        ])
    ]),
    
    # Tarjeta para mostrar el número de graduados
    html.Div(id="graduados-numero", style={
        "padding": "20px",
        "backgroundColor": "white",
        "borderRadius": "8px",
        "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
        "marginBottom": "30px",
        "textAlign": "center"
    }),
    
    # Tabla para mostrar los datos de empleo
    html.Div([
        html.H2("Tiempo para Conseguir Empleo", style={
            "textAlign": "center",
            "color": "#1e3a8a",
            "marginBottom": "20px"
        }),
        html.Div(id="tabla-empleo")
    ])
])

# Callback para manejar el botón "Nacional"
@app.callback(
    Output("selector-sedes", "value"),
    Input("boton-nacional", "n_clicks"),
    prevent_initial_call=True
)
def mostrar_datos_nacionales(n_clicks):
    return "Nacional"

# Callback para actualizar el número de graduados
@app.callback(
    Output("graduados-numero", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_numero_graduados(anio_seleccionado, sede_seleccionada):
    # Filtrar por año y sede
    df_filtrado = df_graduados[
        (df_graduados["Año"] == anio_seleccionado) & 
        (df_graduados["SEDES"] == sede_seleccionada)
    ]
    
    # Obtener el resultado
    if not df_filtrado.empty:
        resultado = df_filtrado["Graduados"].iloc[0]
    else:
        resultado = None
    
    # Formatear el resultado
    if resultado is None or pd.isna(resultado):
        return html.Div([
            html.H3(f"Sede: {sede_seleccionada} ({anio_seleccionado})"),
            html.P("No hay datos disponibles de graduados", style={
                "fontSize": "24px",
                "color": "#dc2626",
                "fontWeight": "bold"
            })
        ])
    else:
        return html.Div([
            html.H3(f"Sede: {sede_seleccionada} ({anio_seleccionado})"),
            html.P(f"Total de graduados: {int(resultado):,}", style={
                "fontSize": "32px",
                "color": "#1e3a8a",
                "fontWeight": "bold",
                "margin": "10px 0"
            }),
            html.Small("Datos de graduados disponibles", style={"color": "#4b5563"})
        ])

# Callback para actualizar la tabla de empleo
@app.callback(
    Output("tabla-empleo", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_tabla_empleo(anio_seleccionado, sede_seleccionada):
    # Filtrar datos de empleo por año y sede
    df_filtrado = df_empleo[
        (df_empleo["Año"] == anio_seleccionado) & 
        (df_empleo["SEDES"] == sede_seleccionada)
    ].copy()
    
    # Calcular porcentajes si hay datos
    if not df_filtrado.empty:
        total_participantes = df_filtrado["Participantes"].sum()
        if total_participantes > 0:
            df_filtrado["Porcentaje"] = (df_filtrado["Participantes"] / total_participantes * 100).round(1)
        else:
            df_filtrado["Porcentaje"] = 0.0
    
    # Crear tabla
    if df_filtrado.empty:
        return html.Div(f"No hay datos disponibles para {sede_seleccionada} en {anio_seleccionado}", style={
            "textAlign": "center",
            "padding": "20px",
            "color": "#dc2626"
        })
    else:
        # Crear encabezado con año y sede
        encabezado = html.Tr([
            html.Th("Situación Laboral", style={"padding": "10px 15px", "textAlign": "left"}),
            html.Th("Participantes", style={"padding": "10px 15px", "textAlign": "right"}),
            html.Th("Porcentaje", style={"padding": "10px 15px", "textAlign": "right"})
        ])
        
        # Crear filas de datos
        filas = []
        for _, row in df_filtrado.iterrows():
            filas.append(html.Tr([
                html.Td(row["Conseguir empleo"], style={"padding": "10px 15px", "borderBottom": "1px solid #e5e7eb"}),
                html.Td(f"{int(row['Participantes']):,}", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb"}),
                html.Td(f"{row['Porcentaje']:.1f}%", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb"})
            ]))
        
        # Crear tabla completa
        return html.Table(
            [encabezado] + filas,
            style={
                "width": "100%",
                "borderCollapse": "collapse",
                "backgroundColor": "white",
                "boxShadow": "0 4px 6px rgba(0,0,0,0.1)",
                "borderRadius": "8px",
                "overflow": "hidden"
            }
        )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run(host='0.0.0.0', port=port, debug=True)