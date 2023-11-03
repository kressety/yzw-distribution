import numpy as np
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display

months_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def plot(yzw_distribution, test_total, test_zero_months, test_higher_months, test_performance, test_noise, test_purging):
    # Define the plotting function
    fig = go.FigureWidget(data=[go.Bar(x=months_labels, y=yzw_distribution(test_total, test_zero_months, test_higher_months, test_performance, test_noise, test_purging))])
    fig.update_layout(title="YZW Distribution", xaxis_title="Month", yaxis_title="Value")

    # Define the update function
    def update_plot(total, zero_months, higher_months, performance, noise, purging):
        new_y = yzw_distribution(total, [months_labels.index(x) for x in zero_months], [months_labels.index(x) for x in higher_months], performance, noise, purging)
        fig.data[0].y = new_y

    # Create widgets
    total_slider = widgets.IntSlider(value=test_total, min=1000, max=1000000, step=1000, description='Total:')
    performance_slider = widgets.FloatSlider(value=test_performance, min=0.1, max=5, step=0.1, description='Performance:')
    noise_slider = widgets.FloatSlider(value=test_noise, min=0, max=0.5, step=0.01, description='Noise:')
    zero_months_selector = widgets.SelectMultiple(options=months_labels, value=[months_labels[index] for index in test_zero_months], description='Zero Months:')
    higher_months_selector = widgets.SelectMultiple(options=months_labels, value=[months_labels[index] for index in test_higher_months], description='Higher Months:')
    purging_checkbox = widgets.Checkbox(value=test_purging, description='Purging')

    # Display widgets and link to the update function
    ui = widgets.interactive(
        update_plot, 
        total=total_slider, 
        zero_months=zero_months_selector,
        higher_months=higher_months_selector,
        performance=performance_slider,
        noise=noise_slider,
        purging=purging_checkbox
    )

    ui.layout.height = 'auto'
    ui = widgets.HBox([ui, fig])
    display(ui)
