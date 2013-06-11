#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, zipfile, re

def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)

def unzipping(z, nowcode="cp949"):
	for f in z.namelist():
		try:
			if f.endswith('/'):
				os.makedirs(f)
			else:
				zfile = z.open(f)
				zstr = zfile.read()
				zstr = unicode(zstr , nowcode, errors="ignore").encode('utf-8', errors="ignore")
				zstr = zstr.replace("\00", "").replace("\x0A", "\n").replace("\x0D","\r")
				if f.startswith('/') is not True:
					f = "/"+f
				f = f.encode('utf-8')
				fp = open(f, 'w')
				fp.write(zstr)
				fp.close()

			print(str(f))

		except Exception as e:
			print("Error : " + str(e))

	z.close()

dlist = os.listdir("/".join(sys.argv[1].split("/")[:-1]))

for fname in dlist:
	arr = sys.argv[1].replace("*",".*").split("/")
	patt = arr[-1]
	if re.match(patt, fname):
		fullpath = "/".join(arr[:-1]) + "/" + fname
		unzipping(zipfile.ZipFile(fullpath))
		print("Extract file : " + fname)
	else:
		unzipping(zipfile.ZipFile(sys.argv[1]))
		break
