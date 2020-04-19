# Feminize your Documents

Tired of reading documents that use masculine nouns and pronouns for talking about
people in the abstract, especially when referring to scientists, programmers, and
engineers? I know I am! Here's a script I wrote to help me get through Thomas S. Kuhn's
*The Structure of Scientific Revolutions* (1962) [1]. Maybe it's useful for you, too!
Works by re-gendering all references to men in PDFs & text-based files. &#9792;

## Usage

1. Get a PDF or text copy of the document you want to convert. HTML and LaTeX
   should probably also work, but I didn't test.
2. Install dependencies (see **Setup** section).
3. Run the `scripts/feminize.py` script in this repository to output a converted
   version of your document.
```
$ python scripts/feminize.py --help
Usage: feminize.py [OPTIONS]

  Read content from INPUT file (.pdf or .txt), replace all male nouns and
  pronouns with female ones, and write to OUTPUT file.

Options:
  -i, --input TEXT   Input file as .txt or .pdf  [required]
  -o, --output TEXT  Output file as .txt  [default: feminized.txt]
  --help             Show this message and exit.
```
4. Check out the printed statistics to see how many words were converted in your
   document.
5. If you want to read the converted document as a PDF, you can copy the text from
   the output file into a Microsoft Word document (or equivalent) and choose "export
   to PDF". (let me know about any easy-to-use python libraries for generating
   PDFs! Wait do I really want that... PDFs are a terrible format. revised: tell me about
   your favorite way to read plaintext!)

## Setup

