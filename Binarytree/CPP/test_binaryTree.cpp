#include <iostream>

#include "binaryTree.h"

 int main(int argc, char *argv[])
 {
   BinaryTree<int> bst = BinaryTree<int>();

   bst.insert(1);
   bst.insert(1);
   bst.insert(2);
   bst.insert(3);
   bst.insert(5);
   bst.insert(5);
   bst.insert(3);
   int masimo = bst.max();
   std::cout << 
   
   return 0;
 }
