# HITCON LAB5 Solution

This was a completely different challenge because this is a statically linked binary. I had almost any rop gadget I required! This was heaven in one way but hell in other. You don't have system, execve or anything. But the good part is it's not that difficult! You just have to have some good experience with ROP and ShellCode(s).  

There is no `execve` or `system` call but there's one very interesting function present in there. Try using radare's internal grep to search for the "stack" in symbols.  
> `is~stack`  
Or you can also use readelf to do this.  
> `readelf -a simplerop | grep stack`
You'll see some interesting functions that you can jump to in your rop!

Even though there's no `execve` or `system` present, you can still do an `execve` syscall!

I learned some new features about radare. You can find rop sequences in radare too. Take a look at the reference link to know more. I also learned about new linux thing

### References
[Defeating baby_rop2 using radare](https://radareorg.github.io/blog/posts/defeating-baby_rop-with-radare2/)
