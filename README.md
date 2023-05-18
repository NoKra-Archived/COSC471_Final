# COSC471 Final Project by Noel Kraus and Ian Smith

## Installation (Mac/Linux)

1. Clone this repository, either by downloading it, or using git clone.

2. Open a terminal and cd to the folder containing it.

3. Create venv:

``python3 -m venv /path/to/folder/COSC471_Final/.venv ``

4. Activate the venv:

``source /path/to/folder/COSC471_Final/.venv/bin/activate``

5. Install dependencies from requirements.txt:

``python -m pip install -r requirements.txt``

## Starting

Use this command on Mac/Linux to start the program from the terminal:

``/path/to/folder/COSC471_Final/.venv/bin/python /path/to/folder/COSC471_Final/main.py``

## Adding a new model to the simulator:

1. Download PrusaSlicer here:

https://www.prusa3d.com/page/prusaslicer_424/

2. Download the 3D print of your choice (should be an STL file)

3. Import file into PrusaSlicer, and slice WITHOUT INFILL.

4. Click "Export GCode" in the bottom right after slicing completes.

5. Save the file to the same folder this readme is in as "[insert name here].txt"

6. Replace "astro.txt" on line 21 in main.py with the name you saved the stl as in step 5.

7. Follow the starting instructions to print with the new model.

## Controls

### Application Controls:

**Quit:** Escape

### Camera Controls:

**Reset:** X


**X-axis rotation:** Left, Right


**Y-axis rotation:** Up, Down


**Pan Left:** A


**Pan Right:** D


**Pan Up:** W


**Pan Down**:S


**Pan Towards:** E


**Pan Away:** Q 

### Printer Controls: 


**Start Printing:** F


**Pause Print:** Z


**Increase Sim Speed:** J


**Decrease Sim Speed:** K

