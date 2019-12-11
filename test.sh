inputtext="input/test1.txt"

cat $inputtext | python3 mapper.py
cat $inputtext | python3 mapper.py | sort -k1,1 | python3 reducer.py