import streamlit as st

def calculate_dli_volume(weight, desired_dose, concentration):
    # weight in kg, desired_dose in cells per kg, concentration in cells per mL
    total_cells_needed = weight * desired_dose
    volume_needed = total_cells_needed / concentration
    return volume_needed

# Streamlit app
st.title("Donor Lymphocyte Infusion (DLI) Volume Calculator")

st.header("Input Parameters")
weight = st.number_input("Recipient Weight (kg)", min_value=0.0, format="%.2f")
desired_dose = st.number_input("Desired Dose (cells per kg)", min_value=0.0, format="%.2e")
concentration = st.number_input("Concentration (cells per mL)", min_value=0.0, format="%.2e")

if st.button("Calculate DLI Volume"):
    if weight > 0 and desired_dose > 0 and concentration > 0:
        volume = calculate_dli_volume(weight, desired_dose, concentration)
        st.success(f"The required DLI Volume is {volume:.2f} mL")
    else:
        st.error("All input values must be greater than zero.")
