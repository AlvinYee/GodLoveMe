'''
Created on 12th Mar, 2018

@author: Alvin Ye
'''
from dbcCoreModel.CoreModel import CANSignal
from dbcCoreModel.CoreModel import CanMsg
from dbcCoreModel.CoreModel import CanNode
import copy
class CanMsgLayoutDecoder(object):
    '''
    supporting all kinds of gaps,different endian-ness, multiple-byte,multiplexer
    '''

    def __init__(self, msgObject):
        '''
        Constructor
        '''
        self.msg = msgObject
        self._unusedBitsHead = [0,0,0,0,0,0,0,0]
        self._unusedBitsTail = [7,7,7,7,7,7,7,7]
        self._gap      = 'unused'
        self._gapIdx   = 0
        self._mulByteIdx   = 0
        self._sortedSignals  = {}
        self._laidSignals= {}
        self.headBit = 0
        self.tailBit = 7
        self._multiplexerIds = []
        self._virtualNode = None
        self._virtualMsg = None
        self._virtualMultiplexer = None
        
    def sortSignal(self):
        for signal in self.msg.MsgSignals.values():
            self._sortedSignals[signal.SignalStartBit] = signal
            #sort signals in the dict by start bit, but return a list of tuples!
        self._sortedSignals = sorted(self._sortedSignals.items(),key = lambda d:d[0])
        
    def createLayoutMuliplexer(self):
        ' this func aims to create multi-msg for multiplexer'
        for signal in self.msg.MsgSignals.values():
            if signal.SignalMultiplexer:
                self._virtualNode = CanNode('_virtualNode')
                self._virtualMultiplexer = signal
                self._virtualMsg = CanMsg(self.msg.MsgId,self.msg.MsgName+"M", self.msg.MsgLen)
                self._virtualMsg.appendSignal(signal.SignalName,signal)
                self._virtualNode.appendTxMsg(self._virtualMsg.MsgName,self._virtualMsg)
            elif signal.SignalMultiplexerId not in self._multiplexerIds and not signal.SignalMultiplexer:
                self._multiplexerIds.append(signal.SignalMultiplexerId)
                self._virtualMsg = CanMsg(self.msg.MsgId,self.msg.MsgName+signal.SignalMultiplexerId,self.msg.MsgLen)
                self._virtualMultiplexer = copy.deepcopy(self._virtualMultiplexer)
                self._virtualMsg.appendSignal(self._virtualMultiplexer.SignalName,self._virtualMultiplexer)
                self._virtualMsg.appendSignal(signal.SignalName,signal)
                self._virtualNode.appendTxMsg(self._virtualMsg.MsgName,self._virtualMsg)
            elif signal.SignalMultiplexerId in self._multiplexerIds and not signal.SignalMultiplexer :
                self._virtualNode.NodeTxMsgs[self.msg.MsgName+signal.SignalMultiplexerId].appendSignal(signal.SignalName,signal)
            else:
                raise AttributeError
        return self._virtualNode
                        
    def createLayout(self):
        #TODO:       
        self.sortSignal()
        for byteIdx in range(0,8):
            byteIdxTemp = byteIdx
            for (startBit,signal) in self._sortedSignals:
