
jupyter_to_html:
	jupyter nbconvert --execute --to html *.ipynb

git_push:
	git add .
	git commit -m "update"
	git push
