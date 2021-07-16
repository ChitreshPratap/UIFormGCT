import os
from enum import Enum

from PyQt5.QtWidgets import QFileDialog, QLineEdit, QPushButton

from src.customized_widgets.FilePathSelectionWidget import FilePathSelectionWidget
from src.utility import PathUtility


class PathType(Enum):
    FILE="file"
    DIR="dir"


class FilePathSelectionWidgetEx(FilePathSelectionWidget):

    def __init__(self,parent,pathType:PathType=PathType.FILE,dialogTitle:str="Choose File",fileType:str="Excel Files(*.xls *.xlsx)",defaultPath="Desktop"):
        super().__init__(parent)
        self.__pathType=pathType
        self.__dialogTitle=dialogTitle
        self.__fileType=fileType
        self.__defaultPath=os.path.expanduser('~/Desktop')
        self.btnBrowse.clicked.connect(self.browsePath)

    def getDialogTitle(self):
        dialog=self.__dialogTitle
        return dialog

    def getFileType(self):
        fileType=self.__fileType
        return fileType

    def getPathType(self)->PathType:
        pathType=self.__pathType
        return pathType

    def browsePath(self):
        selectedPath=self.lineEditPath.text()
        pathType=self.getPathType()
        if selectedPath.strip()!="":
            if pathType == PathType.DIR:
                defaultPath=selectedPath
            elif pathType == PathType.FILE:
                defaultPath=PathUtility.toPath(selectedPath).parent.__str__()
        else:
            defaultPath=self.__defaultPath

        dialogTitle=self.getDialogTitle()
        if pathType == PathType.DIR:
            path = QFileDialog.getExistingDirectory(self,dialogTitle,defaultPath)
            self.lineEditPath.setText(path)

        elif pathType == PathType.FILE :
            fileType = self.getFileType()
            fName=QFileDialog.getOpenFileName(self,dialogTitle,defaultPath,fileType)
            self.lineEditPath.setText(fName[0])

    def getPathWidget(self)->QLineEdit:
        pathWidget=self.lineEditPath
        return pathWidget

    def getBrowseWidget(self)->QPushButton:
        browseWidget=self.btnBrowse
        return browseWidget

    def clear(self):
        self.lineEditPath.setText("")

    def getPath(self)->str:
        path=self.lineEditPath.text()
        return path