#ifndef BINARYNODE_H
#define BINARYNODE_H
#define NULL 0

template <typename T>
class BinaryNode
{
  public:
    BinaryNode (){
      this->duplicates = -1;
      this->left_child = NULL;
      this->right_child = NULL;
      this->data = NULL;
    };

    virtual ~BinaryNode (){};

    BinaryNode<T> *left_child;
    BinaryNode<T> *right_child;

    void insert(T value){
      if (this->data == NULL) {
        this->data = value;
        this->duplicates++;
        this->left_child = new BinaryNode<T>();
        this->right_child = new BinaryNode<T>();

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
          //delete this->right_child;
          //delete this->left_child;
          //delete this->data;
          this->left_child = NULL;
          this->right_child = NULL;
          this->data = NULL;
        }
        this->duplicates--;

      } else if( this->data < value){
        this->right_child->remove(value);

      } else if( this->data > value){
        this->left_child->remove(value);

      }
    }

    BinaryNode<T>* max(){
      if(this->right_child->data == NULL){
        return this;
      }
      return this->right_child->max();
    }

    BinaryNode<T>* min(){
      if(this->left_child->data == NULL){
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
};

#endif /* BINARYNODE_H */
