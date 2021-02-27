from qt_regexp import *
import sys
from pathlib import Path
import os
import pandas as pd
import re
import numpy as np
from traceback import format_exception

tdir = Path(os.getcwd())
sdir = None

tbl: pd.DataFrame = None


def open_task(wnd: QtWidgets.QMainWindow):
    global tdir, tbl
    file, _ = QtWidgets.QFileDialog.getOpenFileName(wnd, 'Отрыть задание', tdir.as_posix(), 'Таблица (*.csv)')
    p = Path(file)
    if p.exists() and p.is_file():
        tdir = p.parent
        tbl = pd.read_csv(file)
        tbl = tbl.replace(np.nan, '', regex=True)
        wnd.setWindowTitle(p.name)


def update_regexp(ui: Ui_wnd_regexp):
    ui.lst_missed.clear()
    ui.lst_unwanted.clear()
    try:
        r = re.compile(ui.edt_regexp.text())
    except Exception as e:
        msg = format_exception(type(e), e, e.__traceback__)
        for l in msg:
            ui.lst_missed.addItem(l)
        return

    if tbl is None:
        return

    for s, m in tbl.values:
        if r.fullmatch(s) and 'no' == m:
            ui.lst_unwanted.addItem(repr(s))
        if (not r.fullmatch(s)) and 'yes' == m:
            ui.lst_missed.addItem(repr(s))

    if 0 == ui.lst_missed.count():
        ui.lst_missed.addItem('>>> Нет пропущенных строк')
    if 0 == ui.lst_unwanted.count():
        ui.lst_unwanted.addItem('>>> Нет лишних строк')


def copy_regexp(ui: Ui_wnd_regexp, wnd: QtWidgets.QMainWindow, app: QtWidgets.QApplication):
    clipboard = app.clipboard()
    clipboard.setText(ui.edt_regexp.text())
    event = QtCore.QEvent(QtCore.QEvent.Clipboard)
    app.sendEvent(clipboard, event)
    QtWidgets.QMessageBox.information(wnd, '', 'Выражение скопировано в буффер обмена!')


about_msg = """
Программа "qt_regexp"

Автор: Рогонов С.А.
Организация: ФГБОУ ВО ТвГУ
https://tversu.ru

2021 Тверской государственный университет ©
"""


def about(wnd: QtWidgets.QMainWindow):
    QtWidgets.QMessageBox.about(wnd, 'О программе', about_msg)


def save_regexp(ui: Ui_wnd_regexp, wnd: QtWidgets.QMainWindow):
    global sdir
    if sdir is None:
        sdir = tdir

    f = sdir / wnd.windowTitle()
    f = f.with_suffix('.regexp')
    file, _ = QtWidgets.QFileDialog.getSaveFileName(wnd, 'Выберите папку для схранения регекспа', f.as_posix(),
                                                    'Регексп (*.regexp)')
    if file:
        p = Path(file)
        sdir = p.parent
        p.write_text(ui.edt_regexp.text())


def setup_behaviour(ui: Ui_wnd_regexp, wnd: QtWidgets.QMainWindow, app: QtWidgets.QApplication) -> None:
    ui.act_quit.triggered.connect(quit)
    ui.act_open_csv.triggered.connect(lambda: open_task(wnd))
    ui.edt_regexp.textChanged.connect(lambda: update_regexp(ui))
    ui.btn_copy_regexp.clicked.connect(lambda: copy_regexp(ui, wnd, app))
    ui.act_about.triggered.connect(lambda: about(wnd))
    ui.act_save_regexp.triggered.connect(lambda: save_regexp(ui, wnd))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    wnd_regexp = QtWidgets.QMainWindow()
    ui = Ui_wnd_regexp()
    ui.setupUi(wnd_regexp)

    setup_behaviour(ui, wnd_regexp, app)

    wnd_regexp.show()
    sys.exit(app.exec_())
