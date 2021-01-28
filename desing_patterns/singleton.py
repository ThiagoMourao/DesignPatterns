class AppSettings(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        '''chama todas as vezes que pedir instanciamento''' 
        self.tema = 'O tema escuro'
        self.font = '18px'


'''Pode ser usado para decorado em quantas classes quiser, implementação já pronta'''
def singleton(the_class):
    instances = {}

    def get_class(*args, **kwargs):
        if the_class not in instances:
            instances[the_class] = the_class(*args, **kwargs)
        return instances[the_class]
    
    return get_class

'''O decorador resolve o problema do __init__ pois é executado antes da instanciação da classe em si, no caso AppSettings2'''
@singleton
class AppSettings2(object):
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class AppSettings3(metaclass=Singleton):
    def __init__(self):
        self.tema = 'O tema escuro'
        self.font = '18px'
