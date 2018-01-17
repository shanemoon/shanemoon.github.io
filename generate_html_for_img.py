

for i in range(1,44):
	
	print("<!-- Image %d -->" % i)
	s = "<li class=\"\" data-responsive=\"img/photos/%d-1440.jpg 1440\" data-src=\"img/photos/%d-1440.jpg\" data-sub-html=\"<h4></h4><p></p>\">\n \
	    <a href=\"\">\n \
	        <img class=\"img-responsive\" src=\"img/photos/%d-1440.jpg\" alt=\"Thumb-%d\">\n \
	    </a>\n \
	</li>"  % (i, i, i, i)

	print( s )

	print('')
