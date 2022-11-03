#!/usr/bin/env python3

from pwn import *

'''
@brief Basic pwn script init
'''
def pwn_basic_init():
    context.terminal = ["tilix", "-a", "session-add-right", "-e"]
    context.log_level = 'debug'
    context.delete_corefiles = True

'''
@brief Find EIP offset automatically in case of buffer overflows.

@param exe_path
@param after String/Character afterwhich pattern must be sent.
'''
def get_eip_offset(exe_path, after, bufsz=512):
    io = process(exe_path)
    pattern = cyclic(bufsz)
    io.sendlineafter(after, pattern)
    io.wait()
    core = io.corefile
    eip_offset = cyclic_find(core.eip)
    debug('eip offset = 0x%x', eip_offset)
    return eip_offset

'''
@brief Find RIP offset automatically in case of buffer overflows.

@param exe_path
@param after String/Character afterwhich pattern must be sent.
'''
# -- Determine rip offset --
def get_rip_offset(elf_path, after, bufsz=512):
    # run binary and send pattern so that we can determine
    # rip offset
    io = process(elf_path)
    cyclic_pattern = cyclic_gen(string.ascii_uppercase, n=4)
    pattern = cyclic_pattern.get(bufsz)
    io.sendlineafter(after, pattern)
    io.wait() # give it some time to get corefile
    # load corefile and read pattern from stack to get offset
    core = io.corefile
    stack = core.rsp
    rip_offset = cyclic_pattern.find(core.read(stack, 4))[0]
    debug('rip offset = %#x', rip_offset)
    return rip_offset
