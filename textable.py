#!/usr/bin/env python

import sys

mode = None
options = []

for opt in sys.argv:
    if opt == '-skip':
        if mode != None:
            print('bad argument')
            quit()
        options.append(('skip',))
    elif opt == '-si':
        if mode == None:
            mode = 'si'
        else:
            print('bad argument')
            quit()
    elif opt == '-text':
        if mode != None:
            print('bad argument')
            quit()
        options.append(('text',))
    else:
        if mode == 'si':
            options.append(('si', opt))
            mode = None
        else:
            infile = open(opt)

for ln in infile:
    ln = ln.lstrip().rstrip()
    tok = ln.split(',')

    texln = ''
    for (t, op) in zip(tok, options):
        if op[0] == 'text':
            texln = texln + t
        elif op[0] == 'si':
            texln = texln + '\\SI{' + t + '}{' + op[1] + '}'
        elif op[0] == 'skip':
            continue
        else:
            print('bad option: ' + op[0])

        texln = texln + ' & '
    
    texln = texln[:texln.rfind('& ')] + '\\\\' 
    
    print(texln)

