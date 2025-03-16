import customtkinter as ctk
import math

from Main_Code_2 import Calculate_Possible_Combinations
from Set_Default_Values import Set_Default_Values_For_GUI, Values_From_Boxes
from Entry_boxes_and_sliders import Make_Entry_boxes_and_sliders
# Create the main window
app = ctk.CTk()
app.title("Engineering Tool")
app.geometry("1250x650")


# Function to calculate based on slider and input values
def calculate():
    print(car_data[2], car_data)

    # [float(EV_range.get()), float(total_energy.get()), float(Pack_mass.get()), float(Max_V.get()), float(Min_V.get()), float(Discharging_power.get()), float(Charging_power.get())]

    desired_EV_characteristics = [EV_range.get(), total_energy.get(), Pack_mass.get(), Max_V.get(), Min_V.get(), Discharging_power.get(), Charging_power.get()]
    slider_values = [float(EV_range_slider.get()), float(total_energy_slider.get()), float(Pack_mass_slider.get()), float(Max_V_slider.get()), float(Min_V_slider.get()),float(Discharging_power_slider.get()), float(Charging_power_slider.get())]
    
    EV_metrics = [EV_mass.get(), EV_drag.get(), EV_front_area.get(), EV_r_r.get()]
    EV_slider_values = [float(EV_mass_slider.get()), float(EV_drag_slider.get()), round(float(EV_front_area_slider.get()), 4), float(EV_r_r_slider.get())]
    # slider_values = [range_slider.get(), total_energy_slider.get(), Pack_mass_slider.get(), Max_V_slider.get(), Min_V_slider.get(), Discharging_power_slider.get(), Charging_power_slider.get()]


    for i in range(len(desired_EV_characteristics)):
        # print(desired_EV_characteristics[i])

        if desired_EV_characteristics[i] == "":
            desired_EV_characteristics[i] = slider_values[i]
        elif i == 0: 
            try: desired_EV_characteristics[i] = float(EV_range.get())
            except: print("non number entered in EV")
        elif i == 1: 
            try: desired_EV_characteristics[i] = float(total_energy.get())
            except: print("non number entered in energy")
        elif i == 2: 
            try: desired_EV_characteristics[i] = float(Pack_mass.get())
            except: print("non number entered in pack mass")
        elif i == 3: 
            try: desired_EV_characteristics[i] = float(Max_V.get())
            except: print("non number entered in max voltage")
        elif i == 4: 
            try: desired_EV_characteristics[i] = float(Min_V.get())
            except: print("non number entered in min voltage")
        elif i == 5: 
            try: desired_EV_characteristics[i] = float(Discharging_power.get())
            except: print("non number entered in discharging")
        elif i == 6: 
            try: desired_EV_characteristics[i] = float(Charging_power.get())
            except: 
                print("non number entered in charging")
        
    if desired_EV_characteristics[5] > desired_EV_characteristics[6]:
        print(desired_EV_characteristics[2])
        desired_EV_characteristics[2] = desired_EV_characteristics[2] - (math.ceil(desired_EV_characteristics[5]/37500) + 1) * 0.2
        print(desired_EV_characteristics[2])
    else:
        desired_EV_characteristics[2] = desired_EV_characteristics[2] - (math.ceil(desired_EV_characteristics[6]/37500) + 1) * 0.2

    for i in range(len(EV_metrics)):
        if EV_metrics[i] == "":
            EV_metrics[i] = EV_slider_values[i]
        elif i == 0: 
            try: EV_metrics[i] = float(EV_mass.get())
            except: print("non number entered in EV mass")
        elif i == 1: 
            try: EV_metrics[i] = float(EV_drag.get())
            except: print("non number entered in EV drag")
        elif i == 2: 
            try: EV_metrics[i] = float(EV_front_area.get())
            except: print("non number entered in EV frontal area")
        elif i == 3: 
            try: EV_metrics[i] = float(EV_r_r.get())
            except: 
                print("non number entered in EV rolling resistance")

    req_range = desired_EV_characteristics[0]
    req_energy = desired_EV_characteristics[1]
    req_max_mass_pack = desired_EV_characteristics[2]
    req_max_V = desired_EV_characteristics[3]
    req_min_V = desired_EV_characteristics[4]
    req_discharging_power = desired_EV_characteristics[5]
    req_charging_power = desired_EV_characteristics[6]


    # req_range, req_energy, req_discharging_power, req_max_V, req_min_V, req_max_mass_pack, req_charging_power = Values_From_Boxes(float(range.get()), float(total_energy.get()), float(Discharging_power.get()), float(Charging_power.get()), float(Max_V.get()), float(Min_V.get()), float(Pack_mass.get()), req_range, req_energy, req_discharging_power, req_max_V, req_min_V, req_max_mass_pack, req_charging_power)
    print(f"Reqired values: {desired_EV_characteristics}")
    print(f"EV values{EV_metrics}")
    

    best_weighted_normaliesed, max_range_row, max_discharging_row, max_charging_row, max_range_row_3_of_4 = Calculate_Possible_Combinations(req_energy, req_discharging_power, req_max_V, req_min_V, req_max_mass_pack, req_charging_power, EV_metrics)

    result_label.configure(text=f"Range: {best_weighted_normaliesed[10]:.2f} \n Minimum charging time: {best_weighted_normaliesed[11]:.2f}(mins)")

