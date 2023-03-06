import urllib.request
import urllib.error

# Define URLs and names for Microsoft services
services = {
    "Microsoft 365": "https://status.office.com/status",
    "OneDrive": "https://status.office.com/onedrive",
}

# Define function to check status of a service
def check_status(url):
    try:
        with urllib.request.urlopen(url) as response:
            if response.getcode() < 400:
                return True
            else:
                return False
    except urllib.error.URLError:
        return False

# Check status of each service
down_services = []
for name, url in services.items():
    status = check_status(url)
    print(f"{name} services are {'up' if status else 'down'}")
    if not status:
        down_services.append(name)
