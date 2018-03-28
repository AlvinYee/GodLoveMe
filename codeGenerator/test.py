'''
Created on 22th, March, 2018

@author: Alvin Ye
'''

import sys
sys.path.append('../')
sys.path.append('../../')
from dbcParser import DbcParser
from CanMsgLayoutDecoder.CanMsgLayoutDecoder import CanMsgLayoutDecoder
from codeGenerator.CanMsgLayoutGenerator import SignalBitFieldSyntaxGenerator

if __name__ == '__main__':
    s = ''
    myParser = DbcParser()
    try:
        myParser.parser_dbc(sys.argv[1])
        print('[INFO]: dbc parsing succeed')
        with open(sys.argv[2], 'w') as hFile:
            with open(sys.argv[3], 'w') as cFile:
                for msg in myParser.can_network.nodes['ESCL'].node_tx_msgs.values():
                    # for signal in msg.msg_signals.values:
                    #     if signal.signal_multiplexer:
                    #         break
                    # else:
                    #     pass
                    try:
                        for virtual_msg in CanMsgLayoutDecoder(msg).decode_msg_with_multiplexer().node_tx_msgs.values():
                            hFile.write('typedef struct _c_{0}_msg_typeTag\n'.format(virtual_msg.msg_name))
                            hFile.write('{\n')
                            decoded_msg, over_byte_bound_virtual_signals = CanMsgLayoutDecoder(
                                virtual_msg).decode_msg_without_multiplexer()
                            signalGenerator = SignalBitFieldSyntaxGenerator(decoded_msg)
                            signalGenerator.bit_field_generator(hFile)
                            hFile.write('\n}')
                            s += '\t_c_{0}_msg_type {1};\n'.format(virtual_msg.msg_name, virtual_msg.msg_name)
                            hFile.write('_c_{0}_msg_type;\n'.format(virtual_msg.msg_name))
                            signalGenerator.signal_union_generator(msg, cFile)
                            signalGenerator.signal_access_macro_syntax(over_byte_bound_virtual_signals, hFile)
                        hFile.write('typedef union _u_{0}_msg_typeTag\n'.format(msg.msg_name))
                        hFile.write('{\n')
                        hFile.write(s)
                        hFile.write('\n}')    
                        hFile.write('_u_{0}_msg_type;\n'.format(msg.msg_name))
                        cFile.write('_u_{0}_msg_type\t\t{1};\n'.format(msg.msg_name, msg.msg_name))
                    except TypeError or AttributeError:
                        hFile.write('typedef struct _c_{0}_msg_typeTag\n'.format(msg.msg_name))
                        hFile.write('{\n')
                        decoded_msg, over_byte_bound_virtual_signals = CanMsgLayoutDecoder(
                            msg).decode_msg_without_multiplexer()
                        signalGenerator = SignalBitFieldSyntaxGenerator(decoded_msg)
                        signalGenerator.bit_field_generator(hFile)
                        hFile.write('\n}')    
                        hFile.write('_c_{0}_msg_type;\n'.format(msg.msg_name))
                        cFile.write('_c_{0}_msg_type\t\t{1};\n'.format(msg.msg_name, msg.msg_name))
                        signalGenerator.signal_struct_generator(cFile)
                        signalGenerator.signal_access_macro_syntax(over_byte_bound_virtual_signals, hFile)
                print('[INFO]: file generation succeed')
    except UnicodeDecodeError:
        print('[ERROR] dbc decoding error, please convert dbc to utf-8 first')
    except KeyError:
        print('[ERROR] input the correct name of ESCL')
    except FileNotFoundError:
        print('[ERROR]: no dbc file designated')    
    except IndexError:
        print('[ERROR]: input or output directory is not properly given')
