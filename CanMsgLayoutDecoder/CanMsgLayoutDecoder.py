'''
Created on 13th, March, 2018

@author: Alvin Ye
'''


class SignalBitFieldSyntaxGenerator:
    '''
    this class acts to slice a message into-byte long and create signal field inside every byte
    '''
    def __init__(self, decoded_msg):
        self.decoded_msg = decoded_msg
        self._sliced_signals_by_byte = [[]]
        self._syntax_type = 'uint8'
        self._syntax_struct = 'struct'
        self._syntax_def = 'typedef'
        self._syntax_delimiter = ":"
        self._syntax_ending = ';\n'
        self._syntax_define = '#define'
        self._syntax_data_type = ''
        self._total_len = 0
        self._byte_idx = 0

        for byte_slice in self._slice_msg_by_byte():
            byte_slice.reverse()
        
    def _slice_msg_by_byte(self):
        for signal in self.decoded_msg.msg_signals.values():
            self._total_len += signal.signal_len
            if self._total_len <= (self._byte_idx + 1) * 8:
                self._sliced_signals_by_byte[self._byte_idx].append(signal)
            else:
                self._sliced_signals_by_byte.append([])
                self._byte_idx += 1
                self._sliced_signals_by_byte[self._byte_idx].append(signal)
        return self._sliced_signals_by_byte
    
    def bit_field_generator(self, file):
        for byte_slice in self._sliced_signals_by_byte:
            for signal in byte_slice:
                file.write(self.bit_field_syntax(signal.signal_name, signal.signal_len))
                
    def bit_field_syntax(self, signal_name, signal_len):
        return ('\t' + self._syntax_type + ' ' + signal_name + self._syntax_delimiter + str(
            signal_len) + self._syntax_ending)
    
    def signal_union_generator(self, union_msg, file):
        for byte_slice in self._sliced_signals_by_byte:
            for signal in byte_slice:
                if not signal.signal_name.startswith('unused'):
                    file.write(self.union_signal_macro_syntax(signal.signal_name, union_msg.msg_name,
                                                              signal.signal_msg_carrier.msg_name))
                    
    def signal_struct_generator(self, file):
        for byte_slice in self._sliced_signals_by_byte:
            for signal in byte_slice:
                if not signal.signal_name.startswith('unused'):
                    file.write(self.struct_signal_macro_syntax(signal.signal_name, signal.signal_msg_carrier.msg_name))

    def union_signal_macro_syntax(self, signal_name, union_msg_name, struct_name):
        return '{0} b_{1}_b\t\t({2}.{3}.{4})\n'.format(self._syntax_define, signal_name, union_msg_name,
                                                       struct_name, signal_name)
      
    def struct_signal_macro_syntax(self, signal_name, struct_msg_name):
        return '{0} b_{1}_b\t\t({2}.{3})\n'.format(self._syntax_define, signal_name, struct_msg_name, signal_name)

    def signal_access_macro_syntax(self, over_byte_bound_virtual_signals, file):
        if over_byte_bound_virtual_signals:
            for virtual_signals in over_byte_bound_virtual_signals:
                s = ''
                bit_shift = 0
                if virtual_signals[0].signal_little_endian:
                    # this is Intel
                    if virtual_signals[0].signal_len <= 8:
                        self._syntax_data_type = 'uint8'
                    elif virtual_signals[0].signal_len <= 16:
                        self._syntax_data_type = 'uint16'
                    elif virtual_signals[0].signal_len <= 32:
                        self._syntax_data_type = 'uint32'
                    elif virtual_signals[0].signal_len <= 64:
                        print('{0} - signal length is greater than CUP width, single access not supported'.format(virtual_signals[0].signal_name))
                        continue
                    for signal in virtual_signals[1:]:
                        s += '((({0}){1})<<{2}) | '.format(self._syntax_data_type, signal.signal_name, bit_shift)
                        bit_shift += signal.signal_len
                    else:
                        s = s.strip('| ')
                        s = '(' + s + ')\n'
                    s = '#define b_{0}_b\t'.format(virtual_signals[0].signal_name) + s
                else:
                    virtual_signals.reverse()
                    if virtual_signals[-1].signal_len <= 8:
                        self._syntax_data_type = 'uint8'
                    elif virtual_signals[0].signal_len <= 16:
                        self._syntax_data_type = 'uint16'
                    elif virtual_signals[0].sinal_len <= 32:
                        self._syntax_data_type = 'uint32'
                    elif virtual_signals[0].signal_len <= 64:
                        print('{0} - signal length is greater than CUP width, single access not supported'.format(virtual_signals[0].signal_name))
                        continue
                    for signal in virtual_signals[:-1]:
                        s += '((({0}){1})<<{2}) | '.format(self._syntax_data_type, signal.signal_name, bit_shift)
                        bit_shift += signal.signal_len
                    else:
                        s = s.strip('| ')
                        s = '(' + s + ')\n'
                    s = '#define b_{0}_b\t'.format(virtual_signals[0].signal_name) + s
                file.write(s)
