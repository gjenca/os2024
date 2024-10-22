#!/bin/bash
PERCENT=10
TITLE="Gallery"
while true
do
	if [ "$1" == "-t" ]
	then
		TITLE="$2"
		shift 2
	elif [ "$1" == "-p" ]
	then
		PERCENT="$2"
		shift 2
	else
		break
	fi
done
cat << THE_END
<html>
<head>
<title>$TITLE</title>
</head>
<body>
<h1>$TITLE</h1>
<ul>
THE_END
if [ ! -d mini ]
then
	mkdir mini
fi
while test "$#" != 0
do
	FILENAME="$1"
	PNGNAME=$(echo "$1" | sed 's/jpg$/png/')
	convert -resize "%$PERCENT" "$1" "mini/$PNGNAME" 2>/dev/null
	echo '<li>'
	echo '<a href="'"$1"'">'
	echo '<img src="'"mini/$PNGNAME"'">'
	echo '</a>'
	echo '</li>'
	shift
done
cat << THE_END
</ul>
</body>
</head>
</html>
THE_END
