from pwn import remote, xor
from Crypto.Util.Padding import unpad

# ncat -v --ssl byte-by-byte.challs.shellmates.club 443


def connect():
    return remote('byte-by-byte.challs.shellmates.club', 443, ssl=True)


# retrieve first 16 bytes of the flag
conn = connect()
conn.recvuntil(b'flag = ')
flag = conn.recvline().decode()[:-2]
num_blocks = len(flag)//32
print(flag)
ct = flag[:32]
print(num_blocks)
conn.recvuntil(b'plaintext: ')
# conn.interactive()
conn.sendline(b'61616161616161616161616161616161616161616161616161616161616161610A')
conn.recvuntil(b'ciphertext: ')
CBC_ct = conn.recvline().decode()[:-2]
print(CBC_ct)
conn.recvuntil(b'ciphertext: ')
conn.sendline(b'ct')
