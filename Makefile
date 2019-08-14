go:
	del *.png && casperjs badoo.js
	

clean:	
	-del *.png

cleandb:	
	-cd database && del *.png  && del *.xml
	
collect:
	casperjs collector.js