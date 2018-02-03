# binary_analysis
## ELF Relocations
1. Compile without standard `libc`:

`gcc -nostdlib obj1 -c -o obj1.o`

2. Dump generated assembly code:

`objdump -d obj1.o`
