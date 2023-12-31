from pychain import pyChain

init = pyChain()

init.Mine(1234,"hello world")
init.Mine(8987,"tachyon")

print(init.chain)
