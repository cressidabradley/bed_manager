import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title
st.title("Hospital Bed Capacity Dashboard")

# Create dummy data for 3 hospital wards
data = {
    'Ward': ['ICU', 'General', 'Maternity'],
    'Total_Beds': [20, 55, 30],
    'Occupied_Beds': [18, 35, 15]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate occupancy rate
df['Occupancy_Rate'] = (df['Occupied_Beds'] / df['Total_Beds'] * 100).round(1)

# Display the data table
st.subheader("Bed Capacity Data")
st.dataframe(df)

# Add slider to filter by occupancy rate
min_occupancy = st.slider(
    "Filter by minimum occupancy rate (%)",
    min_value=0.0,
    max_value=100.0,
    value=0.0,
    step=5.0
)

# Filter data based on slider
filtered_df = df[df['Occupancy_Rate'] >= min_occupancy]

# Display filtered data
st.subheader(f"Wards with occupancy rate ≥ {min_occupancy}%")
st.dataframe(filtered_df)

# Create bar chart for occupancy
if not filtered_df.empty:
    st.subheader("Bed Occupancy Chart")

    fig = px.bar(
        filtered_df,
        x='Ward',
        y='Occupancy_Rate',
        title=f'Bed Occupancy Rates (≥ {min_occupancy}%)',
        labels={'Occupancy_Rate': 'Occupancy Rate (%)'},
        color='Ward',
        color_discrete_sequence=['#FF6B6B', '#4ECDC4', '#45B7D1']
    )

    # Add text labels on bars
    fig.update_traces(texttemplate='%{y}%', textposition='outside')

    st.plotly_chart(fig)
else:
    st.warning("No wards match the selected occupancy filter.")

# Additional metrics
st.subheader("Summary Statistics")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Beds", df['Total_Beds'].sum())

with col2:
    st.metric("Total Occupied", df['Occupied_Beds'].sum())

with col3:
    avg_occupancy = df['Occupancy_Rate'].mean().round(1)
    st.metric("Average Occupancy", f"{avg_occupancy}%")