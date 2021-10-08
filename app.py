import dash
import dash_core_components as dcc
import dash_html_components as html
import os
from numpy.lib.polynomial import poly1d
import pandas as pd

import time
import functions
from datetime import datetime


##### INICIAMOS LA APP #####
app = dash.Dash(__name__)

##### AQUI VA TODA LA ESTRUCTURA DE NUESTRA PAGINA 
app.layout= html.Div(
  #CONTENEDOR PRINCIPAL
  className="main-container",
  children=[
    html.P(id="hidden-p", style={'display': 'none'}),
    # CABEZERA DONDE VA EL LOGO
    html.Div(
      className='header', children=[
        html.Img(src='./assets/Images/unnamed.png', className='logo')
      ]
    ),
    # aqui va todo lo demás
    html.Section(
      className='main',
      children=[
        ####Este componente interval es muy importante, es el que nos da el tiempo de actualización de la página                    
        #ES SU UNÍCO PROPOSITO (ES INVISIBLE, NO SE MOSTRARÁ NADA EN LA PÁGINA)
        dcc.Interval(
            id='interval-component',
            interval=500, # milisegundos
            n_intervals=0
        ),
        html.Section(
          className="lateral-section",
          children=[
            html.Div(
              className="buttons",
              children = [
                html.Div(
                  className="start-stop-buttons",
                  children = [
                    html.Button('Iniciar', className='start-button', id='start-button'),
                    html.Button('Detener', className='stop-button', id='stop-button')
                  ]
                ),
                html.Button("Generar Reporte", className= "report-button", id= "guardar-reporte") 
              ]
            ),
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
            html.Div(
              className="card fecha",
              children = [
                html.H4(id="date", children="20-08-2021"),
                html.H4(id="hour", children="17:43"),
              ]
            ),
            html.Div(
              className="card time",
              children = [
                html.H4("Tiempo de Misión"),
                html.H3(id='mision-time' ,children="00:00"),
              ]
            ),
          ]
        ),
        # iniciamos componente de los tabs (las pestañas para cambiar de métrica a imagen)
        dcc.Tabs(className='main-tabs',
                  value='tab-cansat',children=[
          # iniciamos el primer tab de metrica
          #### COHETE SECCIÓN 
          dcc.Tab(id='tab-cohete',
                  className='custom-tab',
                  selected_className='custom-tab--selected', 
                  label='Cohete', 
                  value='tab-cohete', children=[
                    ###Contenido del primer tab

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
                            # Sección ALTITUD
                            html.Div(
                              className="card co-altitud",
                              children = [
                                html.H4("Altitud"),
                                html.H3(id='co-altitud', children="0"),
                                html.P("metros")
                              ]
                            ),
                            # Sección COORDENADAS
                            html.Div(
                              className=("card co-coordenadas"),
                              children = [
                                html.H4("Coordenadas"),
                                html.Div(
                                  className="subcard values-2",
                                  children = [
                                    html.H3(id='co-latitud', children="0"),
                                    html.H3(id='co-longitud', children="0"),
                                  ]
                                ),
                                html.Div(
                                  className= "subcard",
                                  children = [
                                    html.P("Latitud"),
                                    html.P("Longitud")
                                  ]
                                )
                              ]
                            ),
                            # Sección POSICION
                            html.Div(
                              className=("card co-position"),
                              children = [
                                html.H4("Posición"),
                                html.Div(
                                  className="subcard",
                                  children = [
                                    html.H3(id ='posX', children="0"),
                                    html.H3(id ='posY', children="0"),
                                    html.H3(id ='posZ', children="0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard",
                                  children = [
                                    html.P("Eje X"),
                                    html.P("Eje Y"),
                                    html.P("Eje Z")
                                  ]
                                )
                              ]
                            ),
                            html.Div(className="card nada"),
                            # Sección VELOCIDAD
                            html.Div(
                              className="card co-velocidad",
                              children = [
                                # html.H4("Velocidad"),
                                # html.H3("30"),
                                # html.P("m/s")
                              ]
                            ),
                            
                            # Sección GRAFICA
                            html.Div(
                              className="card-graph",
                              children= [
                                dcc.Tabs(
                                  className="tabs-subgraph",
                                  value="map-graph",
                                  children = [
                                    dcc.Tab( 
                                      className="custom-subtab",
                                      selected_className='custom-subtab--selected',
                                      label="Mapa",
                                      value="map-graph",
                                      children=[
                                        html.Div(
                                          className="graph-map-container",
                                          children=[
                                            dcc.Graph(
                                              id="map-graph",
                                              figure=functions.plot_map()
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
          #### CANSAT SECCIÓN 
          dcc.Tab(id='tab-cansat',
                  className='custom-tab', 
                  selected_className='custom-tab--selected',
                  label='Cansat', 
                  value='tab-cansat', children=[
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
                              className="card ca-altitud",
                              children = [
                                html.H4("Altitud"),
                                html.H3(id='ca-altitud', children="0"),
                                html.P("metros")
                              ]
                            ),
                            # Sección COORDENADAS
                            html.Div(
                              className=("card ca-coordenadas"),
                              children = [
                                html.H4("Coordenadas"),
                                html.Div(
                                  className="subcard values-2",
                                  children = [
                                    html.H3(id='ca-latitud', children="0"),
                                    html.H3(id='ca-longitud', children="0"),
                                  ]
                                ),
                                html.Div(
                                  className= "subcard",
                                  children = [
                                    html.P("Latitud"),
                                    html.P("Longitud")
                                  ]
                                )
                              ]
                            ),
                            # Sección TEMPERATURA
                            html.Div(
                              className="card temperatura",
                              children = [
                                html.H4("Temperatura"),
                                html.H3(id='ca-temperatura', children="0"),
                                html.P("°C")
                              ]
                            ),
                            # Sección PRESION
                            html.Div(
                              className="card presión",
                              children = [
                                html.H4("Presión"),
                                html.H3(id ='ca-presion', children="0"),
                                html.P("Pa")
                              ]
                            ),
                            # Sección HUMEDAD
                            html.Div(
                              className="card humedad",
                              children = [
                                html.H4("Humedad"),
                                html.H3(id='ca-humedad', children="0"),
                              ]
                            ),
                            # Sección ACELEROMETRO
                            html.Div(
                              className=("card acelerometro"),
                              children = [
                                html.H4("Acelerometro"),
                                html.Div(
                                  className="subcard values-3",
                                  children = [
                                    html.H3(id ='ca-aceleX', children="0"),
                                    html.H3(id ='ca-aceleY', children="0"),
                                    html.H3(id ='ca-aceleZ', children="0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard",
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
                              className=("card giroscopio"),
                              children = [
                                html.H4("Giroscopio"),
                                html.Div(
                                  className="subcard values-3",
                                  children = [
                                    html.H3(id ='ca-giroX', children="0"),
                                    html.H3(id ='ca-giroY', children="0"),
                                    html.H3(id ='ca-giroZ', children="0")
                                  ]
                                ),
                                html.Div(
                                  className= "subcard",
                                  children = [
                                    html.P("Eje X"),
                                    html.P("Eje Y"),
                                    html.P("Eje Z")
                                  ]
                                )
                              ]
                            ),
                            # Sección VELOCIDAD - bateria
                            html.Section(
                              className="vel-bat",
                              children=[
                                html.Section(
                                  className="pila",
                                  children= [
                                    html.Div(className="pila-head"), 
                                    html.Div(
                                      className="pila-body", 
                                      children= [
                                        html.Div(
                                          className="pila-fondo",
                                          id="pila-porcentaje",
                                          children=[
                                            html.Div(
                                              className="pila-pila",
                                            ),
                                            html.H5(id="battery-percent", children=["100%"])
                                          ]
                                        )
                                      ]
                                    )
                                  ]
                                ),
                                html.Section(
                                  className="card velocidad",
                                  children = [
                                    html.H4("Velocidad"),
                                    html.H3(id = "ca-velocidad", children="0"),
                                    html.P("m/s")
                                  ]
                                )
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
                                      label="Graficas",
                                      value="ac-gi-graph",
                                      children=[
                                        html.Div(
                                          className="graph-ace-giro-container",
                                          children=[
                                            dcc.Graph(
                                              id='acel-gyro-graph',
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
                                            ),
                                            html.Div(
                                              className="controlador-pila-container",
                                              children=[
                                                dcc.Slider(
                                                  className="controlador-pila",
                                                  min=0,
                                                  max=100,
                                                  updatemode="drag",
                                                  marks={0:'0', 100:'100'},
                                                  value=100
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
                      ]
                    )
                  ])
        ])
      ]
    )
  ]
)
active = False
dic = {"A":[], "G": []}
df_data = pd.DataFrame() 
#Esta función nos da la orden para empezar a recibir datos
@app.callback(
  dash.dependencies.Output('hidden-p', 'children'),
  [dash.dependencies.Input('start-button', 'n_clicks'),
  dash.dependencies.Input('stop-button', 'n_clicks'),
  dash.dependencies.Input('guardar-reporte', 'n_clicks')]
)
def mision_starter_stopper(start, stop, report):
  global active, dic, time_starter, df_data
  
  ctx = dash.callback_context

  if not ctx.triggered:
    raise dash.exceptions.PreventUpdate
  else:
    clicked_button = ctx.triggered[0]['prop_id'].split('.')[0] .split('-')[0]
  
  print(clicked_button)
  if clicked_button=="start":
    print("Se presiono start")
    if active == False:
      time_starter = time.time()
      dic = {"A":[], "G": []}
      active = True
    else:
      raise dash.exceptions.PreventUpdate

  elif clicked_button=="stop":
    print("Se presiono stop")
    if active == True:
      active = False
    else: 
      raise dash.exceptions.PreventUpdate

  elif clicked_button =="guardar":
    print("Se presiono guardar")

    if active == False:
      hora = functions.current_time()
      fecha = functions.today_date().replace("/","-")
      file_name = "datos-" + fecha + "-" + hora + ".csv"
      df_data.to_csv("./DatosGuardados/"+ file_name, index=False, mode="a", header=True)
      print("Generado")
  return None


## ESTA ES LA FUNCIÓN QUE ACTUALIZA LOS VALORES
## RECIBE AL CONTADOR LLAMADO INTERVAL DE LA LINEA 47
## EL CONTADOR LE DA LA SEÑAL PARA QUE LOS OUTPUTS SE REFRESQUEN
## EL INTERVAL TIENE UN TIEMPO DE ACTUALIZACION DE 0.5 SEGUNDOS O 500 MILISEGUNDOS
previa_ve = 0
@app.callback(
  dash.dependencies.Output('piro1', 'style'),
  dash.dependencies.Output('piro2', 'style'),
  dash.dependencies.Output('igni1', 'style'),
  dash.dependencies.Output('igni2', 'style'),
  dash.dependencies.Output('switch1', 'style'),
  dash.dependencies.Output('switch2', 'style'),
  dash.dependencies.Output('switch3', 'style'),
  dash.dependencies.Output('co-altitud', 'children'),
  dash.dependencies.Output('co-latitud', 'children'),
  dash.dependencies.Output('co-longitud', 'children'),
  dash.dependencies.Output('posX', 'children'),
  dash.dependencies.Output('posY', 'children'),
  dash.dependencies.Output('posZ', 'children'),
  dash.dependencies.Output('map-graph','figure'),
  dash.dependencies.Output('ca-altitud', 'children'),
  dash.dependencies.Output('ca-latitud', 'children'),
  dash.dependencies.Output('ca-longitud', 'children'),
  dash.dependencies.Output('ca-temperatura', 'children'),
  dash.dependencies.Output('ca-presion', 'children'),
  dash.dependencies.Output('ca-humedad', 'children'),
  dash.dependencies.Output('ca-aceleX', 'children'),
  dash.dependencies.Output('ca-aceleY', 'children'),
  dash.dependencies.Output('ca-aceleZ', 'children'),
  dash.dependencies.Output('ca-giroX', 'children'),
  dash.dependencies.Output('ca-giroY', 'children'),
  dash.dependencies.Output('ca-giroZ', 'children'),
  dash.dependencies.Output('ca-velocidad', 'children'),
  dash.dependencies.Output('acel-gyro-graph','figure'),
  dash.dependencies.Output('mision-time', 'children'),
  dash.dependencies.Output("pila-porcentaje", 'children'),
  [dash.dependencies.Input('interval-component', 'n_intervals')] 
)
def data_listener(n):
  global dic, active, time_starter, previa_ve, df_data

  if active == False:
    raise dash.exceptions.PreventUpdate

  # try:
  #   output = functions.open_serial(4) # ESTA FUNCIÓN TRAE LOS VALORES DEL PUERTO SERIAL Cambiar puerto si es necesario
  # except:
  #   print("Error al conectar con puerto serial")
  output = functions.random_generator()

  if output == None:
    p1    = dash.no_update
    p2    = dash.no_update
    i1    = dash.no_update
    i2    = dash.no_update
    sw1   = dash.no_update
    sw2   = dash.no_update
    sw3   = dash.no_update
    co_al = dash.no_update
    co_la = dash.no_update
    co_lo = dash.no_update
    px    = dash.no_update
    py    = dash.no_update
    pz    = dash.no_update
    maps  = dash.no_update
    ca_al = dash.no_update
    ca_la = dash.no_update
    ca_lo = dash.no_update
    ca_al = dash.no_update
    ca_la = dash.no_update
    ca_lo = dash.no_update
    ca_te = dash.no_update
    ca_pr = dash.no_update
    ca_hu = dash.no_update
    ca_ax = dash.no_update
    ca_ay = dash.no_update
    ca_az = dash.no_update
    ca_gx = dash.no_update
    ca_gy = dash.no_update
    ca_gz = dash.no_update
    ca_ve = dash.no_update
    graph_giro_ace = dash.no_update
    pila_value = 1000 
  else: 
    p1   = functions.red_green(output["P1"])
    p2   = functions.red_green(output["P2"])
    i1   = functions.red_green(output["I1"])
    i2   = functions.red_green(output["I2"])
    sw1  = functions.red_green(output["Sw1"])
    sw2  = functions.red_green(output["Sw2"])
    sw3  = functions.red_green(output["Sw3"])
    co_al= output["co-Al"]
    co_la= output["co-La"]
    co_lo= output["co-Lo"]
    px   = output["Px"]
    py   = output["Py"]
    pz   = output["Pz"]
    maps = functions.plot_map()
    ca_al = output["ca-Al"]
    ca_la = output["ca-La"]
    ca_lo = output["ca-Lo"]
    ca_te = output["ca-Te"]
    ca_pr = output["ca-Pr"]
    ca_hu = output["ca-Hu"]
    ca_ax = output["ca-Ax"]
    ca_ay = output["ca-Ay"]
    ca_az = output["ca-Az"]
    ca_gx = output["ca-Gx"]
    ca_gy = output["ca-Gy"]
    ca_gz = output["ca-Gz"]
    pila_value = output['Bat']  
    pila_value_str = str(pila_value) + "%"
    g,a = functions.graphs_values(output)
    previa_ve += a * 0.5
    ca_ve = round(previa_ve, 2)
    dic['A'].append(a)
    dic['G'].append(g)
    output['A'] = a
    output['G'] = g
    output['Ve'] = ca_ve 
    output['Time'] = datetime.now().strftime("%H:%M:%S")
    df_data = df_data.append(output, ignore_index=True)

    graph_giro_ace = functions.plot_graphs_ace_giro(dic)


  # La hora y el tiempo de misión solo se actualizarán cada segundo
  if n%2 != 1: #Si no es un segundo exacto no te actualices
    mision_time = dash.no_update
  else:
    mision_time = functions.get_time_mision(time_starter)

  if pila_value == 1000:
    pila = dash.no_update
  elif pila_value < 20:
    pila = [html.Div(
              className="pila-pila",
              style={'height': pila_value_str, "background-color": "#F95738"}
            ),
            html.H5(id="battery-percent", children=[pila_value_str])]
  else:
    pila = [html.Div(
              className="pila-pila",
              style={'height': pila_value_str, "background-color": "#55F165"}
            ),
            html.H5(id="battery-percent", children=[pila_value_str])]
  
  return p1, p2, i1, i2, sw1, sw2, sw3, co_al, co_la, co_lo, px, py, pz, maps , ca_al, ca_la, ca_lo, ca_te, ca_pr, ca_hu, ca_ax, ca_ay, ca_az, ca_gx, ca_gy, ca_gz, ca_ve, graph_giro_ace, mision_time, pila


@app.callback(
  dash.dependencies.Output('date', 'children'),
  dash.dependencies.Output('hour', 'children'),
  [dash.dependencies.Input('interval-component', 'n_intervals')] 
)
def date_and_hour(n):
  global active

  if active == True:
    raise dash.exceptions.PreventUpdate
  # La hora y el tiempo de misión solo se actualizarán cada segundo
  if n%2 != 1: #Si no es un segundo exacto no te actualices
    hour = dash.no_update
  else:
    hour = functions.current_time() 
  # La fecha solo se actualizará al iniciar el programa
  if n ==0 : #Si el intervalo es 1 (acaba de arrancar) actualizate
    date = functions.today_date()
  else:
    date = dash.no_update

  return date, hour

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