import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import time 

# st.write() will write anything!
st.write("Hello world 123!")
3 + 4
"hello world" if False else "bye"

# anytime something must be updated on the screen, Streamlit reruns the ENTIRE script from top to bottom

pressed = st.button("Press me")
print("First:", pressed)

pressed2 = st.button("Second Button")
print("Second:", pressed2)
st.divider()
# Text Elements
st.title("Super Simple Title")
st.header("This is a header")
st.subheader("Subheader")
st.markdown("This is **Markdown**")
st.caption("small text or caption")
code_example= """
def greet(name):
    print('hello', name)
"""
st.code(code_example, language="python")

st.divider()
# images HAS TO BE PUT IN a folder called "static"
st.image(os.path.join(os.getcwd(), "static", "pikachu_coffee.jpg"))

st.divider()

# dataframes will automatically have the option to be downloaded
# into a csv!
st.subheader("Dataframe")
df = pd.DataFrame({
    'Name':['Alice', 'Bob', 'Charlie', 'David'],
    'Age':[25,32,37,45],
    'Occupation':['Engineer', 'Doctor', 'Artist', 'Chef']
})
st.dataframe(df)

# Data Editor / Editable daraframe
st.subheader("Data Editor")
editable_df = st.data_editor(df)

# Static Table Section
st.subheader("Static Table")
st.table(df)

# Metrics Section
st.subheader("Metrics")
st.metric(label="Total Rows", value=len(df))
st.metric(label="Average Age", value  =round(df['Age'].mean(),1))

# JSON & Dict Section
st.subheader("JSON and Dicionary")
sample_dict = {
    "name":"Alice",
    "age":25,
    "skills":["Python", "Data Science", "Machine Learning"]
}
st.json(sample_dict)

# Also show it as a dictionary
st.write("Dictionary view:", sample_dict)

st.divider()
# Streamlit Charts Demo

st.title("Streamlit Charts Demo")
# Generate sample data
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
)

# Area Chart
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar Chart
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Line Chart
st.subheader("Area Chart")
st.line_chart(chart_data)

# Scatter Chart
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
    'x':np.random.randn(100),
    'y':np.random.randn(100)
})
st.scatter_chart(scatter_data)

# Map section
st.subheader("Map")
map_data = pd.DataFrame (
    np.random.randn(100,2) / [50,50] + [1.2789, 103.8536],
    columns=['lat','lon']
)
st.map(map_data)

# Pyplot
st.subheader("Pyplot Chart")
fig, ax = plt.subplots()

ax.plot(chart_data['A'], label='A')
ax.plot(chart_data['B'], label='B')
ax.plot(chart_data['C'], label='C')
ax.set_title("Pyplot Line Chart")
ax.legend()
st.pyplot(fig)

st.divider()

# streamlit form demo
st.title("User Information Form Demo")

form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None
}

min_date = datetime(1900, 1,1)
max_date = datetime.now()

with st.form(key="user_info_form"):
    form_values["name"] = st.text_input("Enter your name: ")
    form_values["height"] = st.number_input("Enter your height (cm): ")
    form_values["gender"] = st.selectbox("Gender", ["Male","Female"])
    form_values["dob"] = st.date_input("Enter your birthdate", max_value=max_date, min_value=min_date)
    
    submit_button = st.form_submit_button(label="Submit")
    if submit_button:
        if not all(form_values.values()):
            st.warning("Please fill in all of the fields!")
        else:
            st.balloons()
            st.write("### Info")
            for (key, value) in form_values.items():
                st.write(f"{key}: {value}")

st.divider()

# dynamic updating of values inside streamlit needs to be tracked using 
# SESSION STATE

st.subheader("Counter variable, WITHOUT session state")
counter = 0

st.write(f"Counter value: {counter}")

if st.button("Increment Counter 1"):
    counter += 1
    st.write(f"Counter incremented to {counter}")
else:
    st.write(f"Counter stays at {counter}")

st.divider()

st.subheader("Counter variable, WITH session state")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter 2"):
    st.session_state.counter += 1
    st.write(f"Counter incremented to {st.session_state.counter}")

if st.button("Reset"):
    st.session_state.counter = 0
else:
    st.write(f"Counter did not reset")

# where you write a statement WILL matter in streamlit
st.write(f"Counter value : {st.session_state.counter}")

st.divider()

# Callbacks
st.title("Callbacks")
if "step" not in st.session_state:
    st.session_state.step = 1

if "info" not in st.session_state:
    st.session_state.info = {}

# callback run BEFORE any other code on the next rerun
def go_to_step2(name):
    st.session_state.info["name"] = name
    st.session_state.step = 2

def go_to_step1():
    st.session_state.step = 1

if st.session_state.step == 1:
    st.header("Part 1: Info")
    name = st.text_input("Name", value=st.session_state.info.get("name",""))

    st.button("Next", on_click=go_to_step2, args=(name,))

if st.session_state.step == 2:
    st.header("Part 2: Review")
    st.subheader("Please review this:")
    st.write(f"**Name**: {st.session_state.info.get('name', '')}")

    if st.button("Submit"):
        st.success("Great!")
        st.balloons()
        st.session_state.info = {}
    
    st.button("Back", on_click=go_to_step1)

