import fileinput
import sys
import re

file = sys.argv[1]
i = 0
with fileinput.input(files=(file)) as f:
    for line in f:
        i += 1
    f.close()

p = re.compile(r'.*(ObjectId\((\"\w+\")\)).*')

with fileinput.input(files=(file), inplace=False) as f:
    for line in f:
        if (f.isfirstline()):
            line = line.replace('{', '[{')
        if (f.lineno() == i):
            line = line.replace('}', '}]')
        else:
            line = line.replace('}', '},')
        match = p.match(line)
        if match is not None and len(match.groups()) > 0:
            line = line.replace(match.groups()[0], match.groups()[1])
        print(line, end='')
            