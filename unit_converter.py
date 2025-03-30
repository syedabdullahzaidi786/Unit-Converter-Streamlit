import streamlit as st
import pandas as pd
import numpy as np

# Set page config
st.set_page_config(
    page_title="Unit Converter",
    page_icon="📏",
    layout="wide"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.title("📏 Unit Converter")
st.markdown("Convert between different units of measurement easily!")

# Define conversion categories and their units
conversion_categories = {
    "Length": {
        "Meters": 1,
        "Kilometers": 1000,
        "Centimeters": 0.01,
        "Millimeters": 0.001,
        "Miles": 1609.34,
        "Yards": 0.9144,
        "Feet": 0.3048,
        "Inches": 0.0254
    },
    "Weight": {
        "Kilograms": 1,
        "Grams": 0.001,
        "Milligrams": 0.000001,
        "Pounds": 0.453592,
        "Ounces": 0.0283495
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K"
    },
    "Area": {
        "Square Meters": 1,
        "Square Kilometers": 1000000,
        "Square Miles": 2589988.11,
        "Square Yards": 0.836127,
        "Square Feet": 0.092903,
        "Acres": 4046.86
    },
    "Volume": {
        "Liters": 1,
        "Milliliters": 0.001,
        "Cubic Meters": 1000,
        "Gallons (US)": 3.78541,
        "Quarts (US)": 0.946353,
        "Pints (US)": 0.473176,
        "Fluid Ounces (US)": 0.0295735
    }
}

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    # Category selection
    category = st.selectbox(
        "Select Conversion Category",
        list(conversion_categories.keys())
    )

    # Get units for selected category
    units = list(conversion_categories[category].keys())

    # Input value
    value = st.number_input(
        "Enter Value to Convert",
        min_value=-1.797e+308,  # Minimum value supported by Streamlit
        max_value=1.797e+308,   # Maximum value supported by Streamlit
        value=1.0
    )

    # From unit selection
    from_unit = st.selectbox("From Unit", units)

with col2:
    # To unit selection
    to_unit = st.selectbox("To Unit", units)

    # Convert button
    if st.button("Convert"):
        if category == "Temperature":
            # Special handling for temperature conversion
            if from_unit == "Celsius":
                if to_unit == "Fahrenheit":
                    result = (value * 9/5) + 32
                elif to_unit == "Kelvin":
                    result = value + 273.15
                else:
                    result = value
            elif from_unit == "Fahrenheit":
                if to_unit == "Celsius":
                    result = (value - 32) * 5/9
                elif to_unit == "Kelvin":
                    result = (value - 32) * 5/9 + 273.15
                else:
                    result = value
            else:  # Kelvin
                if to_unit == "Celsius":
                    result = value - 273.15
                elif to_unit == "Fahrenheit":
                    result = (value - 273.15) * 9/5 + 32
                else:
                    result = value
        else:
            # Regular unit conversion
            base_value = value * conversion_categories[category][from_unit]
            result = base_value / conversion_categories[category][to_unit]

        # Display result with formatting
        st.success(f"Converted Value: {result:.4f} {to_unit}")

# Add some helpful information
st.markdown("---")
st.markdown("""
    ### Tips:
    - Select the category of units you want to convert
    - Enter the value you want to convert
    - Choose the source unit and target unit
    - Click Convert to see the result
""")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
