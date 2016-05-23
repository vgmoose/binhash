#!/bin/python
import os, hashlib, time

print "   binhash   \n-------------\n   g) generate a binhash\n   c) compare two binhashes"
choice = raw_input(">> ").lower()

defaultPath = os.environ['PATH']

width = 0
try:
	rows, cols = os.popen('stty size', 'r').read().split()
	width = int(cols)
except:
	pass

def update(message):
	bonus = ""
	if width != 0:
		if len(message) > width:
			message = message[-1*width:]
		bonus = " " * (width - len(message) )
	print "\033[F" + message + bonus

if "g" in choice:
	directories = raw_input("Path ["+defaultPath+"]: ") or defaultPath
	print "Generating binhash...\n"

	binmap = {}

	dirs = directories.split(":")
	for d in dirs:
		#update("Checking " + d + "...")
		for root, sub, files, in os.walk(d):
			for f in files:
				af = root + "/" + f
				#update("Checking if " + af + " is executable...") 
				exe = os.access(af, os.X_OK)
				try:
					if exe:
						update("Hashing " + af + "...")
						binmap[af] = hashlib.md5(open(af,'rb').read()).hexdigest()
						update(af + " hashed to " + binmap[af])
				except:
					pass
	update("All done!")
	filename = "binhash" + str(int(time.time())) + ".txt"
	output = open(filename, "w")
	for key in binmap:
		output.write(key+":\t"+binmap[key]+"\n")
	output.close()
	print "Wrote binhash to " + filename + "!" 

elif "c" in choice:
	path1 = raw_input("Path to 1st binhash: ")
	path2 = raw_input("Path to 2nd binhash: ")

	binmap1 = {}
	intersect = {}

	# load all hashes from file 1
	for line in open(path1, "r"):
		data = line.split(":\t")
		binmap1[data[0]] = data[1]

	# load all intersecting from file 2
	for line in open(path2, "r"):
		data = line.split(":\t")
		if data[0] in binmap1:
			intersect[data[0]] = (binmap1[data[0]], data[1])
	
	# start comparing
	total = len(intersect)
	mismatch = 0

	for key in intersect:
		if intersect[key][0] != intersect[key][1]:
			mismatch += 1
			print key + " differs! (" + intersect[key][0][:6] + " vs " + intersect[key][1][:6] + ")"

	print "Total files: " + str(total)
	print "Total differing: " + str(mismatch)

else:
	print "Invalid selection!"
