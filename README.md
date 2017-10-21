# Rollup Aggregation 

#### To test the code:
```bash

python rollup.py -i ./testcases/case2.txt -o outputfile.txt --c position
python rollup.py -i ./testcases/case2.txt -o outputfile.txt --c company,position

python rollup.py -i ./testcases/case1.txt -o outputfile.txt --c a,b,c
python rollup.py -i ./testcases/case1.txt -o outputfile.txt --c a,b
python rollup.py -i ./testcases/case1.txt -o outputfile.txt

python rollup.py -i ./testcases/case100.txt -o outputfile.txt --c 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
python rollup.py -i ./testcases/case100.txt -o outputfile.txt --c 1,2,3,4,5,6,7,8,9,10,11,12,13
python rollup.py -i ./testcases/case100.txt -o outputfile.txt --c 1,2,3,4,5,6,7,8,9,10
python rollup.py -i ./testcases/case100.txt -o outputfile.txt --c 1,2,3,4,5,6,7,8,
python rollup.py -i ./testcases/case100.txt -o outputfile.txt --c 1,2,3,4,5

```