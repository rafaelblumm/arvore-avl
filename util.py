def avl_tree_to_dict(node):
    if node is None:
        return None

    children = []
    if node.right:
        children.append(avl_tree_to_dict(node.right))
    if node.left:
        children.append(avl_tree_to_dict(node.left))

    return {
        "name": str(node.value),
        "children": children
    }
