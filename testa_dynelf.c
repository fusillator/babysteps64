#include <stdio.h>
main(){
  int x;
  printf("Info leak service!\n");
  fflush(stdout);
  while(!feof(stdin)) {
    scanf("%x",&x);
    write(1,x,4);
    fflush(stdout);
  }
}
