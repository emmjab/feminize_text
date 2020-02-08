Feminize Kuhn
=============

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
