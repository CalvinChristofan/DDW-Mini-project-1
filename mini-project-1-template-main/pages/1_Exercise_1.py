import streamlit as st
from datetime import datetime
from library import gen_random_int, create_string, my_sort

st.set_page_config(
    page_title="Exercise 1"
)

st.header("Exercise 1")


def generate():
    # TODO: Task 1
    #
    # replace the None to call the gen_random_int() function
    # array: list[int] = None

    # call create_string() function to convert the list to a single string
    # array_str: str = None

    # store into session_state
    ### your code ###

    st.session_state['numbers'] = array_str


def sort_generated_numbers():
    # TODO: Task 2
    #
    # Retrieves the generated number from the session_state
    numbers: str = st.session_state.numbers

    # Write code to create a list of integers
    # array_int: list[int] = None

    # Sort the list using my_sort() function

    # convert the list to a single string by calling create_string() funcation
    # array_str: str = None

    # store in session_state
    ### your code ###

    st.session_state['sorted_numbers'] = array_str


def clear():
    st.session_state['numbers'] = ""
    st.session_state['sorted_numbers'] = ""


if 'numbers' not in st.session_state:
    st.session_state.numbers = ""

if 'sorted_numbers' not in st.session_state:
    st.session_state.sorted_numbers = ""

st.button("Generate", on_click=generate)

st.write("Generated Numbers:", st.session_state['numbers'])

# TODO: Task 3
#
# Write code to create a button called "Sort" and
# bind it to sort_generated_numbers() function
# st.button(your code here)

# Write a code to display the sorted numbers in this format:
# Sorted Numbers: list of numbers
# use session_state called sorted_numbers to pass the data
# st.write(your code here)

### your code ###

# this code is provided to clear the page
st.button("Clear", on_click=clear)
