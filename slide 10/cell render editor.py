import wx
import wx.grid as gridlib

class RendererEditorGrid(gridlib.Grid):
    def __init__(self, parent):
        super().__init__(parent, -1)
        self.CreateGrid(2, 3)  # 5 Zeilen, 4 Spalten

        # Daten setzen
        self.SetCellValue(0, 0, "True")
        self.SetCellValue(0, 1, "123.45")
        self.SetCellValue(0, 2, "Hello, wxPython!")

        self.SetCellValue(1, 0, "Option 2")
        self.SetCellValue(1, 1, "42")
        self.SetCellValue(1, 2, "Hello, world!")

        # Renderer setzen
        self.SetCellRenderer(0, 0, gridlib.GridCellBoolRenderer())
        self.SetCellRenderer(0, 1, gridlib.GridCellFloatRenderer())
        self.SetCellRenderer(0, 2, gridlib.GridCellStringRenderer())

        self.SetCellEditor(0, 0, gridlib.GridCellBoolEditor())
        self.SetCellEditor(0, 1, gridlib.GridCellFloatEditor())
        self.SetCellEditor(0, 2, gridlib.GridCellTextEditor())

        # Editor setzen
        self.SetCellEditor(1, 0, gridlib.GridCellChoiceEditor(["Option 1", "Option 2", "Option 3"]))
        self.SetCellEditor(1, 1, gridlib.GridCellNumberEditor(0, 1000))
        self.SetCellEditor(1, 2, gridlib.GridCellTextEditor())

        self.SetCellRenderer(1, 0, gridlib.GridCellStringRenderer())
        self.SetCellRenderer(1, 1, gridlib.GridCellNumberRenderer())
        self.SetCellRenderer(1, 2, gridlib.GridCellStringRenderer())

        # Labels setzen
        colLabels = ["Boolean", "Float", "String"]
        for col in range(3):
            self.SetColLabelValue(col, colLabels[col])

        # Gitter-Updates erzwingen
        self.ForceRefresh()

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, "Renderer und Editor Beispiel", size=(600, 400))
        grid = RendererEditorGrid(frame)
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
