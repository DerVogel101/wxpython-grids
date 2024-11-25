import wx
import wx.grid as gridlib

class SimpleGrid(gridlib.Grid):
    def __init__(self, parent):
        super().__init__(parent, -1)

        # Erstellen eines Grids mit 5 Zeilen und 3 Spalten
        self.CreateGrid(5, 3)

        # Setzen von Zellenwerten
        data = [
            ["1", "Alice", "23"],
            ["2", "Bob", "30"],
            ["3", "Charlie", "28"],
            ["4", "David", "35"],
            ["5", "Eve", "40"]
        ]
        for row in range(5):
            for col in range(3):
                self.SetCellValue(row, col, data[row][col])

        # Setzen der Spaltenbeschriftungen
        colLabels = ["ID", "Name", "Age"]
        for col in range(3):
            self.SetColLabelValue(col, colLabels[col])

        # Bearbeitung der Zellen aktivieren/deaktivieren
        self.EnableEditing(True)

        # Hintergrundfarbe einer Zelle setzen
        self.SetCellBackgroundColour(2, 1, wx.Colour(255, 255, 0))  # Gelbe Zelle

        # Grid aktualisieren
        self.ForceRefresh()

class MyApp(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, -1, "Einfaches Grid Beispiel", size=(400, 300))
        grid = SimpleGrid(frame)
        frame.Show(True)
        return True

if __name__ == "__main__":
    app = MyApp(False)
    app.MainLoop()