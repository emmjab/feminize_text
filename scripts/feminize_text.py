import os, sys
import click
import tika
from tika import parser
import json
import re

## functions for loading/converting pdfs or txt files
def load_pdf(input):
    '''Return the parsed pdf content using tika'''
    parsed = parser.from_file(input)
    metadata, content = parsed["metadata"], parsed["content"]

    # for debugging, this is what gets read from the pdf via tika
    with open(input+"_metadata.log", 'w') as m:
        m.write(json.dumps(metadata))
    with open(input+"_content.log", 'w') as c:
        c.write(content)

    return content

def load_txt(input):
    '''Return the text from input file'''
    with open(input, 'r') as f:
        return f.read()

def parse_content_by_filetype(input):
    file_name, file_ext = os.path.splitext(input)
    if file_ext.lower() == ".pdf":
        click.echo("...parsing as PDF")
        content = load_pdf(input)
    else:
        click.echo("...parsing as text file")
        content = load_text(input)
    return content

## regex matches for words to change
def m_to_w(match):
    m_n = match.group()
    if m_n[0] == "m": return "wo"+m_n
    else: return "Wo"+m_n.lower()

def he_to_she(match):
    he = match.group()
    if he[0] == "h": return "she"
    else: return "She"

def him_his_to_her(match):
    hi_ = match.group()
    if hi_[0] == "h": return "her"
    else: return "Her"

# subn()
# Does the same thing as sub(), but returns the new string and the number of replacements
# then i get the count for free too

@click.command()
@click.option('-i', '--input', required=True, help='Input file as .txt or .pdf')
@click.option('-o', '--output', default="feminized.txt", help='Output file as .txt')

def feminize(input, output):
    '''Read content from INPUT file (.pdf or .txt), replace all male nouns and
       pronouns with female ones, and write to OUTPUT file.'''

    click.echo("Grabbing content from %s, either pdf or text..." % input)
    content = parse_content_by_filetype(input)

    total_words = len(re.findall(r'\w+', content))
    if not total_words:
        click.echo("Found 0 words in this document.")
        return

    click.echo("Running m[]n to wom[]n conversion...")
    mw = re.compile(r'\b[Mm][ae]n\b')
    content, mw_count = mw.subn(m_to_w, content)
    click.echo("%s m[]n are now wom[]n" % str(mw_count))

    click.echo("Running he to she conversion...")
    heshe = re.compile(r'\b[Hh]e\b')
    content, heshe_count = heshe.subn(he_to_she, content)
    click.echo("%s he are now she" % str(heshe_count))

    click.echo("Running him/his to her conversion...")
    himsher = re.compile(r'\b[Hh]i[ms]\b')
    content, himsher_count = himsher.subn(him_his_to_her, content)
    click.echo("%s him/his are now her" % str(himsher_count))

    click.echo("Writing text to output file: %s" % output)
    with open(output, 'w') as f:
        f.write(content)
    click.echo("Total %s word changes out of %s to feminize your text!" %
                    (str(mw_count+heshe_count+himsher_count),
                    str(total_words)))

if __name__ == "__main__":
    feminize()
