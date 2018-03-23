# -*- coding: utf-8 -*- 
'''
Created on 9th Mar, 2018

@author: Alvin Ye

this is a light-weight dbc abstraction of minimal core CAN elements
'''

class CanNetwork(object):
    '''
    classdocs
    '''
    def __init__(self,baudrate = None,version = None,nodes = None):
        '''
        Constructor
        '''
        self._baudrate = baudrate
        self._version = version
        self._nodes   = {}
        
    @property
    def Version(self):
        return self._version
    @Version.setter
    def Version(self,version):
        self._version = version
    @property
    def Nodes(self):
        return self._nodes
    
    def appendNodes(self,nodeName,nodeObject):
        self._nodes[nodeName] = nodeObject
        
class CanNode(object):
    '''
    classsdocs
    '''
    def __init__(self,nodeName,nodeId=None,txMsgs = None,rxMsgs = None):
        self._nodeId = nodeId
        self._nodeName = nodeName
        self._txMsgs = {}
        self._rxMsgs = {}
        
    @property
    def NodeId(self):
        return self._nodeId
    
    @property
    def NodeName(self):
        return self._nodeName
    
    @property
    def NodeTxMsgs(self):
        return self._txMsgs
    
    def appendTxMsg(self,txMsgName,txMsgObject):
        self._txMsgs[txMsgName] = txMsgObject
        
    @property
    def NodeRxmsgs(self):
        return self._rxMsgs
        
    def appendRxMsg(self,rxMsgName,rxMsgObject):
        self._rxMsgs[rxMsgName] = rxMsgObject
        
class CanMsg(object):
    '''
    classdocs
    '''
    def __init__(self,msgId,msgName,msgLen,msgType = None,msgSender= None, msgReceivers = None,msgSendType = None,signals = None):
        '''
        Constructor
        '''
        self._msgId = msgId
        self._msgName = msgName
        self._msgLen   = msgLen
        self._msgType  = msgType
        self._msgSender = msgSender
        self._msgReceivers = msgReceivers
        self._msgSendType = msgSendType
        self._signals = {}
                    
    @property
    def MsgId(self):
        return self._msgId
    
    @property
    def MsgName(self):
        return self._msgName
    @MsgName.setter
    def MsgName(self,msgName):
        self._msgName = msgName
    @property
    def MsgLen(self):
        return self._msgLen
    
    @property
    def MsgType(self):
        return self._msgType
    
    @property
    def MsgSender(self):
        return self._msgSender
    @MsgSender.setter
    def MsgSender(self,nodeObject):
        self._msgSender = nodeObject
    
    @property
    def MsgReceivers(self):
        return self._msgReceivers
    
    def appendMsgRecevier(self,nodeName,nodeObject):
        self._msgReceivers[nodeName] = nodeObject
        
    @property
    def MsgSignals(self):
        return self._signals
    
    def appendSignal(self,signalName,signalObject):
        self._signals[signalName] = signalObject
        
class CANSignal(object):
    '''
    classdocs
    '''
    def __init__(self, name, startBit, length, littleEndian=1, signed=False, factor=1.0, offset=0.0, valueMin=0.0,
                 valueMax=0.0, unit="", Multiplexer=None, multiplexerId=None,msgCarrier = None):
        self._name = name
        self._startBit = startBit
        self._length = length
        self._littleEndian = littleEndian
        self._signed = signed
        self._factor = factor
        self._offset = offset
        self._valueMin = valueMin
        self._valueMax = valueMax
        self._unit = unit
        self._Multiplexer = Multiplexer
        self._multiplexerId = multiplexerId
        self._msgCarrier = msgCarrier
        
    @property
    def SignalName(self):
        return self._name
    
    @property
    def SignalStartBit(self):
        return self._startBit
    
    @SignalStartBit.setter
    def SignalStartBit(self,startBit):
        self._startBit = startBit
        
    @property
    def SignalLength(self):
        return self._length
    
    @SignalLength.setter
    def SignalLength(self,length):
        self._length = length
        
    @property
    def SignalLittleEndian(self):
        return self._littleEndian
    
    @property
    def SignalSigned(self):
        return self._signed
    
    @property
    def SignalFactor(self):
        return self._factor
    
    @property
    def SignalOffset(self):
        return self._offset
    
    @property
    def SignalMinValue(self):
        return self._valueMin
    
    @property
    def SignalMaxValue(self):
        return self._valueMax
    
    @property
    def SignalUnit(self):
        return self._unit
    
    @property
    def SignalMultiplexer(self):
        return self._Multiplexer
    
    @SignalMultiplexer.setter
    def SignalMultiplexer(self,multiplexer):
        self._Multiplexer = multiplexer    
        
    @property
    def SignalMultiplexerId(self):
        return self._multiplexerId
    
    @SignalMultiplexerId.setter
    def SignalMultiplexerId(self,multiplexerId):
        self._multiplexerId = multiplexerId
        
    @property
    def SignalMsgCarrier(self):
        return self._msgCarrier
    
    @SignalMsgCarrier.setter
    def SignalMsgCarrier(self,msgCarrier):
        self._msgCarrier = msgCarrier
