import plotly.graph_objects as go
import pandas as pd

# Load OBM and WBM data into dataframes
obm_data = pd.read_csv('OBM.txt')
wbm_data = pd.read_csv('WBM.txt')

# Create a list of available parameters for comparison
available_parameters = obm_data.columns.intersection(wbm_data.columns)

# Create an initial set of visible traces (empty)
visible_traces = [False] * len(available_parameters)

# Initialize the figure
fig = go.Figure()

# Add an empty trace for each parameter
for parameter in available_parameters:
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name=parameter, visible=False))

# Create dropdown menu options for selecting parameters
dropdown_buttons = [
    {
        'label': parameter,
        'method': 'update',
        'args': [{'visible': [parameter == trace.name for trace in fig.data]}]
    }
    for parameter in available_parameters
]

# Add a "Show All" button
dropdown_buttons.append(
    {
        'label': 'Show All',
        'method': 'update',
        'args': [{'visible': [True] * len(available_parameters)}]
    }
)

# Define the layout
fig.update_layout(
    updatemenu=[
        {
            'buttons': dropdown_buttons,
            'direction': 'down',
            'showactive': True,
            'x': 0.05,
            'xanchor': 'left',
            'y': 1.15,
            'yanchor': 'top',
        }
    ],
    title='Compare Parameters (Select from Dropdown)',
    xaxis_title='Time',
    yaxis_title='Value',
    height=800,
)

# Show the plot
fig.show()