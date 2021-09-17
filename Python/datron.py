from modules import toolgetmod

tlist = toolgetmod.fileTlistFUSION("fusion/test.txt")
result = []
for ele in tlist:
    result.append(toolgetmod.clearFUSION(ele))

print(result)
