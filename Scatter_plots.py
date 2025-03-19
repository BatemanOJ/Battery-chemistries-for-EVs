import customtkinter as ctk
import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_scatter(successful_combinations_1_bat, successful_combinations_2_bat):
    print(f"Trying to scatter")
    
    if successful_combinations_1_bat != None and successful_combinations_2_bat != None:
        range_data_bat_1 = [row[10] for row in successful_combinations_1_bat]
        charging_data_bat_1 = [row[11] for row in successful_combinations_1_bat]
        range_data_bat_2 = [row[10] for row in successful_combinations_2_bat]
        charging_data_bat_2 = [row[11] for row in successful_combinations_2_bat]

        plot_window = ctk.CTkToplevel()
        plot_window.title("Range vs. Minimum Charging Time")
        plot_window.geometry("500x400")
        
        # Create a new figure
        fig, ax = plt.subplots()
        ax.scatter(range_data_bat_1, charging_data_bat_1, color='red', label='1 Battery Options')
        ax.scatter(range_data_bat_2, charging_data_bat_2, color='blue', label='2 Battery Options')
        
        ax.set_title("Range vs. Minimum Charging Time")
        ax.set_xlabel("Range (km)")
        ax.set_ylabel("Minimum charging time (10-80%) (mins)")
        ax.legend()

        # Embed the plot in the GUI
        canvas = FigureCanvasTkAgg(fig, master=plot_window)  # Embed in the frame
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, pady=10, padx=10)

    else:
        print("No data to plot")