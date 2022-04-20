#ifndef STACK_H
#define STACK_H
#include "stackNode.h"



template <typename T>
class Stack
{
  private:
    StackNode<T>* root;
  public:
    Stack(){
      root = new StackNode<T>();
    }
    virtual ~Stack(){
    }


    void clear(){
      this->root->clear();
    }

    bool contains(T value){
      return this->root->contains(value);
    }

    void push(T value){
      this->root = this->root->push(value);
    }

    T pop(){
      T aux = this->root->getData();
      this->root = this->root->pop();
      return aux;
    }

    T peek(){
      T aux = this->root->getData();
      return aux;
    }

    void remove(T value){
      this->root->remove(value);
    }


};

#endif /* STACK_H */
