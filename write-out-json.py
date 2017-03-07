#!/usr/bin/env python
# Cobbled together from multiple stack overflow pages

import io
import json
import sys
import traceback


def write_out_json(data):
    filename = 'output.json'

    try:
        to_unicode = unicode
    except NameError:
        to_unicode = str

    try:
        with io.open(filename, 'w') as f:
            output_string = json.dumps(data, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
            f.write(to_unicode(output_string))

    except IOError:
        print 'Error writing in ' + filename
        sys.exit(0)


def main():
    try:
        diction = {'key': 'value', 'key2': 'value2'}
        write_out_json(diction)
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
    except Exception:
        traceback.print_exc(file=sys.stdout)
    sys.exit(0)

if __name__ == "__main__":
    main()
