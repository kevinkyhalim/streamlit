import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# define page functions
def intro():
    st.title("Welcome to my App")
    st.write("""
        This is the introduction page. \n
        Use the dropdown to navigate to different demos
             """)

def plotting_demo():
    st.subheader("Pyplot Chart")
    fig, ax = plt.subplots()
    chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['A','B','C']
    )
    ax.plot(chart_data['A'], label='A')
    ax.plot(chart_data['B'], label='B')
    ax.plot(chart_data['C'], label='C')
    ax.set_title("Pyplot Line Chart")
    ax.legend()
    st.pyplot(fig)

def mapping_demo():
    st.subheader("Map")
    map_data = pd.DataFrame (
    np.random.randn(100,2) / [50,50] + [1.2789, 103.8536],
    columns=['lat','lon']
    )
    st.map(map_data)

def data_fame_demo():
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

# Dictionary to map page names to function
page_names_to_funcs = {
    "-": intro,
    "Plotting Demo": plotting_demo,
    "Mapping Demo": mapping_demo,
    "Dataframe Demo": data_fame_demo
}

# side bar for page navigation
selected_page = st.sidebar.selectbox("Choose a page", options=page_names_to_funcs.keys())

# Run the function associated with the selected page
page_names_to_funcs[selected_page]()