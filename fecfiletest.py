import fecfile
import sys
import ujson as json

for item in fecfile.iter_file('test.fec'):
	sys.stdout.write(json.dumps(item.data) + '\n')
