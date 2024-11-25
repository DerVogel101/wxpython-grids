import wx
import wx.grid as gridlib

class CustomGrid(gridlib.Grid):
    def __init__(self, parent):
        super().__init__(parent, -1)
        self.CreateGrid(5, 3)

        # Set cell values
        self.SetCellValue(0, 0, "True")
        self.SetCellValue(0, 1, "123.45")
        self.SetCellValue(0, 2, "Hello, wxPython!")

        self.SetCellValue(1, 0, "Option 2")
        self.SetCellValue(1, 1, "42")
        self.SetCellValue(1, 2, "Hello, world!")

        # Set renderers
        self.SetCellRenderer(0, 0, gridlib.GridCellBoolRenderer())
        self.SetCellRenderer(0, 1, gridlib.GridCellFloatRenderer())
        self.SetCellRenderer(0, 2, gridlib.GridCellStringRenderer())

        # Set editors
        self.SetCellEditor(0, 0, gridlib.GridCellBoolEditor())
        self.SetCellEditor(0, 1, gridlib.GridCellFloatEditor())
        self.SetCellEditor(0, 2, gridlib.GridCellTextEditor())

        self.SetCellEditor(1, 0, gridlib.GridCellChoiceEditor(["Option 1", "Option 2", "Option 3"]))
        self.SetCellEditor(1, 1, gridlib.GridCellNumberEditor(0, 1000))
        self.SetCellEditor(1, 2, gridlib.GridCellTextEditor())

        # Hide column -1 (row labels)
        self.SetRowLabelSize(0)

        # Hide column labels
        self.SetColLabelSize(0)

        # Bind events
        self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.on_cell_left_click)
        self.Bind(gridlib.EVT_GRID_CELL_CHANGING, self.on_cell_changing)

    def on_cell_left_click(self, event):
        row = event.GetRow()
        col = event.GetCol()
        wx.MessageBox(f"Cell ({row}, {col}) clicked", "Info", wx.OK | wx.ICON_INFORMATION)
        event.Skip()

    def on_cell_changing(self, event):
        row = event.GetRow()
        col = event.GetCol()
        new_value = event.GetString()
        wx.MessageBox(f"Cell ({row}, {col}) changing to {new_value}", "Info", wx.OK | wx.ICON_INFORMATION)
        event.Skip()

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, "Custom Grid Example", size=(600, 400))
        grid = CustomGrid(frame)
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()