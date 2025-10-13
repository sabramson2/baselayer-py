import util as u


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


test0()