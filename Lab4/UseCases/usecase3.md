**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 3

<hr>

**Use Case**: Canvas Clearing

**Primary Actor**: User

**Goal in Context**: To clear the entire canvas and fill it with the last selected color.

**Preconditions**: The program is running and is in a responsive state.
The drawing canvas is active and ready to receive input.
The user has selected a color (default or any of the available colors).

**Trigger**: Pressing the space key on the keyboard.
  
**Scenario**: The user decides to clear the current drawings and start afresh.
The user presses the space key.
The system clears all the drawings from the canvas.
The system fills the entire canvas with the last color selected by the user.
 
**Exceptions**: If the program becomes unresponsive, the user may need to restart the program or address the root cause of the unresponsiveness.

**Priority**: High

**When available**: First release

**Channel to actor**: The primary actor communicates with the system through the keyboard. The system should respond within 1 second of the keyboard event.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: May consider layer management or history tracking.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
