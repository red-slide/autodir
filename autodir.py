import itertools
import sys
import requests
from python.autodir.modules.get_dash import *

# List to store URLs that return status code 200
found_links = []

def generate_and_test_words(min_length, max_length, charset, base_url):
    # ensures the base URL has a scheme (http or https)
    if not base_url.startswith('http://') and not base_url.startswith('https://'):
        base_url = 'http://' + base_url  # adds http:// if scheme is missing

    total_words = sum(len(charset) ** length for length in range(min_length, max_length + 1))
    words_processed = 0

    # show found URLs
    found_links_line = []

    for length in range(min_length, max_length + 1):
        for word in itertools.product(charset, repeat=length):
            current_word = ''.join(word)
            url = f"{base_url}/{current_word}"

            # Update the progress line in the terminal
            sys.stdout.write("\033[K")
            sys.stdout.write(f"Testing: {url} ({words_processed + 1}/{total_words})\n")
            sys.stdout.write("\033[F" * (len(found_links_line) + 1))

            # Update the list of found URLs
            for link in found_links_line:
                sys.stdout.write(f"{link}\033[K\n")

            sys.stdout.flush()

            try:
                response = requests.get(url)
                status_code = response.status_code

                if status_code == 200:
                    found_links.append(f"Found 200 OK: {url}")
                    found_links_line = found_links.copy()
                    sys.stdout.write("\033[K")
                    sys.stdout.write(f"Testing: {url} ({words_processed + 1}/{total_words})\n")
                    sys.stdout.flush()

            except requests.RequestException as e:
                # Displays request errors silently on the same progress line
                sys.stdout.write("\033[K")
                sys.stdout.write(f"Error requesting {url}: {e}\n")
                sys.stdout.flush()

            words_processed += 1

    # Display the final list of URLs found and the final progress
    sys.stdout.write("\033[K")
    print(get_dash()+"\nFinished processing all words.")
    print("True Links Found:")
    for link in found_links:
        print(link)

def main():
    try:
        os.system('clear')
        print("""    _         _          ____  _      
   / \  _   _| |_ ___   |  _ \(_)_ __ 
  / _ \| | | | __/ _ \  | | | | | '__|
 / ___ \ |_| | || (_) | | |_| | | |   
/_/   \_\__,_|\__\___/  |____/|_|_| \n""")

        base_url = input("Enter the base URL (e.g., http://example.com): ").strip()
        min_length = int(input("Minimum length of the character set: ").strip())
        max_length = int(input("Maximum length of the character set: ").strip())
        charset = input("Enter the charset (e.g., abc123): ").strip()

        # Check if charset is provided
        if not charset:
            print("Charset is required.")
            return

        print(get_dash())

        # validates the size of the charset
        if min_length < 1 or max_length < min_length:
            print("Invalid length values.")
            return

        print("Starting word generation and testing...")
        generate_and_test_words(min_length, max_length, charset, base_url)

    except KeyboardInterrupt:
        # Catch the keyboardinterrupt and provide a friendly message
        print(get_dash() + "\nProcess interrupted by user.\n")

        if len(found_links) > 0:
            print("True Links Found:")
            for link in found_links:
                print(link)

if __name__ == "__main__":
    main()

