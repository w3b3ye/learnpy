#!/usr/bin/env python3
#Understanding scopes, local vs global

def local():
    m = 7
    print(m)

m = 5
print(m)

#Call the function
local()

exit()

