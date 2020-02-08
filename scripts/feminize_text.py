import sys
import tika
from tika import parser
import json

def parse_text(filepath):
    '''Return the parsed pdf content using tika'''
    parsed = parser.from_file(filepath)
    return (parsed["metadata"], parsed["content"])

def count_men(content):
    '''Return the number of instances of "men"'''
    men = content.count(" men ")
    man = content.count(" man ")
    Men = content.count(" Men ")
    Man = content.count(" Man ")
    men_comma = content.count(" men,")
    men_period = content.count(" men.")
    man_comma = content.count(" man,")
    man_period = content.count(" man.")
    Man_comma = content.count(" Man,")
    Men_comma = content.count(" Men,")
    return men+man+Men+Man+men_comma+men_period+man_comma+man_period+Man_comma+Men_comma

def count_women(content):
    women = content.count(" women ")
    woman = content.count(" woman ")
    Women = content.count(" Women ")
    Woman = content.count(" Woman ")
    women_comma = content.count(" women,")
    women_period = content.count(" women.")
    woman_comma = content.count(" woman,")
    woman_period = content.count(" woman.")
    Woman_comma = content.count(" Woman,")
    Women_comma = content.count(" Women,")
    return women+woman+Women+Woman+women_comma+women_period+woman_comma+woman_period+Woman_comma+Women_comma

def count_pronouns(content):
    return content.count(" his ")+content.count(" him ")+content.count(" he ")

def change_pronouns(content):
    '''Change all male pronouns to female pronouns, even when referring to specific people'''

    content = content.replace(" his ", " her ")
    content = content.replace("His ", "Her ")
    content = content.replace(" him ", " her ")
    content = content.replace(" him,", "her,")
    content = content.replace(" him.", "her.")
    content = content.replace(" he ", " she ")
    content = content.replace("He ", "She ")
    return content


def make_female(content):
    '''Change all instances of man and men to woman and women'''
    content = content.replace(" man ", " woman ")
    content = content.replace(" men ", " women ")
    content = content.replace("Man ", "Woman ")
    content = content.replace("Men ", "Women ")
    content = content.replace(" man,", " woman,")
    content = content.replace(" men,", " women,")
    content = content.replace("Man,", "Woman,")
    content = content.replace("Men,", "Women,")
    content = content.replace(" man.", " woman.")
    content = content.replace(" men.", " women.")

    content = change_pronouns(content)

    # note, there are probably cases that look like:
    # "men, ", but I'm not going to bother replacing these.
    return content

if __name__ == "__main__":
    filepath = sys.argv[1]
    print(filepath)
    metadata,content = parse_text(filepath)
    print(type(metadata), type(content))
    metadata = json.dumps(metadata)
    #content = json.dumps(content)
    with open("metadata.txt", "w") as f:
        f.write(metadata)
    with open("content.txt", "w") as g:
        g.write(content)

    print("Men = " + str(count_men(content)))
    print("Women = " + str(count_women(content)))
    print("Male pronouns est. = " + str(count_pronouns(content)))

    feminized = make_female(content)

    print("Men = " + str(count_men(feminized)))
    print("Women = " + str(count_women(feminized)))

    with open("women.txt", "w") as h:
        h.write(feminized)
