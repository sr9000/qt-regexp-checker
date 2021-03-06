# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_regexp.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wnd_regexp(object):
    def setupUi(self, wnd_regexp):
        wnd_regexp.setObjectName("wnd_regexp")
        wnd_regexp.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(wnd_regexp)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.edt_regexp = QtWidgets.QLineEdit(self.frame)
        self.edt_regexp.setObjectName("edt_regexp")
        self.horizontalLayout.addWidget(self.edt_regexp)
        self.btn_copy_regexp = QtWidgets.QToolButton(self.frame)
        self.btn_copy_regexp.setObjectName("btn_copy_regexp")
        self.horizontalLayout.addWidget(self.btn_copy_regexp)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lst_missed = QtWidgets.QListWidget(self.widget)
        self.lst_missed.setEnabled(False)
        self.lst_missed.setObjectName("lst_missed")
        self.verticalLayout_2.addWidget(self.lst_missed)
        self.horizontalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.frame_2)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lst_unwanted = QtWidgets.QListWidget(self.widget_2)
        self.lst_unwanted.setEnabled(False)
        self.lst_unwanted.setObjectName("lst_unwanted")
        self.verticalLayout_3.addWidget(self.lst_unwanted)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout.addWidget(self.frame_2)
        wnd_regexp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(wnd_regexp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 27))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        wnd_regexp.setMenuBar(self.menubar)
        self.act_open_csv = QtWidgets.QAction(wnd_regexp)
        self.act_open_csv.setObjectName("act_open_csv")
        self.act_about = QtWidgets.QAction(wnd_regexp)
        self.act_about.setObjectName("act_about")
        self.act_quit = QtWidgets.QAction(wnd_regexp)
        self.act_quit.setObjectName("act_quit")
        self.act_save_regexp = QtWidgets.QAction(wnd_regexp)
        self.act_save_regexp.setObjectName("act_save_regexp")
        self.act_load_regexp = QtWidgets.QAction(wnd_regexp)
        self.act_load_regexp.setObjectName("act_load_regexp")
        self.menu_file.addAction(self.act_open_csv)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.act_save_regexp)
        self.menu_file.addAction(self.act_load_regexp)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.act_quit)
        self.menu_help.addAction(self.act_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(wnd_regexp)
        QtCore.QMetaObject.connectSlotsByName(wnd_regexp)

    def retranslateUi(self, wnd_regexp):
        _translate = QtCore.QCoreApplication.translate
        wnd_regexp.setWindowTitle(_translate("wnd_regexp", "MainWindow"))
        self.label_3.setText(_translate("wnd_regexp", "Регексп:"))
        self.btn_copy_regexp.setText(_translate("wnd_regexp", "📋"))
        self.label.setText(_translate("wnd_regexp", "Пропущенные строки"))
        self.label_2.setText(_translate("wnd_regexp", "Лишние строки"))
        self.menu_file.setTitle(_translate("wnd_regexp", "Файл"))
        self.menu_help.setTitle(_translate("wnd_regexp", "Помощь"))
        self.act_open_csv.setText(_translate("wnd_regexp", "Открыть задание"))
        self.act_about.setText(_translate("wnd_regexp", "О программе"))
        self.act_quit.setText(_translate("wnd_regexp", "Выйти"))
        self.act_save_regexp.setText(_translate("wnd_regexp", "Сохранить регексп"))
        self.act_load_regexp.setText(_translate("wnd_regexp", "Загрузить регексп"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    wnd_regexp = QtWidgets.QMainWindow()
    ui = Ui_wnd_regexp()
    ui.setupUi(wnd_regexp)
    wnd_regexp.show()
    sys.exit(app.exec_())
