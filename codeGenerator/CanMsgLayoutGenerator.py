'''
Created on 13th, March, 2018

@author: Alvin Ye
'''


class SignalBitFieldGenerator:


    '''
    this class acts to slice a message into-byte long and create signal field inside every byte
    '''
    def __init__(self, laidSignals):
        self._laidSignals = laidSignals
        self._byte_slicedSignals= [[]]
        self._syntax_type = 'uint8'
        self._syntax_struct = 'struct'
        self._syntax_def    = 'typedef'
        self._syntax_delimiter = ":"
        self._syntax_ending = ';\n'
        self._totalLen = 0
        self._byteIdx = 0
        self._syntax_define = '#define'
        
        for byte_slice in self.byte_slicer():
            byte_slice.reverse()
        
    def byte_slicer(self):
        for signal in self._laidSignals.values():
            self._totalLen += signal.signal_len
            if self._totalLen <= (self._byteIdx+1)*8:
                self._byte_slicedSignals[self._byteIdx].append(signal)
            else:
                self._byte_slicedSignals.append([])
                self._byteIdx +=1
                self._byte_slicedSignals[self._byteIdx].append(signal)
        return self._byte_slicedSignals
    
    def bit_field_generator(self, file):
        for byte_slice in self._byte_slicedSignals:
            for signal in byte_slice:
                file.write(self.bit_field_struct_syntax(signal.signal_name, signal.signal_len))
                
    def bit_field_struct_syntax(self, signal_name, signalLenth):
        return ('\t'+self._syntax_type+' '+signal_name+self._syntax_delimiter+str(signalLenth)+self._syntax_ending)
    
    def signal_access_union_generator(self, unionMsg, file):
        for byte_slice in self._byte_slicedSignals:
            for signal in byte_slice:
                if not signal.signal_name.startswith('unused'):
                    file.write(self.signal_access_macro_syntax_union(signal.signal_name, unionMsg.msg_name, signal.signal_msg_carrier.msg_name))
                    
    def signal_access_struct_generator(self, file):
        for byte_slice in self._byte_slicedSignals:
            for signal in byte_slice:
                if not signal.signal_name.startswith('unused'):
                    file.write(self.signal_access_macro_syntax_struct(signal.signal_name, signal.signal_msg_carrier.msg_name))
                
    def signal_access_macro_syntax_union(self, signal_name, unionmsg_name, structmsg_name):
        return '{0} b_{1}_b\t\t({2}.{3}.{4})\n'.format(self._syntax_define, signal_name, unionmsg_name, structmsg_name, signal_name)
      
    def signal_access_macro_syntax_struct(self, signal_name, structmsg_name):
        return '{0} b_{1}_b\t\t({2}.{3})\n'.format(self._syntax_define, signal_name, structmsg_name, signal_name)
