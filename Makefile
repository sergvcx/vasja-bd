go:
	del *.png && casperjs badoo.js

clean:	
	del *.png
	
collect:
	casperjs collector.js