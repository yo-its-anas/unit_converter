import streamlit as st

st.title("Unit Converter Application⏳📐")
st.markdown("### Converts Weight, Time & Length")
st.write("Choose a category, enter the value and get your results")

category = st.selectbox("Choose a Category", ["Weight","Temperature","Length"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "kilometers to miles":
            return value * 0.621371
        elif unit == "miles to kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "pounds to kilograms":
            return value / 2.20462
        
    elif category == "Temperature":
        if unit == "Celsius to Fahrenheit":
            return (value * 9/5) + 32
        elif unit == "Celsius to Kelvin":
            return value + 273.15
        
if category == "Length":
    unit = st.selectbox("Select your conversation",["kilometers to miles","miles to kilometers"])
elif category == "Weight":
    unit = st.selectbox("Select your Conversation",["Kilograms to Pounds","pounds to kilograms"])
elif category=="Temperature":
    unit= st.selectbox("Select your conversation",["Celsius to Fahrenheit","Celsius to Kelvin"])

value = st.number_input("Enter the Value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is: {result}")
