#include <iostream>
#include <sstream>
#include <string>

// % cpp doesn't handle negatives
// like you expect python would lol
int modulo(int a, int b) { return (a % b + b) % b; }

int main(int argc, char *argv[]) {

  int dial_pointer = 50;
  int dial_range = 100;
  int counter = 0;
  std::string line;

  while (std::getline(std::cin, line)) {
    std::istringstream iss(line);

    char c;
    int dist = 0;

    iss >> c >> dist;

    // go backwards if L, forwards if R
    int dir = (c == 'L') ? -1 : 1;

    dial_pointer = modulo(dial_pointer + (dir * dist), dial_range);

    if (dial_pointer == 0) {
      counter++;
    }
  }

  std::cout << counter << std::endl;

  return 0;
}
