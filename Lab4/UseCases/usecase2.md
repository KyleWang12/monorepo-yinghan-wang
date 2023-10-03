**TODO for your task:** Edit the Text in italics with your text.

<hr>

# Use Case 2

<hr>

**Use Case**: Color Selection

**Primary Actor**: User

**Goal in Context**: To change the color of the pencil to the desired color for drawing on the canvas.

**Preconditions**: The program is running and is in a responsive state.
The drawing canvas is active and ready to receive input.

**Trigger**: Pressing one of the number keys (1 through 8) on the keyboard.
  
**Scenario**: The user decides to change the color they're drawing with. Then the user presses a number key indicating a specific color. The system then changes the current drawing color to the selected color.
 
**Exceptions**: The user presses a key that is not in the range of 1 through 8. The color does not change, and there might be an optional visual or auditory cue indicating an invalid input.

**Priority**: High

**When available**: First release

**Channel to actor**: The primary actor communicates with the system through the keyboard. The system should respond within 1 second of the keyboard event.

**Secondary Actor**: N/A

**Channels to Secondary Actors**: N/A

**Open Issues**: It might be worth exploring the use of a color wheel or a more advanced color picker for more artistic flexibility.

<hr>



(adapted by Pressman and Maxim, Software Engineering: A Practitioner’s Approach, pp. 151-152, from Cockburn,
A., Writing Effective Use-Cases, Addison-Wesley, 2001)
