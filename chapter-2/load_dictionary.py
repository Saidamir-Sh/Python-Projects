"""Load a text file as a list.

Argumets:
- text file name (and directory path, if needed.)

Exceptions:
- IOError if filename is not found

Returns"
- list of all words in a text file in lower case.

Requires - import sys
"""

import sys

def load(file):
    """Open text file & return a list of lowercase strings."""
    try:
        with open(file) as in_file: # maybe specify encoding for open()
            loaded_txt = in_file.read().strip().split('\n')
            loaded_txt = [txt.lower() for txt in loaded_txt]
            return loaded_txt
    except IOError as e:
        # later use fstring instead of format, shorter.
        print("{}\nError opening: {}. Terminating program.".format(e, file), file=sys.stderr)
        sys.exit(1)
