#include <iostream>

#include "binaryTree.h"

int main(int argc, char *argv[])
{

  int len, len2;
  std::cin >> len; // elements to insert
  std::cin >> len2; // size of elements to remove
  BinaryTree<int> bst = BinaryTree<int>();

  for (int i = 0; i < len; ++i) {
    int aux;
    std::cin >> aux;
    bst.insert(aux);
  }

  for (int i = 0; i < len2; ++i) {
    int aux;
    std::cin >> aux;
    bst.remove(aux);
  }

  std::cout << bst.min() << std::endl;
  std::cout << bst.max() << std::endl;

  return 0;
}
