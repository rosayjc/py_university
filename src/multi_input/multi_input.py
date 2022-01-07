#!/usr/bin/env python
# coding: utf-8

# In[1]:


from ipywidgets import Textarea 
import io 
 
if 'input' in globals(): 
    del input 
 
class custom_input(): 
    def __init__(self): 
        self.__sio = io.StringIO('') 
        self.shell = get_ipython() 
        if self.shell.events.callbacks['pre_run_cell'] != []: 
            self.shell.events.callbacks['pre_run_cell'] = [] 
        self.shell.events.register('pre_run_cell', self.pre_run_cell) 
 
    def __call__(self): 
        return self.__sio.readline().strip() 
 
    def pre_run_cell(self,info): 
        text = self.shell.user_ns.get('text_area', None).value 
        self.__sio = io.StringIO(text) 
 
input = custom_input() 
 
text_area = Textarea() 
display(text_area)

