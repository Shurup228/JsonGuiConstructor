from utils.Interpreter import Interpreter

if __name__ == '__main__':
    interpreter = Interpreter("test.json")
    tree = interpreter.get_tree()
    interpreter.run()
