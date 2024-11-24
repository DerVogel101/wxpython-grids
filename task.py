import wx
import wx.grid as gridlib
from main import GridFrame
import random

class TaskFrame(GridFrame):
    def __init__(self, parent):
        """
        Constructor
        This method initializes the inherited frame and its components.
        Important attributes:
        - `self.number_grid`: The grid object
        - `self.randomize_numbers`: The button to generate random numbers
        - `self.max_number_mark_button`: The button to mark the highest number
        The event handlers are already connected.
        """
        GridFrame.__init__(self, parent)
        self.set_float_renderer()
        self.set_float_editor()
        self.randomize_all_cells()

    def randomize_all_cells(self):
        """
        Generate random numbers for all cells in the grid and colorize them the same as in colorize_cell.
        """
        ...

    def set_float_renderer(self):
        """
        Set the renderer for all cells in the grid to display float values.
        """
        ...

    def set_float_editor(self):
        """
        Set the editor for all cells in the grid to edit float values.
        """
        ...

    def colorize_cell(self, event):
        """
        Event handler for cell change
        Change the background color of the cell when the value is changed, based on if the value is negative or positive.
        """
        row = event.GetRow()
        col = event.GetCol()
        self.colorize_cell_direct(row, col)
        event.Skip()

    def colorize_cell_direct(self, row, col):
        """
        Change the background color of the cell based on the value.
        """
        ...

    def set_random_numbers(self, event):
        """
        Event handler for random number generation
        This method is called when the 'Randomize Numbers' button is clicked.
        It will generate random numbers and set them to the grid.
        """
        ...
        event.Skip()

    def mark_highest(self, event):
        """
        This method is called when the 'Mark Highest Number' button is clicked.
        It will mark the highest number in the grid with a different background color.
        """
        ...
        event.Skip()

if __name__ == "__main__":
    app = wx.App(False)
    frame = TaskFrame(None)
    frame.Show(True)
    app.MainLoop()