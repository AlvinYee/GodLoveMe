'''
Created on 13th,March,2018

@author: Alvin Ye
'''
import sys
sys.path.append('../')
import dbcParser
if __name__ == "__main__":
    myParser = dbcParser.dbcParser()
    try:
        myParser.parseDbc(sys.argv[1])
        with open(sys.argv[2],'w') as f:
            myParser.iterateDbc(f)
        print('[INFO]: dbc parsing succeed')
    except UnicodeDecodeError:
        print("[ERROR] dbc decoding error, please convert dbc to utf-8 first")
    except KeyError:
        print("[ERROR] input the correct name of ESCL")
    except FileNotFoundError:
        print("[ERROR]: no dbc file designated")
    except IndexError:
        print("[ERROR]: input or output directory is not properly given")
