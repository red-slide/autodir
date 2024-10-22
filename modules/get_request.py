async def get_request(word, parsed_url, session, semaphore):
    url = parsed_url+word
    # Limits the number of simultaneous requests
    async with semaphore:
        try:
            # timeout for each request
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    print(f"\r\033[2K\033[36m[+]\033[0m Found: {url}")
                    return url  # Returns the link with status code 200

        except Exception as e:
            print(f"Error with {url}: {e}")
    
    # Explicitly returns None for all conditions that are not 200
    return None
