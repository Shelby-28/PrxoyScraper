import requests
from bs4 import BeautifulSoup

# URL to retrieve the text from
url = "https://free-proxy-list.net/"

try:
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    response.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all table rows containing proxy information
    rows = soup.find_all("tr")

    # Check if rows are found
    if len(rows) > 0:
        # Extract the proxy information from the rows
        proxies = []
        for row in rows:
            columns = row.find_all("td")
            if len(columns) >= 2:
                ip = columns[0].get_text()
                port = columns[1].get_text()
                proxies.append(f"{ip}:{port}")

        # Remove unwanted lines starting with "Total:" and country statistics
        proxies = [proxy for proxy in proxies if not proxy.startswith(("Total:", " US:", " IN:", " KH:", " BD:", " JP:", " VE:", " DO:"))]

        # Save the proxy information to a file
        with open("proxy.txt", "w") as file:
            file.write("\n'".join(proxies))

        print("Proxy information saved to 'proxy.txt' file.")
    else:
        raise Exception("No table rows found containing proxy information.")

except requests.exceptions.RequestException as e:
    print(f"Error: Failed to retrieve text from {url}. Exception: {e}")
except Exception as e:
    print(f"Error: {e}")
