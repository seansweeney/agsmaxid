#! python

# System libraries
import sys

# url fetch
from urllib import request

# json encode/decode
import json

# Define custom exception class for JSON parser
class JsonErrorException(Exception):
    pass

def main(argv=None):

    # The first argument (if there is one) is the URL of the map service
    if len(sys.argv) == 2:
        url = sys.argv[1] + '?f=json'
    else:
        print(f'Usage: {sys.argv[0]} <url to MapServer>')
        exit(1)

    try:
        with request.urlopen(url) as response:
            data = json.loads(response.read())
        # Check that data returned is not an error object
        if 'error' in data:
            raise JsonErrorException(str(data))
    except JsonErrorException as e:
        print(f'"Error returned when extracting status information for {url}')
        print(str(e))
        return 1

    allids = [layer['id'] for layer in data['layers']] + [layer['id'] for layer in data['tables']]
    print(f'Max ID: {str(max(allids))}')

    return 0

# Script start
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
