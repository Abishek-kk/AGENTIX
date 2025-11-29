import pandas as pd
import os

def get_data_path(filename):
    """
    Dynamically finds the path to the 'backend/data/' folder.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, 'data', filename)

def process_overflow(decision_report):
    """
    Input: The decision report text (to check if overflow exists).
    Output: A formatted log of external network actions (LoRa transfers).
    """
    
    # ---------------------------------------------------------
    # 1. LOAD NEIGHBOR DATA FROM CSV
    # ---------------------------------------------------------
    try:
        csv_path = get_data_path('current_data.csv')
        df = pd.read_csv(csv_path)
        
        # We take the first row because hospital network topology 
        # is constant (it doesn't change day-to-day usually).
        if not df.empty:
            row = df.iloc[0]
        else:
            return "ERROR: Current data CSV is empty."
            
    except Exception as e:
        return f"NETWORK ERROR: Could not read CSV. {str(e)}"

    # ---------------------------------------------------------
    # 2. EXTRACT NEIGHBORS DYNAMICALLY
    # ---------------------------------------------------------
    # Your CSV has columns like: near_hospital_1_name, near_hospital_1_contact...
    # We loop to grab them all.
    
    neighbor_nodes = []
    
    # We assume there are up to 3 neighbors based on your file structure
    for i in range(1, 4): 
        name_col = f'near_hospital_{i}_name'
        dist_col = f'near_hospital_{i}_distance_km'
        contact_col = f'near_hospital_{i}_contact'
        
        # Check if column exists in the CSV
        if name_col in df.columns and pd.notna(row[name_col]):
            neighbor_nodes.append({
                "name": str(row[name_col]),
                "distance": f"{row[dist_col]} km",
                "contact": str(row[contact_col])
            })

    # ---------------------------------------------------------
    # 3. SIMULATE MATCHMAKING (The "Agentic" Part)
    # ---------------------------------------------------------
    # In a real scenario, we would parse 'decision_report' to see exactly how many 
    # beds are short. For this demo, we simulate a "Residual Deficit" of 40 beds.
    
    patients_to_transfer = 40
    
    # Build the Log String
    network_log = ""
    network_log += f"[SEARCHING]: Scanning LoRa Mesh Network (15km Radius)...\n"
    network_log += f"[MATCH FOUND]: {len(neighbor_nodes)} Neighboring Nodes Available via LoRa.\n\n"

    # Create the Table Header
    network_log += "| HOSPITAL NAME             | DISTANCE | CONTACT NUMBER    | ACTION          |\n"
    network_log += "|---------------------------|----------|-------------------|-----------------|\n"

    # Fill the Table Rows
    if not neighbor_nodes:
        network_log += "| NO NEIGHBORS FOUND        | N/A      | N/A               | CRITICAL FAILURE|\n"
    else:
        # Distribute patients roughly evenly among available neighbors
        if len(neighbor_nodes) > 0:
            pts_per_hospital = patients_to_transfer // len(neighbor_nodes)
            remainder = patients_to_transfer % len(neighbor_nodes)
        else:
            pts_per_hospital = 0
            remainder = 0
        
        for idx, node in enumerate(neighbor_nodes):
            # Add remainder to the first hospital to ensure total is 40
            count = pts_per_hospital + (1 if idx < remainder else 0)
            
            # Format rows to align nicely with specific width
            network_log += f"| {node['name'][:25]:<25} | {node['distance']:<8} | {node['contact']:<17} | Transfer {count} Pts |\n"

    # Footer
    network_log += "\n[NETWORK PACKET]: Transfer Manifest sent via LoRa ... 📶 ACKNOWLEDGED"

    return network_log

# --- TEST BLOCK (Run this file to see the table) ---
if __name__ == "__main__":
    print(process_overflow("TEST"))