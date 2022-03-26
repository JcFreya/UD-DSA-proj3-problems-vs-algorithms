# Problem 5: Autocomplete with Tries

## Reason
Use dic normal dictionary to store the nodes. For TrieNode, we have is_word to show if it's a valid word at this node and value.
The Trie itself has the root node(the first characters of word) and its children nodes, meanwhile has insert/find functions. 1) To insert, will need to traverse each character and see if it's in the dictionary. We either move to the next character or add the new character in. 2) To search the target, we do the same traverse the trie (including all children nodes) and check if the word is in dictionary

## Efficiency

- Time complexity
  - insert/find takes O(n) time complexity, where n in number for characters in the word.
  - suffixes O(n*m) where n is word length and m is number of words

- Space complexity
  - insert: O(n), the space taken for node is constant
  - suffixes: O(n*m) where n is word length and m is number of words
