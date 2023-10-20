import streamlit as st
import pandas as pd

# Set the page configuration
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Define a function to display the DataFrame
def main():
    st.title("Ayushman Bharat Insurance Scheme - Dummy Cost Structure")

    # Create a multi-column layout to push subheading to the right
    col1, col2 = st.columns([4,1])  # Adjusting the ratio to push content to the right
    
    with col1:
        st.write("")  # Empty space
    
    with col2:
        st.subheader("Figures in ₹ Lakhs")

    # Read the Excel file directly
    df = pd.read_excel("D:/App/Cost Structures/Dummy Cost Structures.xlsx")

    # Replace NaN values in all columns with empty strings
    df = df.fillna("")

    # Set the maximum column width to None
    pd.set_option('display.max_colwidth', None)

    # Display the DataFrame
    st.table(df)

if __name__ == "__main__":
    main()
