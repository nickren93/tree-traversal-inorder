class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
  


def treeTraversalInorder(root):
    # type your code here  
    res = []
    
    def dfs(node):
        if not node:
            return
        
        dfs(node.left)            # 1. left
        res.append(node.value)   # 2. root
        dfs(node.right)          # 3. right
    
    dfs(root)
    return res


def treeTraversalInorder(node, res=None):
    if res is None:
        res = []
    
    if node is None:
        return res
    
    if node.left:
        treeTraversalInorder(node.left, res)
    
    res.append(node.value)
    
    if node.right:
        treeTraversalInorder(node.right, res)

    return res


'''
below has issue:

def treeTraversalInorder(node, res = []):
    if node == None:
        return res
    
    if node.left:
        treeTraversalInorder(node.left, res)
    
    res.append(node.value)
    
    if node.right:
        treeTraversalInorder(node.right, res)

    return res


issue explain:
    Issue: res=[] default argument (VERY IMPORTANT)

    this line: def treeTraversalInorder(node, res = []):
    👉 This is a classic Python bug.
    Why it's bad:

    The same list is reused across function calls:

    treeTraversalInorder(root1)
    treeTraversalInorder(root2)

    👉 res will keep old values 😬
'''




'''
below is iterative method using While loop:
'''
def treeTraversalInorder(root):
    res = []
    stack = []
    current = root
    
    while current or stack:
        
        # go left as far as possible
        while current:
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        res.append(current.value)
        
        current = current.right
    
    return res



'''
My original wrong version:

def treeTraversalInorder(node, res = []):
    if node == None:
        return res
    
    if node.left:
        return treeTraversalInorder(node.left, res)
    res.append(node)
    
    if node.right:
        return treeTraversalInorder(node.right)

    return res

'''


# if (require.main === module) {
#   // add your own tests in here
#   let root = new Node(2, new Node(-10), new Node(20));
#   console.log("Expecting: [-10, 2, 20]");
#   console.log(treeTraversalInorder(root));

#   console.log("");

#   root = new Node(10, new Node(0, null, new Node(5)), new Node(20, null, new Node(30)));
#   console.log("Expecting: [0, 5, 10, 20, 30] ");
#   console.log(treeTraversalInorder(root));
# }

# module.exports = {
#   Node,
#   treeTraversalInorder
# };

# // Please add your pseudocode to this file
# // And a written explanation of your solution
