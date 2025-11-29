from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
import os

# Add the 'agents' folder to the system path so we can import them
sys.path.append(os.path.join(os.path.dirname(__file__), 'agents'))

# Import your AI Agents
from agents import monitor, decision, automation, network, learning, result

app = Flask(__name__)
CORS(app) # Allows the Frontend to talk to this Backend

@app.route('/')
def home():
    return "🏥 HealthTech AI Backend is Running!"

@app.route('/api/run_simulation', methods=['POST'])
def run_simulation():
    try:
        # 1. Get the Date from the Frontend
        data = request.json
        user_date = data.get('date', '2025-10-25') # Default date if none provided

       

        # 2. CALL MONITOR (The Eyes)
        # We assume monitor.run_monitor() accepts a date
        monitor_output = monitor.run_monitor(user_date)

        # 3. CALL DECISION (The Brain)
        decision_output = decision.make_decision(monitor_output)

        # 4. CALL AUTOMATION (The Hands)
        automation_output = automation.run_automation_sequence(decision_output)

        # 5. CALL NETWORK (The Voice - LoRa)
        network_output = network.process_overflow(decision_output)

        # 6. CALL LEARNING (The Memory) & RESULT (The Report)
        final_report = learning.run_learning_module(
            monitor_output, 
            decision_output, 
            automation_output, 
            network_output
        )
        
        # 7. Send the Result back to Frontend
        return jsonify({
            "status": "success",
            "message": "Simulation Complete",
            "data": {
                "monitor": monitor_output,
                "decision": decision_output,
                "automation": automation_output,
                "network": network_output,
                "final_report": final_report
            }
        })

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)