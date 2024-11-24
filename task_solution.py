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
        for row in range(self.number_grid.GetNumberRows()):
            for col in range(self.number_grid.GetNumberCols()):
                random_value = random.uniform(-100, 100)
                self.number_grid.SetCellValue(row, col, str(random_value))
                self.colorize_cell_direct(row, col)

    def set_float_renderer(self):
        """
        Set the renderer for all cells in the grid to display float values.
        """
        float_renderer = gridlib.GridCellFloatRenderer()
        for row in range(self.number_grid.GetNumberRows()):
            for col in range(self.number_grid.GetNumberCols()):
                self.number_grid.SetCellRenderer(row, col, float_renderer)

    def set_float_editor(self):
        """
        Set the editor for all cells in the grid to edit float values.
        """
        float_editor = gridlib.GridCellFloatEditor()
        for row in range(self.number_grid.GetNumberRows()):
            for col in range(self.number_grid.GetNumberCols()):
                self.number_grid.SetCellEditor(row, col, float_editor)

    def colorize_cell(self, event):
        row = event.GetRow()
        col = event.GetCol()
        self.colorize_cell_direct(row, col)
        event.Skip()

    def colorize_cell_direct(self, row, col):
        """
        Change the background color of the cell based on the value.
        """
        value = self.number_grid.GetCellValue(row, col)

        try:
            value = float(value)
            if value == 0:
                self.number_grid.SetCellBackgroundColour(row, col, wx.Colour(255, 255, 255))
            elif value < 0:
                self.number_grid.SetCellBackgroundColour(row, col, wx.Colour(255, 0, 0))  # Red for negative values
            else:
                self.number_grid.SetCellBackgroundColour(row, col, wx.Colour(0, 255, 0))  # Green for positive values
        except ValueError:
            self.number_grid.SetCellBackgroundColour(row, col, wx.Colour(255, 255, 255))  # White for non-numeric values

        self.number_grid.ForceRefresh()

    def set_random_numbers(self, event):
        """
        Event handler for random number generation
        This method is called when the 'Randomize Numbers' button is clicked.
        It will generate random numbers and set them to the grid.
        """
        self.randomize_all_cells()
        event.Skip()

    def mark_highest(self, event):
        """
        This method is called when the 'Mark Highest Number' button is clicked.
        It will mark the highest number in the grid with a different background color.
        """
        max_value = float('-inf')
        max_row, max_col = -1, -1

        for row in range(self.number_grid.GetNumberRows()):
            for col in range(self.number_grid.GetNumberCols()):
                try:
                    value = float(self.number_grid.GetCellValue(row, col))
                    if value > max_value:
                        max_value = value
                        max_row, max_col = row, col
                except ValueError:
                    continue

        if max_row != -1 and max_col != -1:
            self.number_grid.SetCellBackgroundColour(max_row, max_col, wx.Colour(0, 0, 255))  # Blue for the highest value
            self.number_grid.ForceRefresh()

        event.Skip()



if __name__ == "__main__":
    app = wx.App(False)
    frame = TaskFrame(None)
    frame.Show(True)
    app.MainLoop()