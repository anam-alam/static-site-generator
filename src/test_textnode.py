import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):

    #This test creates two TextNode objects with the same properties and asserts that they are equal
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD) 
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2) 

    #This test creates two TextNode objects with the same properties and asserts that they are not equal
    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.LINK, None)
        node2 = TextNode("This is a text node", TextType.LINK, None)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is text node", TextType.LINK, "https://www.google.com/")
        node2 = TextNode("This is text node", TextType.LINK,"https://www.google.com/")
        self.assertEqual(node,node2)

        
    


if __name__ == "__main__":
    unittest.main()