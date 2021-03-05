class PrefixTreeNode:

  def __init__(self, letter):

    #the character string
    self.letter = letter

    #references to other child nodes
    self.children = []

    #is this node the end of a word or not?
    self.terminal = False

class PrefixTree:

  def __init__(self):

    self.root = PrefixTreeNode("")

  def search(self, prefix):
    '''This method will return true if a given prefix is present false if not
    input = "ca"
    output = True'''
    #start at the root
    #search for first letter of the prefix in root's children
    #if the letter is not there
    #return False
    #if it is there
    #look for next letter, so basically
    #go to that first letter node and check its children
    #repeat until whole prefix is found or false
    current = self.root

    for letter in prefix:
      foundit = 0

      for child in current.children:
        if child.letter == letter:
          #found that letter check child's children
          current = child
          foundit = 1
          break

      if foundit == 0:
        return False

    return True

  def insert(self, word):
    '''This method will add a new word to the prefix tree
    input = "dog" 
    '''
    #start with root
    #check children of root and if first letter of word is not there
    #add a new node with letter
    #else do nothing
    #repeat, get the node corresponding to the letter
    #check it's children for the next letter
    current = self.root
    for letter in word:

      alreadythereflag = 0
      #check if letter in children
      for child in current.children:
        if child.letter == letter:
          #already there
          current = child
          alreadythereflag = 1
      #I exit this loop without having found a child with the letter
      #then add it
      if alreadythereflag != 1:
        childnode = PrefixTreeNode(letter)
        current.children.append(childnode)
        current = childnode

    #when I'm at the end set to terminal to True
    current.terminal = True

  def find_all_words(self):
    '''returns a list of valid words in the tree starting with the given Prefix
    input "cat"
    output ["category", "cat"] '''
    #TODO: think about how to implement this
    words = []

    #traversal
    current = self.root
    #check all the children of this current node
    #check all their children and so on, traversal
    for child in current.children:
      #traverse
      self.traverse(child, words.append, child.letter)


    return words

  def traverse(self, node, visit, acc):
    #base case
    if node.terminal:
      #TODO: not quite what I want
      visit(acc)

    #recursive case
    for child in node.children:
      self.traverse(child, visit, acc + child.letter)

  def delete(self, word):
    #stretch challenge
    '''This method will remove a word from the prefix tree
    input = "dog" '''
    pass