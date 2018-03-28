'''
Created on 12th Mar, 2018

@author: Alvin Ye
'''
from dbcCoreModel.CoreModel import CanSignal
from dbcCoreModel.CoreModel import CanMsg
from dbcCoreModel.CoreModel import CanNode
import copy


class CanMsgLayoutDecoder(object):
    '''
    supporting all kinds of gaps, different endian-ness, multiple-byte, multiplexer
    '''

    def __init__(self, msg_object):
        '''
        Constructor
        '''
        self.msg = msg_object
        self._unusedBitsHead = [0, 0, 0, 0, 0, 0, 0, 0]
        self._unusedBitsTail = [7, 7, 7, 7, 7, 7, 7, 7]
        self._gap = 'unused'
        self._gapIdx = 0
        self._mulByteIdx = 0
        self._sortedSignals = {}
        self._laidSignals = {}
        self.headBit = 0
        self.tailBit = 7
        self._multiplexer_ids = []
        self._virtualNode = None
        self._virtualMsg = None
        self._virtualMultiplexer = None
        
    def _sort_signal(self):
        for signal in self.msg.msg_signals.values():
            self._sortedSignals[signal.signal_start_bit] = signal
            #  sort signals in the dict by start bit, but return a list of tuples!
        self._sortedSignals = sorted(self._sortedSignals.items(), key=lambda d: d[0])
        
    def create_layout_multiplexer(self):
        '''this func aims to create multi-msg for multiplexer'''
        for signal in self.msg.msg_signals.values():
            if signal.signal_multiplexer:
                self._virtualNode = CanNode('_virtualNode')
                self._virtualMultiplexer = signal
                self._virtualMsg = CanMsg(self.msg.msg_id, self.msg.msg_name+"M", self.msg.msg_len)
                self._virtualMsg.append_signal(signal.signal_name, signal)
                self._virtualNode.append_tx_msg(self._virtualMsg.msg_name, self._virtualMsg)
            elif signal.signal_multiplexer_id not in self._multiplexer_ids and not signal.signal_multiplexer:
                self._multiplexer_ids.append(signal.signal_multiplexer_id)
                self._virtualMsg = CanMsg(self.msg.msg_id, self.msg.msg_name+signal.signal_multiplexer_id, self.msg.msg_len)
                self._virtualMultiplexer = copy.deepcopy(self._virtualMultiplexer)
                self._virtualMsg.append_signal(self._virtualMultiplexer.signal_name, self._virtualMultiplexer)
                self._virtualMsg.append_signal(signal.signal_name, signal)
                self._virtualNode.append_tx_msg(self._virtualMsg.msg_name, self._virtualMsg)
            elif signal.signal_multiplexer_id in self._multiplexer_ids and not signal.signal_multiplexer:
                self._virtualNode.node_tx_msgs[self.msg.msg_name+signal.signal_multiplexer_id].append_signal(signal.signal_name, signal)
            else:
                raise AttributeError
        return self._virtualNode
                        
    def create_layout(self):
        self._sort_signal()
        for byteIdx in range(0, 8):
            byte_idx_temp = byteIdx
            for (start_bit, signal) in self._sortedSignals:
                #  iterate from byte0-byte7
                if byte_idx_temp * 8 <= start_bit <= (byte_idx_temp+1) * 8-1:
                    #  check endian-ness
                    if signal.signal_little_endian > 0:
                        #  this is Intel
                        #  check multiple-byte?
                        if self._unusedBitsHead[byteIdx] + signal.signal_len < 9:
                            #  1 check any gap
                            if start_bit % 8 != self._unusedBitsHead[byteIdx]:
                                #  create gap signal
                                self._laidSignals[self._gap+str(self._gapIdx)] = CanSignal(self._gap+str(self._gapIdx), self._unusedBitsHead[byteIdx], start_bit % 8-self._unusedBitsHead[byteIdx], little_endian=1, msg_carrier=signal.signal_msg_carrier)
                                #  shift unused bit position
                                self._unusedBitsHead[byteIdx] = start_bit % 8
                                self._gapIdx += 1
                            #  create signal within one byte
                            self._laidSignals[signal.signal_name] = CanSignal(signal.signal_name, signal.signal_start_bit % 8, signal.signal_len, little_endian=1, msg_carrier=signal.signal_msg_carrier)
                            #  tracking unused bit
                            self._unusedBitsHead[byteIdx] += signal.signal_len
                        else:                    
                            while signal.signal_len + self._unusedBitsHead[byteIdx] > 8:
                                self._laidSignals[signal.signal_name+str(self._mulByteIdx)] = CanSignal(signal.signal_name + str(self._mulByteIdx), signal.signal_start_bit % 8, self.tailBit-self._unusedBitsHead[byteIdx]+1, little_endian=1, msg_carrier=signal.signal_msg_carrier)
                                self._mulByteIdx += 1
                                signal.signal_len -= self.tailBit-self._unusedBitsHead[byteIdx] + 1
                                signal.signal_start_bit += self.tailBit-self._unusedBitsHead[byteIdx] + 1
                                #  current byte will be full
                                self._unusedBitsHead[byteIdx] = self.tailBit + 1
                                if byteIdx < 7:
                                    byteIdx += 1
                            else:
                                #  create signal within signal byte
                                self._laidSignals[signal.signal_name+str(self._mulByteIdx)] = CanSignal(signal.signal_name+str(self._mulByteIdx), signal.signal_start_bit % 8, signal.signal_len, little_endian=1, msg_carrier=signal.signal_msg_carrier)
                                self._mulByteIdx = 0
                                #  unusedBits needs to shifted 
                                self._unusedBitsHead[byteIdx] += signal.signal_len
                    else:
                        #  this is Motorola
                        #  check multiple-byte?
                        if self._unusedBitsHead[byteIdx] + signal.signal_len < 9:
                            #  check any gap
                            if start_bit%8 - signal.signal_len + 1 > self._unusedBitsHead[byteIdx]:
                                # create gap signal
                                self._laidSignals[self._gap+str(self._gapIdx)] = CanSignal(self._gap+str(self._gapIdx), self._unusedBitsHead[byteIdx], start_bit % 8-signal.signal_len+1-self._unusedBitsHead[byteIdx], little_endian=1, msg_carrier=signal.signal_msg_carrier)
                                # shift unused bit position
                                self._unusedBitsHead[byteIdx] = start_bit % 8-signal.signal_len + 1
                                self._gapIdx += 1
                            # create signal within signal byte
                            self._laidSignals[signal.signal_name] = CanSignal(signal.signal_name, signal.signal_start_bit % 8, signal.signal_len, little_endian=0, msg_carrier=signal.signal_msg_carrier)
                            self._unusedBitsHead[byteIdx] += signal.signal_len
                        else:         
                            while signal.signal_start_bit % 8 - self._unusedBitsHead[byteIdx] +1 < signal.signal_len:
                                self._laidSignals[signal.signal_name+str(self._mulByteIdx)] = CanSignal(signal.signal_name + str(self._mulByteIdx), signal.signal_start_bit % 8, signal.signal_start_bit % 8+1, little_endian=0, msg_carrier=signal.signal_msg_carrier)
                                self._mulByteIdx += 1
                                signal.signal_len -= signal.signal_start_bit % 8-self._unusedBitsHead[byteIdx] + 1
                                # signal.signal_start_bit + =  8*(byteIdx+1)-1
                                signal.signal_start_bit = 8 * (byteIdx + 2) - 1
                                self._unusedBitsHead[byteIdx] = signal.signal_start_bit % 8 + 1
                                if byteIdx < 7:
                                    byteIdx += 1
                            else:                              
                                # create signal within signal byte
                                self._laidSignals[signal.signal_name+str(self._mulByteIdx)] = CanSignal(signal.signal_name+str(self._mulByteIdx), signal.signal_start_bit % 8, signal.signal_len, little_endian=0, msg_carrier=signal.signal_msg_carrier)
                                self._mulByteIdx = 0    
                                self._unusedBitsHead[byteIdx] = signal.signal_start_bit % 8+1
                # gap stuffing at the tail of byte
            if self._unusedBitsHead[byte_idx_temp] <= self.tailBit:
                    self._laidSignals[self._gap+str(self._gapIdx)] = CanSignal(self._gap+str(self._gapIdx), self._unusedBitsHead[byte_idx_temp], self.tailBit-self._unusedBitsHead[byte_idx_temp]+1, little_endian=1, msg_carrier=signal.signal_msg_carrier)
                    self._gapIdx += 1
                    self._unusedBitsHead[byte_idx_temp] = self.tailBit+1
        return self._laidSignals
