''' PROBLEMA
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
'''

from unittest import TestCase, main
from app import likes

class TestLikes(TestCase):
  
  def test_no_likes(self):
    self.assertEquals(likes([]), 'no one likes this')

  def test_one_like(self):
    self.assertEquals(likes(['Jacob']), 'Jacob like this')
    
  def test_two_likes(self):
    self.assertEquals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
    
  def test_three_likes(self):
    self.assertEquals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
    
  def test_four_likes(self):
    self.assertEquals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')

main()