def non_number_message():
    # Create the label
    message_label = ctk.CTkLabel(app, text="Please enter a valid number", font=(None, 25), fg_color="red", text_color="black", 
                                 corner_radius=5, width=220, height=28)
    message_label.grid(row=9, column=3, columnspan=2, padx=10, pady=10)
    
    # Remove the label after 5 seconds
    app.after(2000, message_label.destroy)

# message_label = ctk.CTkLabel(app, text="Please enter a valid number", text_color="red", font=(None, 18))
# message_label.grid(row=9, column=3, columnspan=2, padx=10, pady=10)

# Function to update slider value label
def update_range_label(value):
    EV_range_label.configure(text=f"Range: {float(value):.0f}")

def update_total_energy_label(value):
    total_energy_label.configure(text=f"Energy: {float(value):.0f}")

def update_Pack_mass_label(value):
    Pack_mass_label.configure(text=f"Pack Mass: {float(value):.0f}")

def update_Max_V_label(value):
    Max_V_label.configure(text=f"Maximum Voltage: {float(value):.0f}")

def update_Min_V_label(value):
    Min_V_label.configure(text=f"Minimum Voltage: {float(value):.0f}")

def update_Discharging_power_label(value):
    Discharging_power_label.configure(text=f"Discharging Power: {float(value):.0f}")

def update_Charging_power_label(value):
    Charging_power_label.configure(text=f"Charging Power: {float(value):.0f}")

def update_EV_mass_label(value):
    EV_mass_label.configure(text=f"EV Mass: {float(value):.0f}")

def update_EV_drag_label(value):
    EV_drag_label.configure(text=f"EV Drag Coefficient: {float(value):.2f}")

def update_EV_front_area_label(value):
    EV_front_area_label.configure(text=f"EV Frontal Area: {float(value):.2f}")

def update_EV_r_r_label(value):
    EV_r_r_label.configure(text=f"EV Rolling Resistance: {float(value):.3f}")

