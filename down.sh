for A in $(seq -f "%03g" 1 18)
do
	echo "wget http://zju-capg.org/myo/data/dba-preprocessed-$A.zip"
	wget http://zju-capg.org/myo/data/dba-preprocessed-$A.zip
done
