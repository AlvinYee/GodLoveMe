'''
Created on 12th Mar, 2018

@author: Alvin Ye
'''
from dbcCoreModel.CoreModel import CANSignal
class CanMsgLayoutDecoder(object):
    '''
    classdocs
    '''

    def __init__(self, msgObject):
        '''
        Constructor
        '''
        self.msg = msgObject
        self._unusedBits = [0,0,0,0,0,0,0,0]
#         self.fieldDef = ''
#         self._prefix   = ' unit8 '
#         self._delimiter = ' : '
#         self._postfix  = ';\n'
        self._gap      = 'unused'
        self._gapIdx   = 0
        self._mulByteIdx   = 0
        self._sortedSignals  = {}
        self._laidSignals= {}

    def sortSignal(self):
        for signal in self.msg.MsgSignals.values():
            self._sortedSignals[signal.SignalStartBit] = signal
            #sort signals in the dict by start bit, but return a list of tuples!
        self._sortedSignals = sorted(self._sortedSignals.items(),key = lambda d:d[0])
     
    def createLayout(self):
        
        self.sortSignal()
        for byteIdx in range(0,8):
            for (startBit,signal) in self._sortedSignals:
                #iterate from byte0-byte7
                if startBit < (byteIdx+1) * 8-1:
                    #1 check any gap
                    if  startBit%8 != self._unusedBits[byteIdx]:
                        #create gap signal
                        self._laidSignals[self._gap+str(self._gapIdx)] = CANSignal(self._gap+str(self._gapIdx),self._unusedBits[byteIdx],startBit%8-self._unusedBits[byteIdx])
                        #shift unused bit position
                        self._unusedBits[byteIdx] = startBit%8
                        self._gapIdx += 1
                    #2 check endian-ness
                    if signal.SignalLittleEndian:
                        #this is Intel
                        #3 check multiple-byte?
                        try:
                            #overflow on one byte
                            while int(signal.SignalLength) + self._unusedBits[byteIdx] > 9:
                                self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),self._unusedBits[byteIdx],8-self._unusedBits[byteIdx])
                                self._mulByteIdx += 1
                                signal.SignalLength -= 8-self._unusedBits[byteIdx]
                                byteIdx += 1
                            else:
                                #create signal within signal byte
                                self._laidSignals[signal.SignalName] = CANSignal(signal.SignalName+str(self._mulByteIdx),self._unusedBits[byteIdx],signal.SignalLength)
                                self._mulByteIdx = 0
                        except:                           
                            pass
                    else:
                        #this is Motorola
                        #check multiple-byte?
                        while signal.SignalLength + self._unusedBits[byteIdx] > 9:
                            self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),self._unusedBits[byteIdx],8-self._unusedBits[byteIdx])
                            self._mulByteIdx += 1
                            signal.SignalLength -= 8-self._unusedBits[byteIdx]
                            byteIdx -= 1
                        else:
                            #create signal within signal byte
                            self._laidSignals[signal.SignalName] = CANSignal(signal.SignalName+str(self._mulByteIdx),self._unusedBits[byteIdx],signal.SignalLength)
                            self._mulByteIdx = 0
                       
        return self._laidSignals
