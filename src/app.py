import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

from features_extraction import *

app = dash.Dash(__name__)
app.config['suppress_callback_exceptions'] = True
app.title = 'Features Extraction NLP'
app.colors = {'background': '#5F5958'}

# Boostrap CSS
external_stylesheets = ['https://codepen.io/mtfaye/pen/MWgpoyp.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H1(children='Topic Modeling App',
                                style={'color': 'white', 'fontSize': 23, 'text-indent': 10, 'line-height': 50},
                                className='banner'
                                )
                    ], className="row"
                ),

                html.Div(children="""This application scrappes text data accross different channel of communication 
                such as emails, text messages and chats and convert into a numeric feature vector with *TF-IDF 
                vectorization* in order to extract meaningful topics. 

                You can play with the parameters to extract more interesting features.
                """
                         , style={
                        'textAlign': 'center'

                    }),
                html.Div(children=[
                    html.H3(children='Extract features from Emails, Chats and SMS files'),

                    html.Div([
                        html.H5("TF-IFD Parameter"),
                        dcc.Input(
                            id='input-x',
                            placeholder='Max features',
                            type='number',
                            value='',
                        ),

                        html.Div(
                            html.Div(id='result')
                        )
                    ])

                ])
            ]),
        html.Div(
            [
                html.P('Developed by Mouhameth T. Faye ',
                       style={'display': 'inline'}
                       ),
                html.A('tahafaye@hotmail.com',
                       href='mailto: tahafaye@hotmail.com'
                       )
            ], className="twelve columns",
            style={'fontSize': 13, 'padding-top': 18}
        )
    ], className="row"

)


@app.callback(
    Output('result', 'children'),
    [Input('input-x', 'value')]
)
def update_result(user_input):
    ngram_range = (1, 2)
    min_df = 1
    max_df = 7
    user_input = user_input

    tfidf = TfidfVectorizer(encoding='utf-8',
                            ngram_range=ngram_range,
                            stop_words=None,
                            lowercase=False,
                            max_df=max_df,
                            min_df=min_df,
                            max_features=user_input,
                            norm='l2',
                            sublinear_tf=True)

    features = tfidf.fit_transform(corpus.Messages)
    labels = corpus.Channel_code

    for wrd, channel_id in sorted(channel_code.items()):
        features_chi2 = chi2(features, labels == channel_id)
        indices = np.argsort(features_chi2[0])
        feature_names = np.array(tfidf.get_feature_names())[indices]
        unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
        bigrams = [v for v in feature_names if len(v.split(' ')) == 2]

    return [

        "# '{}' channel:".format(wrd),
        "  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-3:])),
        "  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-6:])),
        ""

    ]


if __name__ == '__main__':
    app.run_server(debug=True)
