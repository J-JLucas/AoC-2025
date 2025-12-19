#include <iostream>

// % cpp doesn't handle negatives
// like you expect python would lol
int modulo(int a, int b) { return (a % b + b) % b; }

int main(int argc, char *argv[]) {

  int test = (0 - 1) % 100;
  std::cout << test << std::endl;

  int test2 = modulo((0 - 1), 100);
  std::cout << test2 << std::endl;

  return 0;
}
