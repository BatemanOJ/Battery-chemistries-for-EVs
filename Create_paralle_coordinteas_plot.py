import customtkinter as ctk
import math
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_parallel_coordinates_plot():
    # Generate some sample data
    df = pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': np.random.rand(100),
        'D': np.random.rand(100),
        'E': np.random.rand(100)
    })

    fig = px.parallel_coordinates(df, 
                              dimensions=['A', 'B', 'C', 'D', 'E'],
                              color='A',
                              color_continuous_scale=px.colors.diverging.Tealrose)
    fig.show()

create_parallel_coordinates_plot()