import customtkinter as ctk


from Main_Code_2 import Calculate_Possible_Combinations
from Set_Default_Values import Set_Default_Values_For_GUI, Values_From_Boxes

# Create the main window
app = ctk.CTk()
app.title("Engineering Tool")
app.geometry("750x700")


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
    entered_box_values = [EV_range.get(), total_energy.get(), Pack_mass.get(), Max_V.get(), Min_V.get(), Discharging_power.get(), Charging_power.get()]
    slider_values = [range_slider.get(), total_energy_slider.get(), Pack_mass_slider.get(), Max_V_slider.get(), Min_V_slider.get(), Discharging_power_slider.get(), Charging_power_slider.get()]

    for i in range(len(entered_box_values)):
        # print(entered_box_values[i])

        if entered_box_values[i] == '':
            entered_box_values[i] = slider_values[i]
        
        if not isinstance(entered_box_values[i], (int, float)):
            print("non number entered")
            # Change this to print a label at the bottom of the GUI saying not a number
    
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
    
    

    output_range, fast_charging_time, battery_numbers, battery_data = Calculate_Possible_Combinations(req_energy, req_discharging_power, req_max_V, req_min_V, req_max_mass_pack, req_charging_power)

    result_label.configure(text=f"Range: {output_range:.2f} \n Minimum charging time: {fast_charging_time:.2f}")


# Function to update slider value label
def update_range_label(value):
    range_label.configure(text=f"{float(value):.0f}")

def update_total_energy_label(value):
    total_energy_label.configure(text=f"{float(value):.0f}")

def update_Pack_mass_label(value):
    Pack_mass_label.configure(text=f"{float(value):.0f}")

def update_Max_V_label(value):
    Max_V_label.configure(text=f"{float(value):.0f}")

def update_Min_V_label(value):
    Min_V_label.configure(text=f"{float(value):.0f}")

def update_Discharging_power_label(value):
    Discharging_power_label.configure(text=f"{float(value):.0f}")

def update_Charging_power_label(value):
    Charging_power_label.configure(text=f"{float(value):.0f}")

def update_sliders(event=None):
    if checkbox_Boxes_to_sliders.get() == 1:  # Check if the checkbox is ticked
        # entered_box_values = [EV_range.get(), total_energy.get(), Pack_mass.get(), Max_V.get(), Min_V.get(), Discharging_power.get(), Charging_power.get()]

        # for i in entered_box_values:
        try:
            value_EV_range_empty = EV_range.get()
            if value_EV_range_empty == "":
                range_slider.set(range_slider.get())
            else:
                value_EV_range = float(EV_range.get())  # Get the value from the entry box
                if range_slider._from_ <= value_EV_range <= range_slider._to:  # Check if the value is within the slider's range
                    range_slider.set(value_EV_range)  # Set the slider to the value
                else:
                    print("EV_range Value is out of range.")
        
            value_total_energy_empty = total_energy.get()
            if value_total_energy_empty == "":
                total_energy_slider.set(total_energy_slider.get())
            else:
                value_total_energy = float(total_energy.get())
                if total_energy_slider._from_ <= value_total_energy <= total_energy_slider._to:
                    total_energy_slider.set(value_total_energy) 
                else:
                    print("energy Value is out of range.")

            value_Pack_mass_empty = Pack_mass.get()
            if value_Pack_mass_empty == "":
                Pack_mass_slider.set(Pack_mass_slider.get())
            else:
                value_Pack_mass = float(Pack_mass.get())
                if Pack_mass_slider._from_ <= value_Pack_mass <= Pack_mass_slider._to:
                    Pack_mass_slider.set(value_Pack_mass) 
                else:
                    print("energy Value is out of range.")

            value_Max_V_empty = Max_V.get()
            if value_Max_V_empty == "":
                Max_V_slider.set(Max_V_slider.get())
            else:
                value_Max_V = float(Max_V.get())
                if Max_V_slider._from_ <= value_Max_V <= Max_V_slider._to:
                    Max_V_slider.set(value_Max_V) 
                else:
                    print("energy Value is out of range.")

            value_Min_V_empty = Min_V.get()
            if value_Min_V_empty == "":
                Min_V_slider.set(Min_V_slider.get())
            else:
                value_Min_V = float(Min_V.get())
                if Min_V_slider._from_ <= value_Min_V <= Min_V_slider._to:
                    Min_V_slider.set(value_Min_V) 
                else:
                    print("energy Value is out of range.")

            value_Discharging_power_empty = Discharging_power.get()
            if value_Discharging_power_empty == "":
                Discharging_power_slider.set(Discharging_power_slider.get())
            else:
                value_Discharging_power = float(Discharging_power.get())
                if Discharging_power_slider._from_ <= value_Discharging_power <= Discharging_power_slider._to:
                    Discharging_power_slider.set(value_Discharging_power) 
                else:
                    print("energy Value is out of range.")

            value_Charging_power_empty = Charging_power.get()
            if value_Charging_power_empty == "":
                Charging_power_slider.set(Charging_power_slider.get())
            else:
                value_Charging_power = float(Charging_power.get())
                if Charging_power_slider._from_ <= value_Charging_power <= Charging_power_slider._to:
                    Charging_power_slider.set(value_Charging_power) 
                else:
                    print("energy Value is out of range.")

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
input_range = 169
input_energy = 27700
input_discharging_power = 90000
input_max_V = 398
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

