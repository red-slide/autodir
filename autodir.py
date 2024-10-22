import asyncio
import aiohttp
import time
import sys

from modules.get_art import get_art
from modules.get_url import get_url
from modules.get_charset import get_charset
from modules.get_range import get_range
from modules.get_dash import get_dash
from modules.get_word import get_word
from modules.get_request import get_request


async def main() -> None:
    try:
        # Obtain and prepare the necessary data
        await get_art()
        parsed_url = await get_url()
        charset = await get_charset()
        length_range = await get_range()
        await get_dash()
    except KeyboardInterrupt:
        print('\r\033[2K\033[36mYou finished the program!\033[0m')
        sys.exit()

    total_words = len(charset) ** length_range[1]
    last_word = None
    words_processed = 0  # Start at 0 to count correctly

    # Limit the number of simultaneous requests
    request_number = 20

    tasks = []  # List to store pending tasks
    found_urls = []  # List to store found URLs
    start_time = time.time() # start time

    try:
        async with aiohttp.ClientSession() as session:
            print("\n\033[44m * START TESTS * \033[0m\n")
            while words_processed < total_words:
                try:
                    # Calculate the next word to be tested
                    current_word = await get_word(charset, length_range, last_word)
                    last_word = current_word

                    # Create a task for the request and add it to the list
                    semaphore = asyncio.Semaphore(request_number)
                    task = asyncio.create_task(get_request(current_word, parsed_url, session, semaphore))
                    tasks.append(task)

                    # Remove completed tasks and add new ones while there is space
                    while len(tasks) >= request_number:
                        done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
                        tasks = list(pending)  # Update the list of pending tasks

                        # Update progress for each completed task
                        for task in done:
                            result = await task
                            if result:
                                found_urls.append(result)

                    # Update the total progress
                    words_processed += 1
                    print(f'\r\033[2K\033[36m[+]\033[0m tested words: ({words_processed}/{total_words})', end='')

                except asyncio.CancelledError:
                    # Handle cancellation gracefully
                    print("\n\033[41m * Task was cancelled! * \033[0m")
                    break

            # Wait for any remaining tasks to finish
            if tasks:
                done, _ = await asyncio.wait(tasks)
                for task in done:
                    result = await task
                    if result:
                        found_urls.append(result)

            print(f'\r\033[2K\033[36m[+]\033[0m tested words: ({words_processed}/{total_words})')

    except Exception as e:
        print(f"\n\033[31mUnexpected error: {e}\033[0m")

    finally:
        await get_dash()
        # Show time and all found URLs
        end_time = time.time()
        duration = end_time - start_time
        print(f"\n\033[40m TOTAL TIME: {duration:.2f}s \033[0m")

        if found_urls:
            print("\033[44m * ALL FOUND URLs * \033[0m\n")
            for url in found_urls:
                print(f'\033[36m[+]\033[0m {url}')
        else:
            print("\033[31mNo URLs were found.\033[0m")


# Execute the program
asyncio.run(main())
