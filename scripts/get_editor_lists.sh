FILES=~/knowlab_real/wikipedia_projects/conservative_articles/*.7z
for f in $FILES

do
	7z e $f
	python coedit.py ${f%.7z}
	rm ${f%.7z}
done
