import sys
import click
import tika
from tika import parser
import json

@click.command()
@click.option('-i', '--input', help='Input file as .txt or .pdf')
@click.option('-o', '--output', help='The person to greet.')

def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

def load_pdf(input):
    '''Return the parsed pdf content using tika'''
    parsed = parser.from_file(input)
    metadata, content = parsed["metadata"], parsed["content"]

    # for debugging, this is what gets read from the pdf via tika
    with open(input+"_metadata.log", 'w') as m:
        m.write(metadata)
    with open(input+"_content.log", 'w') as c:
        c.write(content)

    return content

def load_txt(input):
    '''Return the text from input file'''
    with open(input, 'r') as f:
        return f.read()

#wom (prefix)
wom        = "wom"
Wom        = "Wom"

#man
_man       = " man"
man        = _man + " "
man_comma  = _man + ","
man_period = _man + "."
Man        = man.replace("m", "M")
Man_comma  = man_comma.replace("m", "M")

#men
men, men_comma, men_period,
Men, Men_comma = [s.replace("a", "e") for s in [man, man_comma, man_period,
                                                Man, Man_comma]]

def man_to_woman(content):
    content = [content.replace(s, s.replace('m', wom))
                    for s in [man, man_comma, man_period,
                              men, men_comma, men_period]]
    content = [content.replace(s, s.replace('M', Wom))
                    for s in [Man, Man_comma,
                              Men, Men_comma]]


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

def his_to_her(content):
    '''Change all male pronouns to female pronouns, even when referring to specific people'''
    content = content.replace(" his ", " her ")
    content = content.replace("His ", "Her ")
    content = content.replace(" him ", " her ")
    content = content.replace(" him,", " her,")
    content = content.replace(" him.", " her.")
    content = content.replace(" he ", " she ")
    content = content.replace("He ", "She ")
    # there are cases that will use "his" as possessive, which
    # would need to change to "hers", but I'm not going to bother figuring
    # this out. e.g. "it was his." -> "it was hers."
    return content

def man_to_woman(content):
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
    # note, there are probably cases that look like:
    # "men, ", but I'm not going to bother replacing these.
    return content

def parse_content_by_filetype(input):
    file_name, file_ext = os.path.splitext(input)
    if file_ext.lower() == ".pdf":
        content = load_pdf(input)
    else:
        content = load_text(input)
    return content


def feminize(input, output):
    '''Read content from INPUT file (.pdf or .txt), replace all male nouns and
       pronouns with female ones, and write to OUTPUT file.'''

    print("Grabbing content from %s, either pdf or text..." % input)
    content = parse_content_by_filetype(input)

    print("Running the noun conversion...")
    content = man_to_woman(content)

    print("Runing the pronoun conversion...")
    content = his_to_her(content)



    print("Writing text to output file: %s" % output)
    with open(output, 'w') as f:
        f.write(content)

if __name__ == "__main__":

    make_female(input, output)

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
