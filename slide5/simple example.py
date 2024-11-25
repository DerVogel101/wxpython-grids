import wx
import wx.grid as gridlib

class ExampleFrame(wx.Frame):
    def __init__(self, parent, title):
        super(ExampleFrame, self).__init__(parent, title=title, size=(600, 400))

        self.grid = gridlib.Grid(self)
        self.grid.CreateGrid(5, 3)

        # Vorab gefüllte Daten
        self.data = [
            ["Alice", "Engineering", "A"],
            ["Bob", "Mathematics", "B"],
            ["Charlie", "Physics", "C"],
            ["David", "Chemistry", "B"],
            ["Eve", "Biology", "A"]
        ]

        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                self.grid.SetCellValue(row, col, self.data[row][col])

        # Spaltenüberschriften
        col_labels = ["Name", "Department", "Grade"]
        for col in range(len(col_labels)):
            self.grid.SetColLabelValue(col, col_labels[col])

        # Bearbeiten aktivieren
        self.grid.EnableEditing(True)

        # Sortieren aktivieren
        self.grid.Bind(gridlib.EVT_GRID_LABEL_LEFT_CLICK, self.on_sort)

        # Änderungen speichern aktivieren
        self.grid.Bind(gridlib.EVT_GRID_CELL_CHANGED, self.on_cell_change)

        # Layout
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def on_sort(self, event):
        col = event.GetCol()
        if col >= 0:
            self.sort_column(col)
        event.Skip()

    def sort_column(self, col):
        # Sortiere die gesamte Zeile basierend auf der ausgewählten Spalte
        self.data.sort(key=lambda row: row[col])

        # Aktualisiere das Grid mit den sortierten Daten
        for row in range(len(self.data)):
            for col in range(len(self.data[row])):
                self.grid.SetCellValue(row, col, self.data[row][col])

    def on_cell_change(self, event):
        row = event.GetRow()
        col = event.GetCol()
        self.data[row][col] = self.grid.GetCellValue(row, col)

if __name__ == "__main__":
    app = wx.App(False)
    frame = ExampleFrame(None, "Grid Example")
    frame.Show(True)
    app.MainLoop()