FILES=~/knowlab_real/wikipedia_projects/liberal_articles/*
for f in $FILES

do
	7z e $f
	python anon.py ${f%.7z}
	rm ${f%.7z}
done