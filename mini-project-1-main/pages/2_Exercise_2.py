import streamlit as st
from library import create_string, my_sort

st.set_page_config(
    page_title="Exercise 2"
)

st.header("Exercise 2")


def sort_numbers():
    # TODO: Task 1
    #
    # Read the numbers entered by the user from session_state
    numbers: str = st.session_state.numbers

    # Create the list of integers from the string
    # array_int: list[int] = None
    array_int: list[int] = [int(n.strip()) for n in numbers.split(", ")]

    # call my_sort() to sort the list of integers
    my_sort(array_int)

    # call create_string() to convert the list to a single string
    # array_str: str = None
    array_str: str = create_string(array_int)

    # store into session_state
    st.session_state['sorted_numbers'] = array_str


def clear():
    st.session_state['numbers'] = ""
    st.session_state['sorted_numbers'] = ""

if 'numbers' not in st.session_state:
    st.session_state.numbers = ""

if 'sorted_numbers' not in st.session_state:
    st.session_state.sorted_numbers = ""

st.text_input("Enter integers separated by comma:", key="numbers")

# TODO: Task 2
#
# Create a button which calls sort_numbers when it is clicked.
# st.button(something, on_click=something)
st.button("Sort", on_click = sort_numbers)

# Display the sorted_numbers from the session_state in this format:
# Sorted Numbers: ...
# st.write(your code here)
st.write("Sorted Numbers:", st.session_state['sorted_numbers'])

# Create a button which calls clear() when it is clicked
# st.button(your code here)
st.button("Clear", on_click = clear)