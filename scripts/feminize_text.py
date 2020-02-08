import sys
import tika
from tika import parser
import json

def parse_text(filepath):
    '''Return the parsed pdf content using tika'''
    parsed = parser.from_file(filepath)
    return (parsed["metadata"], parsed["content"])

def make_female(content):
    '''Change all instances of man and men to woman and women'''
    return True

if __name__ == "__main__":
    filepath = sys.argv[1]
    print(filepath)
    metadata,content = parse_text(filepath)
    print(type(metadata), type(content))
    with open("metadata.txt", "w") as f:
        f.write(json.dumps(metadata))
    with open("content.txt", "w") as g:
        g.write(json.dumps(content))
