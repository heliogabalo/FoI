awk '{ sub("\r$", ""); print }' \
	file-copy.spec \
	> file-copy2.spec
