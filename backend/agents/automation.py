import time
import random
from datetime import datetime

class HospitalAutomator:
    def __init__(self):
        self.log = []

    def log_action(self, system, action, status):
        # Helper to format the logs nicely
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {system:<12} | {action:<40} ... {status}"
        self.log.append(entry)
        # We also print to console for debugging
        # print(entry) 

    def run_automation_sequence(self, decision_report):
        """
        Input: The text report from decision.py
        Output: A formatted log of actions taken.
        """
        self.log = [] # Reset log
        
        # -----------------------------------------------------
        # 1. PARSE THE DECISION (Simple Logic Extraction)
        # -----------------------------------------------------
        # Since the AI output is text, we use simple keyword detection 
        # to trigger the right robots.
        
        doctors_needed = 15 # Default
        oxygen_needed = 100 # Default
        
        # Smart Parsing: If the AI mentioned "Oxygen", we verify stock
        if "Oxygen" in decision_report or "Supply" in decision_report:
            oxygen_needed = 200
            
        if "Staff" in decision_report or "Doctor" in decision_report:
            doctors_needed = 20

        # -----------------------------------------------------
        # 2. EXECUTE ACTIONS
        # -----------------------------------------------------
        
        # A. STAFFING
        self.log_action("👨‍⚕️ HR_SYSTEM", f"Emergency Roster (+{doctors_needed} Doctors)", "ACTIVATED")
        self.log_action("💬 COMMS_API", "SMS Alerts sent to Staff", "DELIVERED")
        
        # B. INVENTORY
        po_num = random.randint(40000, 49999)
        self.log_action("💊 INVENTORY_BOT", f"PO #{po_num} ({oxygen_needed} O2 Cylinders)", "ORDERED")
        
        # C. FACILITIES
        self.log_action("🛌 HOSPITAL_OPS", "Protocol 'Plan D' (Discharge)", "EXECUTED")

        # -----------------------------------------------------
        # 3. RETURN THE LOG
        # -----------------------------------------------------
        return "\n".join(self.log)

# Wrapper function for app.py
def run_automation_sequence(decision_text):
    bot = HospitalAutomator()
    return bot.run_automation_sequence(decision_text)

# --- TEST BLOCK (Runs only if you click 'Play' on this file) ---
if __name__ == "__main__":
    test_decision = "CRITICAL: Oxygen supply low. Staff shortage imminent."
    print(run_automation_sequence(test_decision))