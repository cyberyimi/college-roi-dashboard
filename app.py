"""
College ROI Dashboard
Interactive dashboard for analyzing college costs vs. return on investment
"""

import dash
from dash import dcc, html, Input, Output, callback
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# Neon Magenta color scheme for Project 2
NEON_MAGENTA = '#ff00ff'
DARK_BG = '#000000'
LIGHT_BG = '#111111'
TEXT_COLOR = '#ffffff'
SECONDARY_COLOR = '#00ffff'  # Neon cyan for accents

# Load processed data
salary_df = pd.read_csv('data/processed_salary_data.csv')
tuition_trend = pd.read_csv('data/processed_tuition_trend.csv')

# Initialize the Dash app
app = dash.Dash(__name__)
app.title = "College ROI Dashboard"

# Layout
app.layout = html.Div(style={'backgroundColor': DARK_BG, 'color': TEXT_COLOR, 'fontFamily': 'Arial, sans-serif', 'minHeight': '100vh', 'padding': '20px'}, children=[
    # Header
    html.Div([
        html.H1("COLLEGE ROI DASHBOARD", 
                style={'textAlign': 'center', 'color': NEON_MAGENTA, 'marginBottom': '10px', 'fontSize': '48px', 'letterSpacing': '2px'}),
        html.P("Analyze the return on investment of different college majors",
               style={'textAlign': 'center', 'color': TEXT_COLOR, 'fontSize': '18px', 'marginBottom': '40px'}),
    ]),
    
    # Key Stats Row
    html.Div([
        html.Div([
            html.H3("763", style={'color': NEON_MAGENTA, 'fontSize': '36px', 'margin': '0'}),
            html.P("Majors Analyzed", style={'color': TEXT_COLOR, 'margin': '5px 0'}),
        ], style={'backgroundColor': LIGHT_BG, 'padding': '20px', 'textAlign': 'center', 'flex': '1', 'margin': '10px', 'border': f'2px solid {NEON_MAGENTA}'}),
        
        html.Div([
            html.H3("$106K", style={'color': NEON_MAGENTA, 'fontSize': '36px', 'margin': '0'}),
            html.P("Avg 4-Year Cost", style={'color': TEXT_COLOR, 'margin': '5px 0'}),
        ], style={'backgroundColor': LIGHT_BG, 'padding': '20px', 'textAlign': 'center', 'flex': '1', 'margin': '10px', 'border': f'2px solid {NEON_MAGENTA}'}),
        
        html.Div([
            html.H3("3 Years", style={'color': NEON_MAGENTA, 'fontSize': '36px', 'margin': '0'}),
            html.P("Avg Break-Even (Engineering)", style={'color': TEXT_COLOR, 'margin': '5px 0'}),
        ], style={'backgroundColor': LIGHT_BG, 'padding': '20px', 'textAlign': 'center', 'flex': '1', 'margin': '10px', 'border': f'2px solid {NEON_MAGENTA}'}),
    ], style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '40px', 'flexWrap': 'wrap'}),
    
    # Charts Row 1
    html.Div([
        html.Div([
            dcc.Graph(id='tuition-trend-chart', style={'height': '400px'}),
        ], style={'flex': '1', 'margin': '10px', 'backgroundColor': LIGHT_BG, 'padding': '20px', 'border': f'2px solid #333'}),
        
        html.Div([
            dcc.Graph(id='salary-by-category-chart', style={'height': '400px'}),
        ], style={'flex': '1', 'margin': '10px', 'backgroundColor': LIGHT_BG, 'padding': '20px', 'border': f'2px solid #333'}),
    ], style={'display': 'flex', 'marginBottom': '20px', 'flexWrap': 'wrap'}),
    
    # ROI Calculator Section
    html.Div([
        html.H2("ROI CALCULATOR", style={'color': NEON_MAGENTA, 'marginBottom': '20px', 'fontSize': '32px'}),
        html.P("Select a major category to see detailed ROI analysis:", style={'color': TEXT_COLOR, 'marginBottom': '20px'}),
        
        dcc.Dropdown(
            id='category-dropdown',
            options=[{'label': cat, 'value': cat} for cat in sorted(salary_df['category'].unique())],
            value='Engineering & Technology',
            style={'backgroundColor': LIGHT_BG, 'color': TEXT_COLOR, 'marginBottom': '30px'}
        ),
        
        html.Div([
            html.Div([
                dcc.Graph(id='top-majors-chart', style={'height': '500px'}),
            ], style={'flex': '2', 'margin': '10px'}),
            
            html.Div([
                dcc.Graph(id='roi-breakdown-chart', style={'height': '500px'}),
            ], style={'flex': '1', 'margin': '10px'}),
        ], style={'display': 'flex', 'flexWrap': 'wrap'}),
    ], style={'backgroundColor': LIGHT_BG, 'padding': '30px', 'margin': '20px 10px', 'border': f'3px solid {NEON_MAGENTA}'}),
    
    # Best Value Majors
    html.Div([
        html.H2("BEST VALUE MAJORS", style={'color': NEON_MAGENTA, 'marginBottom': '20px', 'fontSize': '32px'}),
        dcc.Graph(id='best-roi-chart', style={'height': '600px'}),
    ], style={'backgroundColor': LIGHT_BG, 'padding': '30px', 'margin': '20px 10px', 'border': f'2px solid #333'}),
    
    # Footer
    html.Div([
        html.P("Data Sources: College Scorecard (tuition) | PayScale (salaries) | Analysis by Monse Rojo", 
               style={'textAlign': 'center', 'color': '#666', 'marginTop': '40px', 'fontSize': '14px'}),
        html.P("Note: ROI calculations use 2016 average tuition costs and assume $40K baseline for high school graduates", 
               style={'textAlign': 'center', 'color': '#666', 'fontSize': '12px'}),
    ]),
])

