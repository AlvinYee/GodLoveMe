'''
Created on 13th,March,2018

@author: Alvin Ye
'''
import dbcParser
if __name__ == "__main__":
    import sys
    myParser = dbcParser.dbcParser()
    try:
        myParser.parseDbc(sys.argv[1])
        myParser.iterateDbc()
        print('INFO: dbc parsing succeed')
    except:
        print("ERROR: no dbc file designated")