def update_sliders(event=None):
    # if checkbox_Boxes_to_sliders.get() == 1:  # Check if the checkbox is ticked
        # desired_EV_characteristics = [EV_range.get(), total_energy.get(), Pack_mass.get(), Max_V.get(), Min_V.get(), Discharging_power.get(), Charging_power.get()]

    # for i in desired_EV_characteristics:
    try:
        value_EV_range_empty = EV_range.get()
        if value_EV_range_empty == "":
            EV_range_slider.set(input_range)
            update_range_label(input_range)
        else:
            try: 
                value_EV_range = float(EV_range.get())  # Get the value from the entry box
                if EV_range_slider._from_ <= value_EV_range <= EV_range_slider._to:  # Check if the value is within the slider's range
                    EV_range_slider.set(value_EV_range)  # Set the slider to the value
                    update_range_label(value_EV_range)
                else:
                    update_range_label(value_EV_range)

            except: 
                print("non number entered in EV range")
                non_number_message()
    
        value_total_energy_empty = total_energy.get()
        if value_total_energy_empty == "":
            total_energy_slider.set(input_energy)
            update_total_energy_label(input_energy)
        else:
            try: 
                value_total_energy = float(total_energy.get())
                if total_energy_slider._from_ <= value_total_energy <= total_energy_slider._to:
                    total_energy_slider.set(value_total_energy) 
                    update_total_energy_label(value_total_energy)
                else:
                    update_total_energy_label(value_total_energy)
            except: 
                print("non number entered in energy")
                non_number_message()

        value_Pack_mass_empty = Pack_mass.get()
        if value_Pack_mass_empty == "":
            Pack_mass_slider.set(input_max_mass_pack)
            update_Pack_mass_label(input_max_mass_pack)
        else:
            try:
                value_Pack_mass = float(Pack_mass.get())
                if Pack_mass_slider._from_ <= value_Pack_mass <= Pack_mass_slider._to:
                    Pack_mass_slider.set(value_Pack_mass) 
                    update_Pack_mass_label(value_Pack_mass)

                else:
                    update_Pack_mass_label(value_Pack_mass)
            except: 
                print("non number entered in mass")
                non_number_message()

        value_Max_V_empty = Max_V.get()
        if value_Max_V_empty == "":
            Max_V_slider.set(input_max_V)  # Assuming input_Max_V is a predefined default value
            update_Max_V_label(input_max_V)
        else:
            try:
                value_Max_V = float(Max_V.get())
                if Max_V_slider._from_ <= value_Max_V <= Max_V_slider._to:
                    Max_V_slider.set(value_Max_V)
                    update_Max_V_label(value_Max_V)
                else:
                    update_Max_V_label(value_Max_V)
            except:
                print("non number entered in Max_V")
                non_number_message()

        value_Min_V_empty = Min_V.get()
        if value_Min_V_empty == "":
            Min_V_slider.set(input_min_V)  # Assuming input_Min_V is a predefined default value
            update_Min_V_label(input_min_V)
        else:
            try:
                value_Min_V = float(Min_V.get())
                if Min_V_slider._from_ <= value_Min_V <= Min_V_slider._to:
                    Min_V_slider.set(value_Min_V)
                    update_Min_V_label(value_Min_V)
                else:
                    update_Min_V_label(value_Min_V)
            except:
                print("non number entered in Min_V")
                non_number_message()

        value_Discharging_power_empty = Discharging_power.get()
        if value_Discharging_power_empty == "":
            Discharging_power_slider.set(input_discharging_power)  # Assuming input_Discharging_power is a predefined default value
            update_Discharging_power_label(input_discharging_power)
        else:
            try:
                value_Discharging_power = float(Discharging_power.get())
                if Discharging_power_slider._from_ <= value_Discharging_power <= Discharging_power_slider._to:
                    Discharging_power_slider.set(value_Discharging_power)
                    update_Discharging_power_label(value_Discharging_power)
                else:
                    update_Discharging_power_label(value_Discharging_power)
            except:
                print("non number entered in Discharging_power")
                non_number_message()

        value_Charging_power_empty = Charging_power.get()
        if value_Charging_power_empty == "":
            Charging_power_slider.set(input_charging_power)  # Assuming input_Charging_power is a predefined default value
            update_Charging_power_label(input_charging_power)
        else:
            try:
                value_Charging_power = float(Charging_power.get())
                if Charging_power_slider._from_ <= value_Charging_power <= Charging_power_slider._to:
                    Charging_power_slider.set(value_Charging_power)
                    update_Charging_power_label(value_Charging_power)
                else:
                    update_Charging_power_label(value_Charging_power)
            except:
                print("non number entered in Charging_power")
                print(EV_mass.get())
                non_number_message()
        
        value_EV_mass = EV_mass.get()
        if value_EV_mass == "":
            EV_mass_slider.set(car_data[0])
            update_EV_mass_label(car_data[0])
        else:
            try: 
                value_EV_mass = float(EV_mass.get())  # Get the value from the entry box
                if EV_mass_slider._from_ <= value_EV_mass <= EV_mass_slider._to:  # Check if the value is within the slider's range
                    EV_mass_slider.set(value_EV_mass)  # Set the slider to the value
                    update_EV_mass_label(value_EV_mass)
                else:
                    update_EV_mass_label(value_EV_mass)

            except: 
                print("non number entered in EV mass")
                non_number_message()
        
        value_EV_drag = EV_drag.get()
        if value_EV_drag == "":
            EV_drag_slider.set(car_data[1])
            update_EV_drag_label(car_data[1])
        else:
            try: 
                value_EV_drag = float(EV_drag.get())  # Get the value from the entry box
                if EV_drag_slider._from_ <= value_EV_drag <= EV_drag_slider._to:  # Check if the value is within the slider's range
                    EV_drag_slider.set(value_EV_drag)  # Set the slider to the value
                    update_EV_drag_label(value_EV_drag)
                else:
                    update_EV_drag_label(value_EV_drag)

            except: 
                print("non number entered in EV drag")
                non_number_message()

        value_EV_front_area = EV_front_area.get()
        if value_EV_front_area == "":
            EV_front_area_slider.set(car_data[2])
            update_EV_front_area_label(car_data[2])
        else:
            try: 
                value_EV_front_area = float(EV_front_area.get())  # Get the value from the entry box
                if EV_front_area_slider._from_ <= value_EV_front_area <= EV_front_area_slider._to:  # Check if the value is within the slider's range
                    EV_front_area_slider.set(value_EV_front_area)  # Set the slider to the value
                    update_EV_front_area_label(value_EV_front_area)
                else:
                    update_EV_front_area_label(value_EV_front_area) 

            except: 
                print("non number entered in EV frontal area")
                non_number_message()

        value_EV_r_r = EV_r_r.get()
        if value_EV_r_r == "":
            EV_r_r_slider.set(car_data[3])
            update_EV_r_r_label(car_data[3])
        else:
            try: 
                value_EV_r_r = float(EV_r_r.get())  # Get the value from the entry box
                if EV_r_r_slider._from_ <= value_EV_r_r <= EV_r_r_slider._to:  # Check if the value is within the slider's range
                    EV_r_r_slider.set(value_EV_r_r)  # Set the slider to the value
                    update_EV_r_r_label(value_EV_r_r)
                else:
                    update_EV_r_r_label(value_EV_r_r)

            except: 
                print("non number entered in EV rolling resistance")
                non_number_message()

    except ValueError:
        print("Invalid input 2. Please enter a number.")


