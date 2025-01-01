Maze solver.<br>
<br>
In this exercise the objective is to get out of, solve, the maze, <br>
and get to the red hangar.<br>
<br>
A number of algorithms might be useful here.<br>
E.g.<br>
<blockquote><i><b>Hand On Wall Rule</b></i>, also known as either the left-hand rule or the right-hand rule. If the maze is simply connected, that is, all its walls are connected together or to the maze's outer boundary, then by keeping one hand in contact with one wall of the maze the solver is guaranteed not to get lost and will reach a different exit if there is one; otherwise, the algorithm will return to the entrance having traversed every corridor next to that connected section of walls at least once.
</blockquote>
For more, see <a href="https://en.wikipedia.org/wiki/Maze-solving_algorithm" target="_blank">Maze solvers</a> (Wikipedia).<br>
<br>
''<i><b>Wall following</b></i>'' (pseudo-code).<br>
<blockquote>
Here is the wall follower algorithm(the left-hand one) at a high level:<br>
<br>
If left is free:<br>
&nbsp; &nbsp; Turn Left<br>
Else if left is occupied and straight is free:<br>
&nbsp; &nbsp; Go Straight<br>
Else if left and straight are occupied:<br>
&nbsp; &nbsp; Turn Right <br>
Else if left/right/straight are occupied or you crashed:  
&nbsp; &nbsp; Turn 180 degrees<br>
</blockquote>
Template code (E-puck, Webot):<br>
<a href="Wall_Following.py">Wall Following</a> (template Python code).<br>
<br>
<br>
''<i><b>Bug algorithm</b></i>'' (pseudo-code).<br>
<blockquote>
 While many planning algorithms assume global knowledge, <br>
 <i><b>bug</b></i> algorithms assume only local knowledge of the environment<br>
 and a global goal position. Bug behaviors are simple:<br>
<br>
 · Follow a wall (right or left)<br>
<br>
· Move in a straight line toward goal<br>
</blockquote>
Template code (E-puck, Webot):<br>
<a href="Bug0.py">Bug0.<br>
<br>
<br>

 <img src="TinyMaze.jpg" alt="Epuck robot solving maze in Webot"> 
