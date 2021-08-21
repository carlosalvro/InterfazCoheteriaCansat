import dash
import dash_core_components as dcc
import dash_html_components as html
import os

from dash_html_components.Button import Button
from dash_html_components.Div import Div
import functions


##### INICIAMOS LA APP #####
app = dash.Dash(__name__)

##### AQUI VA TODA LA ESTRUCTURA DE NUESTRA PAGINA 
app.layout= html.Div(
  #CONTENEDOR PRINCIPAL
  className="main-container",
  children=[
    # CABEZERA DONDE VA EL LOGO
    html.Div(
      className='header', children=[
        html.Img(src='./assets/Images/Kan-Horizontal.png', className='logo')
      ]
    ),
    # aqui va todo lo demás
    html.Section(
      className='main',
      children=[
        # iniciamos componente de los tabs (las pestañas para cambiar de métrica a imagen)
        dcc.Tabs(className='main-tabs',
                  value='tab-cohete',children=[
          # iniciamos el primer tab de metrica
          dcc.Tab(id='tab-cohete',
                  className='custom-tab',
                  selected_className='custom-tab--selected', 
                  label='Cohete', 
                  value='tab-cohete', children=[
                    ###Contenido del primer tab
####Este componente interval es muy importante, es el que nos da el tiempo de actualización de la página                    
                    #ES SU UNÍCO PROPOSITO (ES INVISIBLE, NO SE MOSTRARÁ NADA EN LA PÁGINA)
                    dcc.Interval(
                        id='interval-component',
                        interval=500, # milisegundos
                        n_intervals=0
                    ),
                    # aqui comienza el contenedor de metricas
                    html.Div(
                      className='tab-section',
                      children=[
                        #TITULO
                        html.H2('Cohete'),
                        #CONTENEDOR PRINCIPAL
                        html.Div(
                          className='principal-metrica-cohete',
                          children=[
                            # Sección BOTONES
                            html.Div(
                              className="card-1 co-buttons",
                              children = [
                                html.Button('Iniciar', className='start-button'),
                                html.Button('Detener', className='stop-button')
                              ]
                            ),
                            # Sección ALTITUD
                            html.Div(
                              className="card-1 co-time",
                              children = [
                                html.H4("Tiempo de Misión"),
                                html.H3("00:00"),
                              ]
                            ),
                            # Sección COORDENADAS
                            html.Div(
                              className=("card-2 co-coordenadas"),
                              children = [
                                html.H4("Coordenadas"),
                                html.Div(
                                  className="subcard-2 values-2",
                                  children = [
                                    html.H3("128.5"),
                                    html.H3("-103.9")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard-2 uds",
                                  children = [
                                    html.P("Latitud"),
                                    html.P("Longitud")
                                  ]
                                )
                              ]
                            ),
                            # Sección ACELEROMETRO
                            html.Div(
                              className=("card-3 co-position"),
                              children = [
                                html.H4("Posición"),
                                html.Div(
                                  className="subcard-3 values-3",
                                  children = [
                                    html.H3("128.5"),
                                    html.H3("-103.9"),
                                    html.H3("150.0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard-3 uds",
                                  children = [
                                    html.P("Eje X"),
                                    html.P("Eje Y"),
                                    html.P("Eje Z")
                                  ]
                                )
                              ]
                            ),
                            # EStados
                            html.Div(
                              className= "estados",
                              children = [
                                html.Div(
                                  className="estado",
                                  children=[
                                    html.Div(id="piro1"),
                                    html.H4("Carga Pirotecnica 1")
                                  ]
                                ),
                                html.Div(
                                  className="estado",
                                  children=[
                                    html.Div(id="piro2"),
                                    html.H4("Carga Pirotecnica 2")
                                  ]
                                ),
                                html.Div(
                                  className="estado",
                                  children=[
                                    html.Div(id="igni1"),
                                    html.H4("Carga de ignición 1")
                                  ]
                                ),
                                html.Div(
                                  className="estado",
                                  children=[
                                    html.Div(id="igni2"),
                                    html.H4("Carga de ignición 2")
                                  ]
                                ),
                                html.Div(
                                  className="estado",
                                  children=[
                                    html.Div(id="switch1"),
                                    html.H4("Switch 1")
                                  ]
                                ),
                                html.Div(
                                  className="estado",
                                  children=[
                                    html.Div(id="switch2"),
                                    html.H4("Switch 2")
                                  ]
                                ),
                                html.Div(
                                  className="estado",
                                  children=[
                                    html.Div(id="switch3"),
                                    html.H4("Switch 3")
                                  ]
                                ),
                              ]
                            ),
                            html.Div(className="card-1 nada"),
                            # Sección VELOCIDAD
                            html.Div(
                              className="card-1 velocidad",
                              children = [
                                html.H4("Velocidad"),
                                html.H3("30"),
                                html.P("m/s")
                              ]
                            ),
                            # Sección FECHA
                            html.Div(
                              className="card-1 fecha",
                              children = [
                                html.H4("20-08-2021"),
                                html.H4("17:43"),
                              ]
                            ),
                            # Sección GRAFICA
                            html.Div(
                              className="card-graph",
                              children= [
                                dcc.Tabs(
                                  className="tabs-subgraph",
                                  value="ac-gi-graph",
                                  children = [
                                    dcc.Tab( id="ac-gi-graph",
                                      className="custom-subtab",
                                      selected_className='custom-subtab--selected',
                                      label="Cansat",
                                      value="ac-gi-graph",
                                      children=[
                                        html.Div(
                                          className="graph-ace-giro-container",
                                          children=[
                                            dcc.Graph(
                                              figure=functions.plot_graphs_ace_giro()
                                            )
                                          ]
                                        )
                                      ]
                                    ),
                                    dcc.Tab(id="cansat-graph2",
                                      className="custom-subtab",
                                      selected_className='custom-subtab--selected',
                                      label="Cansat",
                                      value="cansat-graph",
                                      children=[
                                          html.Div(
                                          className="graph-cansat-container",
                                          children=[
                                            dcc.Graph(
                                              figure=functions.plot_cansat()
                                            )
                                          ]
                                        )
                                      ]
                                    )
                                  ]
                                )
                              ]
                            )
                          ]
                        )
                      ]
                    )
                  ]),
          #contenido del segundo tab de imagen 
          dcc.Tab(id='tab-image',
                  className='custom-tab', 
                  selected_className='custom-tab--selected',
                  label='Cansat', 
                  value='tab-image', children=[
                    ###Contenido del segundo tab
                    ## IMAGEN
                    html.Div(
                      className='tab-section',
                      children=[
                        # TITULO
                        html.H2('Cansat'),
                        # CONTENEDOR PRINCIPAL
                        html.Div(
                          className='principal-metrica-cansat',
                          children=[
                            # Sección ALTITUD
                            html.Div(
                              className="card-1 ca-altitud",
                              children = [
                                html.H4("Altitud"),
                                html.H3("120"),
                                html.P("metros")
                              ]
                            ),
                            # Sección COORDENADAS
                            html.Div(
                              className=("card-2 ca-coordenadas"),
                              children = [
                                html.H4("Coordenadas"),
                                html.Div(
                                  className="subcard-2 values-2",
                                  children = [
                                    html.H3("128.5"),
                                    html.H3("-103.9")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard-2 uds",
                                  children = [
                                    html.P("Latitud"),
                                    html.P("Longitud")
                                  ]
                                )
                              ]
                            ),
                            # Sección TEMPERATURA
                            html.Div(
                              className="card-1 temperatura",
                              children = [
                                html.H4("Temperatura"),
                                html.H3("30"),
                                html.P("°C")
                              ]
                            ),
                            # Sección PRESION
                            html.Div(
                              className="card-1 presión",
                              children = [
                                html.H4("Presión"),
                                html.H3("2"),
                                html.P("Pa")
                              ]
                            ),
                            # Sección HUMEDAD
                            html.Div(
                              className="card-1 humedad",
                              children = [
                                html.H4("Humedad"),
                                html.H3("3"),
                              ]
                            ),
                            # Sección ACELEROMETRO
                            html.Div(
                              className=("card-3 acelerometro"),
                              children = [
                                html.H4("Acelerometro"),
                                html.Div(
                                  className="subcard-3 values-3",
                                  children = [
                                    html.H3("128.5"),
                                    html.H3("-103.9"),
                                    html.H3("150.0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard-3 uds",
                                  children = [
                                    html.P("Eje X"),
                                    html.P("Eje Y"),
                                    html.P("Eje Z")
                                  ]
                                )
                              ]
                            ),
                            # Sección GIROSCOPIO
                            html.Div(
                              className=("card-3 giroscopio"),
                              children = [
                                html.H4("Giroscopio"),
                                html.Div(
                                  className="subcard-3 values-3",
                                  children = [
                                    html.H3("128.5"),
                                    html.H3("-103.9"),
                                    html.H3("150.0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard-3 uds",
                                  children = [
                                    html.P("Eje X"),
                                    html.P("Eje Y"),
                                    html.P("Eje Z")
                                  ]
                                )
                              ]
                            ),
                            # Sección VELOCIDAD
                            html.Div(
                              className="card-1 velocidad",
                              children = [
                                html.H4("Velocidad"),
                                html.H3("30"),
                                html.P("m/s")
                              ]
                            ),
                            # Sección FECHA
                            html.Div(
                              className="card-1 fecha",
                              children = [
                                html.H4("20-08-2021"),
                                html.H4("17:43"),
                              ]
                            ),
                            # Sección GRAFICA
                            html.Div(
                              className="card-graph",
                              children= [
                                dcc.Tabs(
                                  className="tabs-subgraph",
                                  value="ac-gi-graph",
                                  children = [
                                    dcc.Tab( id="ac-gi-graph2",
                                      className="custom-subtab",
                                      selected_className='custom-subtab--selected',
                                      label="Cansat",
                                      value="ac-gi-graph",
                                      children=[
                                        html.Div(
                                          className="graph-ace-giro-container",
                                          children=[
                                            dcc.Graph(
                                              figure=functions.plot_graphs_ace_giro()
                                            )
                                          ]
                                        )
                                      ]
                                    ),
                                    dcc.Tab(id="cansat-graph",
                                      className="custom-subtab",
                                      selected_className='custom-subtab--selected',
                                      label="Cansat",
                                      value="cansat-graph",
                                      children=[
                                          html.Div(
                                          className="graph-cansat-container",
                                          children=[
                                            dcc.Graph(
                                              figure=functions.plot_cansat()
                                            )
                                          ]
                                        )
                                      ]
                                    )
                                  ]
                                )
                              ]
                            )
                          ]
                        )
                      ]
                    )
                  ])
        ])
      ]
    )
  ]
)

## ESTA ES LA FUNCIÓN QUE ACTUALIZA LOS VALORES
## RECIBE AL CONTADOR LLAMADO INTERVAL DE LA LINEA 47
## EL CONTADOR LE DA LA SEÑAL PARA QUE LOS OUTPUTS SE REFRESQUEN
## EL INTERVAL TIENE UN TIEMPO DE ACTUALIZACION DE 0.5 SEGUNDOS O 500 MILISEGUNDOS
# @app.callback(
#   dash.dependencies.Output('altitud', 'children'),
#   dash.dependencies.Output('latitud', 'children'),
#   dash.dependencies.Output('longitud', 'children'),
#   dash.dependencies.Output('temperatura', 'children'),
#   dash.dependencies.Output('presion', 'children'),
#   dash.dependencies.Output('humedad', 'children'),
#   dash.dependencies.Output('aceleX', 'children'),
#   dash.dependencies.Output('aceleY', 'children'),
#   dash.dependencies.Output('aceleZ', 'children'),
#   dash.dependencies.Output('giroX', 'children'),
#   dash.dependencies.Output('giroY', 'children'),
#   dash.dependencies.Output('giroZ', 'children'),
#   dash.dependencies.Output('date', 'children'),
#   dash.dependencies.Output('hour', 'children'),
#   [dash.dependencies.Input('interval-component', 'n_intervals')] 
# )
# def data_listener(n):
#   output = functions.open_serial() # ESTA FUNCIÓN TRAE LOS VALORES DEL PUERTO SERIAL
#   al = output[0]
#   la = output[1]
#   lo = output[2]
#   te = output[3]
#   pr = output[4]
#   hu = output[5]
#   ax = output[6]
#   ay = output[7]
#   az = output[8]
#   gx = output[9]
#   gy = output[10]
#   gz = output[11]
#   date = functions.today_date()
#   hour = functions.current_time()
#   return al, la, lo, te, pr, hu, ax, ay, az, gx, gy, gz, date, hour



## ESTA FUNCIÓN ES LA RESPONSABLE DE LA INTERACCIÓN CON LA IMAGEN 
## ESTA EN CAMBIO SOLO TIENE 1 OUTPUT QUE ES LA IMAGEN A LA QUE SE LE 
## PUEDEN MOVER LOS VALORES DE hsv O LOS blurs 
## LO QUE HACE QUE SE ACTUALICE ES EL CAMBIO EN LO INPUTS
## QUE EN ESTE CASO SON LOS SLIDERS Y LOS BOTONES
gau = 0
med = 0
res = 0

# @app.callback(
#   dash.dependencies.Output("imagen-cansat", "children"),
#   [dash.dependencies.Input('boton-adelante','n_clicks'),
#   dash.dependencies.Input('boton-atras','n_clicks'),
#   dash.dependencies.Input('H-slider','value'),
#   dash.dependencies.Input('S-slider','value'),
#   dash.dependencies.Input('V-slider','value'),
#   dash.dependencies.Input('gauss','n_clicks'),
#   dash.dependencies.Input('median','n_clicks'),
#   dash.dependencies.Input('reset','n_clicks')]
# )
# def image_controler(adelante, atras, H, S, V, gauss, median, reset):
#   global gau, med, res

#   image_number = adelante - atras
#   image = IMGS_PATH[image_number]
#   min = [H[0], S[0], V[0]]
#   max = [H[1], S[1], V[1]]

#   if gauss!=gau:
#     image = functions.gaussian_blur(image)
#     print("Apply 1 time gauss")
#     gau = gauss
#   else:
#     pass

#   if median!=med:
#     image = functions.median_blur(image)
#     print("Apply 1 time median")
#     med =median

#   if reset!= res:
#     image = IMGS_PATH[image_number]
#     res = reset
#   else:
#     pass
  
#   return [dcc.Graph(
#             className='graph',
#             figure= functions.plot_image(image, min, max)
#           ),
#         html.P(f'H: {H}  S: {S}  V: {V}')]


if __name__=='__main__':
  app.run_server(debug=True)