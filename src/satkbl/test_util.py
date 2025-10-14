import util as u
import ctx
import req

class TestObj:
    def __init__(s):
        s.a = 123
        s.b = 'hello'


def test0():
    o = TestObj()
    '''
    o = {
        'a': 234,
        'b': 'world'
    }
    '''
    u.p(u.pp(u.otom(o)))
    u.p(u.b64e('hello world'))
    u.exampleCpuPool()

def test1():
    c = ctx.generic('http://example.com')
    r = req.geth(c, '')
    u.lrd(r)

#test0()
test1()
