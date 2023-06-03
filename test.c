#include <stdio.h>

void myFunction(int a) {

  printf("I just got %d executed!",a);
}

int main() 
{
  myFunction(3); // call the function
  return 0;
}