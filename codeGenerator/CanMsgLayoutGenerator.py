'''
Created on 13th,March,2018

@author: Alvin Ye
'''
class c_signalBitField_Genertor():
    '''
    this class acts to slice a message into-byte long and create signal field inside every byte
    '''
    def __init__(self,laidSignals):
        self._laidSignals = laidSignals
        self._byteSlicedSignals= [[]]
        self._syntax_type = 'uint8'
        self._syntax_struct = 'struct'
        self._syntax_def    = 'typedef'
        self._syntax_delimiter = ":"
        self._syntax_ending = ';\n'
        self._totalLen = 0
        self._byteIdx = 0
        self._syntax_define = '#define'
        
        for byteslice in self.byteSlicer():
            byteslice.reverse()
        
    def byteSlicer(self):
        for signal in self._laidSignals.values():
            self._totalLen += signal.SignalLength
            if self._totalLen <= (self._byteIdx+1)*8:
                self._byteSlicedSignals[self._byteIdx].append(signal)
            else:
                self._byteSlicedSignals.append([])
                self._byteIdx +=1
                self._byteSlicedSignals[self._byteIdx].append(signal)
        return self._byteSlicedSignals
    
    def bitField_Genertor(self,file):
        for byteslice in self._byteSlicedSignals:
            for signal in byteslice:
                file.write(self.c_syntax_bitField_structor(signal.SignalName, signal.SignalLength))
                
    def c_syntax_bitField_structor(self,signalName,signalLenth):
        return ('\t'+self._syntax_type+' '+signalName+self._syntax_delimiter+str(signalLenth)+self._syntax_ending)      
    
    def signalAccessUnion_Genertor(self,unionMsg,file):   
        for byteslice in self._byteSlicedSignals:
            for signal in byteslice:
                if not signal.SignalName.startswith('unused'):
                    file.write(self.signalAccessMacroSyntaxUnion(signal.SignalName,unionMsg.MsgName, signal.SignalMsgCarrier.MsgName))    
                    
    def signalAccessStruct_Genertor(self,file):   
        for byteslice in self._byteSlicedSignals:
            for signal in byteslice:
                if not signal.SignalName.startswith('unused'):
                    file.write(self.signalAccessMacroSyntaxStruct(signal.SignalName, signal.SignalMsgCarrier.MsgName))  
                
    def signalAccessMacroSyntaxUnion(self,signalName,unionMsgName,structMsgName):
        return ('{0} b_{1}_b\t\t({2}.{3}.{4})\n'.format(self._syntax_define,signalName,unionMsgName,structMsgName,signalName))   
      
    def signalAccessMacroSyntaxStruct(self,signalName,structMsgName):
        return ('{0} b_{1}_b\t\t({2}.{3})\n'.format(self._syntax_define,signalName,structMsgName,signalName))   
