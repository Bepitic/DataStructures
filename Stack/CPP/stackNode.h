#ifndef STACKNODE_H
#define STACKNODE_H

#ifndef NULL
#define NULL 0
#endif /* NULL */

#include <iostream>

template <typename T>
class StackNode
{
  public:
    StackNode<T> *next;
    StackNode<T> *previous;

    StackNode (){
      this->Inicialized = false;
      this->previous = NULL;
    };

    StackNode (T data){
      this->Inicialized = true;
      this->data = data;
      this->previous = NULL;
    };

    virtual ~StackNode (){};

    StackNode<T>* push(T& value){
      StackNode<T> *aux = new StackNode<T>(value);
      this->previous = aux;
      aux->next = this;
      return aux;
    }

    StackNode<T>* pop(){
      if(this->Inicialized or this->next == NULL){

        StackNode<T>* aux = this->previous;
        this->previous = NULL;
        this->next = NULL;
        //this->data = NULL;
        this->Inicialized = false;

        return aux;
      }
      return this;
    }

    void remove(T value){
      StackNode<T> *aux = this;
      while(aux != NULL){
        if(data == value){
        
          aux->previous->next = aux->next;
          aux->next->previous = aux->previous;

          aux->previous = NULL;
          aux->next = NULL;
          //aux->data = NULL;
          aux->Inicialized = false;


          return;
        }else{
          aux = this->next;
        }
      }

    }


    T getData() {
      return this->data;
    }

  private:
    T data;
    bool Inicialized;
};

#endif /* STACKNODE_H */
