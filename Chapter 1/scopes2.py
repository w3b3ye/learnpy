#!/usr/bin/env python3
#Understanding scopes, local vs global

def local():
    
    print(m, 'print from local function')

m = 5
print(m, 'print from global scope')

#Call the function
local()

exit()
