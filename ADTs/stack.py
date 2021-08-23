class ArrayBasedStack(object):
  def __init__(self, maxSize = 10):
    self.array = []
    self.maxSize = maxSize

  def getSize(self):
    return len(self.array)

  def push(self, val):
    if len(self.array) == self.maxSize:
      # print("FullStackException")
      pass
    else:
      self.array.append(val)

  def pop(self):
    if len(self.array) == 0:
      # print("EmptyStackException")
      pass
    else:
      return self.array.pop()

  def printStack(self):
    if len(self.array) != 0:
      stackString = ""
      for i in range(len(self.array)):
        stackString += str(self.array[i]) + " "
      print(stackString)
    else:
      print("Stack is empty!")

class SequenceRobot():
  # With stacks, there are two possible operations: push and pop. The default steps array contains
  #   multiple tuples, each containing an operation in the first index and a number in the second
  #   index.
  #
  # If the operation is a "push", then the following number is the value to push onto the stack.
  # If the operation is a "pop", then the following number is the number of times to pop.
  def __init__(self, stackSize = 3, steps = [("push", 1), ("push", 2), ("push", 3), ("push", 4), ("pop", 4)]):
    self.steps = steps
    self.stackSize = stackSize

  def getSteps(self):
    return self.steps

  def addStep(self, step):
    self.steps.append(step)
  
  def removeLastStep(self):
    return self.steps.pop()

  def printStep(self, step, stack):
    if step[0] == "push":
      print("After pushing {0}: ".format(step[1]))
    else:
      print("After popping: ")
    stack.printStack()

  def runArrayBasedStackMethods(self):
    stack = ArrayBasedStack(self.stackSize)
    
    print("\n*** For a stack with max size {0} ***".format(self.stackSize))

    # Go through each step
    for step in self.getSteps():
      if step[0] == "push":
        stack.push(step[1])
        self.printStep(step, stack)
      else:
        for i in range(step[1]):
          stack.pop()
          self.printStep(step, stack)
        

def main():
  menuChoice = ""
  menu = "\n***** Stacks Menu *****\n" +\
          "1. Array-based Stack\n" +\
          "2. Growable Array-based Stack\n" +\
          "Q. Quit\n" +\
          "Enter a choice: "

  while True:
    menuChoice = input(menu).lower()
    robot = SequenceRobot()

    if menuChoice == "1":
      robot.runArrayBasedStackMethods()
    elif menuChoice == "2":
      print("2")
    elif menuChoice == "q" or menuChoice == "quit":
      break
    else:
      print("Invalid option!\n")


if __name__ == '__main__':
  main()