#                 if signal.SignalMultiplexerId or signal.SignalMultiplexer:
#                     continue
                #iterate from byte0-byte7
                if byteIdxTemp * 8 <= startBit <= (byteIdxTemp+1) * 8-1:
                    #check endian-ness
                    if signal.SignalLittleEndian > 0 :
                        #this is Intel
                        #check multiple-byte?
                        if self._unusedBitsHead[byteIdx] + signal.SignalLength < 9:# unusedBits indicates 
                            #1 check any gap
                            if  startBit%8 != self._unusedBitsHead[byteIdx]:
                                #create gap signal
                                self._laidSignals[self._gap+str(self._gapIdx)] = CANSignal(self._gap+str(self._gapIdx),self._unusedBitsHead[byteIdx],startBit%8-self._unusedBitsHead[byteIdx],littleEndian=1,msgCarrier=signal.SignalMsgCarrier)
                                #shift unused bit position
                                self._unusedBitsHead[byteIdx] = startBit%8
                                self._gapIdx += 1
                            #create signal within one byte
                            self._laidSignals[signal.SignalName] = CANSignal(signal.SignalName,signal.SignalStartBit%8,signal.SignalLength,littleEndian=1,msgCarrier=signal.SignalMsgCarrier)
                            self._unusedBitsHead[byteIdx] += signal.SignalLength# unusedBits indicates 
                        else:                    
                            while signal.SignalLength + self._unusedBitsHead[byteIdx] > 8:
                                self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),signal.SignalStartBit%8,self.tailBit-self._unusedBitsHead[byteIdx]+1,littleEndian=1,msgCarrier = signal.SignalMsgCarrier)
                                self._mulByteIdx += 1
                                signal.SignalLength -= self.tailBit-self._unusedBitsHead[byteIdx] +1
                                signal.SignalStartBit += self.tailBit-self._unusedBitsHead[byteIdx] + 1
                                #current byte will be full
                                self._unusedBitsHead[byteIdx] = self.tailBit + 1
                                if byteIdx < 7:
                                    byteIdx += 1
                            else:
                                #create signal within signal byte
                                self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),signal.SignalStartBit%8,signal.SignalLength,littleEndian=1,msgCarrier = signal.SignalMsgCarrier)
                                self._mulByteIdx = 0
                                # unusedBits needs to shifted 
                                self._unusedBitsHead[byteIdx] += signal.SignalLength
                    else:
                        #this is Motorola
                        #check multiple-byte?
                        if self._unusedBitsHead[byteIdx] + signal.SignalLength < 9:# unusedBits indicates 
                            #check any gap
                            if startBit%8 - signal.SignalLength +1 >  self._unusedBitsHead[byteIdx] :
                                #create gap signal
                                self._laidSignals[self._gap+str(self._gapIdx)] = CANSignal(self._gap+str(self._gapIdx),self._unusedBitsHead[byteIdx],startBit%8-signal.SignalLength+1-self._unusedBitsHead[byteIdx],littleEndian=1,msgCarrier = signal.SignalMsgCarrier)
                                #shift unused bit position
                                self._unusedBitsHead[byteIdx] = startBit%8-signal.SignalLength+1
                                self._gapIdx += 1
                            #create signal within signal byte
                            self._laidSignals[signal.SignalName] = CANSignal(signal.SignalName,signal.SignalStartBit%8,signal.SignalLength,littleEndian=0,msgCarrier = signal.SignalMsgCarrier)
                            self._unusedBitsHead[byteIdx] += signal.SignalLength
                        else:         
                            while signal.SignalStartBit%8 - self._unusedBitsHead[byteIdx] +1 < signal.SignalLength:
                                self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),signal.SignalStartBit%8,signal.SignalStartBit%8+1,littleEndian=0,msgCarrier = signal.SignalMsgCarrier)
                                self._mulByteIdx += 1
                                signal.SignalLength -= signal.SignalStartBit%8-self._unusedBitsHead[byteIdx] + 1
                                #signal.SignalStartBit += 8*(byteIdx+1)-1
                                signal.SignalStartBit = 8*(byteIdx+2)-1
                                self._unusedBitsHead[byteIdx] = signal.SignalStartBit%8+1
                                if byteIdx < 7:
                                    byteIdx += 1
                            else:                              
                                #create signal within signal byte
                                self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),signal.SignalStartBit%8,signal.SignalLength,littleEndian=0,msgCarrier = signal.SignalMsgCarrier)
                                self._mulByteIdx = 0    
                                self._unusedBitsHead[byteIdx] = signal.SignalStartBit%8+1 # todo: this is a bug
                #gap stuffing at the tail of byte
            if self._unusedBitsHead[byteIdxTemp] <= self.tailBit:
                    self._laidSignals[self._gap+str(self._gapIdx)] = CANSignal(self._gap+str(self._gapIdx),self._unusedBitsHead[byteIdxTemp],self.tailBit-self._unusedBitsHead[byteIdxTemp]+1,littleEndian=1,msgCarrier = signal.SignalMsgCarrier)   
                    self._gapIdx +=1
                    self._unusedBitsHead[byteIdxTemp] = self.tailBit+1
        return self._laidSignals
