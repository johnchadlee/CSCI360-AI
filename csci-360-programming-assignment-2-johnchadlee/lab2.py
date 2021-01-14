# you can add imports but you should not rely on libraries that are not already provided in "requirements.txt #
from heapq import heappush, heappop
import copy

def a_star_search(stack):
    # print(stack)
    # flip_sequence = []
    # # --- v ADD YOUR CODE HERE v --- #
    # start = stack.copy()
    # openSet = []
    # closedSet = []
    # seq = []
    # g = 0 # depth of tree
    # f = 0
    # heappush(openSet, (f, seq, start) )
    # while openSet:
    #     current = openSet[0]
    #     # g += 1 #increase g to match the depth
    #     if current[2].check_ordered() == True:
    #         return flip_sequence
    #     #Generate neighbor nodes
    #     heappop(openSet)
    #     closedSet.append(current[2])
    #     for idx, val in enumerate(current[2].order):
    #         temp_seq = copy.deepcopy(flip_sequence)
    #         neighbor = current[2].copy()
    #         neighbor.flip_stack(idx+1)
    #         neighbor.flip = idx + 1
    #         temp_seq.append(neighbor.flip)
    #         # print(openSet)
    #         h = 0
    #         # Calculate h score
    #         for i in range(neighbor.num_books - 1):
    #             if neighbor.orientations[i] == 1 and neighbor.orientations[i+1] == 1 and neighbor.order[i] + 1 == neighbor.order[i+1]: 
    #                 continue
    #             else: 
    #                 h = h + 1 
    #         # Calculate f score
    #         if neighbor not in closedSet:  
    #             g += 1 #increase g to match the depth 
    #             f = g + h 
    #             if (f, temp_seq, neighbor) not in openSet:
    #                 heappush(openSet, (f, temp_seq, neighbor)) 
    #                 closedSet.append(neighbor)
    #             else:
    #                 continue    
                          
    #     flip_sequence.append((openSet[0])[2].flip)
        



    print(stack)
    flip_sequence = []
    # --- v ADD YOUR CODE HERE v --- #
    start = stack.copy()
    openSet = []
    closedSet = []
    g = 0 # depth of tree
    f = 0
    counter = 100
    heappush(openSet, (f, counter, start) )
    while openSet:
        # g+=1
        current = heappop(openSet)
        if current[2].check_ordered() == True:
            # print("Solution found")
            print(current[2])
            return flip_sequence
        closedSet.append(current[2])
        #Generate neighbor nodes
        for idx, val in enumerate(current[2].order):
            neighbor = current[2].copy()
            neighbor.flip_stack(idx+1)
            neighbor.flip = idx + 1
            neighbor.g = g
            neighbor.h = 0
            # Calculate h score
            for i in range(neighbor.num_books - 1):
                if neighbor.orientations[i] == 1 and neighbor.orientations[i+1] == 1 and neighbor.order[i] + 1 == neighbor.order[i+1]: 
                    continue
                else: 
                    neighbor.h = neighbor.h + 1 
            # Calculate f score        
            if neighbor not in closedSet:
                # temp_g = g + 1 #increase g to match the depth
                g+=1
                # temp_g = g
                f = neighbor.g + neighbor.h
                if (f, counter, neighbor) not in openSet:
                    # neighbor.g = temp_g
                    # f = neighbor.g + neighbor.h
                    heappush(openSet, (f, counter, neighbor))
                    # closedSet.append(neighbor)
                    counter-=1
    
        flip_sequence.append((openSet[0])[2].flip)

    
    return

    # ---------------------------- #


def weighted_a_star_search(stack, epsilon=None, N=1):
    # Weighted A* is extra credit

    flip_sequence = []

    # --- v ADD YOUR CODE HERE v --- #

    return flip_sequence

    # ---------------------------- #
