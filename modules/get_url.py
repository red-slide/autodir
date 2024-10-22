import sys
import requests
from urllib.parse import urlparse, urlunparse, urljoin

async def get_url():
    """Receives a URL from the user, makes a request, and returns the sanitized URL if valid."""
    url = input("\033[36m[+]\033[0m Enter the URL: ").strip()

    # Parse the URL and add 'http' if no scheme is provided
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'http://' + url

    # Parse the URL again to ensure all parts are correctly handled
    parsed_url = urlparse(url)

     # Ensure 'www.' is present if no subdomain is provided
    domain_parts = parsed_url.netloc.split('.')
    if len(domain_parts) == 2:  # Only add 'www.' if there is no subdomain
        netloc = 'www.' + parsed_url.netloc
        url = urlunparse((parsed_url.scheme, netloc, parsed_url.path, parsed_url.params, parsed_url.query, parsed_url.fragment))
    
    
    # Ensure there's a trailing slash after the subdomain if not present
    if not parsed_url.path:
        url = urljoin(url, '/')

    try:
        # Make a request to the URL with the scheme
        response = requests.get(url)
        
        # Check if the response status code is in acceptable ranges (1xx, 2xx, 3xx, 4xx)
        if response.status_code:
            print('\033[36m[+]\033[0m Enter the URL: \033[A'+url)
            return url

    except requests.RequestException as e:
        print(f"Error making request to the URL: {e}")
        sys.exit()
