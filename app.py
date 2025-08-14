import pandas as pd
import dash
from dash import dcc, html, Input, Output

# Crear DataFrame con tus datos
datos = [
    ("1840", "QUITO"),
    ("400", "AMBATO"),
    ("96", "SANTO DOMINGO"),
    ("554", "ESMERALDAS"),
    ("751", "IBARRA"),
    ("n/a", "MANABÍ"),
]

df = pd.DataFrame(datos, columns=["Graduados", "SEDES"])

# Convertir a numérico (los 'n/a' se convierten en NaN)
df["Graduados"] = pd.to_numeric(df["Graduados"], errors="coerce")

# App
app = dash.Dash(__name__)

app.layout = html.Div([
    # Dropdown para seleccionar sede
    dcc.Dropdown(
        id="selector-sedes",
        options=[{"label": sede, "value": sede} for sede in df["SEDES"]],
        value=df["SEDES"].iloc[0],  # Valor por defecto
        clearable=False
    ),
    
    # Display para mostrar el número de graduados
    html.Div(id="graduados-numero", style={
        "fontSize": "24px",
        "marginTop": "20px",
        "padding": "15px",
        "backgroundColor": "#f0f0f0",
        "borderRadius": "8px"
    })
])

# Callback para actualizar el número de graduados
@app.callback(
    Output("graduados-numero", "children"),
    Input("selector-sedes", "value")
)
def actualizar_numero_graduados(sede_seleccionada):
    # Filtrar por sede seleccionada
    resultado = df[df["SEDES"] == sede_seleccionada]["Graduados"].iloc[0]
    
    # Formatear el resultado
    if pd.isna(resultado):
        return f"No hay datos disponibles de graduados para {sede_seleccionada}"
    else:
        return html.Div([
            html.H3(f"Sede: {sede_seleccionada}"),
            html.P(f"Total de graduados: {int(resultado):,}", style={
                "fontSize": "32px",
                "color": "#1e3a8a",
                "fontWeight": "bold"
            })
        ])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8050))
    app.run(host='0.0.0.0', port=port, debug=True)