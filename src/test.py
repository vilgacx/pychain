from pychain import pyChain

init = pyChain()

init.Mine(1234,"hello world")
init.Mine(8987,"vilgacx")

print(init.chain)
