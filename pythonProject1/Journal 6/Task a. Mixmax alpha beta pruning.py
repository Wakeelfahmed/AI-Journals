import math

def minimax(depth, nodeIdex, isMax, score, height):
    if depth == height:
        print("Node: ", score[nodeIdex])
        return score[nodeIdex]
    elif (isMax):
        print("a")
        return max(minimax(depth + 1, (nodeIdex * 2), False, score, height),
                   minimax(depth + 1, nodeIdex * 2 + 1, False, score, height))
    else:
        print("b")
        return min(minimax(depth + 1, (nodeIdex * 2), True, score, height),
                   minimax(depth + 1, nodeIdex * 2 + 1, True, score, height))


score = [-1, 3, 5, 1, -6, 4, 0, 9]
height = math.log(len(score), 2)
print("Height of Tree", math.ceil(height))
result = minimax(0, 0, True, score, math.ceil(height))
print("optimal value", result)
