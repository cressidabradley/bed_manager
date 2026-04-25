# Hospital Bed Capacity Dashboard

A Streamlit-based dashboard for monitoring hospital bed capacity across different wards.

## Features

- **Dummy Data**: Sample bed capacity data for ICU, General, and Maternity wards
- **Interactive Bar Chart**: Visual representation of bed occupancy rates
- **Filtering Slider**: Filter wards by minimum occupancy rate
- **Summary Statistics**: Total beds, occupied beds, and average occupancy

## Installation

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The dashboard will be available at `http://localhost:8501`

## Data Structure

The dashboard uses dummy data with the following structure:
- Ward: Name of the hospital ward
- Total_Beds: Total number of beds in the ward
- Occupied_Beds: Number of currently occupied beds
- Occupancy_Rate: Calculated percentage of bed utilization
