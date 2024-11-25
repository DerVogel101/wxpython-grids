import wx
import wx.grid as gridlib

class MyGridTable(gridlib.GridTableBase):
    def __init__(self):
        super().__init__()
        self.data = [
            ["1", "Alice", "23"],
            ["2", "Bob", "30"],
            ["3", "Charlie", "28"],
            ["4", "David", "35"],
            ["5", "Eve", "40"]
        ]
        self.colLabels = ["ID", "Name", "Age"]

    def GetNumberRows(self):
        return len(self.data)

    def GetNumberCols(self):
        return len(self.colLabels)

    def IsEmptyCell(self, row, col):
        return not self.data[row][col]

    def GetValue(self, row, col):
        return self.data[row][col]

    def SetValue(self, row, col, value):
        self.data[row][col] = value

    def GetColLabelValue(self, col):
        return self.colLabels[col]


class CustomGrid(gridlib.Grid):
    def __init__(self, parent):
        super().__init__(parent, -1)
        table = MyGridTable()
        self.SetTable(table, takeOwnership=True)

        # Spalten- und Zeilenbeschriftungen verstecken
        self.SetColLabelSize(0)  # Versteckt die Spaltenbeschriftungen
        self.SetColSize(0, 0)  # Versteckt die ID-Spalte (erste Spalte)

        # Renderer setzen
        self.SetCellRenderer(0, 1, gridlib.GridCellStringRenderer())
        self.SetCellRenderer(0, 2, gridlib.GridCellNumberRenderer())

        # Editor setzen
        self.SetCellEditor(1, 1, gridlib.GridCellTextEditor())
        self.SetCellEditor(1, 2, gridlib.GridCellNumberEditor())

        # Event-Handler setzen
        self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.onCellLeftClick)
        self.Bind(gridlib.EVT_GRID_CELL_CHANGING, self.onCellChanging)

    def onCellLeftClick(self, event):
        row = event.GetRow()
        col = event.GetCol()
        value = self.GetTable().GetValue(row, col)
        print(f"Zelle angeklickt - Zeile: {row}, Spalte: {col}, Wert: {value}")
        event.Skip()

    def onCellChanging(self, event):
        row = event.GetRow()
        col = event.GetCol()
        old_value = self.GetTable().GetValue(row, col)
        new_value = event.GetString()
        print(f"Zelle ändert sich - Zeile: {row}, Spalte: {col}, Alter Wert: {old_value}, Neuer Wert: {new_value}")
        event.Skip()


class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, "Grid und GridTableBase Beispiel", size=(600, 400))
        grid = CustomGrid(frame)
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()
