import fileinput
import sys
import re
import os

def convert_file_to_json(file, encoding, file2):
    i = 0
    with fileinput.input(files=(file),openhook=fileinput.hook_encoded(encoding)) as f:
        for line in f:
            i += 1
        f.close()

    p = re.compile(r'.*(ObjectId\((\"\w+\")\)).*')
    f2 = open(file2, 'w')
    with fileinput.input(files=(file), inplace=False, openhook=fileinput.hook_encoded(encoding)) as f:
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
            f2.write(line)
        f.close()
    
for file in os.listdir('.'):
    if (file.endswith('.txt')):
        try:
            convert_file_to_json(file, "utf-8", file.replace(".txt", ".json"))
        except:
            convert_file_to_json(file, "utf-16", file.replace(".txt", ".json"))