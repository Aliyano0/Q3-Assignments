import streamlit as st
from pint import UnitRegistry

# Initialize Unit Registry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# List of unit categories and their units
unit_types = {
    "Length": ["meters", "kilometers", "feet", "yards", "miles"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Weight": ["kilograms", "grams", "pounds", "ounces"],
    "Volume": ["liters", "milliliters", "gallons", "quarts"],
    "Speed": ["meters per second", "kilometers per hour", "miles per hour", "feet per second"],
    "Energy": ["joules", "kilojoules", "calories", "kilocalories", "BTU"],
    "Pressure": ["pascals", "bar", "psi", "atmosphere"],
    "Time": ["seconds", "minutes", "hours", "days", "weeks"],
    "Digital Storage": [
        "bytes", "kilobytes", "megabytes", "gigabytes", "terabytes",
        "petabytes", "exabytes", "bit", "kilobit", "megabit", "gigabit"
    ],
    "Data Transfer Rate": [
        "bits per second", "kilobits per second", "megabits per second",
        "gigabits per second", "terabits per second", "bytes per second",
        "kilobytes per second", "megabytes per second"
    ],
}

# UI Setup
st.set_page_config(page_title="🔁 Unit Converter", layout="wide")
st.title("🔁 Unit Converter")

# User selects unit category
option = st.selectbox("Select a unit category:", list(unit_types.keys()))

# Dynamic unit selection
unit_from = st.selectbox("From:", unit_types[option])
unit_to = st.selectbox("To:", unit_types[option])

# Input value
value = st.number_input("Enter a value:", min_value=1.0)

# Conversion Logic
if st.button(f"Convert {unit_from} to {unit_to}"):
    try:
        result = Q_(value, getattr(ureg, unit_from)).to(getattr(ureg, unit_to))
        st.success(f"{value} {unit_from} = {result.magnitude:.2f} {unit_to}")
    except Exception as e:
        st.error("Invalid conversion. Please try a valid unit.")

