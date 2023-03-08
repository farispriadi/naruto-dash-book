import plotly.graph_objects as go 
import pandas as pd 
from dash import Dash 
from dash import html, dcc 
import base64 

databooks1 = {
	'Shinobi': ['naruto','sasuke'],
	'Ninjutsu':[2,2.5],
	'Taijutsu':[1.5,2.5],
	'Genjutsu':[1,1.5],
	'Intelligence':[1,2],
	'Strength':[2,2],
	'Speed':[2,3],
	'Stamina':[4,2],
	'Hand seals':[1,3],
	'Level': ['genin','genin'],
	'Team': ['7','7'],
	'Supervisor': ['kakashi','kakashi']

}

df = pd.DataFrame(databooks1)
print(df)
r_naruto = df[df['Shinobi']=='naruto'].iloc[0][1:9]
print(r_naruto)
r_sasuke = df[df['Shinobi']=='sasuke'].iloc[0][1:9]
print(r_naruto)

fig = go.Figure()

fig.add_traces([
		go.Scatterpolar(
				theta=df.columns[1:9],
				r=r_naruto,
				fill='toself',
      			name='Naruto',
      			mode = 'lines+markers',
      			line=dict(width=0),

			),
		go.Scatterpolar(
				theta=df.columns[1:9],
				r=r_sasuke,
				fill='toself',
      			name='Sasuke',
      			mode = 'lines+markers',
      			line=dict(width=0),
			)
	])

annotations = []

layout = dict(polar=dict(radialaxis=dict(
				visible=True,
				gridcolor='grey',
				range=[0,5],
				showticklabels=False,
				linewidth = 1,
				linecolor='grey',
				
			),
			angularaxis = dict(linecolor='grey',gridcolor='grey')
		),
		showlegend=False)

fig.update_layout(layout
	)

fig.update_polars(bgcolor='rgba(255,255,255,0)',)

# fig.show()
app = Dash(__name__)
image1_png = 'Sasuke_Part_1.png'
image1_base64 = base64.b64encode(open(image1_png, 'rb').read()).decode('ascii')
image2_png = 'Naruto_Part_1.png'
image2_base64 = base64.b64encode(open(image2_png, 'rb').read()).decode('ascii')

app.layout = html.Div([
		html.Div([
			html.H2("Compare Shinobi Stats"),
		]),
		html.Div([
			html.Div([
					dcc.Dropdown(options=['Naruto','Sasuke'],value='Sasuke',style={'width':'165px','color':'black','background-color':'rgba(255, 153, 187,0.5)'}),
					html.Div([
						html.Img(src='data:image/png;base64,{}'.format(image1_base64),height='120px'),
						],style={'height':'150px'})
				],style={'width':'800px','flex':'50%'}),
			html.Div([
					dcc.Dropdown(options=['Naruto','Sasuke'],value='Naruto',style={'width':'165px','color':'black','background-color':'rgba(153, 204, 255,0.5)'}),
					html.Div([
						html.Img(src='data:image/png;base64,{}'.format(image2_base64),height='120px'),
						],style={'height':'150px'})
				],style={'width':'800px','flex':'50%'}),
		],style={'display': 'flex','flex-wrap': 'wrap'}),
		html.Div([
			dcc.Graph(figure=fig,id="graph-stats"),

		],id='graph-container',),
	],id='main-container',style={'width':'600px'})

if __name__ == "__main__":
	app.run_server()