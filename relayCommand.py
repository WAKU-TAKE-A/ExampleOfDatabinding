# -*- coding: utf-8 -*-

"""
Implement the 'ICommand' interface.

* http://mark-dot-net.blogspot.com/2010/10/wpf-and-mvvm-in-ironpython.html
"""

from System.Windows.Input import ICommand

class RelayCommand(ICommand):
    def __init__(self, execute):
        self.execute = execute
    
    def Execute(self, parameter):
        self.execute()
        
    def add_CanExecuteChanged(self, handler):
        pass
    
    def remove_CanExecuteChanged(self, handler):
        pass

    def CanExecute(self, parameter):
        return True
