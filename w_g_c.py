"""
FARMER WOLF GOAT CABBAGE
the game contains
farmer,wolf,goat,cabbage
they have to cross the river by certain rules
rules:
  wolf-eat-goat-eat-cabbage
  if farmer present they will not eat any other
  we have across them the river
  farmer can take only one at a time. so that no other one can eat
  all three should cross the river safe
ANALYSIS:
  We're looking for a "solution for the problem" that reaches a goal.
  That's a solution search problem.
  we can use BFS() Algorithm
  The possible moves we get
  [('goat1', 'cabbage1'), ('farmer1', 'wolf1')]
  [('wolf1', 'cabbage1'), ('farmer1', 'goat1')]
  [('wolf1', 'goat1'), ('farmer1', 'cabbage1')]
  checks the condtions and place the possible move in game_state
  if end state is equal to game_state then trace the path solution
Representation:
  bank_1 = ( "farmer", "wolf", "goat", "cabbage")
  bank_2 = ()
  root_node={
    "state" : [ bank_1, bank_2],
    "parent" : None
  }
  visited = {}
  fringe = [root_node]
"""
def path(visited,node):
  """
  RETURNS THE PATH OF SOLUTION
  Args:
    visited(<dict>) : contains the nodes which are already expanded
    node(<dict>) : contains goal node to trace the solution path
  """
  solution_path = [node]
  while solution_path[-1]["parent"]:
    solution_path.append(visited[tuple(solution_path[-1]["parent"])])
  return solution_path

def goal_state(game_state):
  """
  RETURNS THE GOAL STATE TRUE OR FALSE
   Args:
    game_state(tuple<(tuple)(tuple)>) : contains the present state of game
   Returns:
    TRUE or FALSE
  """
  if game_state[0]:
    return False
  return True

def possible_move(game_node):
  """
  RETURN POSSIBLE MOVES
  Args:
    gamenode(tuple<(tuple)(tuple)>) : contains the present state of game
  Returns:
    moves<list> : returns all possible moves
  """
  moves = []
  bank1 = list(game_node[0])
  bank2 = list(game_node[1])
  if "farmer" in bank1:
    bank1_copy = bank1[:]
    bank2_copy = bank2[:]
    bank1_copy.remove("farmer")
    bank2_copy.append("farmer")
    for move in bank1_copy:
      bank1_copy1 = bank1_copy[:]
      bank2_copy2 = bank2_copy[:]
      bank1_copy1.remove(move)
      bank2_copy2.append(move)
      moves.append([tuple(bank1_copy1),tuple(bank2_copy2)])
  else:
    bank1_copy = bank1[:]
    bank2_copy = bank2[:]
    bank2_copy.remove("farmer")
    bank1_copy.append("farmer")
    for move in bank2_copy:
      bank1_copy1 = bank1_copy[:]
      bank2_copy2 = bank2_copy[:]
      bank2_copy2.remove(move)
      bank1_copy1.append(move)
      moves.append([tuple(bank1_copy1),tuple(bank2_copy2)])
    moves.append([tuple(bank1_copy),tuple(bank2_copy)])
  return moves

def conditions(game_node):
  """
  RETURNS THE TRUE OR FALSE
  Args:
    gamenode(tuple<(tuple)(tuple)>) : contains the present state of game
  Returns:
    TRUE or FALSE
  """
  if "goat" in game_node[0] and "cabbage" in game_node[0]: 
    return "farmer" in game_node[0]
  if "wolf" in game_node[0] and "goat" in game_node[0]:
    return "farmer" in game_node[0]
  if "goat" in game_node[1] and "cabbage" in game_node[1]:
    return "farmer" in game_node[1]
  if "wolf" in game_node[1] and "goat" in game_node[1]:
    return "farmer" in game_node[1]
  return True

def search(visited,fringe):
  """
  RETURNS THE SOLUTION
  Args:
    visited(dict) ={((bank1),(bank2)):{"state":((bank1),(bank2)),"parent":none}}
    fringe(list)  = next expansions
  """
  while fringe:
    node = fringe[0]
    fringe = fringe[1:]
    visited[tuple(node["state"])] = node
    if goal_state((node["state"])):
      return path(visited,node)
    childern = []
    for child_state in possible_move(node["state"]):
      if conditions(child_state):
        childern.append(
          {
            "state" : tuple(child_state),
            "parent" : node["state"]
          }
          )
    for child in childern:
      if child["state"] not in visited:
        fringe.append(child)

bank_1 = ( "farmer", "wolf", "goat", "cabbage")
bank_2 = ()
root_node={
    "state" : [ bank_1, bank_2],
    "parent" : None
  }
visited = {}
fringe = [root_node]
finial_path = search(visited,fringe)
solution = reversed(finial_path)
for i in solution:
  print(*i["state"])
