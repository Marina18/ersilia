from ersilia.api.create_api import ErsiliaAPI

mdl = ErsiliaAPI("eos3b5e")
mdl.serve()
input = ["CCCCO", "C", "CC"]
df = mdl.run(input, 100)
#mdl.example("example_filename", True, True, 5, False)
#mdl.delete()
# mdl = ErsiliaAPI("eos3b5e")
# input = ["CCCCO", "CCO", "CCCN"]
# df = mdl.run(input, 100)
# mdl.close()
mdl.info()


