import requests
import time
import yaml

MAX_NUMBER = 1000000
MIN_NUMBER = 1

# Verify if the string is an integer or not
def verify_number(s):
    try:
        num = int(s)
        if num >= 1 & num <= 1000000:
            return True
    except ValueError:
        return False

quotes = [
    "Dr J: If it works, it means you forgot about something",
    "Wyatt: i can't believe dr j is trying to tempt me away from the light of god",
    "Wyatt: well, looks like [dr] j has baited me once again",
    "dr j: i may be failing my turing test. who cares? ive passed enough of tests that i can now apply pain to you",
    "Dr J: it’s so easy to write if statements if we know what statements they are",
]

def test_timing():
    # open yaml file that contains urls
    with open(r'url.yaml') as file:
        # Dictionary of urls. The the key is a description of the url, and the value is the url itself.
        urls = yaml.load(file, Loader=yaml.FullLoader)
        # Loop through the urls
        for url in urls.items():
            # Print the description of the url and the time
            start = time.time()

            # make the request
            r = requests.get(url[1])

            # get the end time
            end = time.time()

            # Verify that the request fits the constraints
            if verify_number(r.text):
                # print the results
                i = int(r.text)
                a = i % (len(quotes))
                print(quotes[a])
            else:
                print("An error has ocurred")

test_timing()
