import requests
from bs4 import BeautifulSoup
import re
import networkx as nx
import matplotlib.pyplot as plt

# Function to validate and classify IOCs
def classify_ioc(ioc):
    if re.match(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", ioc):  # IPv4
        return 'IP Address'
    elif re.match(r"\b[0-9a-f]{32}\b", ioc, re.IGNORECASE):  # MD5 Hash
        return 'MD5 Hash'
    elif re.match(r"\b[0-9a-f]{40}\b", ioc, re.IGNORECASE):  # SHA1 Hash
        return 'SHA1 Hash'
    elif re.match(r"\b[0-9a-f]{64}\b", ioc, re.IGNORECASE):  # SHA256 Hash
        return 'SHA256 Hash'
    elif re.match(r"(?i)(https?://[^\s/$.?#].[^\s]*)", ioc):  # URL
        return 'URL'
    else:
        return 'Unknown'

# Function to scrape IOCs from a website
def scrape_iocs(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract potential IOCs
        text = soup.get_text()
        iocs = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)  # Example: Extracting IPs
        return list(set(iocs))
    except requests.RequestException as e:
        print(f"Error fetching IOCs: {e}")
        return []

# Function to correlate IOCs (example: grouping by type)
def correlate_iocs(ioc_list):
    correlation_graph = nx.Graph()
    for ioc in ioc_list:
        ioc_type = classify_ioc(ioc)
        correlation_graph.add_node(ioc, type=ioc_type)
        # Add relationships (this is an example; define your logic)
        for other_ioc in ioc_list:
            if ioc != other_ioc:
                correlation_graph.add_edge(ioc, other_ioc)
    return correlation_graph

# Visualization
def visualize_graph(graph):
    pos = nx.spring_layout(graph)
    types = nx.get_node_attributes(graph, 'type')
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_labels(graph, pos, labels=types)
    plt.show()

# Example Usage
if __name__ == "__main__":
    # Input: List of IOCs
    iocs = ["8.8.8.8", "1.1.1.1", "http://malicious.com", "44d88612fea8a8f36de82e1278abb02f"]  # MD5 Example

    # Alternatively, scrape from a URL
    url = "https://example.com/threat-feed"
    scraped_iocs = scrape_iocs(url)
    iocs.extend(scraped_iocs)

    # Correlate IOCs
    graph = correlate_iocs(iocs)
    
    # Visualize the correlation
    visualize_graph(graph)
