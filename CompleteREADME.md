AI Programming Assignment-5

Overview->
This repository contains implementations of various Artificial Intelligence concepts including search algorithms, knowledge representation, recommendation systems, and probabilistic reasoning.

The work includes:
* MinMax Search
* Alpha-Beta Search
* Heuristic Alpha-Beta Search
* Monte-Carlo Tree Search (MCTS)
* AI Based Travel Planner
* Knowledge Graphs
* Bayesian Networks

---

1.MinMax Search

MinMax is a decision-making algorithm used in two-player games. It evaluates all possible moves and selects the optimal move assuming both players play optimally.

Run
python MinMaxSearch.py

2.Alpha-Beta Search
Alpha-Beta pruning is an optimization of the MinMax algorithm. It eliminates branches that cannot influence the final decision, reducing the number of nodes evaluated.

Run
python Alpha-Beta_Search.py

3.Heuristic Alpha-Beta Search
This implementation combines Alpha-Beta pruning with a heuristic evaluation function and depth-limited search to improve efficiency.

Run
python "Heuristic alpha-beta search.py"

4.Monte Carlo Tree Search
Monte-Carlo Tree Search uses random simulations to estimate the best decision in a search space.

Run
python Monte-CarloTree.py

5.AI-Based Travel Planner
A simple travel planning system that uses a predefined knowledge base of tourist places, food recommendations, and cost assessment to generate a personalized travel itinerary.

Features
* Tourist place recommendations
* Food recommendations
* Cost estimation
* Personalized travel planning

Run
python Travelplanner.py

Sample input
* City: Hyderabad
* Budget: 10000
* Days: 2
* Interest: Historical Places

6.Knowledge Graphs

Knowledge Graphs represent entities and relationships using graph structures. They are widely used in search engines, recommendation systems, and intelligent assistants.

Tools
* Neo4j
* RDF
* Protégé
* GraphDB
* NetworkX

Run
python "Knowledge Graph.py"

7.Bayesian Networks
Bayesian Networks are probabilistic graphical models used for reasoning under uncertainty.

Example
Rain → Wet Grass

Tools
* pgmpy
* GeNIe
* Netica
* BayesiaLab

Run
python Bayesian_Network.py

Repository Files
MinMaxSearch.py

Alpha-Beta_Search.py

Heuristic alpha-beta search.py

Monte-CarloTree.py

Travelplanner.py

Knowledge Graph.py

Bayesian_Network.py

sample_data.txt

sample_data_knowledge graph.txt

Sample_txt_bayesian_network.txt
