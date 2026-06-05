import streamlit as st
from datetime import datetime
from library import gen_random_int, create_string, my_sort

st.set_page_config(
    page_title="Exercise 1"
)

st.header("Exercise 1")


def generate():
    array: list[int] = gen_random_int(10, datetime.now().timestamp())
    array_str: str = create_string(array)

    st.session_state['numbers'] = array_str


def sort_generated_numbers():
    numbers: str = st.session_state.numbers
    array_int: list[int] = [int(n) for n in numbers.rstrip('.').split(', ')]
    my_sort(array_int)
    array_str: str = create_string(array_int)

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
st.button("Sort", on_click=sort_generated_numbers)

# Write a code to display the sorted numbers in this format:
# Sorted Numbers: list of numbers
# use session_state called sorted_numbers to pass the data
st.write(f"Sorted Numbers: {st.session_state.get('sorted_numbers', '')}")

# this code is provided to clear the page
st.button("Clear", on_click=clear)
