Maze solver.<br>
<br>
In this exercise the objective i to solve the maze, <br>
and get to the red hangar.<br>
<br>
A number of algorithms might be useful here.<br>
E.g.<br>
<blockquote>Hand On Wall Rule, also known as either the left-hand rule or the right-hand rule. If the maze is simply connected, that is, all its walls are connected together or to the maze's outer boundary, then by keeping one hand in contact with one wall of the maze the solver is guaranteed not to get lost and will reach a different exit if there is one; otherwise, the algorithm will return to the entrance having traversed every corridor next to that connected section of walls at least once.
</blockquote>
For more see <a href="https://en.wikipedia.org/wiki/Maze-solving_algorithm" target="_blank">Maze solvers</a> (Wikipedia)<br>
<br>
Wall following (pseudo-code).<br>
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

 <img src="TinyMaze.jpg" alt="Epuck robot solving maze in Webot"> 
