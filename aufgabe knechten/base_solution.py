# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

import gettext
_ = gettext.gettext

###########################################################################
## Class GridFrame
###########################################################################

class GridFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Grid Numbers"), pos = wx.DefaultPosition, size = wx.Size( 740,391 ), style = wx.CAPTION|wx.FRAME_NO_TASKBAR|wx.MAXIMIZE_BOX|wx.STAY_ON_TOP|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 100,100 ), wx.DefaultSize )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

        box_sizer = wx.BoxSizer( wx.VERTICAL )

        self.number_grid = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

        # Grid
        self.number_grid.CreateGrid( 7, 7 )
        self.number_grid.EnableEditing( True )
        # self.number_grid.CreateGrid( 7, 2 )
        # self.number_grid.EnableEditing( False )
        self.number_grid.EnableGridLines( True )
        self.number_grid.EnableDragGridSize( False )
        self.number_grid.SetMargins( 0, 0 )

        # Columns
        self.number_grid.EnableDragColMove( False )
        self.number_grid.EnableDragColSize( True )
        self.number_grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.number_grid.AutoSizeRows()
        self.number_grid.EnableDragRowSize( True )
        self.number_grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.number_grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        box_sizer.Add( self.number_grid, 0, wx.ALL, 5 )

        self.randomize_numbers = wx.Button( self, wx.ID_ANY, _(u"Randomize Numbers"), wx.DefaultPosition, wx.DefaultSize, 0 )
        box_sizer.Add( self.randomize_numbers, 0, wx.ALL, 5 )

        self.max_number_mark_button = wx.Button( self, wx.ID_ANY, _(u"Mark Highest Number"), wx.DefaultPosition, wx.DefaultSize, 0 )
        box_sizer.Add( self.max_number_mark_button, 0, wx.ALL, 5 )


        self.SetSizer( box_sizer )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.number_grid.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.colorize_cell )
        # self.number_grid.Bind( wx.grid.EVT_GRID_CELL_CHANGED, self.set_random_numbers )
        self.randomize_numbers.Bind( wx.EVT_BUTTON, self.set_random_numbers )
        self.max_number_mark_button.Bind( wx.EVT_BUTTON, self.mark_highest )
        self.max_number_mark_button.Bind(wx.EVT_RIGHT_DOWN, self.mark_lowest)

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def colorize_cell( self, event ):
        event.Skip()

    def set_random_numbers( self, event ):
        event.Skip()

    def mark_highest( self, event ):
        event.Skip()

    def mark_lowest( self, event ):
        event.Skip()

if __name__ == "__main__":
    app = wx.App(False)
    frame = GridFrame(None)
    frame.Show(True)
    app.MainLoop()