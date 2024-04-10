import requests
import time

from proxy_constants import proxies, start_time, end_time


start_time = start_time()
start_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))

url = "http://ident.me/"

# Loop through the dictionary of proxies.
for proxy_key, proxy_value in proxies.items():
    try:
        response = requests.get(
            url, proxies={"http": proxy_value, "https": proxy_value}, timeout=10
        )
        ip_address = response.text
        print(f"Your new IP address using {proxy_key} is:", ip_address)
    except Exception as e:
        print(f"Failed to connect using proxy {proxy_key}: {e}")
        continue

end_time = end_time()
end_time_formatted = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
total_time = end_time - start_time
print("Total Time: ", total_time)
