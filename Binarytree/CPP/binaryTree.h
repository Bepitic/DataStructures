#ifndef BINARYTREE_H
#define BINARYTREE_H

#define NULL 0

#include "binaryNode.h"

template <typename T>
class BinaryTree
{
  private:
    BinaryNode<T>* root;
  public:
    BinaryTree();
    virtual ~BinaryTree();

    T max(){
      return this->max()->getData();
    }
    T min(){
      return this->min()->getData();
    }

    void insert(T value){
      this->root->insert(value);
    }

    void remove(T value){
      this->root->remove(value);
    }

};

#endif /* BINARYTREE_H */