The PDF parsing requires the [apache tika library](https://github.com/chrismattmann/tika-python),
which you can install like a normal python library along with the other (very
minimal) requirements.

```
pip install -r requirements.txt
```

However, if you don't already have a JDK on your machine (my Mac did not), you should
first [install it from here](https://www.oracle.com/technetwork/java/javase/downloads/jdk13-downloads-5672538.html).
See my stream of consciousness thoughts in the **Background & documentation** section
if you get stuck. Note that you only need to worry about this if you want to convert
a pdf. (Of course, you probably want to convert a PDF ;P)


## Example

### Execution
```
$ python scripts/feminize.py -i ../documents/Kuhn_Structure_of_Scientific_Revolutions.pdf

Grabbing content from documents/Kuhn_Structure_of_Scientific_Revolutions.pdf...
...parsing as PDF
Running m[]n to wom[]n conversion...
* 107 m[]n are now wom[]n
Running he to she conversion...
* 189 he are now she
Running him/his to her conversion...
* 251 him/his are now her
Writing text to output file: feminized.txt
* Total 547 word changes out of 79992 (0.68%) to feminize your text!
* 12.33% of sentences changed (assume one change per sentence for est. 4436 sentences)
```

### Raw input snippet

>The study of paradigms, including many that are far more specialized than those
 named illustratively above, is what mainly prepares the student for
 membership in the particular scientific community with which **he** will
 later practice. Because **he** there joins **men** who learned the bases of their
 field from the same concrete models, **his** subsequent practice will
 seldom evoke overt disagreement over fundamentals. **Men** whose
 research is based on shared paradigms are committed to the same rules
 and standards for scientific practice. That commitment and the
 apparent consensus it produces are prerequisites for normal science,
 i.e., for the genesis and continuation of a particular research tradition.

(excerpt from the chapter, *The Route to Normal Science*; see [1])

### Converted output snippet

>The study of paradigms, including many that are far more specialized than those
 named illustratively above, is what mainly prepares the student for
 membership in the particular scientific community with which **she** will
 later practice. Because **she** there joins **women** who learned the bases of their
 field from the same concrete models, **her** subsequent practice will
 seldom evoke overt disagreement over fundamentals. **Women** whose
 research is based on shared paradigms are committed to the same rules
 and standards for scientific practice. That commitment and the
 apparent consensus it produces are prerequisites for normal science,
 i.e., for the genesis and continuation of a particular research tradition.

(based on an excerpt from the chapter, *The Route to Normal Science*; see [1])

## Debugging

For best results, use `python 3.7`.

PDF parsing is a real nightmare, but tika worked for me basically straight out of
the box once I installed the JDK (see **Setup** section).

One note is that your converted document might have a ton of newlines before you
get to the actual content, so before you freak out at an empty output file, try
scrolling down. If you still don't see any output, you can check out the two log
files that get written: the "\_content.log" and the "\_metadata.log". If these
files are both empty, something went wrong with the parsing & you're on your own :)

You can read the following section to follow my development process, which might help.

## Background & documentation of the script-writing process

2h project including thinking time and file downloading time.

I keep getting distracted by all the times Kuhn says "men in science". I might
have an easier time reading *The Structure of Scientific Revolutions* if I replace
all instances of "men" with "women".

I found this apache tika library for parsing PDFs.
https://github.com/chrismattmann/tika-python

The tika library kicked off a download of a jar file that ended up here:

```
$ python scripts/feminize.py -i ../texts/Kuhn_Structure_of_Scientific_Revolutions.pdf
2020-02-08 11:06:05,685 [MainThread  ] [INFO ]  Retrieving http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server/1.23/tika-server-1.23.jar to /var/folders/9h/ttx3gqgd6jbfxzybwz7mqq7r0000gn/T/tika-server.jar.
```

Still I didn't have a JDK on my machine, so I had to download it here:
https://www.oracle.com/technetwork/java/javase/downloads/jdk13-downloads-5672538.html

And the last thing to do is remind tika where the jar is (but I think it might
already know):

```
TIKA_SERVER_JAR=/var/folders/9h/ttx3gqgd6jbfxzybwz7mqq7r0000gn/T/tika-server.jar
```

The readme for the tika project explains all the env vars to set, but that's the
only one I needed (and I probably didn't because I didn't move the jar from where
it was downloaded).

And it's done! Below script counts the number of instances of men & women (in
different forms), replaces all of the former with the latter, and returns a text
file with the changes.

```
python scripts/feminize.py -i ../texts/Kuhn_Structure_of_Scientific_Revolutions.pdf
```

I then copy-pasted the text into a word doc and exported as a PDF (somehow it
wasn't easy to find a text-to-pdf python library... I couldn't ever imagine why...).
The spacing on the result isn't great, but i's not horrible either, and I'll
finish reading the book like this.

### Conclusions

I'm satisfied with the output for now. In a second iteration I could work with
the pronouns (spoiler: I later ended up including changing the pronouns). For instance,
right now there are sentences like:

> "Intellectually such a woman has made his choice, but the conversion required
  if it is to be effective eludes him."

Right now it's amusing enough to me that I could leave it, OR, also not a lot of
work, change ALL the pronouns into feminine pronouns. Changing all the pronouns
would leave us with:

> "Maxwell herself was a Newtonian who believed that light and electromagnetism
  in general were due to variable displacements of the particles of a mechanical
  ether."

Actually in the process of looking for when "his" actually refers to a specific
person, I noticed so many generic ones, and I think i'll go ahead with the pronouns.

### Pronouns

Ok, I changed the code to by default swap the pronouns as well. I like this even
better, due to the actually not insignificant number (~370), compared to instances
of "men" and "woman" (~100).

(edit: This snippet is from an older version of this code; current counts in the
**Example** section earlier in this document. Thank you, regular expressions, for
detecting more 10 more noun changes and 70 more pronoun changes than my original
hacky code could find.)

```
 python scripts/feminize_text.py ../texts/Kuhn_Structure_of_Scientific_Revolutions.pdf
../texts/Kuhn_Structure_of_Scientific_Revolutions.pdf
Men = 97
Women = 1
Male pronouns est. = 370
Men = 0
Women = 98
```

But it also occurred to me along the way that it might be less of a hassle to just
change them all to neutral pronouns (e.g. they, their). One reason I'm going to
read the text with the female pronouns is because I want to feel the impact of it.
"They" still conjures a "male image", where "men" are still the default. So if
pushed completely in the other direction we can see the world in a different light.

I'm not going to comment at all about who was in Kuhn's world, and who were the
scientists in history. If the women were written out or they weren't there at all,
it's not stated today. But, in order to not discourage women who are already in
the field, this is a small act to test a subtle effect.

The other reason I'm doing all the pronouns also, instead of randomly spattering
femaleness around is because sometimes the feminine pronouns are clearly used in
a text more for the "ignorant student", and I want to not give randomness the
chance to conjure that image.

[1] Kuhn, T. S. (1962). The structure of scientific revolutions. Chicago: University of Chicago Press.
