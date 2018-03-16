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
        self._unusedBitsHead = [0,0,0,0,0,0,0,0]
        self._unusedBitsTail = [8,8,8,8,8,8,8,8]
#         self.fieldDef = ''
#         self._prefix   = ' unit8 '
#         self._delimiter = ' : '
#         self._postfix  = ';\n'
        self._gap      = 'unused'
        self._gapIdx   = 0
        self._mulByteIdx   = 0
        self._sortedSignals  = {}
        self._laidSignals= {}
        self.headBit = 0
        self.tailBit = 7

    def sortSignal(self):
        for signal in self.msg.MsgSignals.values():
            self._sortedSignals[signal.SignalStartBit] = signal
            #sort signals in the dict by start bit, but return a list of tuples!
        self._sortedSignals = sorted(self._sortedSignals.items(),key = lambda d:d[0])
     
#     def createLayout(self):
#         #TODO:       
#         self.sortSignal()
#         for byteIdx in range(0,8):
#             for (startBit,signal) in self._sortedSignals:
#                 #iterate from byte0-byte7
#                 if startBit < (byteIdx+1) * 8-1:
#                     #1 check any gap
#                     if  startBit%8 != self._unusedBitsHead[byteIdx]:
#                         #create gap signal
#                         self._laidSignals[self._gap+str(self._gapIdx)] = CANSignal(self._gap+str(self._gapIdx),self._unusedBitsHead[byteIdx],startBit%8-self._unusedBitsHead[byteIdx])
#                         #shift unused bit position
#                         self._unusedBitsHead[byteIdx] = startBit%8
#                         self._gapIdx += 1
#                     #2 check endian-ness
#                     if signal.SignalLittleEndian:
#                         #this is Intel
#                         #3 check multiple-byte?
#                         try:
#                             #overflow on one byte
#                             while int(signal.SignalLength) + self._unusedBitsHead[byteIdx] > 9:
#                                 self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),self._unusedBitsHead[byteIdx],8-self._unusedBitsHead[byteIdx])
#                                 self._mulByteIdx += 1
#                                 signal.SignalLength -= 8-self._unusedBitsHead[byteIdx]
#                                 if byteIdx < 7:
#                                     byteIdx += 1
#                             else:
#                                 #create signal within signal byte
#                                 self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),self._unusedBitsHead[byteIdx],signal.SignalLength)
#                                 self._mulByteIdx = 0
#                         except:                           
#                             pass
#                     else:
#                         #this is Motorola
#                         #check multiple-byte?
#                         while signal.SignalLength + self._unusedBitsHead[byteIdx] > 9:
#                             self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),self._unusedBitsHead[byteIdx],8-self._unusedBitsHead[byteIdx])
#                             self._mulByteIdx += 1
#                             signal.SignalLength -= 8-self._unusedBitsHead[byteIdx]
#                             if byteIdx < 7:
#                                 byteIdx += 1
#                         else:
#                             #create signal within signal byte
#                             self._laidSignals[signal.SignalName] = CANSignal(signal.SignalName+str(self._mulByteIdx),self._unusedBitsHead[byteIdx],signal.SignalLength)
#                             self._mulByteIdx = 0
#                        
#         return self._laidSignals
    def createLayout(self):
        #TODO:       
        self.sortSignal()
        for byteIdx in range(0,8):
            for (startBit,signal) in self._sortedSignals:
                if signal.SignalMultiplexerId or signal.SignalIsMultiplexer:
                    continue
                #iterate from byte0-byte7
                if byteIdx * 8 <= startBit <= (byteIdx+1) * 8-1:
                    #check endian-ness
                    if signal.SignalLittleEndian > 0 :
                        #this is Intel
                        #check multiple-byte?
                        if self._unusedBitsHead[byteIdx] + signal.SignalLength < 9:# unusedBits indicates 
                            #1 check any gap
                            if  startBit%8 != self._unusedBitsHead[byteIdx]:
                                #create gap signal
                                self._laidSignals[self._gap+str(self._gapIdx)] = CANSignal(self._gap+str(self._gapIdx),self._unusedBitsHead[byteIdx],startBit%8-self._unusedBitsHead[byteIdx])
                                #shift unused bit position
                                self._unusedBitsHead[byteIdx] = startBit%8
                                self._gapIdx += 1
                            #create signal within one byte
                            self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName,signal.SignalStartBit%8,signal.SignalLength,littleEndian=1)
                            self._unusedBitsHead[byteIdx] += signal.SignalLength# unusedBits indicates 
                        else:                    
                            while signal.SignalLength + self._unusedBitsHead[byteIdx] > 8:
                                self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),signal.SignalStartBit%8,self.tailBit-self._unusedBitsHead[byteIdx]+1,littleEndian=1)
                                self._mulByteIdx += 1
                                signal.SignalLength -= self.tailBit-self._unusedBitsHead[byteIdx] +1
                                signal.SignalStartBit += self.tailBit-self._unusedBitsHead[byteIdx] + 1
                                #current byte will be full
                                self._unusedBitsHead[byteIdx] = self.tailBit + 1
                                if byteIdx < 7:
                                    byteIdx += 1
                            else:
                                #create signal within signal byte
                                self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),signal.SignalStartBit%8,signal.SignalLength,littleEndian=1)
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
                                self._laidSignals[self._gap+str(self._gapIdx)] = CANSignal(self._gap+str(self._gapIdx),self._unusedBitsHead[byteIdx],startBit%8-signal.SignalLength+1-self._unusedBitsHead[byteIdx])
                                #shift unused bit position
                                self._unusedBitsHead[byteIdx] = startBit%8-signal.SignalLength+1
                                self._gapIdx += 1
                            #create signal within signal byte
                            self._laidSignals[signal.SignalName] = CANSignal(signal.SignalName,signal.SignalStartBit%8,signal.SignalLength,littleEndian=0)
                            self._unusedBitsHead[byteIdx] += signal.SignalLength
                        else:         
                            while signal.SignalStartBit%8 - self._unusedBitsHead[byteIdx] +1 < signal.SignalLength:
                                self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),signal.SignalStartBit%8,signal.SignalStartBit%8+1,littleEndian=0)
                                self._mulByteIdx += 1
                                signal.SignalLength -= signal.SignalStartBit%8-self._unusedBitsHead[byteIdx] + 1
                                #signal.SignalStartBit += 8*(byteIdx+1)-1
                                signal.SignalStartBit = 8*(byteIdx+2)-1
                                if byteIdx < 7:
                                    byteIdx += 1
                            else:                              
                                #create signal within signal byte
                                self._laidSignals[signal.SignalName+str(self._mulByteIdx)] = CANSignal(signal.SignalName+str(self._mulByteIdx),signal.SignalStartBit%8,signal.SignalLength,littleEndian=0)
                                self._mulByteIdx = 0                       
        return self._laidSignals
