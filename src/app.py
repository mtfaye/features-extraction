import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from features_extraction import extract_features


def generate_table(dataframe):

    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(len(dataframe))]
    )


app = dash.Dash(__name__)
app.config['suppress_callback_exceptions'] = True
app.title = 'NLP Application'
app.colors = {'background': '#5F5958'}

# Boostrap CSS
external_stylesheets = ['https://codepen.io/mtfaye/pen/MWgpoyp.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.Div(
            [
                html.H1(children='features extraction app',
                        style={'color': 'white', 'fontSize': 23, 'text-indent': 10, 'line-height': 50},
                        className='banner'
                        )
            ], className="row"
        ),

        html.Div([
            html.Div(html.H5(
                children=""" About: """
            )
                , style={'textAlign': 'left'}),
            html.P(

                """This application extracts text across three different channels of communication; emails, 
                sms and chats. It then performs a statistical modeling technique to find interesting subject. The 
                table below shows the result. It contains the 15 most important features for each channel. At this 
                point it becomes our job as a human to interpret the result and after looking at the scores for 
                each channel, I think these features convey a collusive behavior from the user. What is your thought? 
                """
            )

        ]),

        html.Div(children=[
            html.P('Select a channel - sms: 1, emails: 2, chats: 3'),
            html.Div(
                [
                    dcc.Dropdown(id='dropdown', options=[
                        {'label': i, 'value': i} for i in extract_features().channel_code.unique()
                    ], multi=True, placeholder='Filter by channel...'),

                    html.Div(id='output_div')
                ], className="row"),
            html.Div(
                [
                    dash_table.DataTable(id='table', columns=[])
                ], className="ten columns"),

            html.Div(
                [
                    html.P('Behavox assignment - Developed by Mouhameth T. Faye ', style={'display': 'inline'}),
                    html.A('tahafaye@hotmail.com', href='mailto: tahafaye@hotmail.com')
                ], className="twelve columns",
                style={'fontSize': 14, 'padding-top': 18}
            )
        ], className="row")
    ], className='ten columns offset-by-one'
)


@app.callback(
    Output('output_div', 'children'),
    [Input('dropdown', 'value')])
def display_table(selector):
    if selector is None:
        return generate_table(extract_features())

    dff = extract_features()[extract_features().channel_code.str.contains('|'.join(selector))]
    return generate_table(dff)


if __name__ == '__main__':
    app.run_server(debug=True)
