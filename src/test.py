from pychain import pyChain

init = pyChain()

# mining
init.Mine(1234,"hello world")
init.Mine(8987,"tachyon")

print(init.chain)

# validate
print(init.Validate())

# tampering
init.chain[1]["data"] = "py"
print(init.Validate())
