Feminize Kuhn
=============

2h project including thinking time and file downloading time.

I keep getting distracted by all the times Kuhn says "men in science". I might have an easier time reading the Structure of Scientific Revolutions if I replace all instances of "men" with "women".

I found this apache tika library for parsing PDFs.
https://github.com/chrismattmann/tika-python

The tika library kicked off a download of a jar file that ended up here:
```
$ python scripts/feminize_text.py texts/Kuhn_Structure_of_Scientific_Revolutions.pdf 
2020-02-08 11:06:05,685 [MainThread  ] [INFO ]  Retrieving http://search.maven.org/remotecontent?filepath=org/apache/tika/tika-server/1.23/tika-server-1.23.jar to /var/folders/9h/ttx3gqgd6jbfxzybwz7mqq7r0000gn/T/tika-server.jar.
```

Still I didn't have a JDK on my machine, so I had to download it here:
https://www.oracle.com/technetwork/java/javase/downloads/jdk13-downloads-5672538.html

And the last thing to do is remind tika where the jar is (but I think it might already know):
TIKA_SERVER_JAR=/var/folders/9h/ttx3gqgd6jbfxzybwz7mqq7r0000gn/T/tika-server.jar
The readme for the tika project explains all the env vars to set, but that's the only one I needed (and I probably didn't because I didn't move the jar from where it was downloaded).

And it's done! Below script counts the number of instances of men & women (in different forms), replaces all of the former with the latter, and returns a text file with the changes.
```
python scripts/feminize_text.py texts/Kuhn_Structure_of_Scientific_Revolutions.pdf
```

I then copy-pasted the text into a word doc and exported as a PDF (somehow it wasn't easy to find a text-to-pdf python library... I couldn't ever imagine why :P). The spacing on the result isn't great, but i's not horrible either, and I'll finish reading the book like this.

### Conclusions

I'm satisfied with the output for now. In a second iteration I could work with the pronouns. For instance, right now there are sentences like:
"Intellectually such a woman has made his choice, but the conversion required if it is to be effective eludes him."

Right now it's amusing enough to me that I could leave it, OR, also not a lot of work, change ALL the pronouns into feminine pronouns. Changing all the pronouns would leave us with:

"Maxwell herself was a Newtonian who believed that light and electromagnetism in general were due to variable displacements of the particles of a mechanical ether."

Actually in the process of looking for when "his" actually refers to a specific person, I noticed so many generic ones, and I think i'll go ahead with the pronouns.

### Pronouns

Ok, I changed the code to by default swap the pronouns as well. I like this even better, due to the actually not insignificant number (~370), compared to instances of "men" and "woman" (~100).

```
 python scripts/feminize_text.py texts/Kuhn_Structure_of_Scientific_Revolutions.pdf 
texts/Kuhn_Structure_of_Scientific_Revolutions.pdf
<class 'dict'> <class 'str'>
Men = 97
Women = 1
Male pronouns est. = 370
Men = 0
Women = 98
```

But it also occurred to me along the way that it might be less of a hassle to just change them all to neutral pronouns (e.g. they, their). One reason I'm going to read the text with the female pronouns is because I want to feel the impact of it. "They" still conjures a "male image", where "men" are still the default. So if pushed completely in the other direction we can see the world in a different light.

I'm not going to comment at all about who was in Kuhn's world, and who were the scientists in history. If the women were written out or they weren't there at all, it's not state today. But, in order to not discourage women who are already in the field, this is a small test to see subtle impact.

The other reason I'm doing all the pronouns also, instead of randomly spattering femaleness around is because sometimes the feminine pronouns are clearly used in a text more for the "ignorant student", and I want to not give randomness the chance to conjure that image.
