class LinkedList:
    
    def __init__(self):
        self.head = None

    def _node_at(self, index: int) -> Node:
        # walks to pos and returns node
        curr_node = self.head
        # is head empty
        if curr_node is None:
            return None
        for step in range(index):
            curr_node = curr_node.nextn
            if curr_node is None:
                break
        return curr_node

    def _walk(self):
        vals = []
        curr_node = self.head
        if curr_node is None:
            return None, []
        while True:
            #print(f"_walk -> {curr_node.val} - {curr_node.nextn}")
            vals.append(curr_node.val)
            if curr_node.nextn is None:
                break
            
            curr_node = curr_node.nextn
        return curr_node, vals 

    def get(self, index: int) -> int:
        node = self._node_at(index)
        if node is None:
            return -1
        return node.val

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)

    def insertTail(self, val: int) -> None:
        last_node, _ = self._walk()
        #print(f"tail -> {last_node.val} - {last_node.nextn}")
        if last_node is None:
            self.head = Node(val, None)
        else:
            last_node.nextn = Node(val, None) 

    def remove(self, index: int) -> bool:
        # handle 0th case
        if index == 0 and self.head is not None:
            self.head = self.head.nextn
            return True
        elif self.head is None:
            return False

        node = self._node_at(index-1)
        node_to_link = self._node_at(index)
        if node is None or node_to_link is None:
            return False
        node.nextn = node_to_link.nextn
        return True

    def getValues(self) -> List[int]:
        print("\ngetValues")
        _, vals = self._walk()
        print(f"getValues -> {vals}")
        return vals 



class Node:
    def __init__(self, val, nextn) -> None:
        self.val = val
        self.nextn = nextn

    def next_node(self):
        return self.nextn
    
    def is_empty(self):
        if self.val == None and self.nextn == None:
            return True
        return False
