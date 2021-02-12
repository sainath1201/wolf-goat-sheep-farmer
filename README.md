# wolf-goat-sheep-farmer
""
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
