# calculator.py

import streamlit as st

# Simple calculator functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

# Streamlit UI for the calculator
st.title("Simple Calculator")

# Dropdown menu for selecting operation
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Input fields for the numbers
num1 = st.number_input("Enter first number", value=0.0)
num2 = st.number_input("Enter second number", value=0.0)

# Perform the operation based on user input
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    # Display the result
    st.write(f"Result: {result}")
