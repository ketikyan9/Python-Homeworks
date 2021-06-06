import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Reading dataset
df=pd.read_excel(r'master.xlsx')

country_cols = ['All', 'Albania', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba',
       'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain',
       'Barbados', 'Belarus', 'Belgium', 'Belize',
       'Bosnia and Herzegovina', 'Brazil', 'Bulgaria', 'Cabo Verde',
       'Canada', 'Chile', 'Colombia', 'Costa Rica', 'Croatia', 'Cuba',
       'Cyprus', 'Czech Republic', 'Denmark', 'Dominica', 'Ecuador',
       'El Salvador', 'Estonia', 'Fiji', 'Finland', 'France', 'Georgia',
       'Germany', 'Greece', 'Grenada', 'Guatemala', 'Guyana', 'Hungary',
       'Iceland', 'Ireland', 'Israel', 'Italy', 'Jamaica', 'Japan',
       'Kazakhstan', 'Kiribati', 'Kuwait', 'Kyrgyzstan', 'Latvia',
       'Lithuania', 'Luxembourg', 'Macau', 'Maldives', 'Malta',
       'Mauritius', 'Mexico', 'Mongolia', 'Montenegro', 'Netherlands',
       'New Zealand', 'Nicaragua', 'Norway', 'Oman', 'Panama', 'Paraguay',
       'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
       'Republic of Korea', 'Romania', 'Russian Federation',
       'Saint Kitts and Nevis', 'Saint Lucia',
       'Saint Vincent and Grenadines', 'San Marino', 'Serbia',
       'Seychelles', 'Singapore', 'Slovakia', 'Slovenia', 'South Africa',
       'Spain', 'Sri Lanka', 'Suriname', 'Sweden', 'Switzerland',
       'Thailand', 'Trinidad and Tobago', 'Turkey', 'Turkmenistan',
       'Ukraine', 'United Arab Emirates', 'United Kingdom',
       'United States', 'Uruguay', 'Uzbekistan']

year_cols = ['1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', 
            '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015',  '2016']

religion_cols = ['Islam', 'Christian', 'No religion', 'Jewish', 'Buddhist', 'Hindus']
religion_cols2 = ['All', 'Islam', 'Christian', 'No religion', 'Jewish', 'Buddhist', 'Hindus']

age_cols = ['5-14 years', '15-24 years', '25-34 years', '35-54 years', '55-74 years', '75+ years']

countries = [{'label': i, 'value': i} for i in country_cols]
years = [{'label': i, 'value': i} for i in year_cols]
religions = [{'label': i, 'value': i} for i in religion_cols]
religions2 = [{'label': i, 'value': i} for i in religion_cols2]

ages = [{'label': i, 'value': i} for i in age_cols]

figure_gen = px.histogram(df, x='generation', color="generation", barmode='group',
                        title= "Suicides by generation",
                        labels={"generation": "Generations"})



coef = np.corrcoef(df['gdp_per_capita ($)'], df["suicides/100k pop"])[0][1]
coef = coef.round(3)
figure_corr = px.scatter(df['gdp_per_capita ($)'], df["suicides/100k pop"])
figure_corr = px.scatter(df, x="gdp_per_capita ($)", y="suicides/100k pop",
                 labels={
                     "gdp_per_capita ($)": "GDP per capita ($)",
                     "suicides/100k pop": "Number of suicides per 100K people",
                 },
                title='Correlation between GDP per capita and number of suicides (Coefficient is {})'.format(coef))


tmp_df = df.groupby(['religion','year'])['population', 'suicides_no'].sum()
tmp_df = tmp_df.reset_index()
tmp_df['normalized_suicides'] = (tmp_df.suicides_no / tmp_df.population) * 100
figure_relig = px.bar(tmp_df, x='year', y='normalized_suicides', color='religion',
                      color_discrete_map={"Islam": "#000000", "Christian": "#4c61f4", "No religion": "#ffbc3f", 
                                          "Jewish": "#fca4ef", "Buddhist": "#f44c4c", "Hindus": "#eaf44c"},
                     labels={"year": "Year", "normalized_suicides": "Normalized number of suicides", "religion": "Religion"},
                     title="Suicides by religions")


external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    {
        'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
        'rel': 'stylesheet',
        'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
        'crossorigin': 'anonymous'
    }
]

app = dash.Dash(external_stylesheets = external_stylesheets)

