# 作者：柚子皮
# 2026年02月24日12时03分20秒
# yexixi2333@gmail.com

class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree:
    def __init__(self):
        self.root = None
        self.help_queue = []  # 辅助队列

    def build_tree(self, node: Node):
        if self.root is None:
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild = node
            else:
                self.help_queue[0].rchild = node
                self.help_queue.pop(0)

    def pre_order(self, node: Node):
        print(node.elem, end=' ')
        if node.lchild is not None:
            self.pre_order(node.lchild)
        if node.rchild is not None:
            self.pre_order(node.rchild)


if __name__ == '__main__':

    my_tree = BinaryTree()
    for i in range(1, 11):
        new_node = Node(i)
        my_tree.build_tree(new_node)
    my_tree.pre_order(my_tree.root)
