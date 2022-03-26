# Problem 7: Request Routing in a Web Server with a Trie

## Reason
To implement an HTTPRouter like what in a typical web server using the Trie data structure. First implement a slightly different Trie (RouteTrieNode, RouteTrie).

RouteTrieNode contains the dictionary which stores all path parts(split from the whole path using '/') and their children, so that we can know if a path is valid or not. And RouteTrieNode has a handler which indicates whether there's a handler on this node which means it can construct a valid path from all parents.

RouteTrie will have a root(RouteTrieNode) which tracks all possible first path part. Then RouteTrie has insert and find methods. When inserting, we traverse the whole trie from root, and check if each path part exists or not, and inset accordingly and update the handler. And finding a path just need to traverse the whole trie

Then we implement the actual Router class. The router will initialize itself with a RouteTrie to hold routes and associated handlers. It also support adding a handler by path and looking up a handler by path. All of these operations will be delegated to the RouteTrie.

## Efficiency

- Time complexity
  O(n), the insert and find operation with Trie structure takes O(n), where n is the number of nodes which split from the path using '/'

- Space complexity
  O(n), the space complexity in this case depends on n which is number of split path from the path using '/'
