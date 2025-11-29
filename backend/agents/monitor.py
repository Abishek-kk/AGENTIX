import pandas as pd
import os
from datetime import datetime, timedelta

def get_data_path(filename):
    """
    Dynamically finds the path to the 'backend/data/' folder.
    This works regardless of which folder you run the script from.
    """
    # Get the directory of this script (backend/agents/)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up one level to 'backend/'
    backend_dir = os.path.dirname(current_dir)
    # Go down into 'data/' and add filename
    return os.path.join(backend_dir, 'data', filename)

def run_monitor(simulation_date_str):
    """
    Main function to analyze hospital status.
    Input: simulation_date_str (e.g., "2025-10-25")
    Output: A detailed context string for the AI.
    """
    
    # ---------------------------------------------------------
    # 1. SETUP DATES (The Time Machine)
    # ---------------------------------------------------------
    try:
        # Parse the input date
        current_date_obj = datetime.strptime(simulation_date_str, "%Y-%m-%d")
    except (ValueError, TypeError):
        # Default to today if input is invalid
        current_date_obj = datetime.now()

    # LOOK AHEAD: We want to predict what happens in 7 days
    target_date_obj = current_date_obj + timedelta(days=7)
    
    # We use "Month-Day" (e.g., "11-01") to compare across years
    target_md = target_date_obj.strftime('%m-%d')
    target_date_full = target_date_obj.strftime('%Y-%m-%d')

   

    # ---------------------------------------------------------
    # 2. LOAD DATA
    # ---------------------------------------------------------
    try:
        past_path = get_data_path('past_data.csv')
        current_path = get_data_path('current_data.csv')

        df_history = pd.read_csv(past_path)
        df_current = pd.read_csv(current_path)
        
    except FileNotFoundError:
        return "CRITICAL ERROR: CSV files not found in 'backend/data/'. Please check file names."

    # ---------------------------------------------------------
    # 3. ANALYZE HISTORY (What happened last year?)
    # ---------------------------------------------------------
    # Filter for rows where the date contains our target Month-Day
    # We convert 'date' column to string just in case
    history_match = df_history[df_history['date'].astype(str).str.contains(target_md)]

    if not history_match.empty:
        # Take the first matching row
        row = history_match.iloc[0]
        
        # Extract specific columns (Matching your CSV structure)
        event_name = row.get('festival_name', 'None')
        if pd.isna(event_name) or str(event_name).lower() == 'nan':
            event_name = "Seasonal Trend"
            
        past_admissions = row.get('daily_admissions', 0)
        past_oxygen = row.get('oxygen_usage_per_day', 0)
        past_aqi = row.get('aqi', 0)
    else:
        # Fallback if no specific historical date is found
        event_name = "Normal Operations"
        past_admissions = 100  # Default average
        past_oxygen = 40
        past_aqi = 150

    # ---------------------------------------------------------
    # 4. ANALYZE PRESENT (Live Sensor Data)
    # ---------------------------------------------------------
    # In a real system, this fetches live DB. Here, we take the latest available row.
    if not df_current.empty:
        curr_row = df_current.iloc[0] # taking top row as "Current State"
        
        curr_staff = curr_row.get('doctors_per_shift', 0)
        curr_bed_occ = curr_row.get('daily_bed_occupancy', 0)
        curr_oxygen_stock = curr_row.get('oxygen_stock_level', 0)
    else:
        curr_staff = 10
        curr_bed_occ = 50
        curr_oxygen_stock = 100

    # ---------------------------------------------------------
    # 5. CONSTRUCT THE CONTEXT PROMPT
    # ---------------------------------------------------------
    # This string is what gets sent to decision.py
    
    monitor_output = f"""
[SIMULATION MODE ACTIVE]
Current Simulated Date: {simulation_date_str}
Target Event Date: {target_date_full} (7 Days Away)
Upcoming Event Detected: {event_name}

[HISTORICAL BASELINE]
On this date last year:
- Daily Admissions: {past_admissions} patients
- Oxygen Usage: {past_oxygen} cylinders
- Air Quality Index (AQI): {past_aqi}

[CURRENT STATUS QUO]
Right now, our live status is:
- Doctors Available: {curr_staff}
- Bed Occupancy: {curr_bed_occ}%
- Oxygen Stock Level: {curr_oxygen_stock} units
"""
    
    return monitor_output.strip()

# --- TEST BLOCK (Runs only if you click 'Play' on this file) ---
if __name__ == "__main__":
    # Test with a date that likely exists in your data or triggers logic
    print(run_monitor("2024-12-25"))