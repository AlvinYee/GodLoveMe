'''
Created on 22th,March,2018

@author: Alvin Ye
'''
import sys
sys.path.append('../')
sys.path.append('../../')

from dbcParser import dbcParser
from CanMsgLayoutDecoder.CanMsgLayoutDecoder import CanMsgLayoutDecoder
from codeGenerator.CanMsgLayoutGenerator import c_signalBitField_Genertor

if __name__ == "__main__":
    s = ''
    myParser = dbcParser()
    try:
        myParser.parseDbc(sys.argv[1])
        print('[INFO]: dbc parsing succeed')
        with open(sys.argv[2],'w') as hFile:
            with open(sys.argv[3],'w') as cFile:
                for msg in myParser._canNetwork.Nodes['ESCL'].NodeTxMsgs.values():
                    try:
                        for m in CanMsgLayoutDecoder(msg).createLayoutMuliplexer().NodeTxMsgs.values():
                            hFile.write("typedef struct _c_{0}_msgTypeTag\n".format(m.MsgName))
                            hFile.write("{\n")
                            signalGenerator = c_signalBitField_Genertor(CanMsgLayoutDecoder(m).createLayout())
                            signalGenerator.bitField_Genertor(hFile) 
                            hFile.write("\n}")
                            s += "\t_c_{0}_msgType {1};\n".format(m.MsgName,m.MsgName)    
                            hFile.write("_c_{0}_msgType;\n".format(m.MsgName))
                            signalGenerator.signalAccessUnion_Genertor(msg,cFile) 
                        hFile.write("typedef union _u_{0}_msgTypeTag\n".format(msg.MsgName))
                        hFile.write("{\n")
                        hFile.write(s)
                        hFile.write("\n}")    
                        hFile.write("_u_{0}_msgType;\n".format(msg.MsgName))   
                        cFile.write("_u_{0}_msgType\t\t{1};\n".format(msg.MsgName,msg.MsgName))             
                    except TypeError:
                        hFile.write("typedef struct _c_{0}_msgTypeTag\n".format(msg.MsgName))
                        hFile.write("{\n")
                        signalGenerator = c_signalBitField_Genertor(CanMsgLayoutDecoder(msg).createLayout())
                        signalGenerator.bitField_Genertor(hFile)    
                        hFile.write("\n}")    
                        hFile.write("_c_{0}_msgType;\n".format(msg.MsgName))
                        cFile.write("_c_{0}_msgType\t\t{1};\n".format(msg.MsgName,msg.MsgName))
                        signalGenerator.signalAccessStruct_Genertor(cFile) 
                print("[INFO]: file generation succeed")
    except UnicodeDecodeError:
        print("[ERROR] dbc decoding error, please convert dbc to utf-8 first")
    except KeyError:
        print("[ERROR] input the correct name of ESCL")
    except FileNotFoundError:
        print("[ERROR]: no dbc file designated")    
    except IndexError:
        print("[ERROR]: input or output directory is not properly given")
