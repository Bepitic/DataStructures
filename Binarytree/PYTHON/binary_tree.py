'''adfa adf adf '''


class Bst():
    ''' The Vehicle object contains lots of vehicles '''

    def __init__(self, item=None, left=None, right=None, parent=None):
        ''' The Vehicle object contains lots of vehicles '''
        self.item = item
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, item):
        ''' The Vehicle object contains lots of vehicles '''
        if not self.item:
            self.item = item
        else:
            if self.item < item:
                if not self.left:
                    self.left = Bst(item=item, parent=self)
                else:
                    self.left.insert(item)

                if not self.right:
                    self.right = Bst(item=item, parent=self)
                else:
                    self.right.insert(item)

    def del_no_sons(self):
        ''' The Vehicle object contains lots of vehicles '''
        if self.parent.left == self:
            self.parent.left = None
        elif self.parent.right == self:
            self.parent.right = None
        else:
            self.item = None

    def del_the_minimun(self):
        ''' Delete the minimun in the tree and return their value'''
        if self.left:
            return self.left.del_the_minimun()

        if self.parent.left == self:
            self.parent.left = None
        else:  # self.parent.right == self:
            self.parent.right = None
        return self.item

    def del_two_sons(self):
        ''' The Vehicle object contains lots of vehicles '''
        self.item = self.right.del_the_minimun()

    def del_r_son(self):
        ''' The Vehicle object contains lots of vehicles '''
        if self.parent.left == self:
            self.parent.left = self.right
        elif self.parent.right == self:
            self.parent.right = self.right
        else:
            self.item = None

    def del_l_son(self):
        ''' The Vehicle object contains lots of vehicles '''
        if self.parent.left == self:
            self.parent.left = self.left
        elif self.parent.right == self:
            self.parent.right = self.left
        else:
            self.item = None

    def delete(self, item):
        ''' The Vehicle object contains lots of vehicles '''

        if self.item == item and (self.left and self.right):
            # estamos en el nodo y tenemos dos hijos.
            self.del_two_sons()

        elif self.item == item and self.right:
            # estamos en el nodo y tenemos el right hijo.
            self.del_r_son()

        elif self.item == item and self.left:
            # estamos en el nodo y tenemos el left hijo.
            self.del_l_son()

        elif self.item == item and (self.left and self.right):
            # estamos en el nodo y no tenemos hijos.
            self.del_no_sons()

        else:  # No estamos en el nodo.
            if self.item < item:
                if not self.left:
                    pass
                    # return  # sys.Error()
                else:
                    self.left.delete(item)
            else:
                if not self.right:
                    pass
                    # return  # sys.Error()
                else:
                    self.right.delete(item)
