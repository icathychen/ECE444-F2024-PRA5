import requests
import time
import csv
import pandas as pd
import matplotlib.pyplot as plt

# Define the API endpoint (AWS Elastic Beanstalk server)
API_URL = "http://your-aws-elastic-beanstalk-endpoint.com/"

# Define your test cases
test_cases = [
    {"input_text": "This is a hoax and a scam!"}, 
    {"input_text": "The govenment has just pass a new law"} 
]

def perform_test(api_url, test, num_calls=100, csv_filename="result.csv"):
    timestamps = []

    for i in range(num_calls):
        start_time = time.time()  
        response = requests.post(api_url, data=test) 
        end_time = time.time() 

        latency = end_time - start_time
        print(f"Call {i+1}: Latency = {latency:.4f} seconds")

        # Record timestamp and latency
        timestamps.append([i+1, latency])

    # Write the results to a CSV file
    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Call Number", "Latency (seconds)"]) 
        writer.writerows(timestamps)

    print(f"Results saved to {csv_filename}")

for idx, test_case in enumerate(test_cases):
    csv_filename = f"result_{idx+1}.csv"
    perform_test(API_URL, test_case, csv_filename=csv_filename)
    

# Load data from CSV files
test_case_1 = pd.read_csv("result_1.csv")
test_case_2 = pd.read_csv("result_2.csv")

# Create a boxplot
plt.figure(figsize=(10, 6))
plt.boxplot([test_case_1['Latency (seconds)'], test_case_2['Latency (seconds)']], labels=['Test Case 1', 'Test Case 2'])
plt.title('API Latency Boxplot for 100 Calls per Test Case')
plt.ylabel('Latency (seconds)')
plt.xlabel('Test Cases')

plt.savefig("latency_boxplot.png")
plt.show()

avg_latency_case_1 = test_case_1['Latency (seconds)'].mean()
avg_latency_case_2 = test_case_2['Latency (seconds)'].mean()

print(f"Average latency for Test Case 1: {avg_latency_case_1:.4f} seconds")
print(f"Average latency for Test Case 2: {avg_latency_case_2:.4f} seconds")
