import customtkinter as ctk


from Main_Code_2 import Calculate_Possible_Combinations
from Set_Default_Values import Set_Default_Values_For_GUI, Values_From_Boxes
from Entry_boxes_and_sliders import Make_Entry_boxes_and_sliders
# Create the main window
app = ctk.CTk()
app.title("Engineering Tool")
app.geometry("1250x600")


# Function to calculate based on slider and input values
def calculate():
    # range = float(entry1.get())
    # Max_V = float(entry1.get())
    # Min_V = float(entry1.get())
    # Total_Energy = float(entry1.get())
    # Charging_Power = float(entry1.get())
    # Discharging_Power = float(entry1.get())
    # Pack_Mass = float(entry1.get())

    # Check values entered into boxes
    # try: 
    #     entered_box_values = [float(EV_range.get()), float(total_energy.get()), float(Pack_mass.get()), float(Max_V.get()), float(Min_V.get()), float(Discharging_power.get()), float(Charging_power.get())]
    # except ValueError:
    #         print("Invalid input 2. Please enter a number.")

    entered_box_values = [EV_range.get(), total_energy.get(), Pack_mass.get(), Max_V.get(), Min_V.get(), Discharging_power.get(), Charging_power.get()]
    slider_values = [float(EV_range_slider.get()), float(total_energy_slider.get()), float(Pack_mass_slider.get()), float(Max_V_slider.get()), float(Min_V_slider.get()),float(Discharging_power_slider.get()), float(Charging_power_slider.get())]
    # slider_values = [range_slider.get(), total_energy_slider.get(), Pack_mass_slider.get(), Max_V_slider.get(), Min_V_slider.get(), Discharging_power_slider.get(), Charging_power_slider.get()]

    for i in range(len(entered_box_values)):
        # print(entered_box_values[i])

        if entered_box_values[i] == "":
            entered_box_values[i] = slider_values[i]
        elif i == 0: 
            try: entered_box_values[i] = float(EV_range.get())
            except: print("non number entered in EV")
        elif i == 1: 
            try: entered_box_values[i] = float(total_energy.get())
            except: print("non number entered in energy")
        elif i == 2: 
            try: entered_box_values[i] = float(Pack_mass.get())
            except: print("non number entered in pack mass")
        elif i == 3: 
            try: entered_box_values[i] = float(Max_V.get())
            except: print("non number entered in max voltage")
        elif i == 4: 
            try: entered_box_values[i] = float(Min_V.get())
            except: print("non number entered in min voltage")
        elif i == 5: 
            try: entered_box_values[i] = float(Discharging_power.get())
            except: print("non number entered in discharging")
        elif i == 6: 
            try: entered_box_values[i] = float(Charging_power.get())
            except: print("non number entered in charging")
        
        # if 0 < entered_box_values[i] < 1000000:
        #     print("non number entered")
        #     # Change this to print a label at the bottom of the GUI saying not a number
    
    # print(entered_box_values)

    req_range = entered_box_values[0]
    req_energy = entered_box_values[1]
    req_max_mass_pack = entered_box_values[2]
    req_max_V = entered_box_values[3]
    req_min_V = entered_box_values[4]
    req_discharging_power = entered_box_values[5]
    req_charging_power = entered_box_values[6]

    # req_range = float(range.get())
    # req_energy = float(total_energy.get())
    # req_discharging_power = float(Discharging_power.get())
    # req_charging_power = float(Charging_power.get())
    # req_max_V = float(Max_V.get())
    # req_min_V = float(Min_V.get())
    # req_max_mass_pack = float(Pack_mass.get())
    


    # req_range, req_energy, req_discharging_power, req_max_V, req_min_V, req_max_mass_pack, req_charging_power = Values_From_Boxes(float(range.get()), float(total_energy.get()), float(Discharging_power.get()), float(Charging_power.get()), float(Max_V.get()), float(Min_V.get()), float(Pack_mass.get()), req_range, req_energy, req_discharging_power, req_max_V, req_min_V, req_max_mass_pack, req_charging_power)
    print(f"Reqired values: {req_range, req_energy, req_discharging_power, req_max_V, req_min_V, req_max_mass_pack, req_charging_power}")
    

    output_range, fast_charging_time, battery_numbers, battery_data = Calculate_Possible_Combinations(req_energy, req_discharging_power, req_max_V, req_min_V, req_max_mass_pack, req_charging_power)

    result_label.configure(text=f"Range: {output_range:.2f} \n Minimum charging time: {fast_charging_time:.2f}")


