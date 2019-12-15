class StateError(Exception):
    def __init__(self):
        super(StateError, self).__init__()

class StateMachine:
    def __init__(self):
        self.handlers = {}  # 状态转移函数字典
        self.startState = None  # 初始状态
        self.endStates = []  # 终止状态集合

    # state为状态名,handler为状态转移函数,start表示是否为初始状态,end表示是否为终止状态
    def add_state(self, state, handler, start=0, end=0):
        self.handlers[state] = handler
        if start:
            self.startState = state
        elif end:
            self.endStates.append(state)

    def run(self, text):
        input = text
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")

        # 从Start状态开始进行处理
        while True:
            try:
                (newState, text) = handler(text)# 经过状态转移函数变换到新状态
            except StateError:
                print('输入链('+input+')不能被自动机接受')
                break
            else:
                if newState in self.endStates:  # 如果跳到终止状态,则打印状态并结束循环
                    print('输入链('+input+')被自动机接受')
                    break
                else:  # 否则将转移函数切换为新状态下的转移函数
                    handler = self.handlers[newState]