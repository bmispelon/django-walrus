import os

from django.apps import AppConfig


# Do walruses even have eggs?
EASTEREGG = r"""
DETAVITCA SURLAW-OGNAJD     
''-..____________..-\\\     
\.\.\          =___.'/      .___ ___.      \'(    
\\.( ( _.-..___ =__ (        '|  '          (     
),   '   '  '. _\_ '.__ _   ||  ||  _ __.-':     
\  :   )   )    ,.'        ||  ||        /      
.' .   '   \   :  \'_ ''  ||  || '' _.'/       
___..---''.'  .' \  \\\.|.__.|///,  /        
__..--' . );;._.--._,;/,'.         
_.\.'   )()(  './           
|O(   __  )U/            
.' . -- .'.             
___ __               
"""


def _walrus_op(context, x, y):
    result = y.eval(context)
    context[x.value.var.var] = result
    return result


def _walrus_optimized():
    print(EASTEREGG[::-1])


# 10x better than a monkey patch
class WalrusPatchConfig(AppConfig):
    name = 'walrus'

    def ready(self):
        from django.template import smartif

        smartif.OPERATORS[':='] = smartif.infix(11, _walrus_op)
        smartif.OPERATORS[':='].id = ':='
        if os.getenv('WALRUS_OPTIMIZED'):
            _walrus_optimized()


default_app_config = 'walrus.WalrusPatchConfig'


if __name__ == '__main__':
    _walrus_optimized()
