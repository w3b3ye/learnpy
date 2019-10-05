#!/usr/bin/env python3
#Understanding scopes, local vs enclosing vs global

def enclosing_func():
    m = 13
    def local():
            print(m,'printing from the local function')
    local()

m = 5
print(m, 'printing from the global scope')

enclosing_func()

