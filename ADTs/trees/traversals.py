# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class BinarySearchTree(object):
  def __init__(self):
    self.root = None
  
  def getRoot(self):
    return self.root

  def insert(self, val):
    if self.root is None:
      self.root = TreeNode(val)
    else:
      self.__insert(val, self.root)
  
  def __insert(self, val, node):
    # Value is placed to left if < root
    if val < node.val:
      if node.left:
        self.__insert(val, node.left)
      else:
        node.left = TreeNode(val)
    # Value is placed to right if >= root
    else:
      if node.right:
        self.__insert(val, node.right)
      else:
        node.right = TreeNode(val)

  def printTree(self):
    if self.root:
      self.__printTree(self.root)

  def __printTree(self, node):
    if node:
      self.__printTree(node.left)
      print(str(node.val) + ' ')
      self.__printTree(node.right)

# class Traversals(object):
#   def preorderTraversal(self, root):


def main():
  bst = BinarySearchTree()

  sequenceString = input("Enter a comma-separated list of unique characters (or nil) to build a tree:\n> ").replace(" ", "")
  sequence = [char for char in sequenceString.split(",")]
  
  for node in sequence:
    bst.insert(node)

  bst.printTree()
  # preorder = Traversals.preorderTraversal(sequence[0])
  # postorder = Traversals.postorderTraversal()

  # print("Tree: {0}\n".format(sequence))
  # print("Preorder: ")

if __name__ == '__main__':
  main()