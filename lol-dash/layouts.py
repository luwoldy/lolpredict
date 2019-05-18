import dash_core_components as dcc
import dash_html_components as html

home_layout = html.Div(
    className= 'container',
    children=[
        html.Img(src="https://files.slack.com/files-pri/TD31W8VC1-FJNEVKEG5/image.png",className="c1"),
        html.Div(className="c2", 
        children = [
            dcc.Input(id='input-1-state', type='text', placeholder='Summoner Name',className='input-field'),
            dcc.Dropdown(
            options=[
                {'label': 'Russia', 'value': 'RU'},
                {'label': 'Korea', 'value': 'KR'},
                {'label': 'Brazil', 'value': 'BR1'},
                {'label': 'Oceania', 'value': 'OC1'},
                {'label': 'Japan', 'value': 'JP1'},
                {'label': 'North America', 'value': 'NA1'},
                {'label': 'EU North', 'value': 'EUN1'},
                {'label': 'EU West', 'value': 'EUW1'},
                {'label': 'Turkey', 'value': 'TR1'},
                {'label': 'Latin America 1', 'value': 'LA1'},
                {'label': 'Latin America 2', 'value': 'LA2'},

            ],
            value='NA1',
            id='input-2-state',
            placeholder="region",
        ),
            html.Button('Go!', id='submit-button'),
        ]),
        html.Div(id="output",className='c5'),
    ])