st.divider()

# layouts
st.title("Layouts")

st.sidebar.title("This is a sidebar")
st.sidebar.write("You can place elements like sliders, buttons, and text here.")
sidebar_input = st.sidebar.text_input("Enter something in the sidebar")

# tabs layout
tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.write("You are in Tab 1")

with tab2:
    st.write("You are in Tab 2")

with tab3:
    st.write("You are in Tab 3")

# Columns layout
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Column 1")
    st.write("Content for column 1")

with col2:
    st.header("Column 2")
    st.write("Content for column 2")

with col3:
    st.header("Column 3")
    st.write("Content for column 3")

# Container
with st.container(border=True):
    st.write("This is inside a container.")
    st.write("You can think of containers as a grouping of elements.")
    st.write("containers help manage sections of the page.")

# Empty Placeholder
placeholder = st.empty()
placeholder.write("This is an empty placeholder, useful for dynamic content.")

if st.button("Update Placeholder"):
    placeholder.write("The content of this placeholder has been updated")

# Expander
with st.expander("Expand for more details"):
    st.header("Expander Title")
    st.write("This is additional information that is hidden by default. You can use expanders to keep your interface cleaner.")

# Popover (Tooltip)
st.write("Hover over this button for a tooltip")
st.button("Button with Tooltip", help="This is a tooltip or popover on hover.")

# Sidebar input handling
if sidebar_input:
    st.write(f"You entered in the sidebar: {sidebar_input}")

st.divider()

# Advanced widget concepts

st.button("Ok")
# key are used to refer to a unique identifier used to accesss values in an object
st.button("Ok", key="btn2")

min_value = st.slider("Set min value", 0, 50, 25)
# the slider below will reset when the slider above is changed!
# the slider_value is identified by its parameters!
# so if the parameter is changed, then the object will be reset
slider_value = st.slider("Slider", min_value, 101, min_value)

# hence store the value in the state as seen below if we don't want the slider to change
if "slider" not in st.session_state:
    st.session_state.slider = 25

st.session_state.slider = st.slider("Slider", min_value, 100, st.session_state.slider)

# If a widget is no longer in the screen, the state is DESTROYED
if "checkbox" not in st.session_state:
    st.session_state.checkbox = False

def toggle_input():
    st.session_state.checkbox = not st.session_state.checkbox

st.checkbox("Show Input Field", value = st.session_state.checkbox, on_change=toggle_input)

if st.session_state.checkbox:
    user_input = st.text_input("Enter something:", value = st.session_state.user_input)
    st.session_state.user_input = user_input
else:
    user_input = st.session_state.get("user_input", "")

st.write(f"User Input: {user_input}")

st.divider()

# Caching
@st.cache_data(ttl=60) # Cache this data for 60 second
def fetch_data():
    # Simulate a slow data-fetching process
    time.sleep(3) # delays to mimic an API call
    return {"data":"This is cached data!"}

st.write("Fetching data...")
data = fetch_data()
st.write(data)

st.divider()

# Cache Resource

file_path = "example.txt"

# using one resource because we are sharing the resource and reading and writing into them
@st.cache_resource
def get_file_handler():
    # Open the file in append mode, which creates the file if it doesn't exist
    file = open(file_path, "a+")
    return file

# use the cached file handler
file_handler = get_file_handler()

# Write to the file using the cached handler
if st.button("Write to File"):
    file_handler.write("New line of text\n")
    file_handler.flush() # Ensure the content is written immediately
    st.success("Wrote a new line to the file!")

# Read and display the file contents
if st.button("Read File"):
    file_handler.seek(0) # Move to the beginning of the file
    content = file_handler.read()
    st.text(content)

# Always make sure to close the file when done (useful for resource cleanup)
st.button("Close File", on_click=file_handler.close)

st.divider()

# st.rerun()

st.title("Counter Example with Immediate Rerun")

if "count" not in st.session_state:
    st.session_state.count = 0

def increment_and_rerun():
    st.session_state.count += 1
    # rerun instantly so we can get the update immediately
    st.rerun()

st.write(f"Current Count: {st.session_state.count}")

if st.button("Increment and Update Immediately"):
    increment_and_rerun()

st.divider()

# Fragments
# A way to rerun only certain portions of your user interface
# and better organize or separate out your code
# cannot return a value from inside a fragment, 
# and hence will need to use session_state to take the variable out of the fragment

st.title("My Awesome App")

@st.fragment()
def toggle_and_text():
    cols = st.columns(2)
    cols[0].toggle("Toggle")
    cols[1].text_area("Enter Text")

@st.fragment()
def filter_and_file():
    new_cols = st.columns(5)
    new_cols[0].checkbox("Filter")
    new_cols[1].file_uploader("Upload image")
    new_cols[2].selectbox("Choose option", ["Option 1", "Option 2", "Option 3"])
    new_cols[3].slider("Select value", 0, 100, 50)
    new_cols[4].text_input("Enter text")

toggle_and_text()
cols = st.columns(2)
cols[0].selectbox("Select", [1,2,3], None)
cols[1].button("Update")
filter_and_file()