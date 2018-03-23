'''
Created on 22th,March,2018

@author: Alvin Ye
'''
from dbcParser.dbcParser import dbcParser
from CanMsgLayoutDecoder.CanMsgLayoutDecoder import CanMsgLayoutDecoder
from codeGenerator.CanMsgLayoutGenerator import c_bitField_Genertor

if __name__ == "__main__":
    import sys
    s = ''
    myParser = dbcParser()
    try:
        myParser.parseDbc(sys.argv[1])
        print('INFO: dbc parsing succeed')
        with open(sys.argv[2],'w') as f:
            for msg in myParser._canNetwork.Nodes['ESCL'].NodeTxMsgs.values():

                try:
                    for m in CanMsgLayoutDecoder(msg).createLayoutMuliplexer().NodeTxMsgs.values():
                        f.write("typedef struct _c_{0}_msgTypeTag\n".format(m.MsgName))
                        f.write("{\n")
                        c_bitField_Genertor(CanMsgLayoutDecoder(m).createLayout()).bitField_Genertor(f) 
                        f.write("\n}")
                        s += "\t_c_{0}_msgType {1};\n".format(m.MsgName,m.MsgName)    
                        f.write("_c_{0}_msgType;\n".format(m.MsgName))
                    f.write("typedef union _u_{0}_msgTypeTag\n".format(msg.MsgName))
                    f.write("{\n")
                    f.write(s)
                    f.write("\n}")    
                    f.write("_u_{0}_msgType;\n".format(msg.MsgName))                    
                except :
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
    except:
        print("ERROR: no dbc file designated")    
