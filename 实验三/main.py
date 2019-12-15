from statemachine import StateMachine, StateError
#状态转换函数,
def S_transition(text):
    #提取字符串的第一个字符，返回当前状态和余下字符
    if(len(text) < 1):
        raise StateError
    else:
        input = text[0]
        if input == 'a':
            newState = 'B'
        else:
            raise StateError
    return (newState, text[1:])

def B_transition(text):
    if (len(text) < 1):
        raise StateError
    else:
        input = text[0]
        if input == 'a':
            if len(text) == 1:
                newState = 'T'
            else:
                newState = 'B'
        elif input == 'b':
            newState = 'S'
        else:
            raise StateError
    return (newState, text[1:])

def T_transition(text):
    return ('T', text)



if __name__ == '__main__':
    FM = StateMachine()
    FM.add_state('S', S_transition, start=True)
    FM.add_state('B', B_transition)
    FM.add_state('T', T_transition, end=True)

    #测试输入链
    FM.run('aababaaababaaa')
    FM.run('ababaababaaba')

