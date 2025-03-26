import customtkinter as ctk
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def plot_scatter(successful_combinations_1_bat, successful_combinations_2_bat):
    
    if successful_combinations_1_bat != None or successful_combinations_2_bat != None:
        range_data_bat_1 = [row[10] for row in successful_combinations_1_bat]
        charging_data_bat_1 = [row[11] for row in successful_combinations_1_bat]
        range_data_bat_2 = [row[10] for row in successful_combinations_2_bat]
        charging_data_bat_2 = [row[11] for row in successful_combinations_2_bat]

        plot_window = ctk.CTkToplevel()
        plot_window.title("Range vs. Minimum Charging Time")
        plot_window.geometry("750x600")
        
        # Create a new figure
        fig, ax = plt.subplots()
        # print(len(range_data_bat_1), len(charging_data_bat_1))
        # print(len(range_data_bat_2), len(charging_data_bat_2))
        ax.scatter(range_data_bat_1, charging_data_bat_1, color='red', label='1 Battery Options')
        ax.scatter(range_data_bat_2, charging_data_bat_2, color='blue', label='2 Battery Options')
        
        ax.set_title("Range vs. Minimum Charging Time")
        ax.set_xlabel("Range (km)")
        ax.set_ylabel("Minimum charging time (10-80%) (mins)")
        ax.legend()

        # Embed the plot in the GUI
        canvas = FigureCanvasTkAgg(fig, master=plot_window)  # Embed in the app
        canvas.draw()
        canvas.get_tk_widget().pack(pady=10, padx=10)

        # range_data_all = np.array(range_data_bat_2 + range_data_bat_1)
        range_data_all = range_data_bat_2
        range_data_all.extend(range_data_bat_1)
        charging_data_all = charging_data_bat_2
        charging_data_all.extend(charging_data_bat_1)
        # range_data_all = np.array(range_data_all)
        print(f"range_data_all: {len(range_data_all)}, charging_data_all: {len(charging_data_all)}")

        index_max_range_row = range_data_all.index(max(range_data_all))
        print(f"max range row: {charging_data_all[index_max_range_row]}")

        index_min_charging_row = charging_data_all.index(min(charging_data_all))
        print(f"max range row: {range_data_all[index_min_charging_row]}")

        
        
        print(range_data_all[-2:])
        print(range_data_bat_1)

        # Hover label
        hover_label = ctk.CTkLabel(plot_window, text="")
        hover_label.pack(pady=10)
        # Click label
        click_label = ctk.CTkLabel(plot_window, text="Click on a point to see details")
        click_label.pack(pady=10)

        canvas.mpl_connect("button_press_event", lambda event: on_click(event, ax, range_data_all, charging_data_all, click_label))   # Click on a point
        # canvas.mpl_connect("motion_notify_event", lambda event: on_hover(event, ax, range_data_all, charging_data_all, hover_label))  # Hover over a point  

    else:
        print("No data to plot")


def on_click(event, ax, range_data_all, charging_data_all, click_label: ctk.CTkLabel):
    if event.inaxes == ax:
        # Find closest point
        distances = np.sqrt((range_data_all - event.xdata) ** 2 + (charging_data_all - event.ydata) ** 2)
        index = np.argmin(distances)
        print(f"Index: {index}\nRange: {range_data_all[index]:.1f}, Charging Time: {charging_data_all[index]:.1f}\nRange clicked: {event.xdata:.1f}, Charging Time clicked: {event.ydata:.1f}")
        click_label.configure(text=f"Range: {range_data_all[index]:.1f}\nCharging Time: {charging_data_all[index]:.1f}")



# def on_hover(event, ax, range_data_all, charging_data_all, hover_label: ctk.CTkLabel):
#     if event.inaxes == ax:
#         distances = np.sqrt((range_data_all - event.xdata) ** 2 + (charging_data_all - event.ydata) ** 2)
#         index = np.argmin(distances)
#         if distances[index] < 5:  # Adjust sensitivity as needed
#             hover_label.configure(text=f"Range: {range_data_all[index]:.1f}\nCharging Time: {charging_data_all[index]:.1f}")
#         else:
#             hover_label.configure(text="")


# def plot_scatter(successful_combinations_1_bat, successful_combinations_2_bat):
    
#     if successful_combinations_1_bat != None or successful_combinations_2_bat != None:
#         range_data_bat_1 = [row[10] for row in successful_combinations_1_bat]
#         charging_data_bat_1 = [row[11] for row in successful_combinations_1_bat]
#         range_data_bat_2 = [row[10] for row in successful_combinations_2_bat]
#         charging_data_bat_2 = [row[11] for row in successful_combinations_2_bat]

#         plot_window = ctk.CTkToplevel()
#         plot_window.title("Range vs. Minimum Charging Time")
#         plot_window.geometry("500x400")
        
#         # Create a new figure
#         fig, ax = plt.subplots()
#         ax.scatter(range_data_bat_1, charging_data_bat_1, color='red', label='1 Battery Options')
#         ax.scatter(range_data_bat_2, charging_data_bat_2, color='blue', label='2 Battery Options')
        
#         ax.set_title("Range vs. Minimum Charging Time")
#         ax.set_xlabel("Range (km)")
#         ax.set_ylabel("Minimum charging time (10-80%) (mins)")
#         ax.legend()

#         # Embed the plot in the GUI
#         canvas = FigureCanvasTkAgg(fig, master=plot_window)  # Embed in the frame
#         canvas.draw()
#         canvas.get_tk_widget().grid(row=1, column=0, pady=10, padx=10)

#     else:
#         print("No data to plot")