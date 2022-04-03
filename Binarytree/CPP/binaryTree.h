#ifndef BINARYTREE_H
#define BINARYTREE_H
#include "binaryNode.h"

template <typename T>
class BinaryTree
{
  private:
    BinaryNode<T>* root;
  public:
    BinaryTree(){
      root = new BinaryNode<T>();
    }
    virtual ~BinaryTree(){};

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
