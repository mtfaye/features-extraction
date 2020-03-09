import dash
import dash_html_components as html
import dash_core_components as dcc

app = dash.Dash(__name__)
app.config['suppress_callback_exceptions'] = True
app.title = 'Features Extraction NLP'
app.colors = {'background': '#5F5958'}

# Boostrap CSS
app.css.append_css({'external_url': 'https://codepen.io/mtfaye/pen/MWgpoyp.css'})


# Markdown text
"""markdown_text1 = 

This application scrappes text data accross different channel of communication such as emails, text messages and 
chats and convert into a numeric feature vector with *TF-IDF vectorization* in order to extract meaningfull topics. 

You can play with the parameters to extract more interesting features.

"""

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H1(children='Communication Analysis App',
                                style={'color': 'white', 'fontSize': 23, 'text-indent': 10, 'line-height': 50},
                                className='banner'
                                )
                    ], className="row"
                ),
                html.Div([
                    html.Div([
                        dcc.Input(id='input_1', value='', type='text',
                                  style={'display': 'inline-block', 'width': '30%'},
                                  placeholder=' Max Features'
                                  ),
                        html.Div(id='output_div'
                                 )
                    ]),
                    html.Div([
                        dcc.Input(id='input_2', value='', type='text',
                                  style={'display': 'inline-block', 'width': '30%'},
                                  placeholder=' Max df'
                                  ),
                        html.Div(id='output_div'
                                 )
                    ]),
                    html.Div([
                        dcc.Input(id='input_3', value='', type='text',
                                  style={'display': 'inline-block', 'width': '30%'},
                                  placeholder=' Min df'
                                  ),
                        html.Div(id='output_div'
                                 )
                    ])

                ]),
                html.Div(
                    [
                        html.P('Developed by Mouhameth T. Faye ',
                               style={'display': 'inline'}
                               ),
                        html.A('tahafaye@hotmail.com',
                               href='tahafaye@hotmail.com'
                               )
                    ], className="twelve columns",
                    style={'fontSize': 13, 'padding-top': 18}
                )
            ], className="row"
        )
    ], className='ten columns offset-by-one'
)

if __name__ == '__main__':
    app.run_server(debug=True)
