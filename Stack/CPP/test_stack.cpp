#include <iostream>
#include "stack.h"


int main(int argc, char *argv[])
{

  int len, len2, len3, len4;
  std::cin >> len; // elements to insert
  std::cin >> len2; // size of elements to remove
  std::cin >> len3; // size of elements to pop
  std::cin >> len4; // size of elements to pop
  Stack<int> stack = Stack<int>();

  for (int i = 0; i < len; ++i) {
    int aux;
    std::cin >> aux;
    stack.push(aux);
  }

  for (int i = 0; i < len2; ++i) {
    int aux;
    std::cin >> aux;
    stack.remove(aux);
  }

  for (int i = 0; i < len3; ++i) {
    int aux;
    aux = stack.pop();
    std::cout << aux << std::endl;
  }

  for (int i = 0; i < len4; ++i) {
    int aux;
    aux = stack.peek();
    std::cout << aux << std::endl;
  }

  //stack.show things

  return 0;
}
