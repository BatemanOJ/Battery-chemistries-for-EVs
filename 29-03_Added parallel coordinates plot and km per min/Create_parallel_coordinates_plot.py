import customtkinter as ctk
import math
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def create_parallel_coordinates_plot(successful_combinations):
    # Generate some sample data

    transposed_data = [list(t) for t in zip(*successful_combinations)]
    # print(transposed_data[10])

    list_km_per_min = []
    for i in range(0, len(successful_combinations)):
        km_per_min = (0.8*successful_combinations[i][10] - 0.1*successful_combinations[i][10])/successful_combinations[i][11]
        list_km_per_min.append(km_per_min)

    Range = np.array(transposed_data[10])
    km_per_min = np.array(list_km_per_min)
    Max_discharging_power = np.array(transposed_data[7])
    Min_pack_mass = np.array(transposed_data[8])

    print(f"km_per_min: {km_per_min}")

    df = pd.DataFrame({
        'Range': Range,
        'Charging km/min (10-80%)': km_per_min, 
        'Max discharging power': Max_discharging_power,
        'Min pack mass': Min_pack_mass
    })

    df_test = pd.DataFrame({
        'A': np.random.rand(100),
        'B': np.random.rand(100),
        'C': np.random.rand(100),
        'D': np.random.rand(100),
        'E': np.random.rand(100)
    })

    fig = px.parallel_coordinates(df, 
                              dimensions=['Range (km)', 'Charging speed (km/min)', 'Max discharging power (W)', 'Min pack mass(kg)'],
                              color='Range',
                              color_continuous_scale=px.colors.diverging.Tealrose)
    fig.show()
    fig_test = px.parallel_coordinates(df_test, 
                              dimensions=['A', 'B', 'C', 'D', 'E'],
                              color='A',
                              color_continuous_scale=px.colors.diverging.Tealrose)
    # fig_test.show()

# create_parallel_coordinates_plot()