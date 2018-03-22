'''
Created on 22th,March,2018

@author: Alvin Ye
'''
from dbcParser.dbcParser import dbcParser
from CanMsgLayoutDecoder.CanMsgLayoutDecoder import CanMsgLayoutDecoder
from codeGenerator.CanMsgLayoutGenerator import c_bitField_Genertor

if __name__ == "__main__":
    import sys
    myParser = dbcParser()
    try:
        myParser.parseDbc(sys.argv[1])
        print('INFO: dbc parsing succeed')
        with open(sys.argv[2],'w') as f:
            for msg in myParser._canNetwork.Nodes['ESCL'].NodeTxMsgs.values():
                f.write("typedef struct _c_{0}_msgTypeTag\n".format(msg.MsgName))
                f.write("{\n")
                c_bitField_Genertor(CanMsgLayoutDecoder(msg).createLayout()).bitField_Genertor(f)
                f.write("\n}")    
                f.write("_c_{0}_msgType;\n".format(msg.MsgName))
            print("INFO: file generation succeed")
    except UnicodeDecodeError:
        print("dbc decoding error, please convert dbc to utf-8 first")
    except KeyError:
        print("input the correct name of ESCL")
#     except:
#         print("ERROR: no dbc file designated")    
