#ifndef BINARYNODE_H
#define BINARYNODE_H

#ifndef NULL
#define NULL 0
#endif /* NULL */


#include <iostream>

template <typename T>
class BinaryNode
{
  public:
    BinaryNode (){
      this->duplicates = -1;
      this->left_child = NULL;
      this->right_child = NULL;
      this->Inicialized = false;
    };

    virtual ~BinaryNode (){};

    BinaryNode<T> *left_child;
    BinaryNode<T> *right_child;

    void insert(T& value){

      if (this->Inicialized == false) {
        this->data = value;
        this->duplicates++;
        this->left_child = new BinaryNode<T>();
        this->right_child = new BinaryNode<T>();
        this->Inicialized = true;

      } else {
        if ( this->data > value) {
          this->left_child->insert(value);

        } else if ( this->data < value) {
          this->right_child->insert(value);

        } else if( this->data == value) {
          this->duplicates++;

        }
      }
    }

    void remove(T value){

      if(this->data == value){

        if(this->duplicates == 0){


          if(this->left_child->Inicialized != this->right_child->Inicialized){
            if(this->left_child->Inicialized){
              BinaryNode<T> *aux = this->left_child;
              this->Inicialized = this->left_child->Inicialized;
              this->data = this->left_child->data;
              this->duplicates = this->left_child->duplicates;
              this->right_child = this->left_child->right_child;
              this->left_child = this->left_child->left_child;
              //delete aux->left_child;
              //delete aux->right_child;
              return;
              
            }
            if(this->right_child->Inicialized){
              BinaryNode<T> *aux = this->right_child;
              this->Inicialized = this->right_child->Inicialized;
              this->data = this->right_child->data;
              this->duplicates = this->right_child->duplicates;
              this->right_child = this->right_child->right_child;
              this->left_child = this->right_child->left_child;
              //delete aux->left_child;
              //delete aux->right_child;
              return;
            }
          }

          if(this->left_child->Inicialized && this->right_child->Inicialized && true){
            BinaryNode<T> *aux = this->right_child->min();
            this->Inicialized = true;
            this->duplicates = aux->duplicates;
            this->data = aux->data;

            aux->left_child = NULL;
            aux->right_child = NULL;
            aux->Inicialized = false;
            aux->duplicates = -1;
            return;
          }
          if(this->left_child->Inicialized && this->right_child->Inicialized && false){
            this->left_child = NULL;
            this->right_child = NULL;
            this->Inicialized = false;
            this->duplicates--;
            return;
          }
        }
        this->duplicates--;


      } else if( this->data < value){
        this->right_child->remove(value);

      } else if( this->data > value){
        this->left_child->remove(value);
      }
    }

    BinaryNode<T>* max(){
      if(this->right_child->Inicialized == false){
        return this;
      }
      return this->right_child->max();
    }

    BinaryNode<T>* min(){
      if(this->left_child->Inicialized == false){
        return this;
      }
      return this->left_child->min();
    }

    T getData() {
      return this->data;
    }

  private:
    long long duplicates;
    T data;
    bool Inicialized;
};

#endif /* BINARYNODE_H */
