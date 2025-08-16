import pandas as pd
import dash
from dash import dcc, html, Input, Output, State
import os

# [TODOS LOS DATOS PERMANECEN IGUALES HASTA EL FINAL DE datos_sector]

# Crear DataFrames con la columna de año
df_graduados = pd.DataFrame(datos_graduados, columns=["Año", "SEDES", "Graduados"])
df_empleo = pd.DataFrame(datos_empleo, columns=["Año", "SEDES", "Conseguir empleo", "Participantes"])
df_situacion = pd.DataFrame(datos_situacion, columns=["Año", "SEDES", "Situación laboral", "Participantes"])
df_sector = pd.DataFrame(datos_sector, columns=["Año", "SEDES", "Sector", "Participantes"])  # Nuevo DataFrame

# Convertir a numérico
df_graduados["Graduados"] = pd.to_numeric(df_graduados["Graduados"], errors="coerce")
df_empleo["Participantes"] = pd.to_numeric(df_empleo["Participantes"], errors="coerce")
df_situacion["Participantes"] = pd.to_numeric(df_situacion["Participantes"], errors="coerce")
df_sector["Participantes"] = pd.to_numeric(df_sector["Participantes"], errors="coerce")  # Nuevo

# Obtener listas únicas para los dropdowns
años_disponibles = sorted(df_graduados["Año"].unique().tolist())
sedes_disponibles = sorted([s for s in df_empleo["SEDES"].unique().tolist() if s != "Nacional"], key=lambda x: x.lower())
sedes_disponibles_con_nacional = sedes_disponibles + ["Nacional"]

# App
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(style={
    "fontFamily": "Arial, sans-serif",
    "padding": "20px",
    "maxWidth": "1400px",  # Aumentado para acomodar 3 tablas
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
    
    # Contenedor para las tres tablas (lado a lado)
    html.Div(style={
        "display": "flex",
        "gap": "20px",
        "marginBottom": "30px",
        "flexWrap": "wrap"
    }, children=[
        # Tabla para mostrar los datos de empleo
        html.Div(style={"flex": "1", "minWidth": "350px"}, children=[
            html.H2("Tiempo para Conseguir Empleo", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"  # Reducido para caber en 3 columnas
            }),
            html.Div(id="tabla-empleo")
        ]),
        
        # Tabla para mostrar la situación laboral
        html.Div(style={"flex": "1", "minWidth": "350px"}, children=[
            html.H2("Situación Laboral Actual", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"  # Reducido para caber en 3 columnas
            }),
            html.Div(id="tabla-situacion")
        ]),
        
        # Nueva tabla para mostrar el sector laboral
        html.Div(style={"flex": "1", "minWidth": "350px"}, children=[
            html.H2("Sector Laboral", style={
                "textAlign": "center",
                "color": "#1e3a8a",
                "marginBottom": "20px",
                "fontSize": "20px"  # Reducido para caber en 3 columnas
            }),
            html.Div(id="tabla-sector")
        ])
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
        # Crear encabezado
        encabezado = html.Tr([
            html.Th("Consiguió empleo", style={"padding": "10px 15px", "textAlign": "left", "fontSize": "14px"}),
            html.Th("Participantes", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"}),
            html.Th("Porcentaje", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"})
        ])
        
        # Crear filas de datos
        filas = []
        for _, row in df_filtrado.iterrows():
            filas.append(html.Tr([
                html.Td(row["Conseguir empleo"], style={"padding": "10px 15px", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"}),
                html.Td(f"{int(row['Participantes']):,}", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"}),
                html.Td(f"{row['Porcentaje']:.1f}%", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"})
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

# Callback para actualizar la tabla de situación laboral
@app.callback(
    Output("tabla-situacion", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_tabla_situacion(anio_seleccionado, sede_seleccionada):
    # Filtrar datos de situación laboral por año y sede
    df_filtrado = df_situacion[
        (df_situacion["Año"] == anio_seleccionado) & 
        (df_situacion["SEDES"] == sede_seleccionada)
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
        # Crear encabezado
        encabezado = html.Tr([
            html.Th("Situación Laboral", style={"padding": "10px 15px", "textAlign": "left", "fontSize": "14px"}),
            html.Th("Participantes", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"}),
            html.Th("Porcentaje", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"})
        ])
        
        # Crear filas de datos
        filas = []
        for _, row in df_filtrado.iterrows():
            filas.append(html.Tr([
                html.Td(row["Situación laboral"], style={"padding": "10px 15px", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"}),
                html.Td(f"{int(row['Participantes']):,}", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"}),
                html.Td(f"{row['Porcentaje']:.1f}%", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"})
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

# Nuevo callback para actualizar la tabla de sector laboral
@app.callback(
    Output("tabla-sector", "children"),
    [Input("selector-anio", "value"),
     Input("selector-sedes", "value")]
)
def actualizar_tabla_sector(anio_seleccionado, sede_seleccionada):
    # Filtrar datos de sector por año y sede
    df_filtrado = df_sector[
        (df_sector["Año"] == anio_seleccionado) & 
        (df_sector["SEDES"] == sede_seleccionada)
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
        # Crear encabezado
        encabezado = html.Tr([
            html.Th("Sector Laboral", style={"padding": "10px 15px", "textAlign": "left", "fontSize": "14px"}),
            html.Th("Participantes", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"}),
            html.Th("Porcentaje", style={"padding": "10px 15px", "textAlign": "right", "fontSize": "14px"})
        ])
        
        # Crear filas de datos
        filas = []
        for _, row in df_filtrado.iterrows():
            filas.append(html.Tr([
                html.Td(row["Sector"], style={"padding": "10px 15px", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"}),
                html.Td(f"{int(row['Participantes']):,}", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"}),
                html.Td(f"{row['Porcentaje']:.1f}%", style={"padding": "10px 15px", "textAlign": "right", "borderBottom": "1px solid #e5e7eb", "fontSize": "14px"})
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