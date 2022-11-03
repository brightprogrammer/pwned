# HITCON LAB4 Solution

This is another buffer overflow challenge. There's a `See_something(addr)` function that can leak values at given addresses. You can use this to leak some useful data! I learned something new here :  
> When you are not calling a function and instead making a direct/indirect jmp to a function that is usally called! like a function from another library then before placing your arguments onto stack, place a valid return address for function to return to!

So your payload will look something like this :
- offset_data
- function address to jump to
- a valid return address
- param1
- param2
- other parameters...

If you're having hard time then try reading about GOT in ELF binaries. `Print_message` is also an interesting function to look at. 
