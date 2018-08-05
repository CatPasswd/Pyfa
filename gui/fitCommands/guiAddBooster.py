import wx
from service.fit import Fit

import gui.mainFrame
from gui import globalEvents as GE
from .calc.fitAddBooster import FitAddBoosterCommand

class GuiAddBoosterCommand(wx.Command):
    def __init__(self, fitID, itemID):
        wx.Command.__init__(self, True, "Booster Add")
        self.mainFrame = gui.mainFrame.MainFrame.getInstance()
        self.sFit = Fit.getInstance()
        self.internal_history = wx.CommandProcessor()
        self.fitID = fitID
        # can set his up no to not have to set variables on our object
        self.cmd = FitAddBoosterCommand(fitID, itemID)

    def Do(self):
        if self.internal_history.Submit(self.cmd):
            self.sFit.recalc(self.fitID)
            wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=self.fitID))
            return True
        return False

    def Undo(self):
        for x in self.internal_history.Commands:
            self.internal_history.Undo()
        self.sFit.recalc(self.fitID)
        wx.PostEvent(self.mainFrame, GE.FitChanged(fitID=self.fitID))
        return True

