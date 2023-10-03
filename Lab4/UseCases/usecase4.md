**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 4

<hr>

**Use Case**: Drawing

**Primary Actor**: User

**Goal in Context**: To draw on the canvas by changing pixel colors as the mouse is dragged.

**Preconditions**: The program is running and is in a responsive state.
The drawing canvas is active and ready to receive input.
The user has selected a color.

**Trigger**:  Pressing and holding the left mouse button while moving the mouse over the canvas.
  
**Scenario**: The user decides to draw on the canvas.
The user selects a color by pressing one of the number keys if they want a specific color.
The user presses and holds the left mouse button.
As the user drags the mouse across the canvas, the pixels underneath change to the selected color, mimicking the behavior of a pencil drawing on paper.
The user releases the mouse button when they finish drawing.
 
**Exceptions**: If the user tries to draw outside the boundaries of the canvas, the system should ensure no changes occur outside the canvas area.

**Priority**: High

**When available**: First release

**Channel to actor**: The primary actor communicates with the system using both the mouse for drawing and the keyboard for selecting colors. The system should respond immediately to mouse movements and clicks.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: May consider different types of pencil.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
