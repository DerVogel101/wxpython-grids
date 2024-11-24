import wx
import wx.grid as gridlib

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="wx.Grid with Float Editor Example")
        panel = wx.Panel(self)
        grid = gridlib.Grid(panel)
        grid.CreateGrid(5, 5)

        # Set the float editor for all cells
        for row in range(5):
            for col in range(5):
                grid.SetCellEditor(row, col, gridlib.GridCellFloatEditor())

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