# Function to update slider value label
def update_range_label(value):
    EV_range_label.configure(text=f"Range: {float(value):.0f}")

def update_total_energy_label(value):
    total_energy_label.configure(text=f"Energy: {float(value):.0f}")

def update_Pack_mass_label(value):
    Pack_mass_label.configure(text=f"Mass: {float(value):.0f}")

def update_Max_V_label(value):
    Max_V_label.configure(text=f"Maximum Voltage: {float(value):.0f}")

def update_Min_V_label(value):
    Min_V_label.configure(text=f"Minimum Voltage: {float(value):.0f}")

def update_Discharging_power_label(value):
    Discharging_power_label.configure(text=f"Discharging Power:{float(value):.0f}")

def update_Charging_power_label(value):
    Charging_power_label.configure(text=f"Charging Power: {float(value):.0f}")

def update_EV_mass_label(value):
    EV_mass_label.configure(text=f"EV Mass: {float(value):.0f}")

def update_sliders(event=None):
    # if checkbox_Boxes_to_sliders.get() == 1:  # Check if the checkbox is ticked
        # entered_box_values = [EV_range.get(), total_energy.get(), Pack_mass.get(), Max_V.get(), Min_V.get(), Discharging_power.get(), Charging_power.get()]

    # for i in entered_box_values:
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

            except: print("non number entered in EV")
    
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
            except: print("non number entered in energy")

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
            except: print("non number entered in mass")

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

    except ValueError:
        print("Invalid input 2. Please enter a number.")

label = ctk.CTkLabel(
    app,
    text="Please enter desired EV chracteristics values or adjust slider:"
    # fg_color="blue",
    # corner_radius=10
)

# Place the label in the window
label.grid(row=0, column= 1, columnspan=2, padx=20, pady=10)

# Nissan Leaf
input_range = 170
input_energy = 28000
input_discharging_power = 90000
input_max_V = 400
input_min_V = 240
input_max_mass_battery = 185.5
input_max_mass_pack = 315
input_charging_power = 50000

# # Normal input values
# input_range = 500
# input_energy = 75000
# input_discharging_power = 250000
# input_max_V = 450
# input_min_V = 280
# input_max_mass_battery = 320
# input_max_mass_pack = 500
# input_charging_power = 150000

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
Pack_mass, Pack_mass_slider, Pack_mass_label = Make_Entry_boxes_and_sliders(app, f"Mass: ", input_max_mass_pack, 5, 2, 1000, 500, 0, 200, "Pack Mass (kg)")
Max_V, Max_V_slider, Max_V_label = Make_Entry_boxes_and_sliders(app, f"Maximum Voltage: ", input_max_V, 7, 2, 1000, 500, 0, 200, "Maximum Voltage (V)")
Min_V, Min_V_slider, Min_V_label = Make_Entry_boxes_and_sliders(app, f"Minimum Voltage ", input_min_V, 9, 2, 600, 300, 0, 120, "Minimum Voltage (V)")
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
# EV mass without battery pack
EV_mass, EV_mass_slider, EV_mass_label = Make_Entry_boxes_and_sliders(app, f"EV Mass: ", input_range, 1, 4, 5000, 2500, 0, 1000, "EV Mass (kg)")
EV_mass_slider.configure(command=update_range_label)



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

checkbox_Boxes_to_sliders = ctk.CTkCheckBox(app, text="Transfer numbers entered to sliders?", command=update_sliders, variable=ctk.IntVar(value=1))
checkbox_Boxes_to_sliders.grid(row=20, column=1, padx=(5, 5), pady=(0, 0), sticky="w")
checkbox_disclamer_label = ctk.CTkLabel(app, text="If un-checked the program will\nuse the box values as default  ")
checkbox_disclamer_label.grid(row= 21, column= 1, padx=10, pady=0)



# Create a label to display the result
result_label = ctk.CTkLabel(app, text="Result: ")
result_label.grid(row= 11, column= 5, padx=10, pady=10)

# Start the main event loop
app.mainloop()