# Create input field for direct numeric entry
# Range
EV_range = ctk.CTkEntry(app, placeholder_text="Range", width=160, height=28)
EV_range.grid(row= 1, column= 1, padx=10, pady=10)
range_slider = ctk.CTkSlider(app, from_=0, to=1000, number_of_steps=200)
range_slider.grid(row= 1, column=2, padx=10, pady=10)
range_slider.set(input_range)
range_slider.configure(command=update_range_label)
range_label = ctk.CTkLabel(app, text=input_range)
range_label.grid(row=2, column=2)

# Total Energy
total_energy = ctk.CTkEntry(app, placeholder_text="Total Energy", width=160, height=28)
total_energy.grid(row= 3, column= 1, padx=10, pady=10)
total_energy_slider = ctk.CTkSlider(app, from_= 0, to=150000, number_of_steps=150)
total_energy_slider.grid(row= 3, column=2, padx=10, pady=10)
total_energy_slider.set(input_energy)
total_energy_slider.configure(command=update_total_energy_label)
total_energy_label = ctk.CTkLabel(app, text=input_energy)
total_energy_label.grid(row= 4, column=2)

Pack_mass = ctk.CTkEntry(app, placeholder_text="Pack Mass", width=160, height=28)
Pack_mass.grid(row= 5, column= 1, padx=10, pady=10)
Pack_mass_slider = ctk.CTkSlider(app, from_=0, to=1000, number_of_steps=200)
Pack_mass_slider.grid(row= 5, column=2, padx=10, pady=10)
Pack_mass_slider.set(input_max_mass_pack)
Pack_mass_slider.configure(command=update_Pack_mass_label)
Pack_mass_label = ctk.CTkLabel(app, text=input_max_mass_pack)
Pack_mass_label.grid(row= 6, column=2)

Max_V = ctk.CTkEntry(app, placeholder_text="Maximum Voltage", width=160, height=28)
Max_V.grid(row= 7, column= 1, padx=10, pady=10)
Max_V_slider = ctk.CTkSlider(app, from_=0, to=1000, number_of_steps=200)
Max_V_slider.grid(row= 7, column=2, padx=10, pady=10)
Max_V_slider.set(input_max_V)
Max_V_slider.configure(command=update_Max_V_label)
Max_V_label = ctk.CTkLabel(app, text=input_max_V)
Max_V_label.grid(row= 8, column=2)

Min_V = ctk.CTkEntry(app, placeholder_text="Minimum Voltage", width=160, height=28)
Min_V.grid(row= 9, column= 1, padx=10, pady=10)
Min_V_slider = ctk.CTkSlider(app, from_=0, to=600, number_of_steps=120)
Min_V_slider.grid(row= 9, column=2, padx=10, pady=10)
Min_V_slider.set(input_min_V)
Min_V_slider.configure(command=update_Min_V_label)
Min_V_label = ctk.CTkLabel(app, text=input_min_V)
Min_V_label.grid(row= 10, column=2)

Discharging_power = ctk.CTkEntry(app, placeholder_text="Peak Discharging Power", width=160, height=28)
Discharging_power.grid(row= 11, column= 1, padx=10, pady=10)
Discharging_power_slider = ctk.CTkSlider(app, from_=0, to=500000, number_of_steps=500)
Discharging_power_slider.grid(row= 11, column=2, padx=10, pady=10)
Discharging_power_slider.set(input_discharging_power)
Discharging_power_slider.configure(command=update_Discharging_power_label)
Discharging_power_label = ctk.CTkLabel(app, text=input_discharging_power)
Discharging_power_label.grid(row= 12, column=2)

Charging_power = ctk.CTkEntry(app, placeholder_text="Peak Charging Power", width=160, height=28)
Charging_power.grid(row= 13, column= 1, padx=10, pady=10)
Charging_power_slider = ctk.CTkSlider(app, from_=0, to=300000, number_of_steps=300)
Charging_power_slider.grid(row= 13, column=2, padx=10, pady=10)
Charging_power_slider.set(input_charging_power)
Charging_power_slider.configure(command=update_Charging_power_label)
Charging_power_label = ctk.CTkLabel(app, text=input_charging_power)
Charging_power_label.grid(row= 14, column=2)

# range_slider.configure(command=update_slider_label)

# Create a button to calculate the result
calc_button = ctk.CTkButton(app, text="Calculate", command=calculate)
calc_button.grid(row= 10, column= 3, padx=10, pady=10)


EV_range.bind("<KeyRelease>", update_sliders)
total_energy.bind("<KeyRelease>", update_sliders)  
Pack_mass.bind("<KeyRelease>", update_sliders)
Max_V.bind("<KeyRelease>", update_sliders)  
Min_V.bind("<KeyRelease>", update_sliders)
Discharging_power.bind("<KeyRelease>", update_sliders)  
Charging_power.bind("<KeyRelease>", update_sliders)

checkbox_Boxes_to_sliders = ctk.CTkCheckBox(app, text="Transfer numbers entered to sliders?", command=update_sliders)
checkbox_Boxes_to_sliders.grid(row=15, column=1, padx=(5, 5), pady=(0, 20), sticky="w")



# Create a label to display the result
result_label = ctk.CTkLabel(app, text="Result: ")
result_label.grid(row= 11, column= 3, padx=10, pady=10)

# Start the main event loop
app.mainloop()

