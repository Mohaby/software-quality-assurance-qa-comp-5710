#output can be found in fuzz_output.jpg
from mining import *


def fuzzDays_between():
   try:
    # one only one day is formatted with datetime
    d1_= datetime(2024, 12, 23, 0, 0)
    d2_ = "june 2, 2024"
    res = days_between(d1_, d2_)
    return res
   except Exception as e:
        print ("Type error:", e)
   

def fuzz_getDevEmailForCommit():
    try:
    #invalid hash
        res = getDevEmailForCommit("this_path_is_invalid", 123)
        return res
    except Exception as e:
        print ("Hash type is unsupported:", e)
    

def fuzz_makeChunks():
    try:
    #extra parameter
        res = makeChunks("list_name", "size_chunk", 123)
        return res
    except Exception as e:  
        print ("Error:", e)
    

def fuzz_getPythonFileCount():
   try:
    #unsupported path type
    res = getPythonFileCount(1)
    return res
   except Exception as e:
     print ("Unsupported path type:", e)
   

def fuzz_dumpContentIntoFile():
   try:
   #invalid path type
    res = dumpContentIntoFile(1, "file" )
    return res
   except Exception as e:
    print ("Invalid path type:", e)
   

if __name__=='__main__':
    fuzz_makeChunks()
    fuzz_dumpContentIntoFile()
    fuzz_getDevEmailForCommit()
    fuzz_getPythonFileCount()
    fuzzDays_between()

