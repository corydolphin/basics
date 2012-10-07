from linkedList import *
import unittest

class LinkedListTest(unittest.TestCase):
  
  def setUp(self):
    unittest.TestCase.setUp(self)

  def insertNodes(self, number):
    ll = LinkedList(Node(0))
    for i in xrange(1,number):
      ll.insert(Node(i))

    return ll

  def checkEquality(self, current, valList):
    for i in valList:
      self.assertTrue(current.val == i)
      current = current.next

  def test_insert(self):
    testCount = 5
    ll = self.insertNodes(testCount)

    self.checkEquality(ll.head, [0, 1, 2, 3, 4])
    self.assertTrue(ll.length() == testCount)

  def test_length(self):
    testCount = 5
    ll = self.insertNodes(testCount)
    self.assertTrue(ll.length() == testCount)

  def test_delete(self):
    testCount = 5
    ll = self.insertNodes(testCount)

    ll.delete(3)
    self.checkEquality(ll.head, [0, 1, 2, 4])
    self.assertTrue(ll.length() == testCount-1)

  def test_reverse(self):
    testCount = 5
    ll = self.insertNodes(testCount)

    ll.reverse()
    self.checkEquality(ll.head, [4, 3, 2, 1, 0])
    self.assertTrue(ll.length() == testCount)

  def test_hasCycle(self):
    ll = LinkedList(Node(0))
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node3.next = node1
    ll.insertNodes([node1, node2, node3])

    self.assertTrue(ll.hasCycle())

if __name__ == '__main__':
  unittest.main()