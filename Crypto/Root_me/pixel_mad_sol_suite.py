result=""
lines=open("lines.txt","r").read()
lists = lines.split(".")
for i in range(len(lists)):
  lists[i] = lists[i].split("+")
  for j in range(len(lists[i])):
    result+= lists[i][j][0] * int(lists[i][j][2:])
  result+="\n"
result = result.replace("0"," ")
result = result.replace("1","*")
print result

