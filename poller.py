#!/usr/bin/python
import shutil
import os
import datetime as dt

topdir = r"<path>"
dstdir = r"<path>"

exten =  ".pdf"
#path = os.path.join(topdir, fname)
#st = os.stat(path)
#mtime = dt.datetime.fromtimestamp(st.st_mtime)
ago = dt.datetime.now() - dt.timedelta(minutes=1)


for dname, names, files in os.walk(topdir):
    for name in files:
        if name.lower().endswith(exten):
            path = os.path.join(dname, name)
            st = os.stat(path)
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                # Prints result of walk
                print(os.path.join(dname, name))
                #copy all files with given extension to the dst folder
                path = os.path.realpath(os.path.join(dname, name))
                shutil.copy2(path, dstdir)