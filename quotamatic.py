import requests
import json

def query_prometheus():
    # URL for the API call
    url = "https://prom-api.coralogix.com/api/v1/query_range"
    
    # Query parameters
    params = {
        "query": "sum(cx_data_usage_bytes_total%7Bsubsystem_name!=\"null\"%7D) by (subsystem_name)",
        "start": "2023-11-20T00:00:00.001Z",
        "end": "2023-11-21T00:00:00.000Z"
    }

    # Make the API call
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Process the data (this part can be customized as needed)
        # For this example, let's just print out the results
        for result in data.get("data", {}).get("result", []):
            print("Subsystem:", result.get("metric", {}).get("subsystem_name"))
            for value in result.get("values", []):
                timestamp = value[0]
                value = value[1]
                print(f"Timestamp: {timestamp}, Value: {value}")
            print("\n")
    else:
        print("Failed to fetch data:", response.status_code, response.text)

if __name__ == "__main__":
    query_prometheus()