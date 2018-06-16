# -*- coding: utf-8 -*-

"""
Implement the 'INotifyPropertyChanged' interface.

* https://anis774.net/blog/tag/ironpython
"""

from System.ComponentModel import INotifyPropertyChanged
from System.ComponentModel import PropertyChangedEventArgs

class BindableBase(INotifyPropertyChanged):
    
    def add_PropertyChanged(self, handler):
        if not hasattr(self, "_propertyChangedHandlers"):
            self._propertyChangedHandlers = [handler]
        else:
            self._propertyChangedHandlers.append(handler)
 
    def remove_PropertyChanged(self, handler):
        if not hasattr(self, "_propertyChangedHandlers"):
            self._propertyChangedHandlers = []
        else:
            try:
                self._propertyChangedHandlers.remove(handler)
            except ValueError:
                pass
 
    def OnPropertyChanged(self, propertyName):
        if not hasattr(self, "_propertyChangedHandlers"):
            self._propertyChangedHandlers = []
        else:
            for handler in self._propertyChangedHandlers:
                handler(self, PropertyChangedEventArgs(propertyName))   
 