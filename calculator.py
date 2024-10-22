import streamlit as st

# Title of the app
st.title("Simple Calculator")

# Input fields for the two numbers
num1 = st.number_input("Enter the first number", value=0)
num2 = st.number_input("Enter the second number", value=0)

# Dropdown to select the operation
operation = st.selectbox("Select operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Function to perform the selected operation
def calculate(num1, num2, operation):
    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

# Button to perform the calculation
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.write(f"The result of {operation} is: {result}")
