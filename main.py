import logging

from utils.Interpreter import Interpreter

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s::%(filename)s - %(message)s")

if __name__ == '__main__':
    interpreter = Interpreter("test.json")
    interpreter.run()
