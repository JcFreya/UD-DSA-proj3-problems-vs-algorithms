'''
# Problem 7: Request Routing in a Web Server with a Trie
HTTPRouter using a Trie
For this exercise we are going to implement an HTTPRouter like you would find in a
typical web server using the Trie data structure we learned previously.

There are many different implementations of HTTP Routers such as regular expressions
or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

The purpose of an HTTP Router is to take a URL path like "/", "/about",
or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return.

In a dynamic web server, the content will often come from a block of code called a handler.

'''

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        # dictionary to track mapping of sub-path and child RouteTrieNodes
        self.children = dict()

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path_parts, handler):
        # Recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        # check None input path
        if path_parts is None or len(path_parts)==0:
            return

        # path_parts = self.split_path(path)
        curr = self.root
        # loop over the parts in path_parts
        for part in path_parts:
            if part in curr.children:
                curr = curr.children[part]
            else:
                curr.insert(part)
                curr = curr.children[part]
        curr.handler = handler

    def find(self, path_parts):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        # check none path
        if path_parts is None:
            return

        # if there's only one part in path
        if len(path_parts) == 1:
            return self.root.handler

        # path_paths = self.split_path(path)
        curr = self.root

        for part in path_parts:
            if part in curr.children:
                curr = curr.children[part]
            else:
                return None

        return curr.handler

    # def split_path(self, path):
    #     # split the path with '/'
    #     return path.split('/')


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, handler, not_found_handler=None):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # Split the path and pass the path parts
        # as a list to the RouteTrie
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler

        # check None input path
        if path is None:
            print("Error: Input path couldn't be None\n")
            return

        if len(path)==0:
            print("Error: Input path couldn't be empty\n")
            return

        # handle trailing slash
        if path[-1] == "/":
            path = path[:-1]

        path_parts = self.split_path(path)

        handler = self.route_trie.find(path_parts)

        if handler is None:
            return self.not_found_handler
        else:
            return handler


    def split_path(self, path):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return path.split('/')


# Test Cases

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/me/test", "test handler")  # add a route

print('----------Test1----------')
# test finding '/' handler
print(router.lookup("/")) # should print 'root handler'
print('\n')

print('----------Test2----------')
# test not found handler
print(router.lookup("/home")) # should print 'not found handler'
print('\n')

print('----------Test3----------')
# test home/about handler
print(router.lookup("/home/about")) # should print 'about handler'
print('\n')

print('----------Test4----------')
# test home/about/ handler
print(router.lookup("/home/about/")) # should print 'about handler'
print('\n')

print('----------Test5----------')
# test /home/about/me handler
print(router.lookup("/home/about/me")) # should print 'not found handler'
print('\n')

print('----------Test6----------')
# test /home/about/me handler
print(router.lookup("/home/about/me/test")) # should print 'test handler'
print('\n')

print('----------Test7----------')
# test empty path input
print(router.lookup("")) # Error: Input path couldn't be empty, None
print('\n')

print('----------Test8----------')
# test None path input
print(router.lookup(None)) # Error: Input path couldn't be None, None
print('\n')