desired_EV_label = ctk.CTkLabel(app, text="Please enter desired EV chracteristics values or adjust slider:")
desired_EV_label.grid(row=0, column= 1, columnspan=2, padx=20, pady=10)
EV_metrics_label = ctk.CTkLabel(app, text="Please enter EV metrics values or adjust slider:")
EV_metrics_label.grid(row=0, column= 3, columnspan=2, padx=20, pady=10)

# Nissan Leaf
input_range = 170
input_energy = 28000
input_discharging_power = 90000
input_max_V = 400
input_min_V = 240
input_max_mass_battery = 185.5
input_max_mass_pack = 315
input_charging_power = 50000

# car_data = [3100, 0.3, 3.38, 0.015, 0] # Rivian R1T             Actual: 505, Calculated: 508
# car_data = [1748, 0.29, 2.37, 0.015, 0] # Kia Niro EV         Actual: 384, Calculated: 405
car_data = [1486, 0.28, 2.32, 0.015, 0] # Nissan Leaf         Actual: 169(excel)/135, Calculated: 179 Using 2 chems: 310
# car_data = [1830, 0.23, 2.268, 0.015, 0] # Tesla model 3      Actual: 576, Calculated: 572
# car_data = [2584, 0.29, 2.3, 0.015, 0] # Polestar 3              Actual: 482, Calculated: 532

# # Normal input values
# input_range = 500
# input_energy = 75000
# input_discharging_power = 250000
# input_max_V = 450
# input_min_V = 280
# input_max_mass_battery = 320
# input_max_mass_pack = 500
# input_charging_power = 150000

# # Initial car data
# car_data[2000, 0.29, 2.35, 0.015]

# Total Energy
total_energy = ctk.CTkEntry(app, placeholder_text="Total Energy", width=160, height=28)
total_energy.grid(row= 3, column= 1, padx=10, pady=10)
total_energy_slider = ctk.CTkSlider(app, from_= 0, to=150000, number_of_steps=150)
total_energy_slider.grid(row= 3, column=2, padx=10, pady=10)
total_energy_slider.set(input_energy)
# total_energy_slider.configure(command=update_total_energy_label)
total_energy_label = ctk.CTkLabel(app, text=input_energy)
total_energy_label.grid(row= 4, column=2)

# Desired EV characteristics
EV_range, EV_range_slider, EV_range_label = Make_Entry_boxes_and_sliders(app, f"Range: ", input_range, 1, 2, 1000, 500, 0, 200, "Range (km)")
total_energy, total_energy_slider, total_energy_label = Make_Entry_boxes_and_sliders(app, f"Energy: ", input_energy, 3, 2, 150000, 75000, 0, 150, "Total Energy (Wh)")
Pack_mass, Pack_mass_slider, Pack_mass_label = Make_Entry_boxes_and_sliders(app, f"Pack Mass: ", input_max_mass_pack, 5, 2, 1000, 500, 0, 200, "Pack Mass (kg)")
Max_V, Max_V_slider, Max_V_label = Make_Entry_boxes_and_sliders(app, f"Maximum Voltage: ", input_max_V, 7, 2, 1000, 500, 0, 200, "Maximum Voltage (V)")
Min_V, Min_V_slider, Min_V_label = Make_Entry_boxes_and_sliders(app, f"Minimum Voltage: ", input_min_V, 9, 2, 600, 300, 0, 120, "Minimum Voltage (V)")
Discharging_power, Discharging_power_slider, Discharging_power_label = Make_Entry_boxes_and_sliders(app, f"Discharging Power: ", input_discharging_power, 11, 2, 500000, 250000, 0, 500, "Peak Discharging Power (W)")
Charging_power, Charging_power_slider, Charging_power_label = Make_Entry_boxes_and_sliders(app, f"Charging Power: ", input_charging_power, 13, 2, 300000, 150000, 0, 300, "Peak Charging Power (W)")

