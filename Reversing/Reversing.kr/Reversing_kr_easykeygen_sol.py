s = "5B134977135E7D13"
count = 0 
for j in range(0,3) :
	print "-"*10, "count : 0x%02x" % count
	for i in range(97,122) : 
		print chr(i), hex(ord(chr(i))^(int(0x10)+count))
	for k in range(65,90) : 
		print chr(k), hex(ord(chr(k))^(int(0x10)+count))
	count = count + 0x10
	if count >= 0x30 : count = 0
print hex(ord('3')^int(0x20))