app.layout = html.Div([
    html.Div([html.H1('Suicide Data Overview 1985 to 2016')], className = 'row'),
    
#     Suicide rate change over the years per country
    html.Div([dcc.Dropdown(
                                id = 'countries_input',
                                options = countries, value = countries[0]['value'], className='five columns')],
    className = 'twelve columns'),
    html.Div([
                   html.Div([dcc.Graph(id='fig1')], className = 'twelve columns'),
            ], className = 'row'),
#     Suicides by generation
    html.Div([
                   html.Div([dcc.Graph(figure=figure_gen)], className = 'twelve columns'),
            ], className = 'row'),
#     Classification by age group and the gender.
    html.Div([dcc.Dropdown(
                                id = 'ages_input',
                                options = ages, value = ages[1]['value'], className='five columns')],
    className = 'twelve columns'),
    html.Div([
                   html.Div([dcc.Graph(id="fig2")], className = 'twelve columns'),
            ], className = 'row'),
#     Correlation between GDP per capita and number of suicides
    html.Div([
                   html.Div([dcc.Graph(figure=figure_corr)], className = 'twelve columns'),
            ], className = 'row'),
#     Suicides by religions
    html.Div([
                   html.Div([dcc.Graph(figure=figure_relig)], className = 'twelve columns'),
            ], className = 'row'),
#     Suicides by gender for selected religion
    html.Div([dcc.Dropdown(
                                id = 'religions_input2',
                                options = religions2, value = religions2[0]['value'], className='five columns')],
    className = 'twelve columns'),
    html.Div([
                   html.Div([dcc.Graph(id="fig3")], className = 'twelve columns'),
            ], className = 'row'),
#     Average suicide over time by religion and the rest (world\selected)
    html.Div([dcc.Dropdown(
                                id = 'religions_input',
                                options = religions, value = religions[0]['value'], className='five columns')],
    className = 'twelve columns'),
    html.Div([
                   html.Div([dcc.Graph(id="fig4")], className = 'twelve columns'),
            ], className = 'row'),
    
    
], className = 'container')






@app.callback(
       Output(component_id = 'fig1', component_property = 'figure'),
       [Input(component_id = 'countries_input', component_property = 'value')]         
)

def update_lineplot_percountry(input_):
    data = df.copy()
    if(input_ != 'All'):
        data = df[df['country'] == input_]
        data = data.groupby(['year','country'])['suicides_no'].sum().reset_index()
    else:
        data = data.groupby(['year'])['suicides_no'].sum().reset_index()   

    figure = px.line(data, x="year", y="suicides_no",
                    title='Suicide rate change over the years for {}'.format(input_),
                    labels={"year": "Year", "suicides_no" : "count"})
    
    return figure


@app.callback(
       Output(component_id = 'fig2', component_property = 'figure'),
       [Input(component_id = 'ages_input', component_property = 'value')]
)

def update_bar(input_):

    data = df.copy()
    data = data[data.age == input_]
    figure = px.bar(data, x='sex', y="suicides_no", color="sex", barmode="overlay",
                    title = 'Suicides by age group for the gender',
                    color_discrete_map={"male": "#256acf", "female": "#cf25a2"},
                    labels={"sex": "Gender", "suicides_no" : "count"})
    return figure

@app.callback(
       Output(component_id = 'fig3', component_property = 'figure'),
       [Input(component_id = 'religions_input2', component_property = 'value')]
)

def update_lineplot_religion_gender(input_):
    data = df.copy()
    if (input_ != "All"):
        data = data.groupby(['religion','year','sex'])['suicides/100k pop'].sum().reset_index()
        data = data[data.religion == input_]
    else:
        data = data.groupby(['year','sex'])['suicides/100k pop'].sum().reset_index()

    data = data.sort_values('year')
    figure = px.line(data, x="year", y="suicides/100k pop", color='sex',
                    title='Suicides by gender for {}'.format(input_),
                    color_discrete_map={"male": "#256acf", "female": "#cf25a2"},
                    labels={"year": "Year", "suicides/100k pop" : "count per 100K people", "sex": "Gender"})
    
    return figure

        

@app.callback(
       Output(component_id = 'fig4', component_property = 'figure'),
       [Input(component_id = 'religions_input', component_property = 'value')]
)

def update_barplot_religion_average(input_):
    data = df.copy()
    data_input = data[data['religion']==input_]
    suicide_input_avg = data_input.groupby('year')['suicides/100k pop'].mean().reset_index()
    suicide_input_avg.columns=['year', 'input_average']

    data_others = data[data['religion']!=input_]
    suicide_world_avg = data_others.groupby('year')['suicides/100k pop'].mean().reset_index()
    suicide_world_avg.columns=['year', 'rest_average']


    temp = pd.merge(suicide_world_avg, suicide_input_avg, right_index = True,
                   left_index = True)
    temp = temp.drop("year_x", axis=1)
    
    
    figure = go.Figure()
    figure.add_trace(go.Bar(
        x=temp.year_y,
        y=temp.rest_average,
        name='The Rest',
        marker_color='#663399'
    ))
    figure.add_trace(go.Bar(
        x=temp.year_y,
        y=temp.input_average,
        name=input_,
        marker_color='#daabe3'
    ))

    figure.update_layout(barmode='group', title='Average suicide over time ({} x The Rest)'.format(input_))

    return figure




if __name__ == '__main__':
    app.run_server(debug = True)
