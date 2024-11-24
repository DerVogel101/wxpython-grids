import wx
import wx.grid as gridlib

class CustomTable(gridlib.GridTableBase):
    def __init__(self):
        super().__init__()
        self.data = [
            ["0", "1"],
            ["-1", "2"]
        ]
        self.col_labels = ["Column 0", "Column 1"]
        self.cell_background_colors = {}

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.col_labels)

    def IsEmptyCell(self, row, col):
        return self.data[row][col] == ""

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        self.data[row][col] = value
        try:
            if float(value) < 0:
                self.SetCellBackgroundColor(row, col, wx.Colour(255, 0, 0))  # Red
            else:
                self.SetCellBackgroundColor(row, col, wx.Colour(255, 255, 255))  # White
        except ValueError:
            self.SetCellBackgroundColor(row, col, wx.Colour(255, 255, 255))

    def GetColLabelValue(self, col):
        return self.col_labels[col]

    def SetCellBackgroundColor(self, row, col, color):
        self.cell_background_colors[(row, col)] = color

    def GetAttr(self, row, col, kind):
        attr = gridlib.GridCellAttr()
        if (row, col) in self.cell_background_colors:
            attr.SetBackgroundColour(self.cell_background_colors[(row, col)])
        return attr

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Custom GridTableBase Example")
        panel = wx.Panel(self)
        grid = gridlib.Grid(panel)
        table = CustomTable()
        grid.SetTable(table, True)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid, 1, wx.EXPAND)
        panel.SetSizer(sizer)
        self.SetSize((400, 300))

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame()
        frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()