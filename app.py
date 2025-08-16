import pandas as pd
import dash
from dash import dcc, html, Input, Output
import os

# Crear DataFrames con tus datos
datos_graduados = [
    ("1840", "QUITO"),
    ("400", "AMBATO"),
    ("96", "SANTO DOMINGO"),
    ("554", "ESMERALDAS"),
    ("751", "IBARRA"),
    ("n/a", "MANABÍ"),
]

datos_empleo = [
    ("Ambato", "Aún no consigo empleo desde mi graduación", "57"),
    ("Ambato", "Me tomó hasta 12 meses (un año) conseguir empleo", "31"),
    ("Ambato", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "8"),
    ("Ambato", "Me tomó hasta 24 meses (dos años) conseguir empleo", "3"),
    ("Ambato", "Me tomó hasta 6 meses conseguir empleo", "59"),
    ("Ambato", "Ya contaba con un empleo al momento de mi graduación", "164"),
    ("Esmeraldas", "Aún no consigo empleo desde mi graduación", "23"),
    ("Esmeraldas", "Me tomó hasta 12 meses (un año) conseguir empleo", "4"),
    ("Esmeraldas", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "2"),
    ("Esmeraldas", "Me tomó hasta 24 meses (dos años) conseguir empleo", "1"),
    ("Esmeraldas", "Me tomó hasta 6 meses conseguir empleo", "5"),
    ("Esmeraldas", "Ya contaba con un empleo al momento de mi graduación", "18"),
    ("Ibarra", "Aún no consigo empleo desde mi graduación", "53"),
    ("Ibarra", "Me tomó hasta 12 meses (un año) conseguir empleo", "26"),
    ("Ibarra", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "9"),
    ("Ibarra", "Me tomó hasta 24 meses (dos años) conseguir empleo", "1"),
    ("Ibarra", "Me tomó hasta 6 meses conseguir empleo", "41"),
    ("Ibarra", "Ya contaba con un empleo al momento de mi graduación", "95"),
    ("Quito", "Aún no consigo empleo desde mi graduación", "185"),
    ("Quito", "Me tomó hasta 12 meses (un año) conseguir empleo", "74"),
    ("Quito", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "21"),
    ("Quito", "Me tomó hasta 24 meses (dos años) conseguir empleo", "10"),
    ("Quito", "Me tomó hasta 6 meses conseguir empleo", "185"),
    ("Quito", "Ya contaba con un empleo al momento de mi graduación", "433"),
    ("Santo Domingo", "Aún no consigo empleo desde mi graduación", "29"),
    ("Santo Domingo", "Me tomó hasta 12 meses (un año) conseguir empleo", "7"),
    ("Santo Domingo", "Me tomó hasta 6 meses conseguir empleo", "15"),
    ("Santo Domingo", "Ya contaba con un empleo al momento de mi graduación", "22"),
    ("Manabí", "Aún no consigo empleo desde mi graduación", "38"),
    ("Manabí", "Me tomó hasta 12 meses (un año) conseguir empleo", "22"),
    ("Manabí", "Me tomó hasta 18 meses (un año y medio) conseguir empleo", "6"),
    ("Manabí", "Me tomó hasta 6 meses conseguir empleo", "36"),
    ("Manabí", "Ya contaba con un empleo al momento de mi graduación", "112"),
    ("Total general", "", "1795"),
]

# Crear DataFrames
df_graduados = pd.DataFrame(datos_graduados, columns=["Graduados", "SEDES"])
df_empleo = pd.DataFrame(datos_empleo, columns=["SEDES", "Conseguir empleo", "Participantes"])

# Convertir a numérico
df_graduados["Graduados"] = pd.to_numeric(df_graduados["Graduados"], errors="coerce")
df_empleo["Participantes"] = pd.to_numeric(df_empleo["Participantes"], errors="coerce")

# Obtener lista de sedes únicas (excluyendo "Total general")
sedes_disponibles = df_empleo[df_empleo["SEDES"] != "Total general"]["SEDES"].unique()

# App
app = dash.Dash(__name__)

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
    
    # Dropdown para seleccionar sede
    html.Div([
        html.Label("Seleccionar Sede:", style={
            "fontWeight": "bold",
            "marginRight": "10px"
        }),
        dcc.Dropdown(
            id="selector-sedes",
            options=[{"label": sede, "value": sede} for sede in sedes_disponibles],
            value=sedes_disponibles[0],  # Valor por defecto
            clearable=False,
            style={"width": "300px"}
        )
    ], style={"marginBottom": "30px"}),
    
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

# Callback para actualizar el número de graduados
@app.callback(
    Output("graduados-numero", "children"),
    Input("selector-sedes", "value")
)
def actualizar_numero_graduados(sede_seleccionada):
    # Normalizar nombres para coincidir (ej: "Ambato" vs "AMBATO")
    sede_normalizada = sede_seleccionada.upper()
    
    # Buscar en el DataFrame de graduados
    resultado = None
    for sede in df_graduados["SEDES"]:
        if sede_normalizada in sede:
            resultado = df_graduados[df_graduados["SEDES"] == sede]["Graduados"].iloc[0]
            break
    
    # Formatear el resultado
    if resultado is None or pd.isna(resultado):
        return html.Div([
            html.H3(f"Sede: {sede_seleccionada}"),
            html.P("No hay datos disponibles de graduados", style={
                "fontSize": "24px",
                "color": "#dc2626",
                "fontWeight": "bold"
            })
        ])
    else:
        return html.Div([
            html.H3(f"Sede: {sede_seleccionada}"),
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
    Input("selector-sedes", "value")
)
def actualizar_tabla_empleo(sede_seleccionada):
    # Filtrar datos de empleo por sede seleccionada
    df_filtrado = df_empleo[df_empleo["SEDES"] == sede_seleccionada].copy()
    
    # Calcular porcentajes si hay datos
    if not df_filtrado.empty:
        total_participantes = df_filtrado["Participantes"].sum()
        if total_participantes > 0:
            df_filtrado["Porcentaje"] = (df_filtrado["Participantes"] / total_participantes * 100).round(1)
        else:
            df_filtrado["Porcentaje"] = 0.0
    
    # Crear tabla
    if df_filtrado.empty:
        return html.Div("No hay datos disponibles para esta sede", style={
            "textAlign": "center",
            "padding": "20px",
            "color": "#dc2626"
        })
    else:
        return html.Table(
            # Encabezados de tabla
            [html.Tr([
                html.Th("Situación Laboral", style={"padding": "10px 15px", "textAlign": "left"}),
                html.Th("Participantes", style={"padding": "10px 15px", "textAlign": "right"}),
                html.Th("Porcentaje", style={"padding": "10px 15px", "textAlign": "right"})
            ])] +
            # Filas de datos
            [html.Tr([
                html.Td(row["Conseguir empleo"], style={"padding": "10px 15px", "borderBottom": "1px solid #e5e7eb"}),
                html.Td(f"{int(row['Participantes']):,}", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb"}),
                html.Td(f"{row['Porcentaje']:.1f}%", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb"})
            ]) for _, row in df_filtrado.iterrows()],
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