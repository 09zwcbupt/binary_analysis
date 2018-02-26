# binary_analysis
## ELF Relocations
1. Compile without standard `libc`:

`gcc -nostdlib obj1 -c -o obj1.o`

2. Dump generated assembly code:

`objdump -d obj1.o`

3. Compile obj2 and then link both file

`gcc -nostdlib obj2.c -c -o obj2.o`

`gcc -nostdlib obj1.o obj2.o -o relocation`

## ptrace
1. compile tracer.c and tracer_test.c:
`gcc tracer.c -o tracer`
`gcc tracer_test.c -o test`
`./tracer test main`
