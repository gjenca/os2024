#!/bin/bash
cat << THE_END
<html>
<head>
<title>Gallery</title>
</head>
<body>
THE_END
while test "$#" != 0
do
	FILENAME="$1"
	echo "Spracuvam $1"
	shift
done
cat << THE_END
</body>
</head>
</html>
THE_END
