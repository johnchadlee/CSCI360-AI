
# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from collections import deque
import copy

def breadth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    visited = deque()
    deq = deque()
    traverse = []
    counter = 0
    seq = deque()
    start_node = stack.copy()
    visited.appendleft(start_node)
    deq.append(start_node)
    seq.append(counter)
    
    while deq:
        s = deq.pop()
        seq.pop()
        if s.check_ordered() == True:
            print(s.order)
            print(s.orientations)
            traverse.append(counter)
            print(seq)
        for idx, val in enumerate(s.order):
            node = s.copy()
            node.flip_stack(idx+1)
            counter = idx+1    
            if node not in visited:
              new_seq = []
              visited.append(node)
              deq.append(node)
              new_seq.append(counter)
              seq.append(new_seq)          
    flip_sequence = traverse

    return flip_sequence
    # ---------------------------- #


def depth_first_search(stack):
    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #
    s = stack.copy()
    stk = []
    stk.append(s)
    visited = deque()
    path = []
    seq = []
    counter = 0
    traverse = []
    while (len(stk)):
        s = stk[-1]
        stk.pop()
        if s.check_ordered() == True:
            print(s.order)
            print(s.orientations)
            traverse.append(counter)
        for idx, val in enumerate(s.order):
            node = s.copy()
            node.flip_stack(idx+1)
            counter = idx+1  
            if node not in visited:
              visited.appendleft(node)
              new_seq = []
              new_seq.append(counter)
              seq.append(new_seq)
              stk.append(node) 
        

    flip_sequence = traverse
    return flip_sequence
    # ---------------------------- #
