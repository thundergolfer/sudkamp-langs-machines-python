from transitions import Machine


class Stuff(object):

    def __init__(self, states=None, machine_cls=Machine):

        self.state = None
        self.message = None
        states = ['A', 'B', 'C', 'D', 'E', 'F'] if states is None else states
        self.machine = machine_cls(self, states=states, initial='A', name='Test Machine')
        self.level = 1
        self.machine_cls = machine_cls

    @staticmethod
    def this_passes():
        return True

    @staticmethod
    def this_fails():
        return False

    @staticmethod
    def this_fails_by_default(boolean=False):
        return boolean

    @staticmethod
    def extract_boolean(event_data):
        return event_data.kwargs['boolean']

    def goodbye(self):
        self.message = "So long, suckers!"

    def hello_world(self):
        self.message = "Hello World!"

    def greet(self):
        self.message = "Hi"

    def meet(self):
        self.message = "Nice to meet you"

    def hello_F(self):
        if not hasattr(self, 'message'):
            self.message = ''
        self.message += "Hello F!"

    def increase_level(self):
        self.level += 1

    def decrease_level(self):
        self.level -= 1

    def set_message(self, message="Hello World!"):
        self.message = message

    def extract_message(self, event_data):
        self.message = event_data.kwargs['message']

    def on_enter_E(self, msg=None):
        self.message = "I am E!" if msg is None else msg

    def on_exit_E(self):
        self.exit_message = "E go home..."

    def on_enter_F(self):
        self.message = "I am F!"


class InheritedStuff(Machine):

    def __init__(self, states, initial='A'):

        self.state = None

        Machine.__init__(self, states=states, initial=initial)

    @staticmethod
    def this_passes():
        return True

    @staticmethod
    def this_fails():
        return False