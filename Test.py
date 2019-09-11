import requests

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

# Java URL
url = 'https://civil-dolphin-251917.appspot.com/'
# print("Java response:", requests.get(url).text)
# Python URL
# url = 'http://silent-region-214714.appspot.com/'
# print("Python response:", requests.get(url).text)

responses = set([])

for test_num in range(10):
    print("Test #" + str(test_num + 1))

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
