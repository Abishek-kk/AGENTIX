import requests
import json

# URL of your Flask App
url = "http://127.0.0.1:5000/api/run_simulation"

# The Date to Simulate
payload = {
    "date": "2025-10-25" 
}
headers = {"Content-Type": "application/json"}

print(f"📡 Sending request to {url}...")

try:
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        
        # CLEAR THE SCREEN (Optional, makes it look like a real app)
        print("\n" * 2)
        
        # PRINT THE DASHBOARD RECEIVED FROM SERVER
        if 'dashboard_content' in data:
            print(data['dashboard_content'])
        else:
            print("⚠️ Data received, but no dashboard content found.")
            print(data)
            
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

except Exception as e:
    print(f"❌ Connection Failed. Is 'python app.py' running? Error: {e}")