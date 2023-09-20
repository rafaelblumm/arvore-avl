def avl_tree_to_dict(node):
    if node is None:
        return None

    children = []
    if node.left:
        children.append(avl_tree_to_dict(node.left))
    if node.right:
        children.append(avl_tree_to_dict(node.right))

    return {
        "name": str(node.data),
        "children": children
    }
