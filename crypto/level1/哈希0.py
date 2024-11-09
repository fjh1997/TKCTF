from hashlib import sha256
unknown="XXXX"
flag="tkctf{TH1S_1s_"+unknown+"}"
print(sha256(flag.encode()).hexdigest()=='5fefaebc4ba0b9fb3b8baeee667d30636ffe55168617bc2c78baeb80ad896dd2')