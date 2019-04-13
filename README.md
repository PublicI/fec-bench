
```
$ npm install
$ pipenv install
$ curl -s "http://docquery.fec.gov/dcdev/posted/1300352.fec" > test.fec
$ wc -l test.fec
 10294029 test.fec
$ du -h test.fec
2.3G	test.fec
$ time pipenv run python fecfiletest.py > /dev/null
real	24m34.245s
user	23m50.230s
sys	0m3.947s
$ time npx fec2json test < test.fec > /dev/null
real	3m10.033s
user	3m1.895s
sys	0m9.437s
```
