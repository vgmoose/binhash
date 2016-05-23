# binhash
A tool to compare hashes of binaries within a directory easier

## Usage
The below command sequence will generate a binhash for all binaries in /bin, /usr/bin, and /sbin:
```
python binhash.py
g
/bin:/usr/bin:/sbin/
```
The file will be written as binhash[unix timestamp].txt

This can then be compared with another file from another machine generated in a similar manner, as follows:
```
python binhash.py
c
my_binhash.txt
friends_binhash.txt
```

If you are on the same architecture and operating system, then you should expect both binhashes to be nearly identical.
