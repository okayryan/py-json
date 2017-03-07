#!/usr/bin/env python
# cobbled through by multiple stack overflows

import json
import sys
import traceback


def read_in_json(filename):
    try:
        with open(filename) as json_data:
            data = json.load(json_data)
            return data
    except IOError:
        print 'Error reading in ' + filename
        sys.exit(0)


def main():
    try:
        filename = 'filename.json'
        my_data = read_in_json(filename)
        print my_data
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
