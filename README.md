Table of contents
=================


   * [Context](#Context)
   * [Domineering game](#domineering-game)
   * [Game Rules](#installation)
   * [Playing Domineering](#Playing-Domineering)
   * [Motivation](#Motivation)
   * [Monte Carlo tree search](#Monte-Carlo-tree-search)
      * [Selection](#Selection)
      * [Expansion](#Expansion)
      * [Simulation](#Simulation)
      * [Backpropagation](#Backpropagation)
   * [Features](#Features)
      * [Playing randomly](#Playing-randomly)
      * [Playing using Monte Carlo Tree search](#Playing-using-Monte-Carlo-Tree-search)
      * [Playing using Reinforcement learning](#Playing-using-Reinforcement-learning)
   * [Installation](#Installation)
   * [How to use?](#How-to-use?)
   * [References](#References)
   * [Dependency](#dependency)


## Context 
The objective of this project is to implement an algorithm that plays: Human vs Computer or Computer vs Computer. The computer can play randomly or using MCTS or using Reinforcement learning.

## Domineering game
<p align="center">
  <img width="460" height="300" src="https://cdn.ima.org.uk/wp/wp-content/uploads/2015/08/Domineering-Comments-on-a-Game-of-No-Chance-figure-6.png">
</p>


## Game Rules
Domineering (also called Stop-Gate or Crosscram) is a mathematical game played on a sheet of graph paper, with any set of designs traced out.
For example, it can be played on a 6×6 square, a checkerboard, an entirely irregular polygon, or any combination thereof.
Two players have a collection of dominoes which they place on the grid in turn, covering up squares.
One player, Left, plays tiles vertically, while the other, Right, plays horizontally. As in most games in combinatorial game theory, the first player who cannot move loses.

## Playing Domineering
You can play domineering game following this link: https://www.jasondavies.com/domineering/#5x5)

## Motivation
The main objective of this project is to create an algorithm that plays randomly, using Monte Carlo Tree Search (MCTS) and using deeplearning techniques.

## Monte Carlo tree search
In computer science, Monte Carlo tree search (MCTS) is a heuristic search algorithm for some kinds of decision processes, most notably those employed in game play. MCTS has been used for decades in computer Go programs. It has been used in other board games like chess and shogi, games with incomplete information such as bridge and poker.

## Principle of playing based on MCTS
The focus of Monte Carlo tree search is on the analysis of the most promising moves, expanding the search tree based on random sampling of the search space. The application of Monte Carlo tree search in games is based on many playouts. In each playout, the game is played out to the very end by selecting moves at random. The final game result of each playout is then used to weight the nodes in the game tree so that better nodes are more likely to be chosen in future playouts.

The most basic way to use playouts is to apply the same number of playouts after each legal move of the current player, then choose the move which led to the most victories.[10] The efficiency of this method—called Pure Monte Carlo Game Search—often increases with time as more playouts are assigned to the moves that have frequently resulted in the current player's victory according to previous playouts. Each round of Monte Carlo tree search consists of four steps:

* Selection:
start from root R and select successive child nodes until a leaf node L is reached. The root is the current game state and a leaf is any node from which no simulation (playout) has yet been initiated. The section below says more about a way of biasing choice of child nodes that lets the game tree expand towards the most promising moves, which is the essence of Monte Carlo tree search.

* Expansion: 
unless L ends the game decisively (e.g. win/loss/draw) for either player, create one (or more) child nodes and choose node C from one of them. Child nodes are any valid moves from the game position defined by L.

* Simulation:
complete one random playout from node C. This step is sometimes also called playout or rollout. A playout may be as simple as choosing uniform random moves until the game is decided (for example in chess, the game is won, lost, or drawn).

* Backpropagation:
use the result of the playout to update information in the nodes on the path from C to R.

![js-standard-style](https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/MCTS_%28English%29_-_Updated_2017-11-19.svg/808px-MCTS_%28English%29_-_Updated_2017-11-19.svg.png)

This graph shows the steps involved in one decision, with each node showing the ratio of wins to total playouts from that point in the game tree for the player that node represents. In the Selection diagram, black is about to move. The root node shows there are 11 wins out of 21 playouts for white from this position so far. It complements the total of 10/21 black wins shown along the three black nodes under it, each of which represents a possible black move.

If white loses the simulation, all nodes along the selection incremented their simulation count (the denominator), but among them only the black nodes were credited with wins (the numerator). If instead white wins, all nodes along the selection would still increment their simulation count, but among them only the white nodes would be credited with wins. In games where draws are possible, a draw causes the numerator for both black and white to be incremented by 0.5 and the denominator by 1. This ensures that during selection, each player's choices expand towards the most promising moves for that player, which mirrors the goal of each player to maximize the value of their move.

Rounds of search are repeated as long as the time allotted to a move remains. Then the move with the most simulations made (i.e. the highest denominator) is chosen as the final answer.

## Features
Here we show the differents strategy of playing:
##### Playing randomly
Given a board state the algorithm search for legal moves given the game rules and choose one of them 

![js-standard-style](https://cdn.ima.org.uk/wp/wp-content/uploads/2015/08/Domineering-Comments-on-a-Game-of-No-Chance-figure-6.png)


Here for example if the computer plays black the legal moves are: [6,ab], [6,de], [6,ef], [5,ab], [4,ab], [4,bc], [3,cd], [1, ab], [1, bc], , [1, cd], [1, de], [1, ef]
In this case the computer choose a randomly a move from legal moves to play its turn.

##### Playing using Monte Carlo Tree search
As mentionned earlier in this case the computer check legal moves and simulate the game to the end to choose move with maximum playout.

##### Playing using Reinforcement learning
A reinforcement learning algorithm and neural networks to the problem of producing an
agent that can play board games.
DeepRL system which combines Deep Neural Networks with Reinforcement Learning is able to master a diverse range of Atari 2600 games to superhuman level with only the raw pixels and score as inputs.

![js-standard-style](http://karpathy.github.io/assets/rl/policy.png)

## Installation
Provide step by step series of examples and explanations about how to get a development env running.

## How to use?
To use this project you might choose the game mode (random, MCTS, DRL) and run the corresponding script.



### References
Jaderberg, M., Czarnecki, W. M., Dunning, I., Marris, L., Lever, G., Castaneda, A. G., ... & Sonnerat, N. (2018). Human-level performance in first-person multiplayer games with population-based deep reinforcement learning. arXiv preprint arXiv:1807.01281.

Silver, D., Schrittwieser, J., Simonyan, K., Antonoglou, I., Huang, A., Guez, A., ... & Chen, Y. (2017). Mastering the game of go without human knowledge. Nature, 550(7676), 354.

Cazenave, T. (2017, July). Improved Policy Networks for Computer Go. In Advances in Computer Games (pp. 90-100). Springer, Cham.

Cazenave, T. (2018). Residual networks for computer Go. IEEE Transactions on Games, 10(1), 107-110.

Cazenave, T. (2016). Improved Architectures for Computer Go.

### Requirements
- Python 3
- Keras
- TensorFlow  
