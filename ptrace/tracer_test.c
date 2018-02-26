#include<stdio.h>
#include<unistd.h>

void test() {
    printf( "Hello world\n" );
}

int main() {
    int i = 0;
    for( i; i < 20; i++ ) {
       sleep( 1 );
       test();
    }
    return 0;
}