EV_range_slider.configure(command=update_range_label)
total_energy_slider.configure(command=update_total_energy_label)
Pack_mass_slider.configure(command=update_Pack_mass_label)
Max_V_slider.configure(command=update_Max_V_label)
Min_V_slider.configure(command=update_Min_V_label)
Discharging_power_slider.configure(command=update_Discharging_power_label)
Charging_power_slider.configure(command=update_Charging_power_label)

# EV metrics

# Total Energy
EV_mass = ctk.CTkEntry(app, placeholder_text="EV Mass (kg)", width=160, height=28)
EV_mass.grid(row= 1, column= 3, padx=10, pady=10)
EV_mass_slider = ctk.CTkSlider(app, from_= 0, to=5000, number_of_steps=2500)
EV_mass_slider.grid(row= 1, column=4, padx=10, pady=10)
EV_mass_slider.set(car_data[0])
# total_energy_slider.configure(command=update_total_energy_label)
EV_mass_label = ctk.CTkLabel(app, text=car_data[0])
EV_mass_label.grid(row= 2, column=4)

# EV mass without battery pack
EV_mass, EV_mass_slider, EV_mass_label = Make_Entry_boxes_and_sliders(app, f"EV Mass: ", car_data[0], 1, 4, 5000, 2500, 0, 1000, "EV Mass (kg)")
EV_mass_slider.configure(command=update_EV_mass_label)
# EV drag coefficient
EV_drag, EV_drag_slider, EV_drag_label = Make_Entry_boxes_and_sliders(app, f"EV Drag Coefficient: ", car_data[1], 3, 4, 1, 0.5, 0, 100, "EV Drag Coefficient")
EV_drag_slider.configure(command=update_EV_drag_label)
# EV frontal area
EV_front_area, EV_front_area_slider, EV_front_area_label = Make_Entry_boxes_and_sliders(app, f"EV Frontal Area: ", car_data[2], 5, 4, 5, 2.5, 0, 200, "EV Frontal Area (m²)")
EV_front_area_slider.configure(command=update_EV_front_area_label)
# EV rolling resistance
EV_r_r, EV_r_r_slider, EV_r_r_label = Make_Entry_boxes_and_sliders(app, f"EV Rolling Resistance: ", car_data[3], 7, 4, 0.04, 0.015, 0, 40, "EV Rolling Resistance (N)")
EV_r_r_slider.configure(command=update_EV_r_r_label)




# Create a button to calculate the result
calc_button = ctk.CTkButton(app, text="Calculate", command=calculate)
calc_button.grid(row= 10, column= 5, padx=10, pady=0)


EV_range.bind("<KeyRelease>", update_sliders)
total_energy.bind("<KeyRelease>", update_sliders)  
Pack_mass.bind("<KeyRelease>", update_sliders)
Max_V.bind("<KeyRelease>", update_sliders)  
Min_V.bind("<KeyRelease>", update_sliders)
Discharging_power.bind("<KeyRelease>", update_sliders)  
Charging_power.bind("<KeyRelease>", update_sliders)
EV_mass.bind("<KeyRelease>", update_sliders)
EV_drag.bind("<KeyRelease>", update_sliders)
EV_front_area.bind("<KeyRelease>", update_sliders)
EV_r_r.bind("<KeyRelease>", update_sliders)

checkbox_Boxes_to_sliders = ctk.CTkCheckBox(app, text="Transfer numbers entered to sliders?", command=update_sliders, variable=ctk.IntVar(value=1))
checkbox_Boxes_to_sliders.grid(row=20, column=1, padx=(5, 5), pady=(0, 0), sticky="w")
checkbox_disclamer_label = ctk.CTkLabel(app, text="If un-checked the program will\nuse the box values as default  ")
checkbox_disclamer_label.grid(row= 21, column= 1, padx=10, pady=0)



# Create a label to display the result
result_label = ctk.CTkLabel(app, text="")
result_label.grid(row= 11, column= 5, padx=10, pady=10)

# Start the main event loop
app.mainloop()