# Callbacks for interactivity
@callback(
    Output('tuition-trend-chart', 'figure'),
    Input('tuition-trend-chart', 'id')
)
def update_tuition_trend(_):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=tuition_trend['year_numeric'],
        y=tuition_trend['tuition_cost'],
        mode='lines+markers',
        line=dict(color=NEON_MAGENTA, width=3),
        marker=dict(size=8, color=NEON_MAGENTA),
        fill='tozeroy',
        fillcolor=f'rgba(255, 0, 255, 0.1)'
    ))
    
    fig.update_layout(
        title="College Tuition Trends (1985-2016)",
        title_font=dict(size=20, color=NEON_MAGENTA),
        xaxis_title="Year",
        yaxis_title="Annual Tuition (Constant Dollars)",
        plot_bgcolor=DARK_BG,
        paper_bgcolor=LIGHT_BG,
        font=dict(color=TEXT_COLOR),
        xaxis=dict(gridcolor='#333', showgrid=True),
        yaxis=dict(gridcolor='#333', showgrid=True),
        hovermode='x unified'
    )
    return fig

@callback(
    Output('salary-by-category-chart', 'figure'),
    Input('salary-by-category-chart', 'id')
)
def update_salary_by_category(_):
    category_avg = salary_df.groupby('category')['early_career_pay'].mean().sort_values(ascending=True)
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=category_avg.index,
        x=category_avg.values,
        orientation='h',
        marker=dict(color=NEON_MAGENTA, line=dict(color='white', width=2))
    ))
    
    fig.update_layout(
        title="Average Starting Salary by Major Category",
        title_font=dict(size=20, color=NEON_MAGENTA),
        xaxis_title="Early Career Pay ($)",
        plot_bgcolor=DARK_BG,
        paper_bgcolor=LIGHT_BG,
        font=dict(color=TEXT_COLOR),
        xaxis=dict(gridcolor='#333', showgrid=True),
        yaxis=dict(gridcolor='#333'),
        height=400
    )
    return fig

@callback(
    Output('top-majors-chart', 'figure'),
    Input('category-dropdown', 'value')
)
def update_top_majors(selected_category):
    category_data = salary_df[salary_df['category'] == selected_category].nlargest(15, 'early_career_pay')
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=category_data['major'],
        x=category_data['early_career_pay'],
        orientation='h',
        name='Early Career',
        marker=dict(color=NEON_MAGENTA, line=dict(color='white', width=1))
    ))
    fig.add_trace(go.Bar(
        y=category_data['major'],
        x=category_data['mid_career_pay'],
        orientation='h',
        name='Mid Career',
        marker=dict(color=SECONDARY_COLOR, line=dict(color='white', width=1))
    ))
    
    fig.update_layout(
        title=f"Top 15 Majors in {selected_category}",
        title_font=dict(size=18, color=NEON_MAGENTA),
        xaxis_title="Salary ($)",
        plot_bgcolor=DARK_BG,
        paper_bgcolor=LIGHT_BG,
        font=dict(color=TEXT_COLOR, size=10),
        xaxis=dict(gridcolor='#333', showgrid=True),
        yaxis=dict(gridcolor='#333'),
        barmode='group',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        height=500,
        margin=dict(l=250)
    )
    return fig

@callback(
    Output('roi-breakdown-chart', 'figure'),
    Input('category-dropdown', 'value')
)
def update_roi_breakdown(selected_category):
    category_data = salary_df[salary_df['category'] == selected_category]
    avg_break_even = category_data[category_data['years_to_break_even'] < 999]['years_to_break_even'].mean()
    
    fig = go.Figure()
    fig.add_trace(go.Indicator(
        mode="number+delta",
        value=avg_break_even,
        title={"text": f"Avg Break-Even<br><span style='font-size:14px'>Years to recover costs</span>"},
        delta={'reference': 5, 'relative': False},
        domain={'x': [0, 1], 'y': [0, 1]},
        number={'suffix': ' years', 'font': {'size': 48, 'color': NEON_MAGENTA}}
    ))
    
    fig.update_layout(
        plot_bgcolor=DARK_BG,
        paper_bgcolor=LIGHT_BG,
        font=dict(color=TEXT_COLOR),
        height=500
    )
    return fig

@callback(
    Output('best-roi-chart', 'figure'),
    Input('best-roi-chart', 'id')
)
def update_best_roi(_):
    best_roi = salary_df[salary_df['years_to_break_even'] < 999].nsmallest(20, 'years_to_break_even')
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=best_roi['major'],
        x=best_roi['years_to_break_even'],
        orientation='h',
        marker=dict(
            color=best_roi['years_to_break_even'],
            colorscale=[[0, NEON_MAGENTA], [0.5, SECONDARY_COLOR], [1, '#ff6600']],
            showscale=True,
            colorbar=dict(title="Years", tickfont=dict(color=TEXT_COLOR)),
            line=dict(color='white', width=1)
        ),
        text=[f"{x:.1f} yrs" for x in best_roi['years_to_break_even']],
        textposition='outside'
    ))
    
    fig.update_layout(
        title="20 Fastest Break-Even Majors",
        title_font=dict(size=24, color=NEON_MAGENTA),
        xaxis_title="Years to Break Even",
        plot_bgcolor=DARK_BG,
        paper_bgcolor=LIGHT_BG,
        font=dict(color=TEXT_COLOR),
        xaxis=dict(gridcolor='#333', showgrid=True),
        yaxis=dict(gridcolor='#333'),
        height=600,
        margin=dict(l=300)
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True, port=8050)
