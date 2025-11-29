🏥 AGENTIX: Autonomous Crisis Command Center

AGENTIX is an intelligent, agentic AI system designed to stabilize hospital operations during unpredictable surges (festivals, epidemics, pollution spikes). It autonomously predicts resource gaps, executes internal mitigation strategies, and coordinates patient transfers via a self-healing LoRa mesh network when local capacity is breached.

🚨 The Problem

Healthcare centers in India face massive, unpredictable patient surges during major festivals (Diwali, Holi) or pollution spikes. These surges lead to:

Staff Burnout: Sudden 1:25 doctor-to-patient ratios.

Supply Exhaustion: Oxygen and ICU beds run out within hours.

Gridlock: Ambulance delays due to lack of real-time inter-hospital coordination.

🛡️ The Solution: Agentix

Agentix moves beyond passive dashboards. It is an Active Defense System that:

Predicts: Uses historical data + live sensor feeds to forecast surges 7 days in advance.

Decides: AI Agents calculate exact resource gaps (e.g., "Need 200 O2 cylinders").

Automates: Auto-triggers staff rosters and supply orders via API.

Connects: If internal capacity fails, it activates a LoRa Mesh Network to find nearby hospitals and route patients automatically.

🏗️ System Architecture

The system is built on a Decoupled Architecture separating the AI Brain (Python) from the Command Interface (React).

1. The Brain (Backend)

Tech: Python, Flask, Pandas, Google Gemini AI.

Agents:

monitor.py: The Time Machine. Compares live data with historical baselines.

decision.py: Generates strategic predictions using LLMs.

automation.py: Simulates API calls for staffing and inventory.

network.py: Manages the LoRa Mesh topology for patient transfers.

learning.py: Aggregates success metrics for future training.

2. The Face (Frontend)

Tech: React (Vite), TypeScript, Tailwind CSS, ShadCN UI.

Features:

Futuristic "Dark Mode" Command Center UI.

Real-time "Typewriter" style logs.

Governance Layer: Mandatory confirmation popups before AI execution.

🚀 Installation & Setup

Prerequisites

Node.js & npm

Python 3.8+

Google Gemini API Key

Step 1: Backend Setup (The Brain)

# 1. Navigate to backend
cd backend

# 2. Create virtual environment (Optional but recommended)
python -m venv venv
# Windows: .\venv\Scripts\Activate
# Mac/Linux: source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure API Key
# Open backend/agents/decision.py and paste your GEMINI_API_KEY.

# 5. Start the Server
python app.py


Server will start on: http://127.0.0.1:5000

Step 2: Frontend Setup (The Interface)

# 1. Open a new terminal and navigate to frontend
cd frontend

# 2. Install dependencies
npm install

# 3. Start the Dashboard
npm run dev


Dashboard will launch at: http://localhost:5173 (or similar)

🎮 Usage Guide

Launch: Open the Frontend link in your browser.

Select Date: Pick a target date (e.g., 2025-10-25 for Diwali simulation).

Initiate: Click the "INITIATE CRISIS PROTOCOL" button.

Governance Check: A security popup will appear asking for authorization. Click "Confirm & Execute".

Watch: The terminal will populate with real-time logs:

Analyzing historical trends...

Predicting oxygen shortage...

Auto-ordering supplies...

Scanning LoRa network for backup hospitals...



🏆 Key Features for Judges

LoRa Integration: Demonstrates offline resilience when internet fails.

Agentic Behavior: The system acts (orders supplies), it doesn't just "show charts".

Governance: built-in safety checks for human-in-the-loop control.

Built with ❤️ for a Resilient Healthcare Future.
