# Fire Evacuation Route System

This repository contains code for a fire evacuation route system that predicts optimal evacuation paths and analyzes factors contributing to effective evacuation. The project is implemented in Python and integrates algorithms for both static and dynamic environments, including Q-learning for adaptive pathfinding and A* for static pathfinding.

## Project Overview
In emergency scenarios such as fires, having efficient evacuation routes can save lives and minimize property damage. This project focuses on developing a robust fire evacuation route system that combines reinforcement learning and heuristic search techniques. By integrating Q-learning for dynamic pathfinding and A* for static pathfinding, the system aims to provide adaptive and efficient evacuation routes in complex environments.

## Tech Stack
The project is implemented using the following technologies:
- Python
- Pandas
- Pygame (for visualization)
- PyCharm (development environment)

## Related Work
The project draws inspiration from related works in the field of emergency response and evacuation systems, including studies on real-time path adaptation, machine learning-based evacuation time prediction, and adaptive route recalculations in dynamic environments.

## Theory and Equations
The project utilizes the following theories and equations:
- **Q-learning with Bellman Equation**: Used to learn adaptive policies for navigating fire scenarios by iteratively updating Q-values.
- **A* Pathfinding**: Employed for static pathfinding to find optimal paths based on heuristic estimates.

## Approach, Implementation, and Results
### Approach
- **Q-learning for Dynamic Pathfinding**: Implemented to adaptively find paths in dynamic environments by updating Q-values iteratively.
- **A* for Static Pathfinding**: Utilized for efficient pathfinding in static environments with fixed obstacles.
- **Integration and Simulation**: Brings together Q-learning and A* pathfinding in a simulated environment to demonstrate their effectiveness.

### Implementation
The system is implemented using Python, with separate modules for Q-learning, A* pathfinding, and integration. Pygame is used for visualization to simulate the evacuation process.

### Results
The project successfully integrates Q-learning and A* pathfinding to provide efficient and adaptive fire evacuation routes. By combining reinforcement learning with heuristic search, the system demonstrates improved performance in complex and evolving environments. Evaluation results include testing scores, precision, recall, and visualizations of evacuation routes.

### ScreenShot


<img src="https://github.com/Lemonnycodes/Fire-Evacuation-/blob/main/imgs/Picture1.jpg" />

<img src= "https://github.com/Lemonnycodes/Fire-Evacuation-/blob/main/imgs/Picture2.jpg"/>


