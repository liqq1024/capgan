for A in $(seq -f "%03g" 1 18)
do
	echo "unzip dba-preprocessed-$A.zip"
		unzip dba-preprocessed-$A.zip -d dba-preprocessed-$A
done
