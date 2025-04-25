from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
from read_sql import media_salario_cargo, qtd_funcionarios, qtd_produtos, maiores_fabricantes, qtd_fretes

app = Dash(external_stylesheets=[dbc.themes.SLATE])

fig1 = px.bar(media_salario_cargo, x="cargo", y="media de salario", title="media salarial por cargo", width=500, height=300, template="plotly_dark")

fig1.update_layout(
   plot_bgcolor="rgb(89,89,89,0.2)",
   paper_bgcolor="rgb(89,89,89,0.2)"
  )

fig1.update_traces(
   marker_color="#1723e2"
  )

fig2 = px.pie(qtd_fretes, names="transportadora", values="qtd de fretes", title="transportadora VS qtd fretes", template="plotly_dark")

fig2.update_layout(
   plot_bgcolor="rgb(89,89,89,0.2)",
   paper_bgcolor="rgb(89,89,89,0.2)"
  )

fig2.update_traces(
   marker=dict(colors=["#1723e2", "#9407ae", "#ae073a"])
  )

fig3 = px.bar(maiores_fabricantes, x="qtd_fabricacoes", y="fabricante", title="maiores fabricantes", orientation='h', template="plotly_dark")

fig3.update_layout(
   plot_bgcolor="rgb(89,89,89,0.2)",
   paper_bgcolor="rgb(89,89,89,0.2)"
  )

fig3.update_traces(
   marker_color="#1723e2"
  )

app.layout = dbc.Container([
   html.H1("Dashboard", style={"text-align":"center", "font-weight":"bold", "margin-bottom":"1rem"}),
   
   dbc.Row([
     dbc.Col([
       dcc.Graph(
         id="fig1",
         figure=fig1
         )
       ], style={"margin-left":"1rem", "margin-right":"4rem"}),
     
     dbc.Col([
       dbc.Card([
         dbc.CardBody([
           html.H4("Quantidade De Funcionarios"),
           html.H3(f"{qtd_funcionarios}")
           ])
         ], style={"margin-top":"0.3rem", "width":"20rem", "text-align":"center", "height":"8rem"}),
         
       dbc.Card([
         dbc.CardBody([
           html.H4("Quantidade De Produtos"),
           html.H3(f"{qtd_produtos}")
           ])
         ], style={"margin-top":"2rem", "width":"20rem", "text-align":"center", "height":"8rem"}),
       ])
     ]),
  
   dbc.Row([
      dbc.Col([
        dcc.Graph(
           id="graf2",
           figure=fig2
          )
        ]),
      
      dbc.Col([
        dcc.Graph(
           id="graf3",
           figure=fig3
          )
        ])
     ], style={"margin-top":"1.5rem"})
  ], fluid=True)
  
if __name__ == "__main__":
  app.run(debug=True)
