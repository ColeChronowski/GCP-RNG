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

# Test the randomness of 1000 random numbers. Fails if 250 or more requests are duplicates. This test is run 10 times in a row.
def test_randomness(url):
    # store the incoming numbers in a set
    responses = set([])

    # conduct the test
    for test_num in range(10):
        print("Test #" + str(test_num + 1))
        
        # store the current number of duplicates for the current test
        num_same = 0

        # get 1000 responses
        for i in range(1000):
            r = requests.get(url)
            # verify that the response is a number
            if verify_number(r.text):
                if r.text in responses:
                    num_same += 1
                    print("Duplicate:", r.text)
                else:
                    responses.add(r.text)
            else:
                print("Error:", r, "is not an integer")

        # verify that at least 750 / 1000 of the random numbers are unique
        if num_same <= 250:
            print("Success!")
        else:
            print("Failure: Too many duplicates")
        responses = set([])

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
                print(url[0], (end - start), "seconds")
            else:
                print("An error has ocurred")

test_timing()