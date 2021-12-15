import UniversityBackend
from WorkNotepad import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import HistoryBackend
import MainBackend
import TableBackend
from datetime import date
import smtplib
import _thread
import requests
import time
import pyperclip


Email = ""
Password = ""


class Table(QMainWindow):
    handle_menu = "close"
    handle_info = "close"
    handle_background = "close"
    fileAddressPhoto_add = ""
    fileAddressPhoto_show = ""
    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]
    day_28 = 2
    title_email = False
    name_email = False
    massage_email = False
    connectionState = False
    year_show = False
    month_show = False
    day_show = False
    frameNum_home = ""
    stateEditShow = "Disable"
    iconAddBtnUni = ""
    frameNum_uni = ""
    stateEditUni = "Disable"
    btn_starFill_UniAdd = False
    btn_starOut_UniAdd = False
    btn_starCircle_UniAdd = False
    btn_heart_UniAdd = False
    btn_circle_UniAdd = False
    btn_done_UniAdd = False
    btn_sad_UniAdd = False
    btn_smile_UniAdd = False
    iconInfoBtnUni = ""
    btn_starFill_UniInfo = False
    btn_starOut_UniInfo = False
    btn_starCircle_UniInfo = False
    btn_heart_UniInfo = False
    btn_circle_UniInfo = False
    btn_done_UniInfo = False
    btn_sad_UniInfo = False
    btn_smile_UniInfo = False
    frameNum_table = ""
    iconAddBtnTable = ""
    btn_starFill_tableAdd = False
    btn_starOut_tableAdd = False
    btn_starCircle_tableAdd = False
    btn_heart_tableAdd = False
    btn_circle_tableAdd = False
    btn_done_tableAdd = False
    btn_sad_tableAdd = False
    btn_smile_tableAdd = False
    iconInfoBtnTable = ""
    btn_starFill_tableInfo = False
    btn_starOut_tableInfo = False
    btn_starCircle_tableInfo = False
    btn_heart_tableInfo = False
    btn_circle_tableInfo = False
    btn_done_tableInfo = False
    btn_sad_tableInfo = False
    btn_smile_tableInfo = False
    stateEditTable = "Disable"
    stateLockBtn = "Disable"

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Work Notepad")
        self.setWindowIcon(QIcon(r"photo\1.jpg"))
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.hideObjects_disable()
        self.function_connection()
        self.refresh_add_func()

    def function_connection(self):
        self.ui.menu_btn.clicked.connect(self.menu_func)
        self.ui.add_btn.clicked.connect(self.addEvent_func)
        self.ui.setting_btn.clicked.connect(self.setting_func)
        self.ui.home_btn.clicked.connect(self.home_func)
        self.ui.table_btn.clicked.connect(self.table_func)
        self.ui.university_btn.clicked.connect(self.university_func)
        self.ui.frame_btn_home_1.clicked.connect(self.frame_1_home)
        self.ui.frame_btn_home_2.clicked.connect(self.frame_2_home)
        self.ui.frame_btn_home_3.clicked.connect(self.frame_3_home)
        self.ui.frame_btn_home_4.clicked.connect(self.frame_4_home)
        self.ui.frame_btn_home_5.clicked.connect(self.frame_5_home)
        self.ui.frame_btn_home_6.clicked.connect(self.frame_6_home)
        self.ui.frame_btn_home_7.clicked.connect(self.frame_7_home)
        self.ui.frame_btn_home_8.clicked.connect(self.frame_8_home)
        self.ui.frame_btn_home_9.clicked.connect(self.frame_9_home)
        self.ui.frame_btn_home_10.clicked.connect(self.frame_10_home)
        self.ui.frame_btn_home_11.clicked.connect(self.frame_11_home)
        self.ui.frame_btn_home_12.clicked.connect(self.frame_12_home)
        self.ui.back_btn_show.clicked.connect(self.home_func)
        self.ui.edit_btn_show.clicked.connect(self.edit_btn_show)
        self.ui.delete_btn_show.clicked.connect(self.delete_btn_home)
        self.ui.year_lineEdit_show.textChanged.connect(
            self.textChanged_year_show)
        self.ui.month_lineEdit_show.textChanged.connect(
            self.textChanged_month_show)
        self.ui.day_lineEdit_show.textChanged.connect(
            self.textChanged_day_show)
        self.ui.submit_btn_show.clicked.connect(self.submit_btn_show)
        self.ui.choose_photo_btn_show.clicked.connect(
            self.browse_fileAddress_photo_show)
        self.ui.clear_btn_uni_add.clicked.connect(self.clearAddUniversity)
        self.ui.icon_done_btn_uni_add.clicked.connect(
            self.doneBtnAddUniversity)
        self.ui.icon_heart_btn_uni_add.clicked.connect(
            self.heartBtnAddUniversity)
        self.ui.icon_circle_btn_uni_add.clicked.connect(
            self.circleBtnAddUniversity)
        self.ui.icon_circleStar_btn_uni_add.clicked.connect(
            self.starCircleBtnAddUniversity)
        self.ui.icon_starOut_btn_uni_add.clicked.connect(
            self.starOutBtnAddUniversity)
        self.ui.icon_sadEmoji_btn_uni_add.clicked.connect(
            self.sadBtnAddUniversity)
        self.ui.icon_smileEmoji_btn_uni_add.clicked.connect(
            self.smileBtnAddUniversity)
        self.ui.icon_starFill_btn_uni_add.clicked.connect(
            self.starFillBtnAddUniversity)
        self.ui.submit_btn_uni_add.clicked.connect(
            self.submitUniversityAddEvent)
        self.ui.uni_btn_1.clicked.connect(self.university_table_frame_1)
        self.ui.uni_btn_2.clicked.connect(self.university_table_frame_2)
        self.ui.uni_btn_3.clicked.connect(self.university_table_frame_3)
        self.ui.uni_btn_4.clicked.connect(self.university_table_frame_4)
        self.ui.uni_btn_5.clicked.connect(self.university_table_frame_5)
        self.ui.uni_btn_6.clicked.connect(self.university_table_frame_6)
        self.ui.uni_btn_7.clicked.connect(self.university_table_frame_7)
        self.ui.uni_btn_8.clicked.connect(self.university_table_frame_8)
        self.ui.uni_btn_9.clicked.connect(self.university_table_frame_9)
        self.ui.uni_btn_10.clicked.connect(self.university_table_frame_10)
        self.ui.uni_btn_11.clicked.connect(self.university_table_frame_11)
        self.ui.uni_btn_12.clicked.connect(self.university_table_frame_12)
        self.ui.uni_btn_13.clicked.connect(self.university_table_frame_13)
        self.ui.uni_btn_14.clicked.connect(self.university_table_frame_14)
        self.ui.uni_btn_15.clicked.connect(self.university_table_frame_15)
        self.ui.uni_btn_16.clicked.connect(self.university_table_frame_16)
        self.ui.uni_btn_17.clicked.connect(self.university_table_frame_17)
        self.ui.uni_btn_18.clicked.connect(self.university_table_frame_18)
        self.ui.uni_btn_19.clicked.connect(self.university_table_frame_19)
        self.ui.uni_btn_20.clicked.connect(self.university_table_frame_20)
        self.ui.uni_btn_21.clicked.connect(self.university_table_frame_21)
        self.ui.uni_btn_22.clicked.connect(self.university_table_frame_22)
        self.ui.uni_btn_23.clicked.connect(self.university_table_frame_23)
        self.ui.uni_btn_24.clicked.connect(self.university_table_frame_24)
        self.ui.uni_btn_25.clicked.connect(self.university_table_frame_25)
        self.ui.uni_btn_26.clicked.connect(self.university_table_frame_26)
        self.ui.uni_btn_27.clicked.connect(self.university_table_frame_27)
        self.ui.uni_btn_28.clicked.connect(self.university_table_frame_28)
        self.ui.uni_btn_29.clicked.connect(self.university_table_frame_29)
        self.ui.uni_btn_30.clicked.connect(self.university_table_frame_30)
        self.ui.uni_btn_31.clicked.connect(self.university_table_frame_31)
        self.ui.uni_btn_32.clicked.connect(self.university_table_frame_32)
        self.ui.uni_btn_33.clicked.connect(self.university_table_frame_33)
        self.ui.uni_btn_34.clicked.connect(self.university_table_frame_34)
        self.ui.uni_btn_35.clicked.connect(self.university_table_frame_35)
        self.ui.uni_btn_36.clicked.connect(self.university_table_frame_36)
        self.ui.uni_btn_37.clicked.connect(self.university_table_frame_37)
        self.ui.uni_btn_38.clicked.connect(self.university_table_frame_38)
        self.ui.uni_btn_39.clicked.connect(self.university_table_frame_39)
        self.ui.uni_btn_40.clicked.connect(self.university_table_frame_40)
        self.ui.uni_btn_41.clicked.connect(self.university_table_frame_41)
        self.ui.uni_btn_42.clicked.connect(self.university_table_frame_42)
        self.ui.uni_btn_43.clicked.connect(self.university_table_frame_43)
        self.ui.uni_btn_44.clicked.connect(self.university_table_frame_44)
        self.ui.uni_btn_45.clicked.connect(self.university_table_frame_45)
        self.ui.uni_btn_46.clicked.connect(self.university_table_frame_46)
        self.ui.uni_btn_47.clicked.connect(self.university_table_frame_47)
        self.ui.uni_btn_48.clicked.connect(self.university_table_frame_48)
        self.ui.uni_btn_49.clicked.connect(self.university_table_frame_49)
        self.ui.uni_btn_50.clicked.connect(self.university_table_frame_50)
        self.ui.uni_btn_51.clicked.connect(self.university_table_frame_51)
        self.ui.uni_btn_52.clicked.connect(self.university_table_frame_52)
        self.ui.uni_btn_53.clicked.connect(self.university_table_frame_53)
        self.ui.uni_btn_54.clicked.connect(self.university_table_frame_54)
        self.ui.uni_btn_55.clicked.connect(self.university_table_frame_55)
        self.ui.uni_btn_56.clicked.connect(self.university_table_frame_56)
        self.ui.uni_btn_57.clicked.connect(self.university_table_frame_57)
        self.ui.uni_btn_58.clicked.connect(self.university_table_frame_58)
        self.ui.uni_btn_59.clicked.connect(self.university_table_frame_59)
        self.ui.uni_btn_60.clicked.connect(self.university_table_frame_60)
        self.ui.uni_btn_61.clicked.connect(self.university_table_frame_61)
        self.ui.uni_btn_62.clicked.connect(self.university_table_frame_62)
        self.ui.uni_btn_63.clicked.connect(self.university_table_frame_63)
        self.ui.back_btn_uni_add.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.University))
        self.ui.back_btn_uni_info.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.University))
        self.ui.delete_btn_uni.clicked.connect(self.deleteEventUniversity)
        self.ui.edit_btn_uni.clicked.connect(self.editEventUniversity)
        self.ui.icon_done_btn.clicked.connect(self.doneBtnInfoUniversity)
        self.ui.icon_heart_btn.clicked.connect(self.heartBtnInfoUniversity)
        self.ui.icon_circle_btn.clicked.connect(self.circleBtnInfoUniversity)
        self.ui.icon_smileEmoji_btn.clicked.connect(
            self.smileBtnInfoUniversity)
        self.ui.icon_sadEmoji_btn.clicked.connect(self.sadBtnInfoUniversity)
        self.ui.icon_starFill_btn.clicked.connect(
            self.starFillBtnInfoUniversity)
        self.ui.icon_starOut_btn.clicked.connect(self.starOutBtnInfoUniversity)
        self.ui.icon_circleStar_btn.clicked.connect(
            self.starCircleBtnInfoUniversity)
        self.ui.clear_btn_uni.clicked.connect(self.clearInfoUniversity)
        self.ui.submit_btn_uni.clicked.connect(self.submitUniversityInfoEvent)
        self.ui.copy_btn_uni.clicked.connect(self.copyLinkInfoUniversity)
        self.ui.table_btn_1.clicked.connect(self.table_frame_1)
        self.ui.table_btn_2.clicked.connect(self.table_frame_2)
        self.ui.table_btn_3.clicked.connect(self.table_frame_3)
        self.ui.table_btn_4.clicked.connect(self.table_frame_4)
        self.ui.table_btn_5.clicked.connect(self.table_frame_5)
        self.ui.table_btn_6.clicked.connect(self.table_frame_6)
        self.ui.table_btn_7.clicked.connect(self.table_frame_7)
        self.ui.table_btn_8.clicked.connect(self.table_frame_8)
        self.ui.table_btn_9.clicked.connect(self.table_frame_9)
        self.ui.table_btn_10.clicked.connect(self.table_frame_10)
        self.ui.table_btn_11.clicked.connect(self.table_frame_11)
        self.ui.table_btn_12.clicked.connect(self.table_frame_12)
        self.ui.table_btn_13.clicked.connect(self.table_frame_13)
        self.ui.table_btn_14.clicked.connect(self.table_frame_14)
        self.ui.table_btn_15.clicked.connect(self.table_frame_15)
        self.ui.table_btn_16.clicked.connect(self.table_frame_16)
        self.ui.table_btn_17.clicked.connect(self.table_frame_17)
        self.ui.table_btn_18.clicked.connect(self.table_frame_18)
        self.ui.table_btn_19.clicked.connect(self.table_frame_19)
        self.ui.table_btn_20.clicked.connect(self.table_frame_20)
        self.ui.table_btn_21.clicked.connect(self.table_frame_21)
        self.ui.table_btn_22.clicked.connect(self.table_frame_22)
        self.ui.table_btn_23.clicked.connect(self.table_frame_23)
        self.ui.table_btn_24.clicked.connect(self.table_frame_24)
        self.ui.table_btn_25.clicked.connect(self.table_frame_25)
        self.ui.table_btn_26.clicked.connect(self.table_frame_26)
        self.ui.table_btn_27.clicked.connect(self.table_frame_27)
        self.ui.table_btn_28.clicked.connect(self.table_frame_28)
        self.ui.table_btn_29.clicked.connect(self.table_frame_29)
        self.ui.table_btn_30.clicked.connect(self.table_frame_30)
        self.ui.table_btn_31.clicked.connect(self.table_frame_31)
        self.ui.table_btn_32.clicked.connect(self.table_frame_32)
        self.ui.table_btn_33.clicked.connect(self.table_frame_33)
        self.ui.table_btn_34.clicked.connect(self.table_frame_34)
        self.ui.table_btn_35.clicked.connect(self.table_frame_35)
        self.ui.table_btn_36.clicked.connect(self.table_frame_36)
        self.ui.table_btn_37.clicked.connect(self.table_frame_37)
        self.ui.table_btn_38.clicked.connect(self.table_frame_38)
        self.ui.table_btn_39.clicked.connect(self.table_frame_39)
        self.ui.table_btn_40.clicked.connect(self.table_frame_40)
        self.ui.table_btn_41.clicked.connect(self.table_frame_41)
        self.ui.table_btn_42.clicked.connect(self.table_frame_42)
        self.ui.table_btn_43.clicked.connect(self.table_frame_43)
        self.ui.table_btn_44.clicked.connect(self.table_frame_44)
        self.ui.table_btn_45.clicked.connect(self.table_frame_45)
        self.ui.table_btn_46.clicked.connect(self.table_frame_46)
        self.ui.table_btn_47.clicked.connect(self.table_frame_47)
        self.ui.table_btn_48.clicked.connect(self.table_frame_48)
        self.ui.table_btn_49.clicked.connect(self.table_frame_49)
        self.ui.table_btn_50.clicked.connect(self.table_frame_50)
        self.ui.table_btn_51.clicked.connect(self.table_frame_51)
        self.ui.table_btn_52.clicked.connect(self.table_frame_52)
        self.ui.table_btn_53.clicked.connect(self.table_frame_53)
        self.ui.table_btn_54.clicked.connect(self.table_frame_54)
        self.ui.table_btn_55.clicked.connect(self.table_frame_55)
        self.ui.table_btn_56.clicked.connect(self.table_frame_56)
        self.ui.table_btn_57.clicked.connect(self.table_frame_57)
        self.ui.table_btn_58.clicked.connect(self.table_frame_58)
        self.ui.table_btn_59.clicked.connect(self.table_frame_59)
        self.ui.table_btn_60.clicked.connect(self.table_frame_60)
        self.ui.table_btn_61.clicked.connect(self.table_frame_61)
        self.ui.table_btn_62.clicked.connect(self.table_frame_62)
        self.ui.table_btn_63.clicked.connect(self.table_frame_63)
        self.ui.submit_btn_table_add.clicked.connect(self.submitTableAddEvent)
        self.ui.icon_smileEmoji_btn_table_add.clicked.connect(
            self.smileBtnAddTable)
        self.ui.icon_sadEmoji_btn_table_add.clicked.connect(
            self.sadBtnAddTable)
        self.ui.icon_circle_btn_table_add.clicked.connect(
            self.circleBtnAddTable)
        self.ui.icon_circleStar_btn_table_add.clicked.connect(
            self.starCircleBtnAddTable)
        self.ui.icon_starFill_btn_table_add.clicked.connect(
            self.starFillBtnAddTable)
        self.ui.icon_starOut_btn_table_add.clicked.connect(
            self.starOutBtnAddTable)
        self.ui.icon_done_btn_table_add.clicked.connect(self.doneBtnAddTable)
        self.ui.icon_heart_btn_table_add.clicked.connect(self.heartBtnAddTable)
        self.ui.clear_btn_table_add.clicked.connect(self.clearAddTable)
        self.ui.delete_btn_table_info.clicked.connect(self.deleteEventTable)
        self.ui.icon_done_table_info.clicked.connect(self.doneBtnInfoTable)
        self.ui.icon_heart_table_info.clicked.connect(self.heartBtnInfoTable)
        self.ui.icon_smileEmoji_table_info.clicked.connect(
            self.smileBtnInfoTable)
        self.ui.icon_sadEmoji_table_info.clicked.connect(self.sadBtnInfoTable)
        self.ui.icon_circle_table_info.clicked.connect(self.circleBtnInfoTable)
        self.ui.icon_circleStar_table_info.clicked.connect(
            self.starCircleBtnInfoTable)
        self.ui.icon_starOut_table_info.clicked.connect(
            self.starOutBtnInfoTable)
        self.ui.icon_starFill_table_info.clicked.connect(
            self.starFillBtnInfoTable)
        self.ui.edit_btn_table_info.clicked.connect(self.editEventTable)
        self.ui.submit_btn_table_info.clicked.connect(
            self.submitEditEventTable)
        self.ui.clear_btn_table_info.clicked.connect(self.clearInfoTable)
        self.ui.back_btn_table_add.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Table))
        self.ui.back_btn_table_info.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Table))
        self.ui.lock_btn.clicked.connect(self.lockBtnHome)

    def mousePressEvent(self, evt):
        self.oldPos = evt.globalPos()

    def mouseMoveEvent(self, evt):
        delta = QPoint(evt.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = evt.globalPos()

    def hideObjects_disable(self):
        self.ui.frame_home_1.hide()
        self.ui.frame_home_2.hide()
        self.ui.frame_home_3.hide()
        self.ui.frame_home_4.hide()
        self.ui.frame_home_5.hide()
        self.ui.frame_home_6.hide()
        self.ui.frame_home_7.hide()
        self.ui.frame_home_8.hide()
        self.ui.frame_home_9.hide()
        self.ui.frame_home_10.hide()
        self.ui.frame_home_11.hide()
        self.ui.frame_home_12.hide()
        self.ui.btn_frame.hide()
        self.ui.info_frame.hide()
        self.ui.background_frame.hide()
        self.ui.send_label.hide()
        self.ui.frameNum_label.hide()
        self.ui.send_email.setEnabled(False)
        self.ui.search_btn_history.setEnabled(False)
        self.ui.delete_btn_history.setEnabled(False)
        self.ui.submit_btn_show.setEnabled(False)
        self.ui.choose_photo_btn_show.setEnabled(False)
        self.ui.title_lineEdit_show.setReadOnly(True)
        self.ui.textEdit_show.setReadOnly(True)
        self.ui.year_lineEdit_show.setReadOnly(True)
        self.ui.month_lineEdit_show.setReadOnly(True)
        self.ui.day_lineEdit_show.setReadOnly(True)
        self.ui.dayName_lineEdit_show.setReadOnly(True)

    def showError(self, title, msg):
        info = QMessageBox(self)
        info.setIcon(QMessageBox.Critical)
        info.setText(msg)
        info.setWindowTitle(title)
        info.show()

    def showInfo(self, title, message):
        info = QMessageBox(self)
        info.setText(message)
        info.setWindowTitle(title)
        info.setIcon(QMessageBox.Information)
        info.show()

    def menu_func(self):
        if self.handle_menu == "close":
            self.ui.btn_frame.show()
            icon = QIcon()
            icon.addPixmap(
                QPixmap("photo/outline_menu_open_black_24dp.png"), QIcon.Normal, QIcon.Off)
            self.ui.menu_btn.setIcon(icon)
            self.Anim_frame(self.ui.btn_frame, 70, 0, 601, 51, True)
            self.handle_menu = "open"
        elif self.handle_menu == "open":
            icon = QIcon()
            icon.addPixmap(
                QPixmap("photo/outline_menu_black_24dp.png"), QIcon.Normal, QIcon.Off)
            self.ui.menu_btn.setIcon(icon)
            self.Anim_frame(self.ui.btn_frame, 70, 0, 601, 51, False)
            self.handle_menu = "close"

    def Anim_frame(self, frame, x, y, width, height, openState):
        if openState:
            self.anim = QPropertyAnimation(frame, b"geometry")
            self.anim.setDuration(500)
            self.anim.setStartValue(QRect(x, y, 0, height))
            self.anim.setEndValue(QRect(x, y, width, height))
            self.anim.start()
        else:
            self.anim = QPropertyAnimation(frame, b"geometry")
            self.anim.setDuration(500)
            self.anim.setStartValue(QRect(x, y, width, height))
            self.anim.setEndValue(QRect(x, y, 0, height))
            self.anim.start()

    def home_func(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)
        self.refresh_add_func()

    @staticmethod
    def check_frames():
        frameState_1 = MainBackend.search_frame("1")
        frameState_2 = MainBackend.search_frame("2")
        frameState_3 = MainBackend.search_frame("3")
        frameState_4 = MainBackend.search_frame("4")
        frameState_5 = MainBackend.search_frame("5")
        frameState_6 = MainBackend.search_frame("6")
        frameState_7 = MainBackend.search_frame("7")
        frameState_8 = MainBackend.search_frame("8")
        frameState_9 = MainBackend.search_frame("9")
        frameState_10 = MainBackend.search_frame("10")
        frameState_11 = MainBackend.search_frame("11")
        frameState_12 = MainBackend.search_frame("12")
        if len(frameState_1) == 0:
            return "1"
        elif len(frameState_2) == 0:
            return "2"
        elif len(frameState_3) == 0:
            return "3"
        elif len(frameState_4) == 0:
            return "4"
        elif len(frameState_5) == 0:
            return "5"
        elif len(frameState_6) == 0:
            return "6"
        elif len(frameState_7) == 0:
            return "7"
        elif len(frameState_8) == 0:
            return "8"
        elif len(frameState_9) == 0:
            return "9"
        elif len(frameState_10) == 0:
            return "10"
        elif len(frameState_11) == 0:
            return "11"
        elif len(frameState_12) == 0:
            return "12"

    def setTooltipDays(self, frame, inputDays):
        _translate = QCoreApplication.translate
        if inputDays < 0:
            if frame == "1":
                self.ui.day_frameH_1.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "2":
                self.ui.day_frameH_2.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "3":
                self.ui.day_frameH_3.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "4":
                self.ui.day_frameH_4.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "5":
                self.ui.day_frameH_5.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "6":
                self.ui.day_frameH_6.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "7":
                self.ui.day_frameH_7.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "8":
                self.ui.day_frameH_8.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "9":
                self.ui.day_frameH_9.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "10":
                self.ui.day_frameH_10.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "11":
                self.ui.day_frameH_11.setToolTip(
                    _translate("MainWindow", "Remaining days"))
            elif frame == "12":
                self.ui.day_frameH_12.setToolTip(
                    _translate("MainWindow", "Remaining days"))
        elif inputDays > 0:
            if frame == "1":
                self.ui.day_frameH_1.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "2":
                self.ui.day_frameH_2.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "3":
                self.ui.day_frameH_3.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "4":
                self.ui.day_frameH_4.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "5":
                self.ui.day_frameH_5.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "6":
                self.ui.day_frameH_6.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "7":
                self.ui.day_frameH_7.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "8":
                self.ui.day_frameH_8.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "9":
                self.ui.day_frameH_9.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "10":
                self.ui.day_frameH_10.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "11":
                self.ui.day_frameH_11.setToolTip(
                    _translate("MainWindow", "Pass days"))
            elif frame == "12":
                self.ui.day_frameH_12.setToolTip(
                    _translate("MainWindow", "Pass days"))
        else:
            if frame == "1":
                self.ui.day_frameH_1.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "2":
                self.ui.day_frameH_2.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "3":
                self.ui.day_frameH_3.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "4":
                self.ui.day_frameH_4.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "5":
                self.ui.day_frameH_5.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "6":
                self.ui.day_frameH_6.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "7":
                self.ui.day_frameH_7.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "8":
                self.ui.day_frameH_8.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "9":
                self.ui.day_frameH_9.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "10":
                self.ui.day_frameH_10.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "11":
                self.ui.day_frameH_11.setToolTip(
                    _translate("MainWindow", "Today"))
            elif frame == "12":
                self.ui.day_frameH_12.setToolTip(
                    _translate("MainWindow", "Today"))

    def refresh_add_func(self):
        dateCurr = QDate.currentDate()
        dateCurr = dateCurr.toString(Qt.ISODate).split("-")
        currYear = dateCurr[0]
        currMonth = dateCurr[1]
        currDay = dateCurr[2]
        frameState_1 = MainBackend.search_frame("1")
        frameState_2 = MainBackend.search_frame("2")
        frameState_3 = MainBackend.search_frame("3")
        frameState_4 = MainBackend.search_frame("4")
        frameState_5 = MainBackend.search_frame("5")
        frameState_6 = MainBackend.search_frame("6")
        frameState_7 = MainBackend.search_frame("7")
        frameState_8 = MainBackend.search_frame("8")
        frameState_9 = MainBackend.search_frame("9")
        frameState_10 = MainBackend.search_frame("10")
        frameState_11 = MainBackend.search_frame("11")
        frameState_12 = MainBackend.search_frame("12")
        if len(frameState_1) != 0:
            self.ui.title_frameH_1.setText(frameState_1[0][2])
            self.ui.Description_frameH_1.setText(frameState_1[0][3])
            self.ui.date_frameH_1.setText(frameState_1[0][4])
            year, month, day = frameState_1[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_1.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("1", delta.days)
            self.ui.frame_home_1.show()
        if len(frameState_2) != 0:
            self.ui.title_frameH_2.setText(frameState_2[0][2])
            self.ui.Description_frameH_2.setText(frameState_2[0][3])
            self.ui.date_frameH_2.setText(frameState_2[0][4])
            year, month, day = frameState_2[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_2.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("2", delta.days)
            self.ui.frame_home_2.show()
        if len(frameState_3) != 0:
            self.ui.title_frameH_3.setText(frameState_3[0][2])
            self.ui.Description_frameH_3.setText(frameState_3[0][3])
            self.ui.date_frameH_3.setText(frameState_3[0][4])
            year, month, day = frameState_3[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_3.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("3", delta.days)
            self.ui.frame_home_3.show()
        if len(frameState_4) != 0:
            self.ui.title_frameH_4.setText(frameState_4[0][2])
            self.ui.Description_frameH_4.setText(frameState_4[0][3])
            self.ui.date_frameH_4.setText(frameState_4[0][4])
            year, month, day = frameState_4[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_4.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("4", delta.days)
            self.ui.frame_home_4.show()
        if len(frameState_5) != 0:
            self.ui.title_frameH_5.setText(frameState_5[0][2])
            self.ui.Description_frameH_5.setText(frameState_5[0][3])
            self.ui.date_frameH_5.setText(frameState_5[0][4])
            year, month, day = frameState_5[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_5.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("5", delta.days)
            self.ui.frame_home_5.show()
        if len(frameState_6) != 0:
            self.ui.title_frameH_6.setText(frameState_6[0][2])
            self.ui.Description_frameH_6.setText(frameState_6[0][3])
            self.ui.date_frameH_6.setText(frameState_6[0][4])
            year, month, day = frameState_6[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_6.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("6", delta.days)
            self.ui.frame_home_6.show()
        if len(frameState_7) != 0:
            self.ui.title_frameH_7.setText(frameState_7[0][2])
            self.ui.Description_frameH_7.setText(frameState_7[0][3])
            self.ui.date_frameH_7.setText(frameState_7[0][4])
            year, month, day = frameState_7[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_7.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("7", delta.days)
            self.ui.frame_home_7.show()
        if len(frameState_8) != 0:
            self.ui.title_frameH_8.setText(frameState_8[0][2])
            self.ui.Description_frameH_8.setText(frameState_8[0][3])
            self.ui.date_frameH_8.setText(frameState_8[0][4])
            year, month, day = frameState_8[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_8.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("8", delta.days)
            self.ui.frame_home_8.show()
        if len(frameState_9) != 0:
            self.ui.title_frameH_9.setText(frameState_9[0][2])
            self.ui.Description_frameH_9.setText(frameState_9[0][3])
            self.ui.date_frameH_9.setText(frameState_9[0][4])
            year, month, day = frameState_9[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_9.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("9", delta.days)
            self.ui.frame_home_9.show()
        if len(frameState_10) != 0:
            self.ui.title_frameH_10.setText(frameState_10[0][2])
            self.ui.Description_frameH_10.setText(frameState_10[0][3])
            self.ui.date_frameH_10.setText(frameState_10[0][4])
            year, month, day = frameState_10[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_10.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("10", delta.days)
            self.ui.frame_home_10.show()
        if len(frameState_11) != 0:
            self.ui.title_frameH_11.setText(frameState_11[0][2])
            self.ui.Description_frameH_11.setText(frameState_11[0][3])
            self.ui.date_frameH_11.setText(frameState_11[0][4])
            year, month, day = frameState_11[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_11.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("11", delta.days)
            self.ui.frame_home_11.show()
        if len(frameState_12) != 0:
            self.ui.title_frameH_12.setText(frameState_12[0][2])
            self.ui.Description_frameH_12.setText(frameState_12[0][3])
            self.ui.date_frameH_12.setText(frameState_12[0][4])
            year, month, day = frameState_12[0][4].split("-")
            firstDate = date(int(year), int(month), int(day))
            secondDate = date(int(currYear), int(currMonth), int(currDay))
            delta = secondDate - firstDate
            self.ui.day_frameH_12.setText(f"{str(-1 * delta.days)} days")
            self.setTooltipDays("12", delta.days)
            self.ui.frame_home_12.show()

    def addEvent_func(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.AddTab)
        self.Anim_frame(self.ui.label, 340, 0, 201, 51, True)
        self.ui.back_btn_add.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        self.ui.todayDate_btn_add.clicked.connect(self.dateOfToday)
        self.ui.submit_btn_add.clicked.connect(self.submit_add_func)
        self.ui.year_lineEdit.textChanged.connect(self.textChangeAdd_Year)
        self.ui.month_lineEdit.textChanged.connect(self.textChangeAdd_Month)
        self.ui.day_lineEdit.textChanged.connect(self.textChangeAdd_Day)
        self.ui.clear_btn_add.clicked.connect(self.clear_add_func)
        self.ui.choose_photo_btn_add.clicked.connect(
            self.browse_fileAddress_photo_add)

    def textChangeAdd_Year(self):
        if not self.ui.year_lineEdit.text().isnumeric():
            self.ui.year_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                                "border-radius:5px;\n"
                                                "")
            self.ui.submit_btn_add.setEnabled(False)
        else:
            self.ui.year_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                "border-radius:5px;\n"
                                                "")
            self.ui.submit_btn_add.setEnabled(True)

    def textChangeAdd_Month(self):
        if not self.ui.month_lineEdit.text().isnumeric():
            self.ui.month_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                                 "border-radius:5px;\n"
                                                 "")
            self.ui.submit_btn_add.setEnabled(False)
        else:
            self.ui.month_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "border-radius:5px;\n"
                                                 "")
            self.ui.submit_btn_add.setEnabled(True)

    def textChangeAdd_Day(self):
        if not self.ui.day_lineEdit.text().isnumeric():
            self.ui.day_lineEdit.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                               "border-radius:5px;\n"
                                               "")
            self.ui.submit_btn_add.setEnabled(False)
        else:
            self.ui.day_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                               "border-radius:5px;\n"
                                               "")
            self.ui.submit_btn_add.setEnabled(True)

    def dateOfToday(self):
        dateCurr = QDate.currentDate()
        dateCurr = dateCurr.toString(Qt.ISODate).split("-")
        self.ui.year_lineEdit.setText(dateCurr[0])
        self.ui.month_lineEdit.setText(dateCurr[1])
        self.ui.day_lineEdit.setText(dateCurr[2])

    def submit_add_func(self):
        frame = self.check_frames()
        dateCurr = QDate.currentDate()
        dateCurr = dateCurr.toString(Qt.ISODate).split("-")
        if len(self.ui.title_lineEdit.text()) != 0:
            if len(self.ui.year_lineEdit.text()) != 0:
                if len(self.ui.month_lineEdit.text()) != 0:
                    if len(self.ui.day_lineEdit.text()) != 0:
                        if int(dateCurr[0]) <= int(self.ui.year_lineEdit.text()) <= int(dateCurr[0]) + 50:
                            if int(dateCurr[1]) <= int(self.ui.month_lineEdit.text()) <= 12:
                                if int(self.ui.month_lineEdit.text()) in self.day_31:
                                    if int(dateCurr[2]) <= int(self.ui.day_lineEdit.text()) <= 31:
                                        inputDate = f"{self.ui.year_lineEdit.text()}-{self.ui.month_lineEdit.text()}-{self.ui.day_lineEdit.text()}"
                                        MainBackend.insert(frame, self.ui.title_lineEdit.text(),
                                                           self.ui.textEdit_add.toPlainText(), inputDate, "active",
                                                           self.fileAddressPhoto_add)
                                        HistoryBackend.insert(self.ui.title_lineEdit.text(),
                                                              self.ui.textEdit_add.toPlainText(), inputDate, "active")
                                        self.refresh_add_func()
                                        self.showInfo(
                                            "Add", "Add was successful.")
                                    else:
                                        self.showError(
                                            "Day", f"Day should be between {dateCurr[2]}-{31}")
                                elif int(self.ui.month_lineEdit.text()) in self.day_30:
                                    if int(dateCurr[2]) <= int(self.ui.day_lineEdit.text()) <= 30:
                                        inputDate = f"{self.ui.year_lineEdit.text()}-{self.ui.month_lineEdit.text()}-{self.ui.day_lineEdit.text()}"
                                        MainBackend.insert(frame, self.ui.title_lineEdit.text(),
                                                           self.ui.textEdit_add.toPlainText(), inputDate, "active",
                                                           self.fileAddressPhoto_add)
                                        HistoryBackend.insert(self.ui.title_lineEdit.text(),
                                                              self.ui.textEdit_add.toPlainText(), inputDate, "active")
                                        self.refresh_add_func()
                                        self.showInfo(
                                            "Add", "Add was successful.")
                                    else:
                                        self.showError(
                                            "Day", f"Day should be between {dateCurr[2]}-{30}")
                                elif int(self.ui.month_lineEdit.text()) == self.day_28:
                                    if int(dateCurr[2]) <= int(self.ui.day_lineEdit.text()) <= 28:
                                        inputDate = f"{self.ui.year_lineEdit.text()}-{self.ui.month_lineEdit.text()}-{self.ui.day_lineEdit.text()}"
                                        MainBackend.insert(frame, self.ui.title_lineEdit.text(),
                                                           self.ui.textEdit_add.toPlainText(), inputDate, "active",
                                                           self.fileAddressPhoto_add)
                                        HistoryBackend.insert(self.ui.title_lineEdit.text(),
                                                              self.ui.textEdit_add.toPlainText(), inputDate, "active")
                                        self.refresh_add_func()
                                        self.showInfo(
                                            "Add", "Add was successful.")
                                    else:
                                        self.showError(
                                            "Day", f"Day should be between {dateCurr[2]}-{28}")
                            else:
                                self.showError(
                                    "Month", f"Month should be between {dateCurr[1]}-{12}")
                        else:
                            self.showError(
                                "Year", f"Year should be between {dateCurr[0]}-{int(dateCurr[0]) + 50}")
                    else:
                        self.showError("Day", "You should fill day lineEdit.")
                else:
                    self.showError("Month", "You should fill month lineEdit.")
            else:
                self.showError("Year", "You should fill year lineEdit.")
        else:
            self.showError("Title", "You should fill title lineEdit.")

    def clear_add_func(self):
        self.ui.title_lineEdit.setText("")
        self.ui.textEdit_add.setText("")
        self.ui.year_lineEdit.setText("")
        self.ui.month_lineEdit.setText("")
        self.ui.day_lineEdit.setText("")
        self.ui.photo_label_add.setPixmap(QPixmap(""))
        self.ui.year_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                            "border-radius:5px;\n"
                                            "")
        self.ui.month_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "border-radius:5px;\n"
                                             "")
        self.ui.day_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "border-radius:5px;\n"
                                           "")
        self.ui.submit_btn_add.setEnabled(True)

    def browse_fileAddress_photo_add(self):
        try:
            fileAddress_photo = QFileDialog.getOpenFileNames(
                self, "Select the photo", "C:/Users/sajjad/Desktop", "source File (*.jpg *.png *.ico)")
            self.fileAddressPhoto_add = fileAddress_photo[0][0]
            self.ui.photo_label_add.setPixmap(
                QPixmap(self.fileAddressPhoto_add))
        except:
            print("")

    def setting_func(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Setting)
        self.Anim_frame(self.ui.label_4, 320, 10, 201, 51, True)
        self.ui.email_btn.clicked.connect(self.email_func)
        self.ui.back_btn_setting.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        self.ui.history_btn.clicked.connect(self.history_func)
        self.ui.info_btn.clicked.connect(self.info_func)
        self.ui.background_btn.clicked.connect(self.background_func)

    def table_func(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Table)
        self.Anim_frame(self.ui.label_99, 340, 0, 201, 51, True)
        self.ui.back_btn_table.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        self.ui.clear_btn_table_info.setEnabled(False)
        self.ui.submit_btn_table_info.setEnabled(False)
        self.ui.class_lineEdit_table_info.setReadOnly(True)
        self.ui.textEdit_detail_table_info.setReadOnly(True)
        self.ui.icon_sadEmoji_table_info.setEnabled(False)
        self.ui.icon_smileEmoji_table_info.setEnabled(False)
        self.ui.icon_circle_table_info.setEnabled(False)
        self.ui.icon_circleStar_table_info.setEnabled(False)
        self.ui.icon_starFill_table_info.setEnabled(False)
        self.ui.icon_starOut_table_info.setEnabled(False)
        self.ui.icon_done_table_info.setEnabled(False)
        self.ui.icon_heart_table_info.setEnabled(False)
        self.refresh_Table()

    def university_func(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.University)
        self.Anim_frame(self.ui.label_16, 340, 0, 201, 51, True)
        self.ui.back_btn_uni.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.Home))
        self.ui.icon_sadEmoji_btn.setEnabled(False)
        self.ui.icon_smileEmoji_btn.setEnabled(False)
        self.ui.icon_done_btn.setEnabled(False)
        self.ui.icon_circle_btn.setEnabled(False)
        self.ui.icon_circleStar_btn.setEnabled(False)
        self.ui.icon_starFill_btn.setEnabled(False)
        self.ui.icon_starOut_btn.setEnabled(False)
        self.ui.icon_heart_btn.setEnabled(False)
        self.ui.class_lineEdit_uni_info.setReadOnly(True)
        self.ui.textEdit_detail_uni_info.setReadOnly(True)
        self.ui.link_lineEdit_uni_info.setReadOnly(True)
        self.ui.clear_btn_uni.setEnabled(False)
        self.ui.submit_btn_uni.setEnabled(False)
        self.refresh_UniversityTable()

    def email_func(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Email)
        self.Anim_frame(self.ui.label_95, 350, 10, 181, 51, True)
        self.ui.back_btn_email.clicked.connect(self.setting_func)
        self.ui.titleEmail_lineEdit.textChanged.connect(
            self.textChange_title_Email)
        self.ui.NameEmail_lineEdit.textChanged.connect(
            self.textChange_name_Email)
        self.ui.massageEmail_textEdit.textChanged.connect(
            self.textChange_massage_Email)
        self.ui.send_email.clicked.connect(self.send_email_func)
        self.ui.clear_email.clicked.connect(self.clear_email_func)
        self.connection_func()
        self.ui.connection_btn.clicked.connect(self.connection_func)

    def textChange_title_Email(self):
        if len(self.ui.titleEmail_lineEdit.text()) == 0:
            self.ui.titleEmail_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "border-radius:5px;\n"
                                                      "border:2px solid red;"
                                                      "")
            self.title_email = False
        else:
            self.ui.titleEmail_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "border-radius:5px;\n"
                                                      "")
            self.title_email = True
        self.accept_submit_btn()

    def textChange_name_Email(self):
        if len(self.ui.NameEmail_lineEdit.text()) == 0:
            self.ui.NameEmail_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "border-radius:5px;\n"
                                                     "border:2px solid red;"
                                                     "")
            self.name_email = False
        else:
            self.ui.NameEmail_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "border-radius:5px;\n"
                                                     "")
            self.name_email = True
        self.accept_submit_btn()

    def textChange_massage_Email(self):
        if len(self.ui.massageEmail_textEdit.toPlainText()) == 0:
            self.ui.massageEmail_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                        "border-radius:5px;\n"
                                                        "border:2px solid red;"
                                                        "")
            self.massage_email = False
        else:
            self.ui.massageEmail_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                        "border-radius:5px;\n"
                                                        "")
            self.massage_email = True
        self.accept_submit_btn()

    def accept_submit_btn(self):
        if self.massage_email and self.title_email and self.name_email:
            self.ui.send_email.setEnabled(True)
        else:
            self.ui.send_email.setEnabled(False)

    def send_email_func(self):
        if self.connectionState:
            _thread.start_new_thread(self.send_email_process, (2,))
        else:
            self.showError("Connection", "Please check your internet.")

    def send_email_process(self, num):
        global Email,Password
        from_email = Email
        password = Password
        to_email = "faniam321@gmail.com"
        try:
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login(from_email, password)
            massage = f"{self.ui.NameEmail_lineEdit.text()}\n{self.ui.titleEmail_lineEdit.text()}\n{self.ui.massageEmail_textEdit.toPlainText()}"
            server.sendmail(from_email, to_email, massage)
            server.quit()
            self.ui.send_label.show()
            time.sleep(5)
            self.ui.send_label.hide()
        except:
            self.showError("Email", "Something went wrong.")

    def clear_email_func(self):
        self.ui.NameEmail_lineEdit.setText("")
        self.ui.titleEmail_lineEdit.setText("")
        self.ui.massageEmail_textEdit.setText("")
        self.ui.titleEmail_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "border-radius:5px;\n"
                                                  "")
        self.ui.NameEmail_lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                 "border-radius:5px;\n"
                                                 "")
        self.ui.massageEmail_textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                    "border-radius:5px;\n"
                                                    "")

    def connection_func(self):
        _thread.start_new_thread(self.connection_process, (2,))

    def connection_process(self, num):
        _translate = QCoreApplication.translate
        url = "https://www.google.com"
        timeout = 5
        try:
            requests.get(url, timeout=timeout)
            self.ui.connection_btn.setText(" Connect")
            self.ui.connection_btn.setToolTip(
                _translate("MainWindow", "Connect"))
            icon = QIcon()
            icon.addPixmap(QPixmap("photo/icons8-wi-fi-green.png"),
                           QIcon.Normal, QIcon.Off)
            self.ui.connection_btn.setIcon(icon)
            self.connectionState = True
        except (requests.ConnectionError, requests.Timeout):
            self.ui.connection_btn.setText(" Disconnect")
            self.ui.connection_btn.setToolTip(
                _translate("MainWindow", "Disconnect"))
            icon = QIcon()
            icon.addPixmap(QPixmap("photo/icons8-wi-fi-red.png"),
                           QIcon.Normal, QIcon.Off)
            self.ui.connection_btn.setIcon(icon)
            self.connectionState = False

    def history_func(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.History)
        self.Anim_frame(self.ui.label_14, 340, 10, 201, 51, True)
        self.ui.back_btn_history.clicked.connect(self.setting_func)
        self.history_TableProcess()
        self.ui.tableWidget_history.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.ui.id_lineEdit_history.textChanged.connect(
            self.textChange_id_history)
        self.ui.search_btn_history.clicked.connect(self.history_search)
        self.ui.showAll_btn_history.clicked.connect(self.history_TableProcess)
        self.ui.clear_btn_history.clicked.connect(self.history_clear)
        self.ui.delete_btn_history.clicked.connect(self.history_delete)

    def history_delete(self):
        btn = QMessageBox.question(
            self, "Delete", "Are you sure?", QMessageBox.Yes | QMessageBox.No)
        if btn == QMessageBox.Yes:
            row = HistoryBackend.search_id(self.ui.id_lineEdit_history.text())
            if len(row) != 0:
                HistoryBackend.delete(self.ui.id_lineEdit_history.text())
                self.history_TableProcess()
            else:
                self.showError(
                    "Delete", f"{self.ui.id_lineEdit_history.text()} is not exist.")

    def history_clear(self):
        rows = HistoryBackend.view()
        if len(rows) != 0:
            btn = QMessageBox.question(self, "Clear All", "Do you want to clear all the information?",
                                       QMessageBox.Yes | QMessageBox.No)
            if btn == QMessageBox.Yes:
                for item in rows:
                    HistoryBackend.delete(item[0])
                self.history_TableProcess()

    def history_search(self):
        row = HistoryBackend.search_id(self.ui.id_lineEdit_history.text())
        if len(row) != 0:
            self.ui.tableWidget_history.setRowCount(len(row))
            delta_days = self.delta_date(row[0][3])
            self.ui.tableWidget_history.setItem(
                0, 0, QTableWidgetItem(str(row[0][0])))
            self.ui.tableWidget_history.setItem(
                0, 1, QTableWidgetItem(row[0][1]))
            self.ui.tableWidget_history.setItem(
                0, 2, QTableWidgetItem(row[0][2]))
            self.ui.tableWidget_history.setItem(
                0, 3, QTableWidgetItem(row[0][3]))
            self.ui.tableWidget_history.setItem(
                0, 4, QTableWidgetItem(str(delta_days) + " Days ago"))
            self.ui.tableWidget_history.setItem(
                0, 5, QTableWidgetItem(row[0][4]))
        else:
            self.showError(
                "Search", f"{self.ui.id_lineEdit_history.text()} is not exist.")

    def textChange_id_history(self):
        if not self.ui.id_lineEdit_history.text().isnumeric() or not len(self.ui.id_lineEdit_history.text()) != 0:
            self.ui.id_lineEdit_history.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "border-radius:5px;\n"
                                                      "border:2px solid red;"
                                                      "")
            self.ui.search_btn_history.setEnabled(False)
            self.ui.delete_btn_history.setEnabled(False)
        else:
            self.ui.id_lineEdit_history.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "border-radius:5px;\n"
                                                      "")
            self.ui.search_btn_history.setEnabled(True)
            self.ui.delete_btn_history.setEnabled(True)

    @staticmethod
    def delta_date(inputDate):
        if len(inputDate) != 0:
            dateCurr = QDate.currentDate()
            dateCurr = dateCurr.toString(Qt.ISODate).split("-")
            currYear = dateCurr[0]
            currMonth = dateCurr[1]
            currDay = dateCurr[2]
            year, month, day = inputDate.split("-")
            delta = date(int(currYear), int(currMonth), int(
                currDay)) - date(int(year), int(month), int(day))
            return delta.days

    def history_TableProcess(self):
        rows = HistoryBackend.view()
        row = 0
        self.ui.tableWidget_history.setRowCount(len(rows))
        for item in rows:
            delta_days = self.delta_date(item[3])
            self.ui.tableWidget_history.setItem(
                row, 0, QTableWidgetItem(str(item[0])))
            self.ui.tableWidget_history.setItem(
                row, 1, QTableWidgetItem(item[1]))
            self.ui.tableWidget_history.setItem(
                row, 2, QTableWidgetItem(item[2]))
            self.ui.tableWidget_history.setItem(
                row, 3, QTableWidgetItem(item[3]))
            self.ui.tableWidget_history.setItem(
                row, 4, QTableWidgetItem(str(delta_days) + " Days ago"))
            self.ui.tableWidget_history.setItem(
                row, 5, QTableWidgetItem(item[4]))
            row += 1

    def info_func(self):
        if self.handle_info == "close":
            self.ui.info_frame.show()
            self.Anim_frame(self.ui.info_frame, 20, 90, 331, 161, True)
            self.handle_info = "open"
        elif self.handle_info == "open":
            self.Anim_frame(self.ui.info_frame, 20, 90, 331, 161, False)
            self.handle_info = "close"

    def background_func(self):
        if self.handle_background == "close":
            self.ui.background_frame.show()
            self.Anim_frame(self.ui.background_frame, 480, 430, 371, 71, True)
            self.handle_background = "open"
        elif self.handle_background == "open":
            self.Anim_frame(self.ui.background_frame, 480, 430, 371, 71, False)
            self.handle_background = "close"

    def frame_1_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("1")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 1")
        self.ui.frameNum_label.show()
        self.frameNum_home = "1"

    def frame_2_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("2")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 2")
        self.ui.frameNum_label.show()
        self.frameNum_home = "2"

    def frame_3_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("3")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 3")
        self.ui.frameNum_label.show()
        self.frameNum_home = "3"

    def frame_4_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("4")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 4")
        self.ui.frameNum_label.show()
        self.frameNum_home = "4"

    def frame_5_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("5")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 5")
        self.ui.frameNum_label.show()
        self.frameNum_home = "5"

    def frame_6_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("6")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 6")
        self.ui.frameNum_label.show()
        self.frameNum_home = "6"

    def frame_7_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("7")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 7")
        self.ui.frameNum_label.show()
        self.frameNum_home = "7"

    def frame_8_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("8")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 8")
        self.ui.frameNum_label.show()
        self.frameNum_home = "8"

    def frame_9_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("9")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 9")
        self.ui.frameNum_label.show()
        self.frameNum_home = "9"

    def frame_10_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("10")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 10")
        self.ui.frameNum_label.show()
        self.frameNum_home = "10"

    def frame_11_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("11")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 11")
        self.ui.frameNum_label.show()
        self.frameNum_home = "11"

    def frame_12_home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ShowInfo)
        row = MainBackend.search_frame("12")
        self.ui.title_lineEdit_show.setText(row[0][2])
        self.ui.textEdit_show.setText(row[0][3])
        year, month, day = row[0][4].split("-")
        self.ui.year_lineEdit_show.setText(str(year))
        self.ui.month_lineEdit_show.setText(str(month))
        self.ui.day_lineEdit_show.setText(str(day))
        oldDate = date(int(year), int(month), int(day))
        self.ui.dayName_lineEdit_show.setText(oldDate.strftime("%a"))
        self.ui.photo_label_show.setPixmap(QPixmap(row[0][6]))
        self.ui.frameNum_label.setText("Event 12")
        self.ui.frameNum_label.show()
        self.frameNum_home = "12"

    def setEnableAndDisableObj(self, state):
        if state:
            self.ui.submit_btn_show.setEnabled(True)
            self.ui.choose_photo_btn_show.setEnabled(True)
            self.ui.title_lineEdit_show.setReadOnly(False)
            self.ui.textEdit_show.setReadOnly(False)
            self.ui.year_lineEdit_show.setReadOnly(False)
            self.ui.month_lineEdit_show.setReadOnly(False)
            self.ui.day_lineEdit_show.setReadOnly(False)
        else:
            self.ui.submit_btn_show.setEnabled(False)
            self.ui.choose_photo_btn_show.setEnabled(False)
            self.ui.title_lineEdit_show.setReadOnly(True)
            self.ui.textEdit_show.setReadOnly(True)
            self.ui.year_lineEdit_show.setReadOnly(True)
            self.ui.month_lineEdit_show.setReadOnly(True)
            self.ui.day_lineEdit_show.setReadOnly(True)

    def edit_btn_show(self):
        if self.stateEditShow == "Disable":
            self.ui.edit_btn_show.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    \n"
                                                "    background-color: rgb(12, 182, 0);\n"
                                                "border-radius:10px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:5px;\n"
                                                "}")
            self.setEnableAndDisableObj(True)
            self.stateEditShow = "Enable"
        elif self.stateEditShow == "Enable":
            self.ui.edit_btn_show.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    \n"
                                                "    background-color: rgb(115, 115, 115);\n"
                                                "border-radius:10px;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:5px;\n"
                                                "}")
            self.setEnableAndDisableObj(False)
            self.stateEditShow = "Disable"

    def textChanged_year_show(self):
        if not self.ui.year_lineEdit_show.text().isnumeric():
            self.ui.year_lineEdit_show.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                                     "border-radius:5px;\n"
                                                     "")
            self.year_show = False
        else:
            self.ui.year_lineEdit_show.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                     "border-radius:5px;\n"
                                                     "")
            self.year_show = True

    def textChanged_month_show(self):
        if not self.ui.month_lineEdit_show.text().isnumeric():
            self.ui.month_lineEdit_show.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                                      "border-radius:5px;\n"
                                                      "")
            self.month_show = False
        else:
            self.ui.month_lineEdit_show.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                      "border-radius:5px;\n"
                                                      "")
            self.month_show = True

    def textChanged_day_show(self):
        if not self.ui.day_lineEdit_show.text().isnumeric():
            self.ui.day_lineEdit_show.setStyleSheet("background-color: rgb(255, 0, 0);\n"
                                                    "border-radius:5px;\n"
                                                    "")
            self.day_show = False
        else:
            self.ui.day_lineEdit_show.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                    "border-radius:5px;\n"
                                                    "")
            self.day_show = True

    def submit_btn_show(self):
        if self.year_show and self.month_show and self.day_show:
            dateCurr = QDate.currentDate()
            dateCurr = dateCurr.toString(Qt.ISODate).split("-")
            if len(self.ui.title_lineEdit_show.text()) != 0:
                if len(self.ui.year_lineEdit_show.text()) != 0:
                    if len(self.ui.month_lineEdit_show.text()) != 0:
                        if len(self.ui.day_lineEdit_show.text()) != 0:
                            if int(dateCurr[0]) <= int(self.ui.year_lineEdit_show.text()) <= int(dateCurr[0]) + 50:
                                if int(dateCurr[1]) <= int(self.ui.month_lineEdit_show.text()) <= 12:
                                    if int(self.ui.month_lineEdit_show.text()) in self.day_31:
                                        if int(dateCurr[2]) <= int(self.ui.day_lineEdit_show.text()) <= 31:
                                            inputDate = f"{self.ui.year_lineEdit_show.text()}-{self.ui.month_lineEdit_show.text()}-{self.ui.day_lineEdit_show.text()} "
                                            self.edit_btn_final(self.ui.title_lineEdit_show.text(),
                                                                self.ui.textEdit_show.toPlainText(), inputDate,
                                                                "updated")
                                            oldDate = date(int(self.ui.year_lineEdit_show.text()),
                                                           int(self.ui.month_lineEdit_show.text(
                                                           )),
                                                           int(self.ui.day_lineEdit_show.text()))
                                            self.ui.dayName_lineEdit_show.setText(
                                                oldDate.strftime("%a"))
                                            self.showInfo(
                                                "Update", "Update was successful.")
                                        else:
                                            self.showError(
                                                "Day", f"Day should be between {dateCurr[2]}-{31}")
                                    elif int(self.ui.month_lineEdit_show.text()) in self.day_30:
                                        if int(dateCurr[2]) <= int(self.ui.day_lineEdit_show.text()) <= 30:
                                            inputDate = f"{self.ui.year_lineEdit_show.text()}-{self.ui.month_lineEdit_show.text()}-{self.ui.day_lineEdit_show.text()}"
                                            self.edit_btn_final(self.ui.title_lineEdit_show.text(),
                                                                self.ui.textEdit_show.toPlainText(), inputDate,
                                                                "updated")
                                            oldDate = date(int(self.ui.year_lineEdit_show.text()),
                                                           int(self.ui.month_lineEdit_show.text(
                                                           )),
                                                           int(self.ui.day_lineEdit_show.text()))
                                            self.ui.dayName_lineEdit_show.setText(
                                                oldDate.strftime("%a"))
                                            self.showInfo(
                                                "Update", "Update was successful.")
                                        else:
                                            self.showError(
                                                "Day", f"Day should be between {dateCurr[2]}-{30}")
                                    elif int(self.ui.month_lineEdit_show.text()) == self.day_28:
                                        if int(dateCurr[2]) <= int(self.ui.day_lineEdit_show.text()) <= 28:
                                            inputDate = f"{self.ui.year_lineEdit_show.text()}-{self.ui.month_lineEdit_show.text()}-{self.ui.day_lineEdit_show.text()}"
                                            self.edit_btn_final(self.ui.title_lineEdit_show.text(),
                                                                self.ui.textEdit_show.toPlainText(), inputDate,
                                                                "updated")
                                            oldDate = date(int(self.ui.year_lineEdit_show.text()),
                                                           int(self.ui.month_lineEdit_show.text(
                                                           )),
                                                           int(self.ui.day_lineEdit_show.text()))
                                            self.ui.dayName_lineEdit_show.setText(
                                                oldDate.strftime("%a"))
                                            self.showInfo(
                                                "Update", "Update was successful.")
                                        else:
                                            self.showError(
                                                "Day", f"Day should be between {dateCurr[2]}-{28}")
                                else:
                                    self.showError(
                                        "Month", f"Month should be between {dateCurr[1]}-{12}")
                            else:
                                self.showError(
                                    "Year", f"Year should be between {dateCurr[0]}-{int(dateCurr[0]) + 50}")
                        else:
                            self.showError(
                                "Day", "You should fill day lineEdit.")
                    else:
                        self.showError(
                            "Month", "You should fill month lineEdit.")
                else:
                    self.showError("Year", "You should fill year lineEdit.")
            else:
                self.showError("Title", "You should fill title lineEdit.")
        else:
            self.showError(
                "Error", "Please check your year,month,day lineEdit.")

    def edit_btn_final(self, title, description, inputDate, state):
        row = MainBackend.search_frame(self.frameNum_home)
        MainBackend.update(row[0][0], self.frameNum_home, title, description, inputDate, "active",
                           self.fileAddressPhoto_show)
        HistoryBackend.insert(title, description, inputDate, state)
        self.refresh_add_func()

    def browse_fileAddress_photo_show(self):
        try:
            fileAddress_photo = QFileDialog.getOpenFileNames(
                self, "Select the photo", "C:/Users/sajjad/Desktop", "source File (*.jpg *.png *.ico)")
            self.fileAddressPhoto_show = fileAddress_photo[0][0]
            self.ui.photo_label_show.setPixmap(
                QPixmap(self.fileAddressPhoto_show))
        except:
            print("")

    @staticmethod
    def insertDeleteData(frame):
        row = MainBackend.search_frame(frame)
        HistoryBackend.insert(row[0][2], row[0][3], row[0][4], "deleted")

    def delete_btn_home(self):
        btn = QMessageBox.question(
            self, "Delete", "Are you sure?", QMessageBox.Ok | QMessageBox.Cancel)
        if btn == QMessageBox.Ok:
            if self.frameNum_home == "1":
                self.insertDeleteData("1")
                MainBackend.delete("1")
                self.home_func()
                self.ui.frame_home_1.hide()
            elif self.frameNum_home == "2":
                self.insertDeleteData("2")
                MainBackend.delete("2")
                self.home_func()
                self.ui.frame_home_2.hide()
            elif self.frameNum_home == "3":
                self.insertDeleteData("3")
                MainBackend.delete("3")
                self.home_func()
                self.ui.frame_home_3.hide()
            elif self.frameNum_home == "4":
                self.insertDeleteData("4")
                MainBackend.delete("4")
                self.home_func()
                self.ui.frame_home_4.hide()
            elif self.frameNum_home == "5":
                self.insertDeleteData("5")
                MainBackend.delete("5")
                self.home_func()
                self.ui.frame_home_5.hide()
            elif self.frameNum_home == "6":
                self.insertDeleteData("6")
                MainBackend.delete("6")
                self.home_func()
                self.ui.frame_home_6.hide()
            elif self.frameNum_home == "7":
                self.insertDeleteData("7")
                MainBackend.delete("7")
                self.home_func()
                self.ui.frame_home_7.hide()
            elif self.frameNum_home == "8":
                self.insertDeleteData("8")
                MainBackend.delete("8")
                self.home_func()
                self.ui.frame_home_8.hide()
            elif self.frameNum_home == "9":
                self.insertDeleteData("9")
                MainBackend.delete("9")
                self.home_func()
                self.ui.frame_home_9.hide()
            elif self.frameNum_home == "10":
                self.insertDeleteData("10")
                MainBackend.delete("10")
                self.home_func()
                self.ui.frame_home_10.hide()
            elif self.frameNum_home == "11":
                self.insertDeleteData("11")
                MainBackend.delete("11")
                self.home_func()
                self.ui.frame_home_11.hide()
            elif self.frameNum_home == "12":
                self.insertDeleteData("12")
                MainBackend.delete("12")
                self.home_func()
                self.ui.frame_home_12.hide()

    def clearAddUniversity(self):
        self.ui.class_lineEdit_add.setText("")
        self.ui.textEdit_detail_add.setText("")
        self.ui.link_lineEdit_add.setText("")
        self.iconAddBtnUni = ""
        self.ui.icon_done_btn_uni_add.setEnabled(True)
        self.ui.icon_circle_btn_uni_add.setEnabled(True)
        self.ui.icon_heart_btn_uni_add.setEnabled(True)
        self.ui.icon_smileEmoji_btn_uni_add.setEnabled(True)
        self.ui.icon_sadEmoji_btn_uni_add.setEnabled(True)
        self.ui.icon_circleStar_btn_uni_add.setEnabled(True)
        self.ui.icon_starFill_btn_uni_add.setEnabled(True)
        self.ui.icon_starOut_btn_uni_add.setEnabled(True)
        self.ui.icon_done_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(115, 115, 115);\n"
                                                    "border-radius:10px;\n"
                                                    "border:none;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")
        self.ui.icon_heart_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "    background-color: rgb(115, 115, 115);\n"
                                                     "border-radius:10px;\n"
                                                     "border:none;\n"
                                                     "}\n"
                                                     "QPushButton:hover{\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "    background-color: rgb(95, 95, 95);\n"
                                                     "border-radius:5px;\n"
                                                     "}")
        self.ui.icon_starOut_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(115, 115, 115);\n"
                                                       "border-radius:10px;\n"
                                                       "border:none;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(95, 95, 95);\n"
                                                       "border-radius:5px;\n"
                                                       "}")
        self.ui.icon_starFill_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(115, 115, 115);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")
        self.ui.icon_circle_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(115, 115, 115);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
        self.ui.icon_circleStar_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(115, 115, 115);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")
        self.ui.icon_smileEmoji_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(115, 115, 115);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")
        self.ui.icon_sadEmoji_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(115, 115, 115);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")

    def doneBtnAddUniversity(self):
        if not self.btn_done_UniAdd:
            self.iconAddBtnUni = "done"
            self.btn_done_UniAdd = True
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(False)
            self.ui.icon_circle_btn_uni_add.setEnabled(False)
            self.ui.icon_starFill_btn_uni_add.setEnabled(False)
            self.ui.icon_starOut_btn_uni_add.setEnabled(False)
            self.ui.icon_heart_btn_uni_add.setEnabled(False)
            self.ui.icon_done_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(170, 85, 127);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")
        elif self.btn_done_UniAdd:
            self.iconAddBtnUni = ""
            self.btn_done_UniAdd = False
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(True)
            self.ui.icon_circle_btn_uni_add.setEnabled(True)
            self.ui.icon_starFill_btn_uni_add.setEnabled(True)
            self.ui.icon_starOut_btn_uni_add.setEnabled(True)
            self.ui.icon_heart_btn_uni_add.setEnabled(True)
            self.ui.icon_done_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(115, 115, 115);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")

    def heartBtnAddUniversity(self):
        if not self.btn_heart_UniAdd:
            self.iconAddBtnUni = "heart"
            self.btn_heart_UniAdd = True
            self.ui.icon_done_btn_uni_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(False)
            self.ui.icon_circle_btn_uni_add.setEnabled(False)
            self.ui.icon_starFill_btn_uni_add.setEnabled(False)
            self.ui.icon_starOut_btn_uni_add.setEnabled(False)
            self.ui.icon_heart_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(170, 85, 127);\n"
                                                         "border-radius:10px;\n"
                                                         "border:none;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(95, 95, 95);\n"
                                                         "border-radius:5px;\n"
                                                         "}")
        elif self.btn_heart_UniAdd:
            self.iconAddBtnUni = ""
            self.btn_heart_UniAdd = False
            self.ui.icon_done_btn_uni_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(True)
            self.ui.icon_circle_btn_uni_add.setEnabled(True)
            self.ui.icon_starFill_btn_uni_add.setEnabled(True)
            self.ui.icon_starOut_btn_uni_add.setEnabled(True)
            self.ui.icon_heart_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(115, 115, 115);\n"
                                                         "border-radius:10px;\n"
                                                         "border:none;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(95, 95, 95);\n"
                                                         "border-radius:5px;\n"
                                                         "}")

    def starOutBtnAddUniversity(self):
        if not self.btn_starOut_UniAdd:
            self.iconAddBtnUni = "starOutline"
            self.btn_starOut_UniAdd = True
            self.ui.icon_done_btn_uni_add.setEnabled(False)
            self.ui.icon_heart_btn_uni_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(False)
            self.ui.icon_circle_btn_uni_add.setEnabled(False)
            self.ui.icon_starFill_btn_uni_add.setEnabled(False)
            self.ui.icon_starOut_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(170, 85, 127);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")
        elif self.btn_starOut_UniAdd:
            self.iconAddBtnUni = ""
            self.btn_starOut_UniAdd = False
            self.ui.icon_done_btn_uni_add.setEnabled(True)
            self.ui.icon_heart_btn_uni_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(True)
            self.ui.icon_circle_btn_uni_add.setEnabled(True)
            self.ui.icon_starFill_btn_uni_add.setEnabled(True)
            self.ui.icon_starOut_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(115, 115, 115);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")

    def starFillBtnAddUniversity(self):
        if not self.btn_starFill_UniAdd:
            self.iconAddBtnUni = "starFill"
            self.btn_starFill_UniAdd = True
            self.ui.icon_done_btn_uni_add.setEnabled(False)
            self.ui.icon_heart_btn_uni_add.setEnabled(False)
            self.ui.icon_starOut_btn_uni_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(False)
            self.ui.icon_circle_btn_uni_add.setEnabled(False)
            self.ui.icon_starFill_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(170, 85, 127);\n"
                                                            "border-radius:10px;\n"
                                                            "border:none;\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(95, 95, 95);\n"
                                                            "border-radius:5px;\n"
                                                            "}")
        elif self.btn_starFill_UniAdd:
            self.iconAddBtnUni = ""
            self.btn_starFill_UniAdd = False
            self.ui.icon_done_btn_uni_add.setEnabled(True)
            self.ui.icon_heart_btn_uni_add.setEnabled(True)
            self.ui.icon_starOut_btn_uni_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(True)
            self.ui.icon_circle_btn_uni_add.setEnabled(True)
            self.ui.icon_starFill_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(115, 115, 115);\n"
                                                            "border-radius:10px;\n"
                                                            "border:none;\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(95, 95, 95);\n"
                                                            "border-radius:5px;\n"
                                                            "}")

    def circleBtnAddUniversity(self):
        if not self.btn_circle_UniAdd:
            self.iconAddBtnUni = "circle"
            self.btn_circle_UniAdd = True
            self.ui.icon_done_btn_uni_add.setEnabled(False)
            self.ui.icon_heart_btn_uni_add.setEnabled(False)
            self.ui.icon_starOut_btn_uni_add.setEnabled(False)
            self.ui.icon_starFill_btn_uni_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(False)
            self.ui.icon_circle_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(170, 85, 127);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")
        elif self.btn_circle_UniAdd:
            self.iconAddBtnUni = ""
            self.btn_circle_UniAdd = False
            self.ui.icon_done_btn_uni_add.setEnabled(True)
            self.ui.icon_heart_btn_uni_add.setEnabled(True)
            self.ui.icon_starOut_btn_uni_add.setEnabled(True)
            self.ui.icon_starFill_btn_uni_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(True)
            self.ui.icon_circle_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(115, 115, 115);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")

    def starCircleBtnAddUniversity(self):
        if not self.btn_starCircle_UniAdd:
            self.iconAddBtnUni = "starCircle"
            self.btn_starCircle_UniAdd = True
            self.ui.icon_done_btn_uni_add.setEnabled(False)
            self.ui.icon_circle_btn_uni_add.setEnabled(False)
            self.ui.icon_heart_btn_uni_add.setEnabled(False)
            self.ui.icon_starOut_btn_uni_add.setEnabled(False)
            self.ui.icon_starFill_btn_uni_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_circleStar_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(170, 85, 127);\n"
                                                              "border-radius:10px;\n"
                                                              "border:none;\n"
                                                              "}\n"
                                                              "QPushButton:hover{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(95, 95, 95);\n"
                                                              "border-radius:5px;\n"
                                                              "}")
        elif self.btn_starCircle_UniAdd:
            self.iconAddBtnUni = ""
            self.btn_starCircle_UniAdd = False
            self.ui.icon_done_btn_uni_add.setEnabled(True)
            self.ui.icon_circle_btn_uni_add.setEnabled(True)
            self.ui.icon_heart_btn_uni_add.setEnabled(True)
            self.ui.icon_starOut_btn_uni_add.setEnabled(True)
            self.ui.icon_starFill_btn_uni_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_circleStar_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(115, 115, 115);\n"
                                                              "border-radius:10px;\n"
                                                              "border:none;\n"
                                                              "}\n"
                                                              "QPushButton:hover{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(95, 95, 95);\n"
                                                              "border-radius:5px;\n"
                                                              "}")

    def smileBtnAddUniversity(self):
        if not self.btn_smile_UniAdd:
            self.iconAddBtnUni = "smileEmoji"
            self.btn_smile_UniAdd = True
            self.ui.icon_done_btn_uni_add.setEnabled(False)
            self.ui.icon_circle_btn_uni_add.setEnabled(False)
            self.ui.icon_heart_btn_uni_add.setEnabled(False)
            self.ui.icon_starOut_btn_uni_add.setEnabled(False)
            self.ui.icon_starFill_btn_uni_add.setEnabled(False)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(170, 85, 127);\n"
                                                              "border-radius:10px;\n"
                                                              "border:none;\n"
                                                              "}\n"
                                                              "QPushButton:hover{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(95, 95, 95);\n"
                                                              "border-radius:5px;\n"
                                                              "}")
        elif self.btn_smile_UniAdd:
            self.iconAddBtnUni = ""
            self.btn_smile_UniAdd = False
            self.ui.icon_done_btn_uni_add.setEnabled(True)
            self.ui.icon_circle_btn_uni_add.setEnabled(True)
            self.ui.icon_heart_btn_uni_add.setEnabled(True)
            self.ui.icon_starOut_btn_uni_add.setEnabled(True)
            self.ui.icon_starFill_btn_uni_add.setEnabled(True)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(115, 115, 115);\n"
                                                              "border-radius:10px;\n"
                                                              "border:none;\n"
                                                              "}\n"
                                                              "QPushButton:hover{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(95, 95, 95);\n"
                                                              "border-radius:5px;\n"
                                                              "}")

    def sadBtnAddUniversity(self):
        if not self.btn_sad_UniAdd:
            self.iconAddBtnUni = "sadEmoji"
            self.btn_sad_UniAdd = True
            self.ui.icon_done_btn_uni_add.setEnabled(False)
            self.ui.icon_circle_btn_uni_add.setEnabled(False)
            self.ui.icon_heart_btn_uni_add.setEnabled(False)
            self.ui.icon_starOut_btn_uni_add.setEnabled(False)
            self.ui.icon_starFill_btn_uni_add.setEnabled(False)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(170, 85, 127);\n"
                                                            "border-radius:10px;\n"
                                                            "border:none;\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(95, 95, 95);\n"
                                                            "border-radius:5px;\n"
                                                            "}")
        elif self.btn_sad_UniAdd:
            self.iconAddBtnUni = ""
            self.btn_sad_UniAdd = False
            self.ui.icon_done_btn_uni_add.setEnabled(True)
            self.ui.icon_circle_btn_uni_add.setEnabled(True)
            self.ui.icon_heart_btn_uni_add.setEnabled(True)
            self.ui.icon_starOut_btn_uni_add.setEnabled(True)
            self.ui.icon_starFill_btn_uni_add.setEnabled(True)
            self.ui.icon_circleStar_btn_uni_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_uni_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_uni_add.setStyleSheet("QPushButton{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(115, 115, 115);\n"
                                                            "border-radius:10px;\n"
                                                            "border:none;\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(95, 95, 95);\n"
                                                            "border-radius:5px;\n"
                                                            "}")

    def insertDataAddEventUniversity(self, frame):
        UniversityBackend.insert(frame, self.ui.class_lineEdit_add.text(),
                                 self.ui.textEdit_detail_add.toPlainText(), self.iconAddBtnUni,
                                 self.ui.link_lineEdit_add.text())
        HistoryBackend.insert(f"class: {self.ui.class_lineEdit_add.text()}",
                              self.ui.textEdit_detail_add.toPlainText(), "", "active")
        self.refresh_UniversityTable()

    def submitUniversityAddEvent(self):
        if len(self.ui.class_lineEdit_add.text()) != 0:
            if len(self.ui.link_lineEdit_add.text()) != 0:
                if len(self.iconAddBtnUni) != 0:
                    self.insertDataAddEventUniversity(self.frameNum_uni)
                    self.showInfo("Add", "Add was successful.")
                    self.ui.stackedWidget.setCurrentWidget(self.ui.University)
                else:
                    self.showError("Icon", "You should choose an icon.")
            else:
                self.showError("Link", "You should fill link lineEdit.")
        else:
            self.showError("Class", "You should fill class lineEdit.")

    def setInformationUniversity(self, frame):
        self.setColorIconInfoUniversity("", False)
        data = UniversityBackend.search_frame(frame)
        if frame == "1":
            self.ui.title_uni_info.setText("Saturday 6:00-8:00")
        elif frame == "2":
            self.ui.title_uni_info.setText("Saturday 8:00-10:00")
        elif frame == "3":
            self.ui.title_uni_info.setText("Saturday 10:00-12:00")
        elif frame == "4":
            self.ui.title_uni_info.setText("Saturday 12:00-14:00")
        elif frame == "5":
            self.ui.title_uni_info.setText("Saturday 14:00-16:00")
        elif frame == "6":
            self.ui.title_uni_info.setText("Saturday 16:00-18:00")
        elif frame == "7":
            self.ui.title_uni_info.setText("Saturday 18:00-20:00")
        elif frame == "8":
            self.ui.title_uni_info.setText("Saturday 20:00-22:00")
        elif frame == "9":
            self.ui.title_uni_info.setText("Saturday 22:00-24:00")
        elif frame == "10":
            self.ui.title_uni_info.setText("Sunday 6:00-8:00")
        elif frame == "11":
            self.ui.title_uni_info.setText("Sunday 8:00-10:00")
        elif frame == "12":
            self.ui.title_uni_info.setText("Sunday 10:00-12:00")
        elif frame == "13":
            self.ui.title_uni_info.setText("Sunday 12:00-14:00")
        elif frame == "14":
            self.ui.title_uni_info.setText("Sunday 14:00-16:00")
        elif frame == "15":
            self.ui.title_uni_info.setText("Sunday 16:00-18:00")
        elif frame == "16":
            self.ui.title_uni_info.setText("Sunday 18:00-20:00")
        elif frame == "17":
            self.ui.title_uni_info.setText("Sunday 20:00-22:00")
        elif frame == "18":
            self.ui.title_uni_info.setText("Sunday 22:00-24:00")
        elif frame == "19":
            self.ui.title_uni_info.setText("Monday 6:00-8:00")
        elif frame == "20":
            self.ui.title_uni_info.setText("Monday 8:00-10:00")
        elif frame == "21":
            self.ui.title_uni_info.setText("Monday 10:00-12:00")
        elif frame == "22":
            self.ui.title_uni_info.setText("Monday 12:00-14:00")
        elif frame == "23":
            self.ui.title_uni_info.setText("Monday 14:00-16:00")
        elif frame == "24":
            self.ui.title_uni_info.setText("Monday 16:00-18:00")
        elif frame == "25":
            self.ui.title_uni_info.setText("Monday 18:00-20:00")
        elif frame == "26":
            self.ui.title_uni_info.setText("Monday 20:00-22:00")
        elif frame == "27":
            self.ui.title_uni_info.setText("Monday 22:00-24:00")
        elif frame == "28":
            self.ui.title_uni_info.setText("Tuesday 6:00-8:00")
        elif frame == "29":
            self.ui.title_uni_info.setText("Tuesday 8:00-10:00")
        elif frame == "30":
            self.ui.title_uni_info.setText("Tuesday 10:00-12:00")
        elif frame == "31":
            self.ui.title_uni_info.setText("Tuesday 12:00-14:00")
        elif frame == "32":
            self.ui.title_uni_info.setText("Tuesday 14:00-16:00")
        elif frame == "33":
            self.ui.title_uni_info.setText("Tuesday 16:00-18:00")
        elif frame == "34":
            self.ui.title_uni_info.setText("Tuesday 18:00-20:00")
        elif frame == "35":
            self.ui.title_uni_info.setText("Tuesday 20:00-22:00")
        elif frame == "36":
            self.ui.title_uni_info.setText("Tuesday 22:00-24:00")
        elif frame == "37":
            self.ui.title_uni_info.setText("Wednesday 6:00-8:00")
        elif frame == "38":
            self.ui.title_uni_info.setText("Wednesday 8:00-10:00")
        elif frame == "39":
            self.ui.title_uni_info.setText("Wednesday 10:00-12:00")
        elif frame == "40":
            self.ui.title_uni_info.setText("Wednesday 12:00-14:00")
        elif frame == "41":
            self.ui.title_uni_info.setText("Wednesday 14:00-16:00")
        elif frame == "42":
            self.ui.title_uni_info.setText("Wednesday 16:00-18:00")
        elif frame == "43":
            self.ui.title_uni_info.setText("Wednesday 18:00-20:00")
        elif frame == "44":
            self.ui.title_uni_info.setText("Wednesday 20:00-22:00")
        elif frame == "45":
            self.ui.title_uni_info.setText("Wednesday 22:00-24:00")
        elif frame == "46":
            self.ui.title_uni_info.setText("Thursday 6:00-8:00")
        elif frame == "47":
            self.ui.title_uni_info.setText("Thursday 8:00-10:00")
        elif frame == "48":
            self.ui.title_uni_info.setText("Thursday 10:00-12:00")
        elif frame == "49":
            self.ui.title_uni_info.setText("Thursday 12:00-14:00")
        elif frame == "50":
            self.ui.title_uni_info.setText("Thursday 14:00-16:00")
        elif frame == "51":
            self.ui.title_uni_info.setText("Thursday 16:00-18:00")
        elif frame == "52":
            self.ui.title_uni_info.setText("Thursday 18:00-20:00")
        elif frame == "53":
            self.ui.title_uni_info.setText("Thursday 20:00-22:00")
        elif frame == "54":
            self.ui.title_uni_info.setText("Thursday 22:00-24:00")
        elif frame == "55":
            self.ui.title_uni_info.setText("Friday 6:00-8:00")
        elif frame == "56":
            self.ui.title_uni_info.setText("Friday 8:00-10:00")
        elif frame == "57":
            self.ui.title_uni_info.setText("Friday 10:00-12:00")
        elif frame == "58":
            self.ui.title_uni_info.setText("Friday 12:00-14:00")
        elif frame == "59":
            self.ui.title_uni_info.setText("Friday 14:00-16:00")
        elif frame == "60":
            self.ui.title_uni_info.setText("Friday 16:00-18:00")
        elif frame == "61":
            self.ui.title_uni_info.setText("Friday 18:00-20:00")
        elif frame == "62":
            self.ui.title_uni_info.setText("Friday 20:00-22:00")
        elif frame == "63":
            self.ui.title_uni_info.setText("Friday 22:00-24:00")
        self.ui.class_lineEdit_uni_info.setText(data[0][1])
        self.ui.textEdit_detail_uni_info.setText(data[0][2])
        self.ui.link_lineEdit_uni_info.setText(data[0][4])
        self.iconInfoBtnUni = data[0][3]
        self.setIconInfoTables(frame, data[0][3], "University")
        self.setColorIconInfoUniversity(data[0][3], True)

    def setIconInfoTables(self, frame, inputIcon, inputType):
        if frame == "1":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_1.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_1.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_1.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_1.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_1.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_1.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_1.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_1.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_1.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_1.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_1.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_1.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_1.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_1.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_1.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_1.setIcon(icon)
        elif frame == "2":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_2.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_2.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_2.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_2.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_2.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_2.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_2.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_2.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_2.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_2.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_2.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_2.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_2.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_2.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_2.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_2.setIcon(icon)
        elif frame == "3":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_3.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_3.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_3.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_3.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_3.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_3.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_3.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_3.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_3.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_3.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_3.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_3.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_3.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_3.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_3.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_3.setIcon(icon)
        elif frame == "4":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_4.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_4.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_4.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_4.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_4.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_4.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_4.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_4.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_4.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_4.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_4.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_4.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_4.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_4.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_4.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_4.setIcon(icon)
        elif frame == "5":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_5.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_5.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_5.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_5.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_5.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_5.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_5.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_5.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_5.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_5.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_5.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_5.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_5.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_5.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_5.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_5.setIcon(icon)
        elif frame == "6":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_6.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_6.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_6.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_6.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_6.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_6.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_6.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_6.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_6.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_6.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_6.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_6.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_6.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_6.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_6.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_6.setIcon(icon)
        elif frame == "7":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_7.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_7.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_7.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_7.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_7.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_7.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_7.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_7.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_7.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_7.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_7.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_7.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_7.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_7.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_7.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_7.setIcon(icon)
        elif frame == "8":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_8.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_8.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_8.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_8.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_8.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_8.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_8.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_8.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_8.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_8.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_8.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_8.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_8.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_8.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_8.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_8.setIcon(icon)
        elif frame == "9":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_9.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_9.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_9.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_9.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_9.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_9.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_9.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_9.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_9.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_9.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_9.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_9.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_9.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_9.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_9.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_9.setIcon(icon)
        elif frame == "10":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_10.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_10.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_10.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_10.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_10.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_10.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_10.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_10.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_10.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_10.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_10.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_10.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_10.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_10.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_10.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_10.setIcon(icon)
        elif frame == "11":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_11.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_11.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_11.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_11.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_11.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_11.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_11.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_11.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_11.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_11.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_11.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_11.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_11.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_11.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_11.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_11.setIcon(icon)
        elif frame == "12":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_12.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_12.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_12.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_12.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_12.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_12.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_12.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_12.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_12.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_12.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_12.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_12.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_12.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_12.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_12.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_12.setIcon(icon)
        elif frame == "13":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_13.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_13.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_13.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_13.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_13.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_13.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_13.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_13.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_13.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_13.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_13.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_13.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_13.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_13.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_13.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_13.setIcon(icon)
        elif frame == "14":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_14.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_14.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_14.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_14.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_14.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_14.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_14.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_14.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_14.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_14.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_14.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_14.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_14.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_14.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_14.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_14.setIcon(icon)
        elif frame == "15":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_15.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_15.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_15.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_15.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_15.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_15.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_15.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_15.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_15.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_15.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_15.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_15.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_15.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_15.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_15.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_15.setIcon(icon)
        elif frame == "16":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_16.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_16.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_16.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_16.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_16.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_16.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_16.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_16.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_16.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_16.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_16.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_16.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_16.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_16.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_16.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_16.setIcon(icon)
        elif frame == "17":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_17.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_17.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_17.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_17.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_17.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_17.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_17.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_17.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_17.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_17.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_17.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_17.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_17.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_17.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_17.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_17.setIcon(icon)
        elif frame == "18":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_18.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_18.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_18.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_18.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_18.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_18.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_18.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_18.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_18.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_18.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_18.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_18.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_18.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_18.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_18.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_18.setIcon(icon)
        elif frame == "19":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_19.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_19.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_19.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_19.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_19.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_19.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_19.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_19.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_19.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_19.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_19.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_19.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_19.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_19.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_19.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_19.setIcon(icon)
        elif frame == "20":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_20.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_20.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_20.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_20.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_20.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_20.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_20.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_20.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_20.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_20.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_20.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_20.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_20.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_20.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_20.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_20.setIcon(icon)
        elif frame == "21":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_21.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_21.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_21.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_21.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_21.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_21.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_21.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_21.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_21.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_21.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_21.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_21.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_21.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_21.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_21.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_21.setIcon(icon)
        elif frame == "22":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_22.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_22.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_22.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_22.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_22.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_22.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_22.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_22.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_22.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_22.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_22.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_22.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_22.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_22.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_22.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_22.setIcon(icon)
        elif frame == "23":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_23.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_23.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_23.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_23.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_23.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_23.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_23.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_23.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_23.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_23.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_23.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_23.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_23.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_23.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_23.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_23.setIcon(icon)
        elif frame == "24":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_24.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_24.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_24.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_24.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_24.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_24.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_24.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_24.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_24.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_24.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_24.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_24.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_24.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_24.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_24.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_24.setIcon(icon)
        elif frame == "25":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_25.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_25.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_25.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_25.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_25.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_25.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_25.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_25.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_25.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_25.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_25.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_25.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_25.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_25.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_25.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_25.setIcon(icon)
        elif frame == "26":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_26.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_26.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_26.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_26.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_26.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_26.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_26.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_26.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_26.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_26.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_26.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_26.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_26.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_26.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_26.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_26.setIcon(icon)
        elif frame == "27":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_27.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_27.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_27.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_27.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_27.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_27.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_27.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_27.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_27.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_27.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_27.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_27.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_27.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_27.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_27.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_27.setIcon(icon)
        elif frame == "28":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_28.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_28.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_28.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_28.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_28.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_28.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_28.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_28.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_28.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_28.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_28.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_28.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_28.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_28.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_28.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_28.setIcon(icon)
        elif frame == "29":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_29.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_29.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_29.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_29.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_29.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_29.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_29.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_29.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_29.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_29.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_29.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_29.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_29.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_29.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_29.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_29.setIcon(icon)
        elif frame == "30":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_30.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_30.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_30.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_30.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_30.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_30.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_30.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_30.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_30.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_30.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_30.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_30.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_30.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_30.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_30.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_30.setIcon(icon)
        elif frame == "31":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_31.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_31.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_31.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_31.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_31.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_31.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_31.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_31.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_31.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_31.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_31.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_31.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_31.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_31.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_31.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_31.setIcon(icon)
        elif frame == "32":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_32.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_32.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_32.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_32.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_32.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_32.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_32.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_32.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_32.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_32.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_32.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_32.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_32.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_32.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_32.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_32.setIcon(icon)
        elif frame == "33":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_33.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_33.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_33.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_33.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_33.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_33.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_33.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_33.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_33.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_33.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_33.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_33.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_33.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_33.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_33.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_33.setIcon(icon)
        elif frame == "34":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_34.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_34.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_34.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_34.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_34.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_34.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_34.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_34.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_34.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_34.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_34.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_34.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_34.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_34.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_34.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_34.setIcon(icon)
        elif frame == "35":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_35.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_35.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_35.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_35.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_35.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_35.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_35.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_35.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_35.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_35.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_35.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_35.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_35.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_35.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_35.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_35.setIcon(icon)
        elif frame == "36":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_36.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_36.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_36.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_36.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_36.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_36.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_36.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_36.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_36.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_36.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_36.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_36.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_36.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_36.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_36.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_36.setIcon(icon)
        elif frame == "37":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_37.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_37.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_37.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_37.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_37.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_37.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_37.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_37.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_37.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_37.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_37.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_37.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_37.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_37.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_37.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_37.setIcon(icon)
        elif frame == "38":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_38.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_38.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_38.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_38.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_38.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_38.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_38.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_38.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_38.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_38.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_38.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_38.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_38.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_38.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_38.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_38.setIcon(icon)
        elif frame == "39":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_39.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_39.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_39.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_39.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_39.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_39.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_39.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_39.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_39.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_39.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_39.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_39.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_39.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_39.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_39.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_39.setIcon(icon)
        elif frame == "40":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_40.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_40.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_40.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_40.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_40.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_40.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_40.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_40.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_40.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_40.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_40.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_40.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_40.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_40.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_40.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_40.setIcon(icon)
        elif frame == "41":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_41.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_41.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_41.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_41.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_41.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_41.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_41.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_41.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_41.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_41.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_41.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_41.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_41.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_41.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_41.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_41.setIcon(icon)
        elif frame == "42":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_42.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_42.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_42.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_42.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_42.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_42.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_42.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_42.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_42.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_42.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_42.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_42.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_42.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_42.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_42.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_42.setIcon(icon)
        elif frame == "43":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_43.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_43.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_43.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_43.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_43.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_43.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_43.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_43.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_43.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_43.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_43.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_43.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_43.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_43.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_43.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_43.setIcon(icon)
        elif frame == "44":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_44.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_44.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_44.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_44.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_44.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_44.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_44.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_44.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_44.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_44.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_44.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_44.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_44.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_44.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_44.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_44.setIcon(icon)
        elif frame == "45":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_45.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_45.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_45.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_45.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_45.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_45.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_45.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_45.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_45.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_45.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_45.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_45.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_45.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_45.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_45.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_45.setIcon(icon)
        elif frame == "46":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_46.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_46.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_46.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_46.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_46.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_46.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_46.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_46.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_46.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_46.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_46.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_46.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_46.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_46.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_46.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_46.setIcon(icon)
        elif frame == "47":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_47.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_47.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_47.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_47.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_47.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_47.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_47.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_47.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_47.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_47.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_47.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_47.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_47.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_47.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_47.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_47.setIcon(icon)
        elif frame == "48":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_48.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_48.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_48.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_48.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_48.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_48.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_48.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_48.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_48.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_48.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_48.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_48.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_48.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_48.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_48.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_48.setIcon(icon)
        elif frame == "49":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_49.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_49.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_49.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_49.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_49.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_49.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_49.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_49.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_49.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_49.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_49.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_49.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_49.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_49.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_49.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_49.setIcon(icon)
        elif frame == "50":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_50.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_50.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_50.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_50.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_50.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_50.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_50.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_50.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_50.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_50.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_50.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_50.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_50.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_50.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_50.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_50.setIcon(icon)
        elif frame == "51":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_51.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_51.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_51.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_51.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_51.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_51.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_51.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_51.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_51.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_51.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_51.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_51.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_51.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_51.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_51.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_51.setIcon(icon)
        elif frame == "52":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_52.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_52.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_52.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_52.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_52.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_52.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_52.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_52.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_52.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_52.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_52.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_52.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_52.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_52.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_52.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_52.setIcon(icon)
        elif frame == "53":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_53.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_53.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_53.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_53.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_53.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_53.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_53.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_53.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_53.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_53.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_53.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_53.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_53.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_53.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_53.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_53.setIcon(icon)
        elif frame == "54":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_54.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_54.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_54.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_54.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_54.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_54.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_54.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_54.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_54.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_54.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_54.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_54.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_54.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_54.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_54.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_54.setIcon(icon)
        elif frame == "55":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_55.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_55.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_55.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_55.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_55.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_55.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_55.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_55.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_55.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_55.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_55.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_55.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_55.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_55.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_55.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_55.setIcon(icon)
        elif frame == "56":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_56.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_56.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_56.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_56.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_56.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_56.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_56.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_56.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_56.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_56.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_56.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_56.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_56.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_56.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_56.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_56.setIcon(icon)
        elif frame == "57":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_57.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_57.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_57.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_57.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_57.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_57.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_57.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_57.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_57.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_57.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_57.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_57.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_57.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_57.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_57.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_57.setIcon(icon)
        elif frame == "58":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_58.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_58.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_58.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_58.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_58.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_58.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_58.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_58.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_58.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_58.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_58.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_58.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_58.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_58.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_58.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_58.setIcon(icon)
        elif frame == "59":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_59.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_59.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_59.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_59.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_59.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_59.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_59.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_59.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_59.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_59.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_59.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_59.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_59.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_59.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_59.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_59.setIcon(icon)
        elif frame == "60":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_60.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_60.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_60.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_60.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_60.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_60.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_60.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_60.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_60.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_60.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_60.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_60.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_60.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_60.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_60.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_60.setIcon(icon)
        elif frame == "61":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_61.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_61.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_61.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_61.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_61.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_61.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_61.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_61.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_61.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_61.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_61.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_61.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_61.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_61.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_61.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_61.setIcon(icon)
        elif frame == "62":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_62.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_62.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_62.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_62.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_62.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_62.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_62.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_62.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_62.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_62.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_62.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_62.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_62.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_62.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_62.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_62.setIcon(icon)
        elif frame == "63":
            if inputIcon == "done":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_done_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_63.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_63.setIcon(icon)
            elif inputIcon == "heart":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_favorite_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_63.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_63.setIcon(icon)
            elif inputIcon == "starOutline":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_outline_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_63.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_63.setIcon(icon)
            elif inputIcon == "starFill":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_star_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_63.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_63.setIcon(icon)
            elif inputIcon == "circle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_circle_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_63.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_63.setIcon(icon)
            elif inputIcon == "starCircle":
                icon = QIcon()
                icon.addPixmap(
                    QPixmap("photo/outline_stars_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_63.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_63.setIcon(icon)
            elif inputIcon == "smileEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_satisfied_alt_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_63.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_63.setIcon(icon)
            elif inputIcon == "sadEmoji":
                icon = QIcon()
                icon.addPixmap(QPixmap(
                    "photo/outline_sentiment_dissatisfied_black_24dp.png"), QIcon.Normal, QIcon.Off)
                if inputType == "University":
                    self.ui.uni_btn_63.setIcon(icon)
                elif inputType == "Table":
                    self.ui.table_btn_63.setIcon(icon)

    def setColorIconInfoUniversity(self, inputIcon, state):
        if state:
            if inputIcon == "done":
                self.ui.icon_done_btn.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(170, 85, 127);\n"
                                                    "border-radius:10px;\n"
                                                    "border:none;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")
            elif inputIcon == "heart":
                self.ui.icon_heart_btn.setStyleSheet("QPushButton{\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "    background-color: rgb(170, 85, 127);\n"
                                                     "border-radius:10px;\n"
                                                     "border:none;\n"
                                                     "}\n"
                                                     "QPushButton:hover{\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "    background-color: rgb(95, 95, 95);\n"
                                                     "border-radius:5px;\n"
                                                     "}")
            elif inputIcon == "starOutline":
                self.ui.icon_starOut_btn.setStyleSheet("QPushButton{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(170, 85, 127);\n"
                                                       "border-radius:10px;\n"
                                                       "border:none;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(95, 95, 95);\n"
                                                       "border-radius:5px;\n"
                                                       "}")
            elif inputIcon == "starFill":
                self.ui.icon_starFill_btn.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(170, 85, 127);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")
            elif inputIcon == "circle":
                self.ui.icon_circle_btn.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(170, 85, 127);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
            elif inputIcon == "starCircle":
                self.ui.icon_circleStar_btn.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(170, 85, 127);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")
            elif inputIcon == "smileEmoji":
                self.ui.icon_smileEmoji_btn.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(170, 85, 127);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")
            elif inputIcon == "sadEmoji":
                self.ui.icon_sadEmoji_btn.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(170, 85, 127);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")
        else:
            self.ui.icon_done_btn.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(115, 115, 115);\n"
                                                "border-radius:10px;\n"
                                                "border:none;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:5px;\n"
                                                "}")
            self.ui.icon_heart_btn.setStyleSheet("QPushButton{\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgb(115, 115, 115);\n"
                                                 "border-radius:10px;\n"
                                                 "border:none;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgb(95, 95, 95);\n"
                                                 "border-radius:5px;\n"
                                                 "}")
            self.ui.icon_starOut_btn.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(115, 115, 115);\n"
                                                   "border-radius:10px;\n"
                                                   "border:none;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(95, 95, 95);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
            self.ui.icon_starFill_btn.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(115, 115, 115);\n"
                                                    "border-radius:10px;\n"
                                                    "border:none;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")
            self.ui.icon_circle_btn.setStyleSheet("QPushButton{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(115, 115, 115);\n"
                                                  "border-radius:10px;\n"
                                                  "border:none;\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(95, 95, 95);\n"
                                                  "border-radius:5px;\n"
                                                  "}")
            self.ui.icon_circleStar_btn.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(115, 115, 115);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
            self.ui.icon_smileEmoji_btn.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(115, 115, 115);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
            self.ui.icon_sadEmoji_btn.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(115, 115, 115);\n"
                                                    "border-radius:10px;\n"
                                                    "border:none;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")

    def refresh_UniversityTable(self):
        for i in range(1, 64):
            data = UniversityBackend.search_frame(str(i))
            if len(data) != 0:
                self.setInformationUniversity(str(i))

    @staticmethod
    def checkEmptyUni(frame):
        search = UniversityBackend.search_frame(frame)
        if len(search) == 0:
            return True
        else:
            return False

    def askForBuildEvent(self):
        info = QMessageBox.question(
            self, "Add Event", "Do you want to open event ?", QMessageBox.Yes | QMessageBox.No)
        if info == QMessageBox.Yes:
            return True
        else:
            return False

    def deleteIconEventUniversity(self):
        icon = QIcon()
        icon.addPixmap(QPixmap(), QIcon.Normal, QIcon.Off)
        if self.frameNum_uni == "1":
            self.ui.uni_btn_1.setIcon(icon)
        elif self.frameNum_uni == "2":
            self.ui.uni_btn_2.setIcon(icon)
        elif self.frameNum_uni == "3":
            self.ui.uni_btn_3.setIcon(icon)
        elif self.frameNum_uni == "4":
            self.ui.uni_btn_4.setIcon(icon)
        elif self.frameNum_uni == "5":
            self.ui.uni_btn_5.setIcon(icon)
        elif self.frameNum_uni == "6":
            self.ui.uni_btn_6.setIcon(icon)
        elif self.frameNum_uni == "7":
            self.ui.uni_btn_7.setIcon(icon)
        elif self.frameNum_uni == "8":
            self.ui.uni_btn_8.setIcon(icon)
        elif self.frameNum_uni == "9":
            self.ui.uni_btn_9.setIcon(icon)
        elif self.frameNum_uni == "10":
            self.ui.uni_btn_10.setIcon(icon)
        elif self.frameNum_uni == "11":
            self.ui.uni_btn_11.setIcon(icon)
        elif self.frameNum_uni == "12":
            self.ui.uni_btn_12.setIcon(icon)
        elif self.frameNum_uni == "13":
            self.ui.uni_btn_13.setIcon(icon)
        elif self.frameNum_uni == "14":
            self.ui.uni_btn_14.setIcon(icon)
        elif self.frameNum_uni == "15":
            self.ui.uni_btn_15.setIcon(icon)
        elif self.frameNum_uni == "16":
            self.ui.uni_btn_16.setIcon(icon)
        elif self.frameNum_uni == "17":
            self.ui.uni_btn_17.setIcon(icon)
        elif self.frameNum_uni == "18":
            self.ui.uni_btn_18.setIcon(icon)
        elif self.frameNum_uni == "19":
            self.ui.uni_btn_19.setIcon(icon)
        elif self.frameNum_uni == "20":
            self.ui.uni_btn_20.setIcon(icon)
        elif self.frameNum_uni == "21":
            self.ui.uni_btn_21.setIcon(icon)
        elif self.frameNum_uni == "22":
            self.ui.uni_btn_22.setIcon(icon)
        elif self.frameNum_uni == "23":
            self.ui.uni_btn_23.setIcon(icon)
        elif self.frameNum_uni == "24":
            self.ui.uni_btn_24.setIcon(icon)
        elif self.frameNum_uni == "25":
            self.ui.uni_btn_25.setIcon(icon)
        elif self.frameNum_uni == "26":
            self.ui.uni_btn_26.setIcon(icon)
        elif self.frameNum_uni == "27":
            self.ui.uni_btn_27.setIcon(icon)
        elif self.frameNum_uni == "28":
            self.ui.uni_btn_28.setIcon(icon)
        elif self.frameNum_uni == "29":
            self.ui.uni_btn_29.setIcon(icon)
        elif self.frameNum_uni == "30":
            self.ui.uni_btn_30.setIcon(icon)
        elif self.frameNum_uni == "31":
            self.ui.uni_btn_31.setIcon(icon)
        elif self.frameNum_uni == "32":
            self.ui.uni_btn_32.setIcon(icon)
        elif self.frameNum_uni == "33":
            self.ui.uni_btn_33.setIcon(icon)
        elif self.frameNum_uni == "34":
            self.ui.uni_btn_34.setIcon(icon)
        elif self.frameNum_uni == "35":
            self.ui.uni_btn_35.setIcon(icon)
        elif self.frameNum_uni == "36":
            self.ui.uni_btn_36.setIcon(icon)
        elif self.frameNum_uni == "37":
            self.ui.uni_btn_37.setIcon(icon)
        elif self.frameNum_uni == "38":
            self.ui.uni_btn_38.setIcon(icon)
        elif self.frameNum_uni == "39":
            self.ui.uni_btn_39.setIcon(icon)
        elif self.frameNum_uni == "40":
            self.ui.uni_btn_40.setIcon(icon)
        elif self.frameNum_uni == "41":
            self.ui.uni_btn_41.setIcon(icon)
        elif self.frameNum_uni == "42":
            self.ui.uni_btn_42.setIcon(icon)
        elif self.frameNum_uni == "43":
            self.ui.uni_btn_43.setIcon(icon)
        elif self.frameNum_uni == "44":
            self.ui.uni_btn_44.setIcon(icon)
        elif self.frameNum_uni == "45":
            self.ui.uni_btn_45.setIcon(icon)
        elif self.frameNum_uni == "46":
            self.ui.uni_btn_46.setIcon(icon)
        elif self.frameNum_uni == "47":
            self.ui.uni_btn_47.setIcon(icon)
        elif self.frameNum_uni == "48":
            self.ui.uni_btn_48.setIcon(icon)
        elif self.frameNum_uni == "49":
            self.ui.uni_btn_49.setIcon(icon)
        elif self.frameNum_uni == "50":
            self.ui.uni_btn_50.setIcon(icon)
        elif self.frameNum_uni == "51":
            self.ui.uni_btn_51.setIcon(icon)
        elif self.frameNum_uni == "52":
            self.ui.uni_btn_52.setIcon(icon)
        elif self.frameNum_uni == "53":
            self.ui.uni_btn_53.setIcon(icon)
        elif self.frameNum_uni == "54":
            self.ui.uni_btn_54.setIcon(icon)
        elif self.frameNum_uni == "55":
            self.ui.uni_btn_55.setIcon(icon)
        elif self.frameNum_uni == "56":
            self.ui.uni_btn_56.setIcon(icon)
        elif self.frameNum_uni == "57":
            self.ui.uni_btn_57.setIcon(icon)
        elif self.frameNum_uni == "58":
            self.ui.uni_btn_58.setIcon(icon)
        elif self.frameNum_uni == "59":
            self.ui.uni_btn_59.setIcon(icon)
        elif self.frameNum_uni == "60":
            self.ui.uni_btn_60.setIcon(icon)
        elif self.frameNum_uni == "61":
            self.ui.uni_btn_61.setIcon(icon)
        elif self.frameNum_uni == "62":
            self.ui.uni_btn_62.setIcon(icon)
        elif self.frameNum_uni == "63":
            self.ui.uni_btn_63.setIcon(icon)

    @staticmethod
    def deleteProcessUniversity(frame):
        data = UniversityBackend.search_frame(frame)
        HistoryBackend.insert(
            f"class: {data[0][1]}", data[0][2], "", "deleted")
        UniversityBackend.delete(frame)

    def deleteEventUniversity(self):
        ques = QMessageBox.question(
            self, "Delete", "Are you sure ?", QMessageBox.Yes | QMessageBox.No)
        if ques == QMessageBox.Yes:
            self.deleteProcessUniversity(self.frameNum_uni)
            self.refresh_UniversityTable()
            self.ui.stackedWidget.setCurrentWidget(self.ui.University)
            self.deleteIconEventUniversity()

    def setEnableObjEditUniversity(self, state):
        if state:
            data = UniversityBackend.search_frame(self.frameNum_uni)
            self.ui.clear_btn_uni.setEnabled(True)
            self.ui.submit_btn_uni.setEnabled(True)
            self.ui.class_lineEdit_uni_info.setReadOnly(False)
            self.ui.textEdit_detail_uni_info.setReadOnly(False)
            self.ui.link_lineEdit_uni_info.setReadOnly(False)
            if data[0][3] == "done":
                self.ui.icon_done_btn.setEnabled(True)
            elif data[0][3] == "heart":
                self.ui.icon_heart_btn.setEnabled(True)
            elif data[0][3] == "starOutline":
                self.ui.icon_starOut_btn.setEnabled(True)
            elif data[0][3] == "starFill":
                self.ui.icon_starFill_btn.setEnabled(True)
            elif data[0][3] == "circle":
                self.ui.icon_circle_btn.setEnabled(True)
            elif data[0][3] == "starCircle":
                self.ui.icon_circleStar_btn.setEnabled(True)
            elif data[0][3] == "smileEmoji":
                self.ui.icon_smileEmoji_btn.setEnabled(True)
            elif data[0][3] == "sadEmoji":
                self.ui.icon_sadEmoji_btn.setEnabled(True)
        else:
            self.ui.clear_btn_uni.setEnabled(False)
            self.ui.submit_btn_uni.setEnabled(False)
            self.ui.class_lineEdit_uni_info.setReadOnly(True)
            self.ui.textEdit_detail_uni_info.setReadOnly(True)
            self.ui.link_lineEdit_uni_info.setReadOnly(True)
            self.ui.icon_done_btn.setEnabled(False)
            self.ui.icon_heart_btn.setEnabled(False)
            self.ui.icon_starOut_btn.setEnabled(False)
            self.ui.icon_starFill_btn.setEnabled(False)
            self.ui.icon_circle_btn.setEnabled(False)
            self.ui.icon_circleStar_btn.setEnabled(False)
            self.ui.icon_smileEmoji_btn.setEnabled(False)
            self.ui.icon_sadEmoji_btn.setEnabled(False)

    def editEventUniversity(self):
        if self.stateEditUni == "Disable":
            self.ui.edit_btn_uni.setStyleSheet("QPushButton{\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "    \n"
                                               "    background-color: rgb(12, 182, 0);\n"
                                               "border-radius:10px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "    background-color: rgb(95, 95, 95);\n"
                                               "border-radius:5px;\n"
                                               "}")
            self.setEnableObjEditUniversity(True)
            self.stateEditUni = "Enable"
        elif self.stateEditUni == "Enable":
            self.ui.edit_btn_uni.setStyleSheet("QPushButton{\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "    \n"
                                               "    background-color: rgb(115, 115, 115);\n"
                                               "border-radius:10px;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "    background-color: rgb(95, 95, 95);\n"
                                               "border-radius:5px;\n"
                                               "}")
            self.setEnableObjEditUniversity(False)
            self.stateEditUni = "Disable"

    def doneBtnInfoUniversity(self):
        if not self.btn_done_UniInfo:
            self.iconInfoBtnUni = "done"
            self.btn_done_UniInfo = True
            self.ui.icon_smileEmoji_btn.setEnabled(False)
            self.ui.icon_sadEmoji_btn.setEnabled(False)
            self.ui.icon_circleStar_btn.setEnabled(False)
            self.ui.icon_circle_btn.setEnabled(False)
            self.ui.icon_starFill_btn.setEnabled(False)
            self.ui.icon_starOut_btn.setEnabled(False)
            self.ui.icon_heart_btn.setEnabled(False)
            self.ui.icon_done_btn.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(170, 85, 127);\n"
                                                "border-radius:10px;\n"
                                                "border:none;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:5px;\n"
                                                "}")
        elif self.btn_done_UniInfo:
            self.iconInfoBtnUni = ""
            self.btn_done_UniInfo = False
            self.ui.icon_smileEmoji_btn.setEnabled(True)
            self.ui.icon_sadEmoji_btn.setEnabled(True)
            self.ui.icon_circleStar_btn.setEnabled(True)
            self.ui.icon_circle_btn.setEnabled(True)
            self.ui.icon_starFill_btn.setEnabled(True)
            self.ui.icon_starOut_btn.setEnabled(True)
            self.ui.icon_heart_btn.setEnabled(True)
            self.ui.icon_done_btn.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(115, 115, 115);\n"
                                                "border-radius:10px;\n"
                                                "border:none;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:5px;\n"
                                                "}")

    def heartBtnInfoUniversity(self):
        if not self.btn_heart_UniInfo:
            self.iconInfoBtnUni = "heart"
            self.btn_heart_UniInfo = True
            self.ui.icon_done_btn.setEnabled(False)
            self.ui.icon_smileEmoji_btn.setEnabled(False)
            self.ui.icon_sadEmoji_btn.setEnabled(False)
            self.ui.icon_circleStar_btn.setEnabled(False)
            self.ui.icon_circle_btn.setEnabled(False)
            self.ui.icon_starFill_btn.setEnabled(False)
            self.ui.icon_starOut_btn.setEnabled(False)
            self.ui.icon_heart_btn.setStyleSheet("QPushButton{\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgb(170, 85, 127);\n"
                                                 "border-radius:10px;\n"
                                                 "border:none;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgb(95, 95, 95);\n"
                                                 "border-radius:5px;\n"
                                                 "}")
        elif self.btn_heart_UniInfo:
            self.iconInfoBtnUni = ""
            self.btn_heart_UniInfo = False
            self.ui.icon_done_btn.setEnabled(True)
            self.ui.icon_smileEmoji_btn.setEnabled(True)
            self.ui.icon_sadEmoji_btn.setEnabled(True)
            self.ui.icon_circleStar_btn.setEnabled(True)
            self.ui.icon_circle_btn.setEnabled(True)
            self.ui.icon_starFill_btn.setEnabled(True)
            self.ui.icon_starOut_btn.setEnabled(True)
            self.ui.icon_heart_btn.setStyleSheet("QPushButton{\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgb(115, 115, 115);\n"
                                                 "border-radius:10px;\n"
                                                 "border:none;\n"
                                                 "}\n"
                                                 "QPushButton:hover{\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    background-color: rgb(95, 95, 95);\n"
                                                 "border-radius:5px;\n"
                                                 "}")

    def starOutBtnInfoUniversity(self):
        if not self.btn_starOut_UniInfo:
            self.iconInfoBtnUni = "starOutline"
            self.btn_starOut_UniInfo = True
            self.ui.icon_done_btn.setEnabled(False)
            self.ui.icon_heart_btn.setEnabled(False)
            self.ui.icon_smileEmoji_btn.setEnabled(False)
            self.ui.icon_sadEmoji_btn.setEnabled(False)
            self.ui.icon_circleStar_btn.setEnabled(False)
            self.ui.icon_circle_btn.setEnabled(False)
            self.ui.icon_starFill_btn.setEnabled(False)
            self.ui.icon_starOut_btn.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(170, 85, 127);\n"
                                                   "border-radius:10px;\n"
                                                   "border:none;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(95, 95, 95);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
        elif self.btn_starOut_UniInfo:
            self.iconInfoBtnUni = ""
            self.btn_starOut_UniInfo = False
            self.ui.icon_done_btn.setEnabled(True)
            self.ui.icon_heart_btn.setEnabled(True)
            self.ui.icon_smileEmoji_btn.setEnabled(True)
            self.ui.icon_sadEmoji_btn.setEnabled(True)
            self.ui.icon_circleStar_btn.setEnabled(True)
            self.ui.icon_circle_btn.setEnabled(True)
            self.ui.icon_starFill_btn.setEnabled(True)
            self.ui.icon_starOut_btn.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(115, 115, 115);\n"
                                                   "border-radius:10px;\n"
                                                   "border:none;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(95, 95, 95);\n"
                                                   "border-radius:5px;\n"
                                                   "}")

    def starFillBtnInfoUniversity(self):
        if not self.btn_starFill_UniInfo:
            self.iconInfoBtnUni = "starFill"
            self.btn_starFill_UniInfo = True
            self.ui.icon_done_btn.setEnabled(False)
            self.ui.icon_heart_btn.setEnabled(False)
            self.ui.icon_starOut_btn.setEnabled(False)
            self.ui.icon_smileEmoji_btn.setEnabled(False)
            self.ui.icon_sadEmoji_btn.setEnabled(False)
            self.ui.icon_circleStar_btn.setEnabled(False)
            self.ui.icon_circle_btn.setEnabled(False)
            self.ui.icon_starFill_btn.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(170, 85, 127);\n"
                                                    "border-radius:10px;\n"
                                                    "border:none;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")
        elif self.btn_starFill_UniInfo:
            self.iconInfoBtnUni = ""
            self.btn_starFill_UniInfo = False
            self.ui.icon_done_btn.setEnabled(True)
            self.ui.icon_heart_btn.setEnabled(True)
            self.ui.icon_starOut_btn.setEnabled(True)
            self.ui.icon_smileEmoji_btn.setEnabled(True)
            self.ui.icon_sadEmoji_btn.setEnabled(True)
            self.ui.icon_circleStar_btn.setEnabled(True)
            self.ui.icon_circle_btn.setEnabled(True)
            self.ui.icon_starFill_btn.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(115, 115, 115);\n"
                                                    "border-radius:10px;\n"
                                                    "border:none;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")

    def circleBtnInfoUniversity(self):
        if not self.btn_circle_UniInfo:
            self.iconInfoBtnUni = "circle"
            self.btn_circle_UniInfo = True
            self.ui.icon_done_btn.setEnabled(False)
            self.ui.icon_heart_btn.setEnabled(False)
            self.ui.icon_starOut_btn.setEnabled(False)
            self.ui.icon_starFill_btn.setEnabled(False)
            self.ui.icon_smileEmoji_btn.setEnabled(False)
            self.ui.icon_sadEmoji_btn.setEnabled(False)
            self.ui.icon_circleStar_btn.setEnabled(False)
            self.ui.icon_circle_btn.setStyleSheet("QPushButton{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(170, 85, 127);\n"
                                                  "border-radius:10px;\n"
                                                  "border:none;\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(95, 95, 95);\n"
                                                  "border-radius:5px;\n"
                                                  "}")
        elif self.btn_circle_UniInfo:
            self.iconInfoBtnUni = ""
            self.btn_circle_UniInfo = False
            self.ui.icon_done_btn.setEnabled(True)
            self.ui.icon_heart_btn.setEnabled(True)
            self.ui.icon_starOut_btn.setEnabled(True)
            self.ui.icon_starFill_btn.setEnabled(True)
            self.ui.icon_smileEmoji_btn.setEnabled(True)
            self.ui.icon_sadEmoji_btn.setEnabled(True)
            self.ui.icon_circleStar_btn.setEnabled(True)
            self.ui.icon_circle_btn.setStyleSheet("QPushButton{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(115, 115, 115);\n"
                                                  "border-radius:10px;\n"
                                                  "border:none;\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(95, 95, 95);\n"
                                                  "border-radius:5px;\n"
                                                  "}")

    def starCircleBtnInfoUniversity(self):
        if not self.btn_starCircle_UniInfo:
            self.iconInfoBtnUni = "starCircle"
            self.btn_starCircle_UniInfo = True
            self.ui.icon_done_btn.setEnabled(False)
            self.ui.icon_circle_btn.setEnabled(False)
            self.ui.icon_heart_btn.setEnabled(False)
            self.ui.icon_starOut_btn.setEnabled(False)
            self.ui.icon_starFill_btn.setEnabled(False)
            self.ui.icon_smileEmoji_btn.setEnabled(False)
            self.ui.icon_sadEmoji_btn.setEnabled(False)
            self.ui.icon_circleStar_btn.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(170, 85, 127);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
        elif self.btn_starCircle_UniInfo:
            self.iconInfoBtnUni = ""
            self.btn_starCircle_UniInfo = False
            self.ui.icon_done_btn.setEnabled(True)
            self.ui.icon_circle_btn.setEnabled(True)
            self.ui.icon_heart_btn.setEnabled(True)
            self.ui.icon_starOut_btn.setEnabled(True)
            self.ui.icon_starFill_btn.setEnabled(True)
            self.ui.icon_smileEmoji_btn.setEnabled(True)
            self.ui.icon_sadEmoji_btn.setEnabled(True)
            self.ui.icon_circleStar_btn.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(115, 115, 115);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")

    def smileBtnInfoUniversity(self):
        if not self.btn_smile_UniInfo:
            self.iconInfoBtnUni = "smileEmoji"
            self.btn_smile_UniInfo = True
            self.ui.icon_done_btn.setEnabled(False)
            self.ui.icon_circle_btn.setEnabled(False)
            self.ui.icon_heart_btn.setEnabled(False)
            self.ui.icon_starOut_btn.setEnabled(False)
            self.ui.icon_starFill_btn.setEnabled(False)
            self.ui.icon_circleStar_btn.setEnabled(False)
            self.ui.icon_sadEmoji_btn.setEnabled(False)
            self.ui.icon_smileEmoji_btn.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(170, 85, 127);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
        elif self.btn_smile_UniInfo:
            self.iconInfoBtnUni = ""
            self.btn_smile_UniInfo = False
            self.ui.icon_done_btn.setEnabled(True)
            self.ui.icon_circle_btn.setEnabled(True)
            self.ui.icon_heart_btn.setEnabled(True)
            self.ui.icon_starOut_btn.setEnabled(True)
            self.ui.icon_starFill_btn.setEnabled(True)
            self.ui.icon_circleStar_btn.setEnabled(True)
            self.ui.icon_sadEmoji_btn.setEnabled(True)
            self.ui.icon_smileEmoji_btn.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(115, 115, 115);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")

    def sadBtnInfoUniversity(self):
        if not self.btn_sad_UniInfo:
            self.iconInfoBtnUni = "sadEmoji"
            self.btn_sad_UniInfo = True
            self.ui.icon_done_btn.setEnabled(False)
            self.ui.icon_circle_btn.setEnabled(False)
            self.ui.icon_heart_btn.setEnabled(False)
            self.ui.icon_starOut_btn.setEnabled(False)
            self.ui.icon_starFill_btn.setEnabled(False)
            self.ui.icon_circleStar_btn.setEnabled(False)
            self.ui.icon_smileEmoji_btn.setEnabled(False)
            self.ui.icon_sadEmoji_btn.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(170, 85, 127);\n"
                                                    "border-radius:10px;\n"
                                                    "border:none;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")
        elif self.btn_sad_UniInfo:
            self.iconInfoBtnUni = ""
            self.btn_sad_UniInfo = False
            self.ui.icon_done_btn.setEnabled(True)
            self.ui.icon_circle_btn.setEnabled(True)
            self.ui.icon_heart_btn.setEnabled(True)
            self.ui.icon_starOut_btn.setEnabled(True)
            self.ui.icon_starFill_btn.setEnabled(True)
            self.ui.icon_circleStar_btn.setEnabled(True)
            self.ui.icon_smileEmoji_btn.setEnabled(True)
            self.ui.icon_sadEmoji_btn.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(115, 115, 115);\n"
                                                    "border-radius:10px;\n"
                                                    "border:none;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")

    def clearInfoUniversity(self):
        self.ui.class_lineEdit_uni_info.setText("")
        self.ui.textEdit_detail_uni_info.setText("")
        self.ui.link_lineEdit_uni_info.setText("")
        self.iconInfoBtnUni = ""
        self.ui.icon_done_btn.setEnabled(True)
        self.ui.icon_circle_btn.setEnabled(True)
        self.ui.icon_heart_btn.setEnabled(True)
        self.ui.icon_smileEmoji_btn.setEnabled(True)
        self.ui.icon_sadEmoji_btn.setEnabled(True)
        self.ui.icon_circleStar_btn.setEnabled(True)
        self.ui.icon_starFill_btn.setEnabled(True)
        self.ui.icon_starOut_btn.setEnabled(True)
        self.ui.icon_done_btn.setStyleSheet("QPushButton{\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(115, 115, 115);\n"
                                            "border-radius:10px;\n"
                                            "border:none;\n"
                                            "}\n"
                                            "QPushButton:hover{\n"
                                            "    color: rgb(255, 255, 255);\n"
                                            "    background-color: rgb(95, 95, 95);\n"
                                            "border-radius:5px;\n"
                                            "}")
        self.ui.icon_heart_btn.setStyleSheet("QPushButton{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    background-color: rgb(115, 115, 115);\n"
                                             "border-radius:10px;\n"
                                             "border:none;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    background-color: rgb(95, 95, 95);\n"
                                             "border-radius:5px;\n"
                                             "}")
        self.ui.icon_starOut_btn.setStyleSheet("QPushButton{\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "    background-color: rgb(115, 115, 115);\n"
                                               "border-radius:10px;\n"
                                               "border:none;\n"
                                               "}\n"
                                               "QPushButton:hover{\n"
                                               "    color: rgb(255, 255, 255);\n"
                                               "    background-color: rgb(95, 95, 95);\n"
                                               "border-radius:5px;\n"
                                               "}")
        self.ui.icon_starFill_btn.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(115, 115, 115);\n"
                                                "border-radius:10px;\n"
                                                "border:none;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:5px;\n"
                                                "}")
        self.ui.icon_circle_btn.setStyleSheet("QPushButton{\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    background-color: rgb(115, 115, 115);\n"
                                              "border-radius:10px;\n"
                                              "border:none;\n"
                                              "}\n"
                                              "QPushButton:hover{\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    background-color: rgb(95, 95, 95);\n"
                                              "border-radius:5px;\n"
                                              "}")
        self.ui.icon_circleStar_btn.setStyleSheet("QPushButton{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(115, 115, 115);\n"
                                                  "border-radius:10px;\n"
                                                  "border:none;\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(95, 95, 95);\n"
                                                  "border-radius:5px;\n"
                                                  "}")
        self.ui.icon_smileEmoji_btn.setStyleSheet("QPushButton{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(115, 115, 115);\n"
                                                  "border-radius:10px;\n"
                                                  "border:none;\n"
                                                  "}\n"
                                                  "QPushButton:hover{\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    background-color: rgb(95, 95, 95);\n"
                                                  "border-radius:5px;\n"
                                                  "}")
        self.ui.icon_sadEmoji_btn.setStyleSheet("QPushButton{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(115, 115, 115);\n"
                                                "border-radius:10px;\n"
                                                "border:none;\n"
                                                "}\n"
                                                "QPushButton:hover{\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    background-color: rgb(95, 95, 95);\n"
                                                "border-radius:5px;\n"
                                                "}")

    def updateDataInfoEventUniversity(self, frame):
        UniversityBackend.update(frame, self.ui.class_lineEdit_uni_info.text(),
                                 self.ui.textEdit_detail_uni_info.toPlainText(), self.iconInfoBtnUni,
                                 self.ui.link_lineEdit_uni_info.text())
        HistoryBackend.insert(f"class: {self.ui.class_lineEdit_uni_info.text()}",
                              self.ui.textEdit_detail_uni_info.toPlainText(), "", "updated")
        self.refresh_UniversityTable()

    def submitUniversityInfoEvent(self):
        if len(self.ui.class_lineEdit_uni_info.text()) != 0:
            if len(self.ui.link_lineEdit_uni_info.text()) != 0:
                if len(self.iconInfoBtnUni) != 0:
                    self.updateDataInfoEventUniversity(self.frameNum_uni)
                    self.showInfo("Update", "Update was successful.")
                else:
                    self.showError("Icon", "You should choose an icon.")
            else:
                self.showError("Link", "You should fill link lineEdit.")
        else:
            self.showError("Class", "You should fill class lineEdit.")

    def copyLinkInfoUniversity(self):
        pyperclip.copy(self.ui.link_lineEdit_uni_info.text())
        self.showInfo("Copy", "Copy was successful.")

    def university_table_frame_1(self):
        self.frameNum_uni = "1"
        if self.checkEmptyUni("1"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Saturday 6:00-8:00")
        else:
            self.setInformationUniversity("1")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_2(self):
        self.frameNum_uni = "2"
        if self.checkEmptyUni("2"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Saturday 8:00-10:00")
        else:
            self.setInformationUniversity("2")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_3(self):
        self.frameNum_uni = "3"
        if self.checkEmptyUni("3"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Saturday 10:00-12:00")
        else:
            self.setInformationUniversity("3")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_4(self):
        self.frameNum_uni = "4"
        if self.checkEmptyUni("4"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Saturday 12:00-14:00")
        else:
            self.setInformationUniversity("4")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_5(self):
        self.frameNum_uni = "5"
        if self.checkEmptyUni("5"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Saturday 14:00-16:00")
        else:
            self.setInformationUniversity("5")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_6(self):
        self.frameNum_uni = "6"
        if self.checkEmptyUni("6"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Saturday 16:00-18:00")
        else:
            self.setInformationUniversity("6")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_7(self):
        self.frameNum_uni = "7"
        if self.checkEmptyUni("7"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Saturday 18:00-20:00")
        else:
            self.setInformationUniversity("7")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_8(self):
        self.frameNum_uni = "8"
        if self.checkEmptyUni("8"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Saturday 20:00-22:00")
        else:
            self.setInformationUniversity("8")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_9(self):
        self.frameNum_uni = "9"
        if self.checkEmptyUni("9"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Saturday 22:00-24:00")
        else:
            self.setInformationUniversity("9")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_10(self):
        self.frameNum_uni = "10"
        if self.checkEmptyUni("10"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Sunday 6:00-8:00")
        else:
            self.setInformationUniversity("10")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_11(self):
        self.frameNum_uni = "11"
        if self.checkEmptyUni("11"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Sunday 8:00-10:00")
        else:
            self.setInformationUniversity("11")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_12(self):
        self.frameNum_uni = "12"
        if self.checkEmptyUni("12"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Sunday 10:00-12:00")
        else:
            self.setInformationUniversity("12")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_13(self):
        self.frameNum_uni = "13"
        if self.checkEmptyUni("13"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Sunday 12:00-14:00")
        else:
            self.setInformationUniversity("13")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_14(self):
        self.frameNum_uni = "14"
        if self.checkEmptyUni("14"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Sunday 14:00-16:00")
        else:
            self.setInformationUniversity("14")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_15(self):
        self.frameNum_uni = "15"
        if self.checkEmptyUni("15"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Sunday 16:00-18:00")
        else:
            self.setInformationUniversity("15")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_16(self):
        self.frameNum_uni = "16"
        if self.checkEmptyUni("16"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Sunday 18:00-20:00")
        else:
            self.setInformationUniversity("16")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_17(self):
        self.frameNum_uni = "17"
        if self.checkEmptyUni("17"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Sunday 20:00-22:00")
        else:
            self.setInformationUniversity("17")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_18(self):
        self.frameNum_uni = "18"
        if self.checkEmptyUni("18"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Sunday 22:00-24:00")
        else:
            self.setInformationUniversity("18")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_19(self):
        self.frameNum_uni = "19"
        if self.checkEmptyUni("19"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Monday 6:00-8:00")
        else:
            self.setInformationUniversity("19")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_20(self):
        self.frameNum_uni = "20"
        if self.checkEmptyUni("20"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Monday 8:00-10:00")
        else:
            self.setInformationUniversity("20")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_21(self):
        self.frameNum_uni = "21"
        if self.checkEmptyUni("21"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Monday 10:00-12:00")
        else:
            self.setInformationUniversity("21")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_22(self):
        self.frameNum_uni = "22"
        if self.checkEmptyUni("22"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Monday 12:00-14:00")
        else:
            self.setInformationUniversity("22")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_23(self):
        self.frameNum_uni = "23"
        if self.checkEmptyUni("23"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Monday 14:00-16:00")
        else:
            self.setInformationUniversity("23")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_24(self):
        self.frameNum_uni = "24"
        if self.checkEmptyUni("24"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Monday 16:00-18:00")
        else:
            self.setInformationUniversity("24")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_25(self):
        self.frameNum_uni = "25"
        if self.checkEmptyUni("25"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Monday 18:00-20:00")
        else:
            self.setInformationUniversity("25")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_26(self):
        self.frameNum_uni = "26"
        if self.checkEmptyUni("26"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Monday 20:00-22:00")
        else:
            self.setInformationUniversity("26")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_27(self):
        self.frameNum_uni = "27"
        if self.checkEmptyUni("27"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Monday 22:00-24:00")
        else:
            self.setInformationUniversity("27")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_28(self):
        self.frameNum_uni = "28"
        if self.checkEmptyUni("28"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Tuesday 6:00-8:00")
        else:
            self.setInformationUniversity("28")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_29(self):
        self.frameNum_uni = "29"
        if self.checkEmptyUni("29"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Tuesday 8:00-10:00")
        else:
            self.setInformationUniversity("29")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_30(self):
        self.frameNum_uni = "30"
        if self.checkEmptyUni("30"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Tuesday 10:00-12:00")
        else:
            self.setInformationUniversity("30")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_31(self):
        self.frameNum_uni = "31"
        if self.checkEmptyUni("31"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Tuesday 12:00-14:00")
        else:
            self.setInformationUniversity("31")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_32(self):
        self.frameNum_uni = "32"
        if self.checkEmptyUni("32"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Tuesday 14:00-16:00")
        else:
            self.setInformationUniversity("32")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_33(self):
        self.frameNum_uni = "33"
        if self.checkEmptyUni("33"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Tuesday 16:00-18:00")
        else:
            self.setInformationUniversity("33")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_34(self):
        self.frameNum_uni = "34"
        if self.checkEmptyUni("34"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Tuesday 18:00-20:00")
        else:
            self.setInformationUniversity("34")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_35(self):
        self.frameNum_uni = "35"
        if self.checkEmptyUni("35"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Tuesday 20:00-22:00")
        else:
            self.setInformationUniversity("35")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_36(self):
        self.frameNum_uni = "36"
        if self.checkEmptyUni("36"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Tuesday 22:00-24:00")
        else:
            self.setInformationUniversity("36")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_37(self):
        self.frameNum_uni = "37"
        if self.checkEmptyUni("37"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Wednesday 6:00-8:00")
        else:
            self.setInformationUniversity("37")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_38(self):
        self.frameNum_uni = "38"
        if self.checkEmptyUni("38"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Wednesday 8:00-10:00")
        else:
            self.setInformationUniversity("38")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_39(self):
        self.frameNum_uni = "39"
        if self.checkEmptyUni("39"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Wednesday 10:00-12:00")
        else:
            self.setInformationUniversity("39")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_40(self):
        self.frameNum_uni = "40"
        if self.checkEmptyUni("40"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Wednesday 12:00-14:00")
        else:
            self.setInformationUniversity("40")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_41(self):
        self.frameNum_uni = "41"
        if self.checkEmptyUni("41"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Wednesday 14:00-16:00")
        else:
            self.setInformationUniversity("41")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_42(self):
        self.frameNum_uni = "42"
        if self.checkEmptyUni("42"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Wednesday 16:00-18:00")
        else:
            self.setInformationUniversity("42")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_43(self):
        self.frameNum_uni = "43"
        if self.checkEmptyUni("43"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Wednesday 18:00-20:00")
        else:
            self.setInformationUniversity("43")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_44(self):
        self.frameNum_uni = "44"
        if self.checkEmptyUni("44"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Wednesday 20:00-22:00")
        else:
            self.setInformationUniversity("44")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_45(self):
        self.frameNum_uni = "45"
        if self.checkEmptyUni("45"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Wednesday 22:00-24:00")
        else:
            self.setInformationUniversity("45")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_46(self):
        self.frameNum_uni = "46"
        if self.checkEmptyUni("46"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Thursday 6:00-8:00")
        else:
            self.setInformationUniversity("46")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_47(self):
        self.frameNum_uni = "47"
        if self.checkEmptyUni("47"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Thursday 8:00-10:00")
        else:
            self.setInformationUniversity("47")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_48(self):
        self.frameNum_uni = "48"
        if self.checkEmptyUni("48"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Thursday 10:00-12:00")
        else:
            self.setInformationUniversity("48")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_49(self):
        self.frameNum_uni = "49"
        if self.checkEmptyUni("49"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Thursday 12:00-14:00")
        else:
            self.setInformationUniversity("49")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_50(self):
        self.frameNum_uni = "50"
        if self.checkEmptyUni("50"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Thursday 14:00-16:00")
        else:
            self.setInformationUniversity("50")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_51(self):
        self.frameNum_uni = "51"
        if self.checkEmptyUni("51"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Thursday 16:00-18:00")
        else:
            self.setInformationUniversity("51")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_52(self):
        self.frameNum_uni = "52"
        if self.checkEmptyUni("52"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Thursday 18:00-20:00")
        else:
            self.setInformationUniversity("52")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_53(self):
        self.frameNum_uni = "53"
        if self.checkEmptyUni("53"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Thursday 20:00-22:00")
        else:
            self.setInformationUniversity("53")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_54(self):
        self.frameNum_uni = "54"
        if self.checkEmptyUni("54"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Thursday 22:00-24:00")
        else:
            self.setInformationUniversity("54")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_55(self):
        self.frameNum_uni = "55"
        if self.checkEmptyUni("55"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Friday 6:00-8:00")
        else:
            self.setInformationUniversity("55")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_56(self):
        self.frameNum_uni = "56"
        if self.checkEmptyUni("56"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Friday 8:00-10:00")
        else:
            self.setInformationUniversity("56")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_57(self):
        self.frameNum_uni = "57"
        if self.checkEmptyUni("57"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Friday 10:00-12:00")
        else:
            self.setInformationUniversity("57")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_58(self):
        self.frameNum_uni = "58"
        if self.checkEmptyUni("58"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Friday 12:00-14:00")
        else:
            self.setInformationUniversity("58")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_59(self):
        self.frameNum_uni = "59"
        if self.checkEmptyUni("59"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Friday 14:00-16:00")
        else:
            self.setInformationUniversity("59")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_60(self):
        self.frameNum_uni = "60"
        if self.checkEmptyUni("60"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Friday 16:00-18:00")
        else:
            self.setInformationUniversity("60")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_61(self):
        self.frameNum_uni = "61"
        if self.checkEmptyUni("61"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Friday 18:00-20:00")
        else:
            self.setInformationUniversity("61")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_62(self):
        self.frameNum_uni = "62"
        if self.checkEmptyUni("62"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Friday 20:00-22:00")
        else:
            self.setInformationUniversity("62")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def university_table_frame_63(self):
        self.frameNum_uni = "63"
        if self.checkEmptyUni("63"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_add)
                self.ui.title_uni_add.setText("Friday 22:00-24:00")
        else:
            self.setInformationUniversity("63")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Uni_info)

    def setColorIconInfoTable(self, inputIcon, state):
        if state:
            if inputIcon == "done":
                self.ui.icon_done_table_info.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(170, 85, 127);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")
            elif inputIcon == "heart":
                self.ui.icon_heart_table_info.setStyleSheet("QPushButton{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(170, 85, 127);\n"
                                                            "border-radius:10px;\n"
                                                            "border:none;\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(95, 95, 95);\n"
                                                            "border-radius:5px;\n"
                                                            "}")
            elif inputIcon == "starOutline":
                self.ui.icon_starOut_table_info.setStyleSheet("QPushButton{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(170, 85, 127);\n"
                                                              "border-radius:10px;\n"
                                                              "border:none;\n"
                                                              "}\n"
                                                              "QPushButton:hover{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(95, 95, 95);\n"
                                                              "border-radius:5px;\n"
                                                              "}")
            elif inputIcon == "starFill":
                self.ui.icon_starFill_table_info.setStyleSheet("QPushButton{\n"
                                                               "    color: rgb(255, 255, 255);\n"
                                                               "    background-color: rgb(170, 85, 127);\n"
                                                               "border-radius:10px;\n"
                                                               "border:none;\n"
                                                               "}\n"
                                                               "QPushButton:hover{\n"
                                                               "    color: rgb(255, 255, 255);\n"
                                                               "    background-color: rgb(95, 95, 95);\n"
                                                               "border-radius:5px;\n"
                                                               "}")
            elif inputIcon == "circle":
                self.ui.icon_circle_table_info.setStyleSheet("QPushButton{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(170, 85, 127);\n"
                                                             "border-radius:10px;\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "QPushButton:hover{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(95, 95, 95);\n"
                                                             "border-radius:5px;\n"
                                                             "}")
            elif inputIcon == "starCircle":
                self.ui.icon_circleStar_table_info.setStyleSheet("QPushButton{\n"
                                                                 "    color: rgb(255, 255, 255);\n"
                                                                 "    background-color: rgb(170, 85, 127);\n"
                                                                 "border-radius:10px;\n"
                                                                 "border:none;\n"
                                                                 "}\n"
                                                                 "QPushButton:hover{\n"
                                                                 "    color: rgb(255, 255, 255);\n"
                                                                 "    background-color: rgb(95, 95, 95);\n"
                                                                 "border-radius:5px;\n"
                                                                 "}")
            elif inputIcon == "smileEmoji":
                self.ui.icon_smileEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                                 "    color: rgb(255, 255, 255);\n"
                                                                 "    background-color: rgb(170, 85, 127);\n"
                                                                 "border-radius:10px;\n"
                                                                 "border:none;\n"
                                                                 "}\n"
                                                                 "QPushButton:hover{\n"
                                                                 "    color: rgb(255, 255, 255);\n"
                                                                 "    background-color: rgb(95, 95, 95);\n"
                                                                 "border-radius:5px;\n"
                                                                 "}")
            elif inputIcon == "sadEmoji":
                self.ui.icon_sadEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                               "    color: rgb(255, 255, 255);\n"
                                                               "    background-color: rgb(170, 85, 127);\n"
                                                               "border-radius:10px;\n"
                                                               "border:none;\n"
                                                               "}\n"
                                                               "QPushButton:hover{\n"
                                                               "    color: rgb(255, 255, 255);\n"
                                                               "    background-color: rgb(95, 95, 95);\n"
                                                               "border-radius:5px;\n"
                                                               "}")
        else:
            self.ui.icon_done_table_info.setStyleSheet("QPushButton{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(115, 115, 115);\n"
                                                       "border-radius:10px;\n"
                                                       "border:none;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(95, 95, 95);\n"
                                                       "border-radius:5px;\n"
                                                       "}")
            self.ui.icon_heart_table_info.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(115, 115, 115);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")
            self.ui.icon_starOut_table_info.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(115, 115, 115);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")
            self.ui.icon_starFill_table_info.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(115, 115, 115);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")
            self.ui.icon_circle_table_info.setStyleSheet("QPushButton{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(115, 115, 115);\n"
                                                         "border-radius:10px;\n"
                                                         "border:none;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(95, 95, 95);\n"
                                                         "border-radius:5px;\n"
                                                         "}")
            self.ui.icon_circleStar_table_info.setStyleSheet("QPushButton{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(115, 115, 115);\n"
                                                             "border-radius:10px;\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "QPushButton:hover{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(95, 95, 95);\n"
                                                             "border-radius:5px;\n"
                                                             "}")
            self.ui.icon_smileEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(115, 115, 115);\n"
                                                             "border-radius:10px;\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "QPushButton:hover{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(95, 95, 95);\n"
                                                             "border-radius:5px;\n"
                                                             "}")
            self.ui.icon_sadEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(115, 115, 115);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")

    def setInformationTable(self, frame):
        self.setColorIconInfoTable("", False)
        data = TableBackend.search_frame(frame)
        if frame == "1":
            self.ui.title_table_info.setText("Saturday 6:00-8:00")
        elif frame == "2":
            self.ui.title_table_info.setText("Saturday 8:00-10:00")
        elif frame == "3":
            self.ui.title_table_info.setText("Saturday 10:00-12:00")
        elif frame == "4":
            self.ui.title_table_info.setText("Saturday 12:00-14:00")
        elif frame == "5":
            self.ui.title_table_info.setText("Saturday 14:00-16:00")
        elif frame == "6":
            self.ui.title_table_info.setText("Saturday 16:00-18:00")
        elif frame == "7":
            self.ui.title_table_info.setText("Saturday 18:00-20:00")
        elif frame == "8":
            self.ui.title_table_info.setText("Saturday 20:00-22:00")
        elif frame == "9":
            self.ui.title_table_info.setText("Saturday 22:00-24:00")
        elif frame == "10":
            self.ui.title_table_info.setText("Sunday 6:00-8:00")
        elif frame == "11":
            self.ui.title_table_info.setText("Sunday 8:00-10:00")
        elif frame == "12":
            self.ui.title_table_info.setText("Sunday 10:00-12:00")
        elif frame == "13":
            self.ui.title_table_info.setText("Sunday 12:00-14:00")
        elif frame == "14":
            self.ui.title_table_info.setText("Sunday 14:00-16:00")
        elif frame == "15":
            self.ui.title_table_info.setText("Sunday 16:00-18:00")
        elif frame == "16":
            self.ui.title_table_info.setText("Sunday 18:00-20:00")
        elif frame == "17":
            self.ui.title_table_info.setText("Sunday 20:00-22:00")
        elif frame == "18":
            self.ui.title_table_info.setText("Sunday 22:00-24:00")
        elif frame == "19":
            self.ui.title_table_info.setText("Monday 6:00-8:00")
        elif frame == "20":
            self.ui.title_table_info.setText("Monday 8:00-10:00")
        elif frame == "21":
            self.ui.title_table_info.setText("Monday 10:00-12:00")
        elif frame == "22":
            self.ui.title_table_info.setText("Monday 12:00-14:00")
        elif frame == "23":
            self.ui.title_table_info.setText("Monday 14:00-16:00")
        elif frame == "24":
            self.ui.title_table_info.setText("Monday 16:00-18:00")
        elif frame == "25":
            self.ui.title_table_info.setText("Monday 18:00-20:00")
        elif frame == "26":
            self.ui.title_table_info.setText("Monday 20:00-22:00")
        elif frame == "27":
            self.ui.title_table_info.setText("Monday 22:00-24:00")
        elif frame == "28":
            self.ui.title_table_info.setText("Tuesday 6:00-8:00")
        elif frame == "29":
            self.ui.title_table_info.setText("Tuesday 8:00-10:00")
        elif frame == "30":
            self.ui.title_table_info.setText("Tuesday 10:00-12:00")
        elif frame == "31":
            self.ui.title_table_info.setText("Tuesday 12:00-14:00")
        elif frame == "32":
            self.ui.title_table_info.setText("Tuesday 14:00-16:00")
        elif frame == "33":
            self.ui.title_table_info.setText("Tuesday 16:00-18:00")
        elif frame == "34":
            self.ui.title_table_info.setText("Tuesday 18:00-20:00")
        elif frame == "35":
            self.ui.title_table_info.setText("Tuesday 20:00-22:00")
        elif frame == "36":
            self.ui.title_table_info.setText("Tuesday 22:00-24:00")
        elif frame == "37":
            self.ui.title_table_info.setText("Wednesday 6:00-8:00")
        elif frame == "38":
            self.ui.title_table_info.setText("Wednesday 8:00-10:00")
        elif frame == "39":
            self.ui.title_table_info.setText("Wednesday 10:00-12:00")
        elif frame == "40":
            self.ui.title_table_info.setText("Wednesday 12:00-14:00")
        elif frame == "41":
            self.ui.title_table_info.setText("Wednesday 14:00-16:00")
        elif frame == "42":
            self.ui.title_table_info.setText("Wednesday 16:00-18:00")
        elif frame == "43":
            self.ui.title_table_info.setText("Wednesday 18:00-20:00")
        elif frame == "44":
            self.ui.title_table_info.setText("Wednesday 20:00-22:00")
        elif frame == "45":
            self.ui.title_table_info.setText("Wednesday 22:00-24:00")
        elif frame == "46":
            self.ui.title_table_info.setText("Thursday 6:00-8:00")
        elif frame == "47":
            self.ui.title_table_info.setText("Thursday 8:00-10:00")
        elif frame == "48":
            self.ui.title_table_info.setText("Thursday 10:00-12:00")
        elif frame == "49":
            self.ui.title_table_info.setText("Thursday 12:00-14:00")
        elif frame == "50":
            self.ui.title_table_info.setText("Thursday 14:00-16:00")
        elif frame == "51":
            self.ui.title_table_info.setText("Thursday 16:00-18:00")
        elif frame == "52":
            self.ui.title_table_info.setText("Thursday 18:00-20:00")
        elif frame == "53":
            self.ui.title_table_info.setText("Thursday 20:00-22:00")
        elif frame == "54":
            self.ui.title_table_info.setText("Thursday 22:00-24:00")
        elif frame == "55":
            self.ui.title_table_info.setText("Friday 6:00-8:00")
        elif frame == "56":
            self.ui.title_table_info.setText("Friday 8:00-10:00")
        elif frame == "57":
            self.ui.title_table_info.setText("Friday 10:00-12:00")
        elif frame == "58":
            self.ui.title_table_info.setText("Friday 12:00-14:00")
        elif frame == "59":
            self.ui.title_table_info.setText("Friday 14:00-16:00")
        elif frame == "60":
            self.ui.title_table_info.setText("Friday 16:00-18:00")
        elif frame == "61":
            self.ui.title_table_info.setText("Friday 18:00-20:00")
        elif frame == "62":
            self.ui.title_table_info.setText("Friday 20:00-22:00")
        elif frame == "63":
            self.ui.title_table_info.setText("Friday 22:00-24:00")
        self.ui.class_lineEdit_table_info.setText(data[0][1])
        self.ui.textEdit_detail_table_info.setText(data[0][2])
        self.iconInfoBtnTable = data[0][3]
        self.setIconInfoTables(frame, data[0][3], "Table")
        self.setColorIconInfoTable(data[0][3], True)

    def refresh_Table(self):
        for i in range(1, 64):
            data = TableBackend.search_frame(str(i))
            if len(data) != 0:
                self.setInformationTable(str(i))

    def doneBtnAddTable(self):
        if not self.btn_done_tableAdd:
            self.iconAddBtnTable = "done"
            self.btn_done_tableAdd = True
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_circleStar_btn_table_add.setEnabled(False)
            self.ui.icon_circle_btn_table_add.setEnabled(False)
            self.ui.icon_starFill_btn_table_add.setEnabled(False)
            self.ui.icon_starOut_btn_table_add.setEnabled(False)
            self.ui.icon_heart_btn_table_add.setEnabled(False)
            self.ui.icon_done_btn_table_add.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(170, 85, 127);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")
        elif self.btn_done_tableAdd:
            self.iconAddBtnTable = ""
            self.btn_done_tableAdd = False
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_circleStar_btn_table_add.setEnabled(True)
            self.ui.icon_circle_btn_table_add.setEnabled(True)
            self.ui.icon_starFill_btn_table_add.setEnabled(True)
            self.ui.icon_starOut_btn_table_add.setEnabled(True)
            self.ui.icon_heart_btn_table_add.setEnabled(True)
            self.ui.icon_done_btn_table_add.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(115, 115, 115);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")

    def heartBtnAddTable(self):
        if not self.btn_heart_tableAdd:
            self.iconAddBtnTable = "heart"
            self.btn_heart_tableAdd = True
            self.ui.icon_done_btn_table_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_circleStar_btn_table_add.setEnabled(False)
            self.ui.icon_circle_btn_table_add.setEnabled(False)
            self.ui.icon_starFill_btn_table_add.setEnabled(False)
            self.ui.icon_starOut_btn_table_add.setEnabled(False)
            self.ui.icon_heart_btn_table_add.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(170, 85, 127);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")
        elif self.btn_heart_tableAdd:
            self.iconAddBtnTable = ""
            self.btn_heart_tableAdd = False
            self.ui.icon_done_btn_table_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_circleStar_btn_table_add.setEnabled(True)
            self.ui.icon_circle_btn_table_add.setEnabled(True)
            self.ui.icon_starFill_btn_table_add.setEnabled(True)
            self.ui.icon_starOut_btn_table_add.setEnabled(True)
            self.ui.icon_heart_btn_table_add.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(115, 115, 115);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")

    def starOutBtnAddTable(self):
        if not self.btn_starOut_tableAdd:
            self.iconAddBtnTable = "starOutline"
            self.btn_starOut_tableAdd = True
            self.ui.icon_done_btn_table_add.setEnabled(False)
            self.ui.icon_heart_btn_table_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_circleStar_btn_table_add.setEnabled(False)
            self.ui.icon_circle_btn_table_add.setEnabled(False)
            self.ui.icon_starFill_btn_table_add.setEnabled(False)
            self.ui.icon_starOut_btn_table_add.setStyleSheet("QPushButton{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(170, 85, 127);\n"
                                                             "border-radius:10px;\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "QPushButton:hover{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(95, 95, 95);\n"
                                                             "border-radius:5px;\n"
                                                             "}")
        elif self.btn_starOut_tableAdd:
            self.iconAddBtnTable = ""
            self.btn_starOut_tableAdd = False
            self.ui.icon_done_btn_table_add.setEnabled(True)
            self.ui.icon_heart_btn_table_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_circleStar_btn_table_add.setEnabled(True)
            self.ui.icon_circle_btn_table_add.setEnabled(True)
            self.ui.icon_starFill_btn_table_add.setEnabled(True)
            self.ui.icon_starOut_btn_table_add.setStyleSheet("QPushButton{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(115, 115, 115);\n"
                                                             "border-radius:10px;\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "QPushButton:hover{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(95, 95, 95);\n"
                                                             "border-radius:5px;\n"
                                                             "}")

    def starFillBtnAddTable(self):
        if not self.btn_starFill_tableAdd:
            self.iconAddBtnTable = "starFill"
            self.btn_starFill_tableAdd = True
            self.ui.icon_done_btn_table_add.setEnabled(False)
            self.ui.icon_heart_btn_table_add.setEnabled(False)
            self.ui.icon_starOut_btn_table_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_circleStar_btn_table_add.setEnabled(False)
            self.ui.icon_circle_btn_table_add.setEnabled(False)
            self.ui.icon_starFill_btn_table_add.setStyleSheet("QPushButton{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(170, 85, 127);\n"
                                                              "border-radius:10px;\n"
                                                              "border:none;\n"
                                                              "}\n"
                                                              "QPushButton:hover{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(95, 95, 95);\n"
                                                              "border-radius:5px;\n"
                                                              "}")
        elif self.btn_starFill_tableAdd:
            self.iconAddBtnTable = ""
            self.btn_starFill_tableAdd = False
            self.ui.icon_done_btn_table_add.setEnabled(True)
            self.ui.icon_heart_btn_table_add.setEnabled(True)
            self.ui.icon_starOut_btn_table_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_circleStar_btn_table_add.setEnabled(True)
            self.ui.icon_circle_btn_table_add.setEnabled(True)
            self.ui.icon_starFill_btn_table_add.setStyleSheet("QPushButton{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(115, 115, 115);\n"
                                                              "border-radius:10px;\n"
                                                              "border:none;\n"
                                                              "}\n"
                                                              "QPushButton:hover{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(95, 95, 95);\n"
                                                              "border-radius:5px;\n"
                                                              "}")

    def circleBtnAddTable(self):
        if not self.btn_circle_tableAdd:
            self.iconAddBtnTable = "circle"
            self.btn_circle_tableAdd = True
            self.ui.icon_done_btn_table_add.setEnabled(False)
            self.ui.icon_heart_btn_table_add.setEnabled(False)
            self.ui.icon_starOut_btn_table_add.setEnabled(False)
            self.ui.icon_starFill_btn_table_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_circleStar_btn_table_add.setEnabled(False)
            self.ui.icon_circle_btn_table_add.setStyleSheet("QPushButton{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(170, 85, 127);\n"
                                                            "border-radius:10px;\n"
                                                            "border:none;\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(95, 95, 95);\n"
                                                            "border-radius:5px;\n"
                                                            "}")
        elif self.btn_circle_tableAdd:
            self.iconAddBtnTable = ""
            self.btn_circle_tableAdd = False
            self.ui.icon_done_btn_table_add.setEnabled(True)
            self.ui.icon_heart_btn_table_add.setEnabled(True)
            self.ui.icon_starOut_btn_table_add.setEnabled(True)
            self.ui.icon_starFill_btn_table_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_circleStar_btn_table_add.setEnabled(True)
            self.ui.icon_circle_btn_table_add.setStyleSheet("QPushButton{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(115, 115, 115);\n"
                                                            "border-radius:10px;\n"
                                                            "border:none;\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(95, 95, 95);\n"
                                                            "border-radius:5px;\n"
                                                            "}")

    def starCircleBtnAddTable(self):
        if not self.btn_starCircle_tableAdd:
            self.iconAddBtnTable = "starCircle"
            self.btn_starCircle_tableAdd = True
            self.ui.icon_done_btn_table_add.setEnabled(False)
            self.ui.icon_circle_btn_table_add.setEnabled(False)
            self.ui.icon_heart_btn_table_add.setEnabled(False)
            self.ui.icon_starOut_btn_table_add.setEnabled(False)
            self.ui.icon_starFill_btn_table_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_circleStar_btn_table_add.setStyleSheet("QPushButton{\n"
                                                                "    color: rgb(255, 255, 255);\n"
                                                                "    background-color: rgb(170, 85, 127);\n"
                                                                "border-radius:10px;\n"
                                                                "border:none;\n"
                                                                "}\n"
                                                                "QPushButton:hover{\n"
                                                                "    color: rgb(255, 255, 255);\n"
                                                                "    background-color: rgb(95, 95, 95);\n"
                                                                "border-radius:5px;\n"
                                                                "}")
        elif self.btn_starCircle_tableAdd:
            self.iconAddBtnTable = ""
            self.btn_starCircle_tableAdd = False
            self.ui.icon_done_btn_table_add.setEnabled(True)
            self.ui.icon_circle_btn_table_add.setEnabled(True)
            self.ui.icon_heart_btn_table_add.setEnabled(True)
            self.ui.icon_starOut_btn_table_add.setEnabled(True)
            self.ui.icon_starFill_btn_table_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_circleStar_btn_table_add.setStyleSheet("QPushButton{\n"
                                                                "    color: rgb(255, 255, 255);\n"
                                                                "    background-color: rgb(115, 115, 115);\n"
                                                                "border-radius:10px;\n"
                                                                "border:none;\n"
                                                                "}\n"
                                                                "QPushButton:hover{\n"
                                                                "    color: rgb(255, 255, 255);\n"
                                                                "    background-color: rgb(95, 95, 95);\n"
                                                                "border-radius:5px;\n"
                                                                "}")

    def smileBtnAddTable(self):
        if not self.btn_smile_tableAdd:
            self.iconAddBtnTable = "smileEmoji"
            self.btn_smile_tableAdd = True
            self.ui.icon_done_btn_table_add.setEnabled(False)
            self.ui.icon_circle_btn_table_add.setEnabled(False)
            self.ui.icon_heart_btn_table_add.setEnabled(False)
            self.ui.icon_starOut_btn_table_add.setEnabled(False)
            self.ui.icon_starFill_btn_table_add.setEnabled(False)
            self.ui.icon_circleStar_btn_table_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_table_add.setStyleSheet("QPushButton{\n"
                                                                "    color: rgb(255, 255, 255);\n"
                                                                "    background-color: rgb(170, 85, 127);\n"
                                                                "border-radius:10px;\n"
                                                                "border:none;\n"
                                                                "}\n"
                                                                "QPushButton:hover{\n"
                                                                "    color: rgb(255, 255, 255);\n"
                                                                "    background-color: rgb(95, 95, 95);\n"
                                                                "border-radius:5px;\n"
                                                                "}")
        elif self.btn_smile_tableAdd:
            self.iconAddBtnTable = ""
            self.btn_smile_tableAdd = False
            self.ui.icon_done_btn_table_add.setEnabled(True)
            self.ui.icon_circle_btn_table_add.setEnabled(True)
            self.ui.icon_heart_btn_table_add.setEnabled(True)
            self.ui.icon_starOut_btn_table_add.setEnabled(True)
            self.ui.icon_starFill_btn_table_add.setEnabled(True)
            self.ui.icon_circleStar_btn_table_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_table_add.setStyleSheet("QPushButton{\n"
                                                                "    color: rgb(255, 255, 255);\n"
                                                                "    background-color: rgb(115, 115, 115);\n"
                                                                "border-radius:10px;\n"
                                                                "border:none;\n"
                                                                "}\n"
                                                                "QPushButton:hover{\n"
                                                                "    color: rgb(255, 255, 255);\n"
                                                                "    background-color: rgb(95, 95, 95);\n"
                                                                "border-radius:5px;\n"
                                                                "}")

    def sadBtnAddTable(self):
        if not self.btn_sad_tableAdd:
            self.iconAddBtnTable = "sadEmoji"
            self.btn_sad_tableAdd = True
            self.ui.icon_done_btn_table_add.setEnabled(False)
            self.ui.icon_circle_btn_table_add.setEnabled(False)
            self.ui.icon_heart_btn_table_add.setEnabled(False)
            self.ui.icon_starOut_btn_table_add.setEnabled(False)
            self.ui.icon_starFill_btn_table_add.setEnabled(False)
            self.ui.icon_circleStar_btn_table_add.setEnabled(False)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(False)
            self.ui.icon_sadEmoji_btn_table_add.setStyleSheet("QPushButton{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(170, 85, 127);\n"
                                                              "border-radius:10px;\n"
                                                              "border:none;\n"
                                                              "}\n"
                                                              "QPushButton:hover{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(95, 95, 95);\n"
                                                              "border-radius:5px;\n"
                                                              "}")
        elif self.btn_sad_tableAdd:
            self.iconAddBtnTable = ""
            self.btn_sad_tableAdd = False
            self.ui.icon_done_btn_table_add.setEnabled(True)
            self.ui.icon_circle_btn_table_add.setEnabled(True)
            self.ui.icon_heart_btn_table_add.setEnabled(True)
            self.ui.icon_starOut_btn_table_add.setEnabled(True)
            self.ui.icon_starFill_btn_table_add.setEnabled(True)
            self.ui.icon_circleStar_btn_table_add.setEnabled(True)
            self.ui.icon_smileEmoji_btn_table_add.setEnabled(True)
            self.ui.icon_sadEmoji_btn_table_add.setStyleSheet("QPushButton{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(115, 115, 115);\n"
                                                              "border-radius:10px;\n"
                                                              "border:none;\n"
                                                              "}\n"
                                                              "QPushButton:hover{\n"
                                                              "    color: rgb(255, 255, 255);\n"
                                                              "    background-color: rgb(95, 95, 95);\n"
                                                              "border-radius:5px;\n"
                                                              "}")

    def clearAddTable(self):
        self.ui.title_lineEdit_add_table.setText("")
        self.ui.textEdit_detail_add_table.setText("")
        self.iconAddBtnTable = ""
        self.ui.icon_done_btn_table_add.setEnabled(True)
        self.ui.icon_circle_btn_table_add.setEnabled(True)
        self.ui.icon_heart_btn_table_add.setEnabled(True)
        self.ui.icon_smileEmoji_btn_table_add.setEnabled(True)
        self.ui.icon_sadEmoji_btn_table_add.setEnabled(True)
        self.ui.icon_circleStar_btn_table_add.setEnabled(True)
        self.ui.icon_starFill_btn_table_add.setEnabled(True)
        self.ui.icon_starOut_btn_table_add.setEnabled(True)
        self.ui.icon_done_btn_table_add.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(115, 115, 115);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
        self.ui.icon_heart_btn_table_add.setStyleSheet("QPushButton{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(115, 115, 115);\n"
                                                       "border-radius:10px;\n"
                                                       "border:none;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(95, 95, 95);\n"
                                                       "border-radius:5px;\n"
                                                       "}")
        self.ui.icon_starOut_btn_table_add.setStyleSheet("QPushButton{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(115, 115, 115);\n"
                                                         "border-radius:10px;\n"
                                                         "border:none;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(95, 95, 95);\n"
                                                         "border-radius:5px;\n"
                                                         "}")
        self.ui.icon_starFill_btn_table_add.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(115, 115, 115);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")
        self.ui.icon_circle_btn_table_add.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(115, 115, 115);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")
        self.ui.icon_circleStar_btn_table_add.setStyleSheet("QPushButton{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(115, 115, 115);\n"
                                                            "border-radius:10px;\n"
                                                            "border:none;\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(95, 95, 95);\n"
                                                            "border-radius:5px;\n"
                                                            "}")
        self.ui.icon_smileEmoji_btn_table_add.setStyleSheet("QPushButton{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(115, 115, 115);\n"
                                                            "border-radius:10px;\n"
                                                            "border:none;\n"
                                                            "}\n"
                                                            "QPushButton:hover{\n"
                                                            "    color: rgb(255, 255, 255);\n"
                                                            "    background-color: rgb(95, 95, 95);\n"
                                                            "border-radius:5px;\n"
                                                            "}")
        self.ui.icon_sadEmoji_btn_table_add.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(115, 115, 115);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")

    def insertDataAddEventTable(self, frame):
        TableBackend.insert(frame, self.ui.title_lineEdit_add_table.text(),
                            self.ui.textEdit_detail_add_table.toPlainText(), self.iconAddBtnTable, "active")
        HistoryBackend.insert(f"Table: {self.ui.title_lineEdit_add_table.text()}",
                              self.ui.textEdit_detail_add_table.toPlainText(), "", "active")
        self.refresh_Table()

    def submitTableAddEvent(self):
        if len(self.ui.title_lineEdit_add_table.text()) != 0:
            if len(self.iconAddBtnTable) != 0:
                self.insertDataAddEventTable(self.frameNum_table)
                self.showInfo("Add Event", "Add was successful.")
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table)
            else:
                self.showError("Icon", "You should choose an icon.")
        else:
            self.showError("Title", "You should fill title lineEdit.")

    @staticmethod
    def checkEmptyTable(frame):
        search = TableBackend.search_frame(frame)
        if len(search) == 0:
            return True
        else:
            return False

    def deleteIconEventTable(self):
        icon = QIcon()
        icon.addPixmap(QPixmap(), QIcon.Normal, QIcon.Off)
        if self.frameNum_table == "1":
            self.ui.table_btn_1.setIcon(icon)
        elif self.frameNum_table == "2":
            self.ui.table_btn_2.setIcon(icon)
        elif self.frameNum_table == "3":
            self.ui.table_btn_3.setIcon(icon)
        elif self.frameNum_table == "4":
            self.ui.table_btn_4.setIcon(icon)
        elif self.frameNum_table == "5":
            self.ui.table_btn_5.setIcon(icon)
        elif self.frameNum_table == "6":
            self.ui.table_btn_6.setIcon(icon)
        elif self.frameNum_table == "7":
            self.ui.table_btn_7.setIcon(icon)
        elif self.frameNum_table == "8":
            self.ui.table_btn_8.setIcon(icon)
        elif self.frameNum_table == "9":
            self.ui.table_btn_9.setIcon(icon)
        elif self.frameNum_table == "10":
            self.ui.table_btn_10.setIcon(icon)
        elif self.frameNum_table == "11":
            self.ui.table_btn_11.setIcon(icon)
        elif self.frameNum_table == "12":
            self.ui.table_btn_12.setIcon(icon)
        elif self.frameNum_table == "13":
            self.ui.table_btn_13.setIcon(icon)
        elif self.frameNum_table == "14":
            self.ui.table_btn_14.setIcon(icon)
        elif self.frameNum_table == "15":
            self.ui.table_btn_15.setIcon(icon)
        elif self.frameNum_table == "16":
            self.ui.table_btn_16.setIcon(icon)
        elif self.frameNum_table == "17":
            self.ui.table_btn_17.setIcon(icon)
        elif self.frameNum_table == "18":
            self.ui.table_btn_18.setIcon(icon)
        elif self.frameNum_table == "19":
            self.ui.table_btn_19.setIcon(icon)
        elif self.frameNum_table == "20":
            self.ui.table_btn_20.setIcon(icon)
        elif self.frameNum_table == "21":
            self.ui.table_btn_21.setIcon(icon)
        elif self.frameNum_table == "22":
            self.ui.table_btn_22.setIcon(icon)
        elif self.frameNum_table == "23":
            self.ui.table_btn_23.setIcon(icon)
        elif self.frameNum_table == "24":
            self.ui.table_btn_24.setIcon(icon)
        elif self.frameNum_table == "25":
            self.ui.table_btn_25.setIcon(icon)
        elif self.frameNum_table == "26":
            self.ui.table_btn_26.setIcon(icon)
        elif self.frameNum_table == "27":
            self.ui.table_btn_27.setIcon(icon)
        elif self.frameNum_table == "28":
            self.ui.table_btn_28.setIcon(icon)
        elif self.frameNum_table == "29":
            self.ui.table_btn_29.setIcon(icon)
        elif self.frameNum_table == "30":
            self.ui.table_btn_30.setIcon(icon)
        elif self.frameNum_table == "31":
            self.ui.table_btn_31.setIcon(icon)
        elif self.frameNum_table == "32":
            self.ui.table_btn_32.setIcon(icon)
        elif self.frameNum_table == "33":
            self.ui.table_btn_33.setIcon(icon)
        elif self.frameNum_table == "34":
            self.ui.table_btn_34.setIcon(icon)
        elif self.frameNum_table == "35":
            self.ui.table_btn_35.setIcon(icon)
        elif self.frameNum_table == "36":
            self.ui.table_btn_36.setIcon(icon)
        elif self.frameNum_table == "37":
            self.ui.table_btn_37.setIcon(icon)
        elif self.frameNum_table == "38":
            self.ui.table_btn_38.setIcon(icon)
        elif self.frameNum_table == "39":
            self.ui.table_btn_39.setIcon(icon)
        elif self.frameNum_table == "40":
            self.ui.table_btn_40.setIcon(icon)
        elif self.frameNum_table == "41":
            self.ui.table_btn_41.setIcon(icon)
        elif self.frameNum_table == "42":
            self.ui.table_btn_42.setIcon(icon)
        elif self.frameNum_table == "43":
            self.ui.table_btn_43.setIcon(icon)
        elif self.frameNum_table == "44":
            self.ui.table_btn_44.setIcon(icon)
        elif self.frameNum_table == "45":
            self.ui.table_btn_45.setIcon(icon)
        elif self.frameNum_table == "46":
            self.ui.table_btn_46.setIcon(icon)
        elif self.frameNum_table == "47":
            self.ui.table_btn_47.setIcon(icon)
        elif self.frameNum_table == "48":
            self.ui.table_btn_48.setIcon(icon)
        elif self.frameNum_table == "49":
            self.ui.table_btn_49.setIcon(icon)
        elif self.frameNum_table == "50":
            self.ui.table_btn_50.setIcon(icon)
        elif self.frameNum_table == "51":
            self.ui.table_btn_51.setIcon(icon)
        elif self.frameNum_table == "52":
            self.ui.table_btn_52.setIcon(icon)
        elif self.frameNum_table == "53":
            self.ui.table_btn_53.setIcon(icon)
        elif self.frameNum_table == "54":
            self.ui.table_btn_54.setIcon(icon)
        elif self.frameNum_table == "55":
            self.ui.table_btn_55.setIcon(icon)
        elif self.frameNum_table == "56":
            self.ui.table_btn_56.setIcon(icon)
        elif self.frameNum_table == "57":
            self.ui.table_btn_57.setIcon(icon)
        elif self.frameNum_table == "58":
            self.ui.table_btn_58.setIcon(icon)
        elif self.frameNum_table == "59":
            self.ui.table_btn_59.setIcon(icon)
        elif self.frameNum_table == "60":
            self.ui.table_btn_60.setIcon(icon)
        elif self.frameNum_table == "61":
            self.ui.table_btn_61.setIcon(icon)
        elif self.frameNum_table == "62":
            self.ui.table_btn_62.setIcon(icon)
        elif self.frameNum_table == "63":
            self.ui.table_btn_63.setIcon(icon)

    @staticmethod
    def deleteProcessTable(frame):
        data = TableBackend.search_frame(frame)
        HistoryBackend.insert(
            f"Table: {data[0][1]}", data[0][2], "", "deleted")
        TableBackend.delete(frame)

    def deleteEventTable(self):
        ques = QMessageBox.question(
            self, "Delete", "Are you sure ?", QMessageBox.Yes | QMessageBox.No)
        if ques == QMessageBox.Yes:
            self.deleteProcessTable(self.frameNum_table)
            self.refresh_Table()
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table)
            self.deleteIconEventTable()

    def setEnableObjEditTable(self, state):
        if state:
            data = TableBackend.search_frame(self.frameNum_table)
            self.ui.clear_btn_table_info.setEnabled(True)
            self.ui.submit_btn_table_info.setEnabled(True)
            self.ui.class_lineEdit_table_info.setReadOnly(False)
            self.ui.textEdit_detail_table_info.setReadOnly(False)
            if data[0][3] == "done":
                self.ui.icon_done_table_info.setEnabled(True)
            elif data[0][3] == "heart":
                self.ui.icon_heart_table_info.setEnabled(True)
            elif data[0][3] == "starOutline":
                self.ui.icon_starOut_table_info.setEnabled(True)
            elif data[0][3] == "starFill":
                self.ui.icon_starFill_table_info.setEnabled(True)
            elif data[0][3] == "circle":
                self.ui.icon_circle_table_info.setEnabled(True)
            elif data[0][3] == "starCircle":
                self.ui.icon_circleStar_table_info.setEnabled(True)
            elif data[0][3] == "smileEmoji":
                self.ui.icon_smileEmoji_table_info.setEnabled(True)
            elif data[0][3] == "sadEmoji":
                self.ui.icon_sadEmoji_table_info.setEnabled(True)
        else:
            self.ui.clear_btn_table_info.setEnabled(False)
            self.ui.submit_btn_table_info.setEnabled(False)
            self.ui.class_lineEdit_table_info.setReadOnly(True)
            self.ui.textEdit_detail_table_info.setReadOnly(True)
            self.ui.icon_done_table_info.setEnabled(False)
            self.ui.icon_heart_table_info.setEnabled(False)
            self.ui.icon_starOut_table_info.setEnabled(False)
            self.ui.icon_starFill_table_info.setEnabled(False)
            self.ui.icon_circle_table_info.setEnabled(False)
            self.ui.icon_circleStar_table_info.setEnabled(False)
            self.ui.icon_smileEmoji_table_info.setEnabled(False)
            self.ui.icon_sadEmoji_table_info.setEnabled(False)

    def editEventTable(self):
        if self.stateEditTable == "Disable":
            self.ui.edit_btn_table_info.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    \n"
                                                      "    background-color: rgb(12, 182, 0);\n"
                                                      "border-radius:10px;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
            self.setEnableObjEditTable(True)
            self.stateEditTable = "Enable"
        elif self.stateEditTable == "Enable":
            self.ui.edit_btn_table_info.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    \n"
                                                      "    background-color: rgb(115, 115, 115);\n"
                                                      "border-radius:10px;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
            self.setEnableObjEditTable(False)
            self.stateEditTable = "Disable"

    def updateDataInfoEventTable(self, frame):
        TableBackend.update(frame, self.ui.class_lineEdit_table_info.text(),
                            self.ui.textEdit_detail_table_info.toPlainText(), self.iconInfoBtnTable,
                            "active")
        HistoryBackend.insert(f"table: {self.ui.class_lineEdit_table_info.text()}",
                              self.ui.textEdit_detail_table_info.toPlainText(), "", "updated")
        self.refresh_Table()

    def submitEditEventTable(self):
        if len(self.ui.class_lineEdit_table_info.text()) != 0:
            if len(self.iconInfoBtnTable) != 0:
                self.updateDataInfoEventTable(self.frameNum_table)
                self.showInfo("Update", "Update was successful.")
            else:
                self.showError("Icon", "You should choose an icon.")
        else:
            self.showError("Title", "You should fill title lineEdit.")

    def clearInfoTable(self):
        self.ui.class_lineEdit_table_info.setText("")
        self.ui.textEdit_detail_table_info.setText("")
        self.iconInfoBtnTable = ""
        self.ui.icon_done_table_info.setEnabled(True)
        self.ui.icon_circle_table_info.setEnabled(True)
        self.ui.icon_heart_table_info.setEnabled(True)
        self.ui.icon_smileEmoji_table_info.setEnabled(True)
        self.ui.icon_sadEmoji_table_info.setEnabled(True)
        self.ui.icon_circleStar_table_info.setEnabled(True)
        self.ui.icon_starFill_table_info.setEnabled(True)
        self.ui.icon_starOut_table_info.setEnabled(True)
        self.ui.icon_done_table_info.setStyleSheet("QPushButton{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(115, 115, 115);\n"
                                                   "border-radius:10px;\n"
                                                   "border:none;\n"
                                                   "}\n"
                                                   "QPushButton:hover{\n"
                                                   "    color: rgb(255, 255, 255);\n"
                                                   "    background-color: rgb(95, 95, 95);\n"
                                                   "border-radius:5px;\n"
                                                   "}")
        self.ui.icon_heart_table_info.setStyleSheet("QPushButton{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(115, 115, 115);\n"
                                                    "border-radius:10px;\n"
                                                    "border:none;\n"
                                                    "}\n"
                                                    "QPushButton:hover{\n"
                                                    "    color: rgb(255, 255, 255);\n"
                                                    "    background-color: rgb(95, 95, 95);\n"
                                                    "border-radius:5px;\n"
                                                    "}")
        self.ui.icon_starOut_table_info.setStyleSheet("QPushButton{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(115, 115, 115);\n"
                                                      "border-radius:10px;\n"
                                                      "border:none;\n"
                                                      "}\n"
                                                      "QPushButton:hover{\n"
                                                      "    color: rgb(255, 255, 255);\n"
                                                      "    background-color: rgb(95, 95, 95);\n"
                                                      "border-radius:5px;\n"
                                                      "}")
        self.ui.icon_starFill_table_info.setStyleSheet("QPushButton{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(115, 115, 115);\n"
                                                       "border-radius:10px;\n"
                                                       "border:none;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(95, 95, 95);\n"
                                                       "border-radius:5px;\n"
                                                       "}")
        self.ui.icon_circle_table_info.setStyleSheet("QPushButton{\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "    background-color: rgb(115, 115, 115);\n"
                                                     "border-radius:10px;\n"
                                                     "border:none;\n"
                                                     "}\n"
                                                     "QPushButton:hover{\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "    background-color: rgb(95, 95, 95);\n"
                                                     "border-radius:5px;\n"
                                                     "}")
        self.ui.icon_circleStar_table_info.setStyleSheet("QPushButton{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(115, 115, 115);\n"
                                                         "border-radius:10px;\n"
                                                         "border:none;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(95, 95, 95);\n"
                                                         "border-radius:5px;\n"
                                                         "}")
        self.ui.icon_smileEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(115, 115, 115);\n"
                                                         "border-radius:10px;\n"
                                                         "border:none;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(95, 95, 95);\n"
                                                         "border-radius:5px;\n"
                                                         "}")
        self.ui.icon_sadEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(115, 115, 115);\n"
                                                       "border-radius:10px;\n"
                                                       "border:none;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(95, 95, 95);\n"
                                                       "border-radius:5px;\n"
                                                       "}")

    def doneBtnInfoTable(self):
        if not self.btn_done_tableInfo:
            self.iconInfoBtnTable = "done"
            self.btn_done_tableInfo = True
            self.ui.icon_smileEmoji_table_info.setEnabled(False)
            self.ui.icon_sadEmoji_table_info.setEnabled(False)
            self.ui.icon_circleStar_table_info.setEnabled(False)
            self.ui.icon_circle_table_info.setEnabled(False)
            self.ui.icon_starFill_table_info.setEnabled(False)
            self.ui.icon_starOut_table_info.setEnabled(False)
            self.ui.icon_heart_table_info.setEnabled(False)
            self.ui.icon_done_table_info.setStyleSheet("QPushButton{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(170, 85, 127);\n"
                                                       "border-radius:10px;\n"
                                                       "border:none;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(95, 95, 95);\n"
                                                       "border-radius:5px;\n"
                                                       "}")
        elif self.btn_done_tableInfo:
            self.iconInfoBtnTable = ""
            self.btn_done_tableInfo = False
            self.ui.icon_smileEmoji_table_info.setEnabled(True)
            self.ui.icon_sadEmoji_table_info.setEnabled(True)
            self.ui.icon_circleStar_table_info.setEnabled(True)
            self.ui.icon_circle_table_info.setEnabled(True)
            self.ui.icon_starFill_table_info.setEnabled(True)
            self.ui.icon_starOut_table_info.setEnabled(True)
            self.ui.icon_heart_table_info.setEnabled(True)
            self.ui.icon_done_table_info.setStyleSheet("QPushButton{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(115, 115, 115);\n"
                                                       "border-radius:10px;\n"
                                                       "border:none;\n"
                                                       "}\n"
                                                       "QPushButton:hover{\n"
                                                       "    color: rgb(255, 255, 255);\n"
                                                       "    background-color: rgb(95, 95, 95);\n"
                                                       "border-radius:5px;\n"
                                                       "}")

    def heartBtnInfoTable(self):
        if not self.btn_heart_tableInfo:
            self.iconInfoBtnTable = "heart"
            self.btn_heart_tableInfo = True
            self.ui.icon_done_table_info.setEnabled(False)
            self.ui.icon_smileEmoji_table_info.setEnabled(False)
            self.ui.icon_sadEmoji_table_info.setEnabled(False)
            self.ui.icon_circleStar_table_info.setEnabled(False)
            self.ui.icon_circle_table_info.setEnabled(False)
            self.ui.icon_starFill_table_info.setEnabled(False)
            self.ui.icon_starOut_table_info.setEnabled(False)
            self.ui.icon_heart_table_info.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(170, 85, 127);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")
        elif self.btn_heart_tableInfo:
            self.iconInfoBtnTable = ""
            self.btn_heart_tableInfo = False
            self.ui.icon_done_table_info.setEnabled(True)
            self.ui.icon_smileEmoji_table_info.setEnabled(True)
            self.ui.icon_sadEmoji_table_info.setEnabled(True)
            self.ui.icon_circleStar_table_info.setEnabled(True)
            self.ui.icon_circle_table_info.setEnabled(True)
            self.ui.icon_starFill_table_info.setEnabled(True)
            self.ui.icon_starOut_table_info.setEnabled(True)
            self.ui.icon_heart_table_info.setStyleSheet("QPushButton{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(115, 115, 115);\n"
                                                        "border-radius:10px;\n"
                                                        "border:none;\n"
                                                        "}\n"
                                                        "QPushButton:hover{\n"
                                                        "    color: rgb(255, 255, 255);\n"
                                                        "    background-color: rgb(95, 95, 95);\n"
                                                        "border-radius:5px;\n"
                                                        "}")

    def starOutBtnInfoTable(self):
        if not self.btn_starOut_tableInfo:
            self.iconInfoBtnTable = "starOutline"
            self.btn_starOut_tableInfo = True
            self.ui.icon_done_table_info.setEnabled(False)
            self.ui.icon_heart_table_info.setEnabled(False)
            self.ui.icon_smileEmoji_table_info.setEnabled(False)
            self.ui.icon_sadEmoji_table_info.setEnabled(False)
            self.ui.icon_circleStar_table_info.setEnabled(False)
            self.ui.icon_circle_table_info.setEnabled(False)
            self.ui.icon_starFill_table_info.setEnabled(False)
            self.ui.icon_starOut_table_info.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(170, 85, 127);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")
        elif self.btn_starOut_tableInfo:
            self.iconInfoBtnTable = ""
            self.btn_starOut_tableInfo = False
            self.ui.icon_done_table_info.setEnabled(True)
            self.ui.icon_heart_table_info.setEnabled(True)
            self.ui.icon_smileEmoji_table_info.setEnabled(True)
            self.ui.icon_sadEmoji_table_info.setEnabled(True)
            self.ui.icon_circleStar_table_info.setEnabled(True)
            self.ui.icon_circle_table_info.setEnabled(True)
            self.ui.icon_starFill_table_info.setEnabled(True)
            self.ui.icon_starOut_table_info.setStyleSheet("QPushButton{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(115, 115, 115);\n"
                                                          "border-radius:10px;\n"
                                                          "border:none;\n"
                                                          "}\n"
                                                          "QPushButton:hover{\n"
                                                          "    color: rgb(255, 255, 255);\n"
                                                          "    background-color: rgb(95, 95, 95);\n"
                                                          "border-radius:5px;\n"
                                                          "}")

    def starFillBtnInfoTable(self):
        if not self.btn_starFill_tableInfo:
            self.iconInfoBtnTable = "starFill"
            self.btn_starFill_tableInfo = True
            self.ui.icon_done_table_info.setEnabled(False)
            self.ui.icon_heart_table_info.setEnabled(False)
            self.ui.icon_starOut_table_info.setEnabled(False)
            self.ui.icon_smileEmoji_table_info.setEnabled(False)
            self.ui.icon_sadEmoji_table_info.setEnabled(False)
            self.ui.icon_circleStar_table_info.setEnabled(False)
            self.ui.icon_circle_table_info.setEnabled(False)
            self.ui.icon_starFill_table_info.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(170, 85, 127);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")
        elif self.btn_starFill_tableInfo:
            self.iconInfoBtnTable = ""
            self.btn_starFill_tableInfo = False
            self.ui.icon_done_table_info.setEnabled(True)
            self.ui.icon_heart_table_info.setEnabled(True)
            self.ui.icon_starOut_table_info.setEnabled(True)
            self.ui.icon_smileEmoji_table_info.setEnabled(True)
            self.ui.icon_sadEmoji_table_info.setEnabled(True)
            self.ui.icon_circleStar_table_info.setEnabled(True)
            self.ui.icon_circle_table_info.setEnabled(True)
            self.ui.icon_starFill_table_info.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(115, 115, 115);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")

    def circleBtnInfoTable(self):
        if not self.btn_circle_tableInfo:
            self.iconInfoBtnTable = "circle"
            self.btn_circle_tableInfo = True
            self.ui.icon_done_table_info.setEnabled(False)
            self.ui.icon_heart_table_info.setEnabled(False)
            self.ui.icon_starOut_table_info.setEnabled(False)
            self.ui.icon_starFill_table_info.setEnabled(False)
            self.ui.icon_smileEmoji_table_info.setEnabled(False)
            self.ui.icon_sadEmoji_table_info.setEnabled(False)
            self.ui.icon_circleStar_table_info.setEnabled(False)
            self.ui.icon_circle_table_info.setStyleSheet("QPushButton{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(170, 85, 127);\n"
                                                         "border-radius:10px;\n"
                                                         "border:none;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(95, 95, 95);\n"
                                                         "border-radius:5px;\n"
                                                         "}")
        elif self.btn_circle_tableInfo:
            self.iconInfoBtnTable = ""
            self.btn_circle_tableInfo = False
            self.ui.icon_done_table_info.setEnabled(True)
            self.ui.icon_heart_table_info.setEnabled(True)
            self.ui.icon_starOut_table_info.setEnabled(True)
            self.ui.icon_starFill_table_info.setEnabled(True)
            self.ui.icon_smileEmoji_table_info.setEnabled(True)
            self.ui.icon_sadEmoji_table_info.setEnabled(True)
            self.ui.icon_circleStar_table_info.setEnabled(True)
            self.ui.icon_circle_table_info.setStyleSheet("QPushButton{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(115, 115, 115);\n"
                                                         "border-radius:10px;\n"
                                                         "border:none;\n"
                                                         "}\n"
                                                         "QPushButton:hover{\n"
                                                         "    color: rgb(255, 255, 255);\n"
                                                         "    background-color: rgb(95, 95, 95);\n"
                                                         "border-radius:5px;\n"
                                                         "}")

    def starCircleBtnInfoTable(self):
        if not self.btn_starCircle_tableInfo:
            self.iconInfoBtnTable = "starCircle"
            self.btn_starCircle_tableInfo = True
            self.ui.icon_done_table_info.setEnabled(False)
            self.ui.icon_circle_table_info.setEnabled(False)
            self.ui.icon_heart_table_info.setEnabled(False)
            self.ui.icon_starOut_table_info.setEnabled(False)
            self.ui.icon_starFill_table_info.setEnabled(False)
            self.ui.icon_smileEmoji_table_info.setEnabled(False)
            self.ui.icon_sadEmoji_table_info.setEnabled(False)
            self.ui.icon_circleStar_table_info.setStyleSheet("QPushButton{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(170, 85, 127);\n"
                                                             "border-radius:10px;\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "QPushButton:hover{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(95, 95, 95);\n"
                                                             "border-radius:5px;\n"
                                                             "}")
        elif self.btn_starCircle_tableInfo:
            self.iconInfoBtnTable = ""
            self.btn_starCircle_tableInfo = False
            self.ui.icon_done_table_info.setEnabled(True)
            self.ui.icon_circle_table_info.setEnabled(True)
            self.ui.icon_heart_table_info.setEnabled(True)
            self.ui.icon_starOut_table_info.setEnabled(True)
            self.ui.icon_starFill_table_info.setEnabled(True)
            self.ui.icon_smileEmoji_table_info.setEnabled(True)
            self.ui.icon_sadEmoji_table_info.setEnabled(True)
            self.ui.icon_circleStar_table_info.setStyleSheet("QPushButton{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(115, 115, 115);\n"
                                                             "border-radius:10px;\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "QPushButton:hover{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(95, 95, 95);\n"
                                                             "border-radius:5px;\n"
                                                             "}")

    def smileBtnInfoTable(self):
        if not self.btn_smile_tableInfo:
            self.iconInfoBtnTable = "smileEmoji"
            self.btn_smile_tableInfo = True
            self.ui.icon_done_table_info.setEnabled(False)
            self.ui.icon_circle_table_info.setEnabled(False)
            self.ui.icon_heart_table_info.setEnabled(False)
            self.ui.icon_starOut_table_info.setEnabled(False)
            self.ui.icon_starFill_table_info.setEnabled(False)
            self.ui.icon_circleStar_table_info.setEnabled(False)
            self.ui.icon_sadEmoji_table_info.setEnabled(False)
            self.ui.icon_smileEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(170, 85, 127);\n"
                                                             "border-radius:10px;\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "QPushButton:hover{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(95, 95, 95);\n"
                                                             "border-radius:5px;\n"
                                                             "}")
        elif self.btn_smile_tableInfo:
            self.iconInfoBtnTable = ""
            self.btn_smile_tableInfo = False
            self.ui.icon_done_table_info.setEnabled(True)
            self.ui.icon_circle_table_info.setEnabled(True)
            self.ui.icon_heart_table_info.setEnabled(True)
            self.ui.icon_starOut_table_info.setEnabled(True)
            self.ui.icon_starFill_table_info.setEnabled(True)
            self.ui.icon_circleStar_table_info.setEnabled(True)
            self.ui.icon_sadEmoji_table_info.setEnabled(True)
            self.ui.icon_smileEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(115, 115, 115);\n"
                                                             "border-radius:10px;\n"
                                                             "border:none;\n"
                                                             "}\n"
                                                             "QPushButton:hover{\n"
                                                             "    color: rgb(255, 255, 255);\n"
                                                             "    background-color: rgb(95, 95, 95);\n"
                                                             "border-radius:5px;\n"
                                                             "}")

    def sadBtnInfoTable(self):
        if not self.btn_sad_tableInfo:
            self.iconInfoBtnTable = "sadEmoji"
            self.btn_sad_tableInfo = True
            self.ui.icon_done_table_info.setEnabled(False)
            self.ui.icon_circle_table_info.setEnabled(False)
            self.ui.icon_heart_table_info.setEnabled(False)
            self.ui.icon_starOut_table_info.setEnabled(False)
            self.ui.icon_starFill_table_info.setEnabled(False)
            self.ui.icon_circleStar_table_info.setEnabled(False)
            self.ui.icon_smileEmoji_table_info.setEnabled(False)
            self.ui.icon_sadEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(170, 85, 127);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")
        elif self.btn_sad_tableInfo:
            self.iconInfoBtnTable = ""
            self.btn_sad_tableInfo = False
            self.ui.icon_done_table_info.setEnabled(True)
            self.ui.icon_circle_table_info.setEnabled(True)
            self.ui.icon_heart_table_info.setEnabled(True)
            self.ui.icon_starOut_table_info.setEnabled(True)
            self.ui.icon_starFill_table_info.setEnabled(True)
            self.ui.icon_circleStar_table_info.setEnabled(True)
            self.ui.icon_smileEmoji_table_info.setEnabled(True)
            self.ui.icon_sadEmoji_table_info.setStyleSheet("QPushButton{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(115, 115, 115);\n"
                                                           "border-radius:10px;\n"
                                                           "border:none;\n"
                                                           "}\n"
                                                           "QPushButton:hover{\n"
                                                           "    color: rgb(255, 255, 255);\n"
                                                           "    background-color: rgb(95, 95, 95);\n"
                                                           "border-radius:5px;\n"
                                                           "}")

    def table_frame_1(self):
        self.frameNum_table = "1"
        if self.checkEmptyTable("1"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Saturday 6:00-8:00")
        else:
            self.setInformationTable("1")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_2(self):
        self.frameNum_table = "2"
        if self.checkEmptyTable("2"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Saturday 8:00-10:00")
        else:
            self.setInformationTable("2")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_3(self):
        self.frameNum_table = "3"
        if self.checkEmptyTable("3"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Saturday 10:00-12:00")
        else:
            self.setInformationTable("3")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_4(self):
        self.frameNum_table = "4"
        if self.checkEmptyTable("4"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Saturday 12:00-14:00")
        else:
            self.setInformationTable("4")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_5(self):
        self.frameNum_table = "5"
        if self.checkEmptyTable("5"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Saturday 14:00-16:00")
        else:
            self.setInformationTable("5")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_6(self):
        self.frameNum_table = "6"
        if self.checkEmptyTable("6"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Saturday 16:00-18:00")
        else:
            self.setInformationTable("6")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_7(self):
        self.frameNum_table = "7"
        if self.checkEmptyTable("7"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Saturday 18:00-20:00")
        else:
            self.setInformationTable("7")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_8(self):
        self.frameNum_table = "8"
        if self.checkEmptyTable("8"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Saturday 20:00-22:00")
        else:
            self.setInformationTable("8")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_9(self):
        self.frameNum_table = "9"
        if self.checkEmptyTable("9"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Saturday 22:00-24:00")
        else:
            self.setInformationTable("9")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_10(self):
        self.frameNum_table = "10"
        if self.checkEmptyTable("10"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Sunday 6:00-8:00")
        else:
            self.setInformationTable("10")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_11(self):
        self.frameNum_table = "11"
        if self.checkEmptyTable("11"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Sunday 8:00-10:00")
        else:
            self.setInformationTable("11")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_12(self):
        self.frameNum_table = "12"
        if self.checkEmptyTable("12"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Sunday 10:00-12:00")
        else:
            self.setInformationTable("12")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_13(self):
        self.frameNum_table = "13"
        if self.checkEmptyTable("13"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Sunday 12:00-14:00")
        else:
            self.setInformationTable("13")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_14(self):
        self.frameNum_table = "14"
        if self.checkEmptyTable("14"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Sunday 14:00-16:00")
        else:
            self.setInformationTable("14")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_15(self):
        self.frameNum_table = "15"
        if self.checkEmptyTable("15"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Sunday 16:00-18:00")
        else:
            self.setInformationTable("15")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_16(self):
        self.frameNum_table = "16"
        if self.checkEmptyTable("16"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Sunday 18:00-20:00")
        else:
            self.setInformationTable("16")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_17(self):
        self.frameNum_table = "17"
        if self.checkEmptyTable("17"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Sunday 20:00-22:00")
        else:
            self.setInformationTable("17")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_18(self):
        self.frameNum_table = "18"
        if self.checkEmptyTable("18"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Sunday 22:00-24:00")
        else:
            self.setInformationTable("18")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_19(self):
        self.frameNum_table = "19"
        if self.checkEmptyTable("19"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Monday 6:00-8:00")
        else:
            self.setInformationTable("19")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_20(self):
        self.frameNum_table = "20"
        if self.checkEmptyTable("20"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Monday 8:00-10:00")
        else:
            self.setInformationTable("20")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_21(self):
        self.frameNum_table = "21"
        if self.checkEmptyTable("21"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Monday 10:00-12:00")
        else:
            self.setInformationTable("21")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_22(self):
        self.frameNum_table = "22"
        if self.checkEmptyTable("22"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Monday 12:00-14:00")
        else:
            self.setInformationTable("22")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_23(self):
        self.frameNum_table = "23"
        if self.checkEmptyTable("23"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Monday 14:00-16:00")
        else:
            self.setInformationTable("23")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_24(self):
        self.frameNum_table = "24"
        if self.checkEmptyTable("24"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Monday 16:00-18:00")
        else:
            self.setInformationTable("24")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_25(self):
        self.frameNum_table = "25"
        if self.checkEmptyTable("25"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Monday 18:00-20:00")
        else:
            self.setInformationTable("25")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_26(self):
        self.frameNum_table = "26"
        if self.checkEmptyTable("26"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Monday 20:00-22:00")
        else:
            self.setInformationTable("26")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_27(self):
        self.frameNum_table = "27"
        if self.checkEmptyTable("27"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Monday 22:00-24:00")
        else:
            self.setInformationTable("27")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_28(self):
        self.frameNum_table = "28"
        if self.checkEmptyTable("28"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Tuesday 6:00-8:00")
        else:
            self.setInformationTable("28")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_29(self):
        self.frameNum_table = "29"
        if self.checkEmptyTable("29"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Tuesday 8:00-10:00")
        else:
            self.setInformationTable("29")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_30(self):
        self.frameNum_table = "30"
        if self.checkEmptyTable("30"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Tuesday 10:00-12:00")
        else:
            self.setInformationTable("30")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_31(self):
        self.frameNum_table = "31"
        if self.checkEmptyTable("31"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Tuesday 12:00-14:00")
        else:
            self.setInformationTable("31")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_32(self):
        self.frameNum_table = "32"
        if self.checkEmptyTable("32"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Tuesday 14:00-16:00")
        else:
            self.setInformationTable("32")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_33(self):
        self.frameNum_table = "33"
        if self.checkEmptyTable("33"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Tuesday 16:00-18:00")
        else:
            self.setInformationTable("33")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_34(self):
        self.frameNum_table = "34"
        if self.checkEmptyTable("34"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Tuesday 18:00-20:00")
        else:
            self.setInformationTable("34")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_35(self):
        self.frameNum_table = "35"
        if self.checkEmptyTable("35"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Tuesday 20:00-22:00")
        else:
            self.setInformationTable("35")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_36(self):
        self.frameNum_table = "36"
        if self.checkEmptyTable("36"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Tuesday 22:00-24:00")
        else:
            self.setInformationTable("36")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_37(self):
        self.frameNum_table = "37"
        if self.checkEmptyTable("37"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Wednesday 6:00-8:00")
        else:
            self.setInformationTable("37")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_38(self):
        self.frameNum_table = "38"
        if self.checkEmptyTable("38"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Wednesday 8:00-10:00")
        else:
            self.setInformationTable("38")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_39(self):
        self.frameNum_table = "39"
        if self.checkEmptyTable("39"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Wednesday 10:00-12:00")
        else:
            self.setInformationTable("39")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_40(self):
        self.frameNum_table = "40"
        if self.checkEmptyTable("40"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Wednesday 12:00-14:00")
        else:
            self.setInformationTable("40")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_41(self):
        self.frameNum_table = "41"
        if self.checkEmptyTable("41"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Wednesday 14:00-16:00")
        else:
            self.setInformationTable("41")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_42(self):
        self.frameNum_table = "42"
        if self.checkEmptyTable("42"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Wednesday 16:00-18:00")
        else:
            self.setInformationTable("42")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_43(self):
        self.frameNum_table = "43"
        if self.checkEmptyTable("43"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Wednesday 18:00-20:00")
        else:
            self.setInformationTable("43")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_44(self):
        self.frameNum_table = "44"
        if self.checkEmptyTable("44"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Wednesday 20:00-22:00")
        else:
            self.setInformationTable("44")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_45(self):
        self.frameNum_table = "45"
        if self.checkEmptyTable("45"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Wednesday 22:00-24:00")
        else:
            self.setInformationTable("45")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_46(self):
        self.frameNum_table = "46"
        if self.checkEmptyTable("46"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Thursday 6:00-8:00")
        else:
            self.setInformationTable("46")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_47(self):
        self.frameNum_table = "47"
        if self.checkEmptyTable("47"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Thursday 8:00-10:00")
        else:
            self.setInformationTable("47")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_48(self):
        self.frameNum_table = "48"
        if self.checkEmptyTable("48"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Thursday 10:00-12:00")
        else:
            self.setInformationTable("48")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_49(self):
        self.frameNum_table = "49"
        if self.checkEmptyTable("49"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Thursday 12:00-14:00")
        else:
            self.setInformationTable("49")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_50(self):
        self.frameNum_table = "50"
        if self.checkEmptyTable("50"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Thursday 14:00-16:00")
        else:
            self.setInformationTable("50")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_51(self):
        self.frameNum_table = "51"
        if self.checkEmptyTable("51"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Thursday 16:00-18:00")
        else:
            self.setInformationTable("51")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_52(self):
        self.frameNum_table = "52"
        if self.checkEmptyTable("52"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Thursday 18:00-20:00")
        else:
            self.setInformationTable("52")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_53(self):
        self.frameNum_table = "53"
        if self.checkEmptyTable("53"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Thursday 20:00-22:00")
        else:
            self.setInformationTable("53")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_54(self):
        self.frameNum_table = "54"
        if self.checkEmptyTable("54"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Thursday 22:00-24:00")
        else:
            self.setInformationTable("54")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_55(self):
        self.frameNum_table = "55"
        if self.checkEmptyTable("55"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Friday 6:00-8:00")
        else:
            self.setInformationTable("55")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_56(self):
        self.frameNum_table = "56"
        if self.checkEmptyTable("56"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Friday 8:00-10:00")
        else:
            self.setInformationTable("56")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_57(self):
        self.frameNum_table = "57"
        if self.checkEmptyTable("57"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Friday 10:00-12:00")
        else:
            self.setInformationTable("57")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_58(self):
        self.frameNum_table = "58"
        if self.checkEmptyTable("58"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Friday 12:00-14:00")
        else:
            self.setInformationTable("58")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_59(self):
        self.frameNum_table = "59"
        if self.checkEmptyTable("59"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Friday 14:00-16:00")
        else:
            self.setInformationTable("59")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_60(self):
        self.frameNum_table = "60"
        if self.checkEmptyTable("60"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Friday 16:00-18:00")
        else:
            self.setInformationTable("60")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_61(self):
        self.frameNum_table = "61"
        if self.checkEmptyTable("61"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Friday 18:00-20:00")
        else:
            self.setInformationTable("61")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_62(self):
        self.frameNum_table = "62"
        if self.checkEmptyTable("62"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Friday 20:00-22:00")
        else:
            self.setInformationTable("62")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def table_frame_63(self):
        self.frameNum_table = "63"
        if self.checkEmptyTable("63"):
            if self.askForBuildEvent():
                self.ui.stackedWidget.setCurrentWidget(self.ui.Table_add)
                self.ui.title_table_add.setText("Friday 22:00-24:00")
        else:
            self.setInformationTable("63")
            self.ui.stackedWidget.setCurrentWidget(self.ui.Table_Info)

    def disableAndEnableBtn(self, state):
        if state:
            self.ui.frame_btn_home_1.setEnabled(False)
            self.ui.frame_btn_home_2.setEnabled(False)
            self.ui.frame_btn_home_3.setEnabled(False)
            self.ui.frame_btn_home_4.setEnabled(False)
            self.ui.frame_btn_home_5.setEnabled(False)
            self.ui.frame_btn_home_6.setEnabled(False)
            self.ui.frame_btn_home_7.setEnabled(False)
            self.ui.frame_btn_home_8.setEnabled(False)
            self.ui.frame_btn_home_9.setEnabled(False)
            self.ui.frame_btn_home_10.setEnabled(False)
            self.ui.frame_btn_home_11.setEnabled(False)
            self.ui.frame_btn_home_12.setEnabled(False)
            self.ui.table_btn_1.setEnabled(False)
            self.ui.table_btn_2.setEnabled(False)
            self.ui.table_btn_3.setEnabled(False)
            self.ui.table_btn_4.setEnabled(False)
            self.ui.table_btn_5.setEnabled(False)
            self.ui.table_btn_6.setEnabled(False)
            self.ui.table_btn_7.setEnabled(False)
            self.ui.table_btn_8.setEnabled(False)
            self.ui.table_btn_9.setEnabled(False)
            self.ui.table_btn_10.setEnabled(False)
            self.ui.table_btn_11.setEnabled(False)
            self.ui.table_btn_12.setEnabled(False)
            self.ui.table_btn_13.setEnabled(False)
            self.ui.table_btn_14.setEnabled(False)
            self.ui.table_btn_15.setEnabled(False)
            self.ui.table_btn_16.setEnabled(False)
            self.ui.table_btn_17.setEnabled(False)
            self.ui.table_btn_18.setEnabled(False)
            self.ui.table_btn_19.setEnabled(False)
            self.ui.table_btn_20.setEnabled(False)
            self.ui.table_btn_21.setEnabled(False)
            self.ui.table_btn_22.setEnabled(False)
            self.ui.table_btn_23.setEnabled(False)
            self.ui.table_btn_24.setEnabled(False)
            self.ui.table_btn_25.setEnabled(False)
            self.ui.table_btn_26.setEnabled(False)
            self.ui.table_btn_27.setEnabled(False)
            self.ui.table_btn_28.setEnabled(False)
            self.ui.table_btn_29.setEnabled(False)
            self.ui.table_btn_30.setEnabled(False)
            self.ui.table_btn_31.setEnabled(False)
            self.ui.table_btn_32.setEnabled(False)
            self.ui.table_btn_33.setEnabled(False)
            self.ui.table_btn_34.setEnabled(False)
            self.ui.table_btn_35.setEnabled(False)
            self.ui.table_btn_36.setEnabled(False)
            self.ui.table_btn_37.setEnabled(False)
            self.ui.table_btn_38.setEnabled(False)
            self.ui.table_btn_39.setEnabled(False)
            self.ui.table_btn_40.setEnabled(False)
            self.ui.table_btn_41.setEnabled(False)
            self.ui.table_btn_42.setEnabled(False)
            self.ui.table_btn_43.setEnabled(False)
            self.ui.table_btn_44.setEnabled(False)
            self.ui.table_btn_45.setEnabled(False)
            self.ui.table_btn_46.setEnabled(False)
            self.ui.table_btn_47.setEnabled(False)
            self.ui.table_btn_48.setEnabled(False)
            self.ui.table_btn_49.setEnabled(False)
            self.ui.table_btn_50.setEnabled(False)
            self.ui.table_btn_51.setEnabled(False)
            self.ui.table_btn_52.setEnabled(False)
            self.ui.table_btn_53.setEnabled(False)
            self.ui.table_btn_54.setEnabled(False)
            self.ui.table_btn_55.setEnabled(False)
            self.ui.table_btn_56.setEnabled(False)
            self.ui.table_btn_57.setEnabled(False)
            self.ui.table_btn_58.setEnabled(False)
            self.ui.table_btn_59.setEnabled(False)
            self.ui.table_btn_60.setEnabled(False)
            self.ui.table_btn_61.setEnabled(False)
            self.ui.table_btn_62.setEnabled(False)
            self.ui.table_btn_63.setEnabled(False)
            self.ui.uni_btn_1.setEnabled(False)
            self.ui.uni_btn_2.setEnabled(False)
            self.ui.uni_btn_3.setEnabled(False)
            self.ui.uni_btn_4.setEnabled(False)
            self.ui.uni_btn_5.setEnabled(False)
            self.ui.uni_btn_6.setEnabled(False)
            self.ui.uni_btn_7.setEnabled(False)
            self.ui.uni_btn_8.setEnabled(False)
            self.ui.uni_btn_9.setEnabled(False)
            self.ui.uni_btn_10.setEnabled(False)
            self.ui.uni_btn_11.setEnabled(False)
            self.ui.uni_btn_12.setEnabled(False)
            self.ui.uni_btn_13.setEnabled(False)
            self.ui.uni_btn_14.setEnabled(False)
            self.ui.uni_btn_15.setEnabled(False)
            self.ui.uni_btn_16.setEnabled(False)
            self.ui.uni_btn_17.setEnabled(False)
            self.ui.uni_btn_18.setEnabled(False)
            self.ui.uni_btn_19.setEnabled(False)
            self.ui.uni_btn_20.setEnabled(False)
            self.ui.uni_btn_21.setEnabled(False)
            self.ui.uni_btn_22.setEnabled(False)
            self.ui.uni_btn_23.setEnabled(False)
            self.ui.uni_btn_24.setEnabled(False)
            self.ui.uni_btn_25.setEnabled(False)
            self.ui.uni_btn_26.setEnabled(False)
            self.ui.uni_btn_27.setEnabled(False)
            self.ui.uni_btn_28.setEnabled(False)
            self.ui.uni_btn_29.setEnabled(False)
            self.ui.uni_btn_30.setEnabled(False)
            self.ui.uni_btn_31.setEnabled(False)
            self.ui.uni_btn_32.setEnabled(False)
            self.ui.uni_btn_33.setEnabled(False)
            self.ui.uni_btn_34.setEnabled(False)
            self.ui.uni_btn_35.setEnabled(False)
            self.ui.uni_btn_36.setEnabled(False)
            self.ui.uni_btn_37.setEnabled(False)
            self.ui.uni_btn_38.setEnabled(False)
            self.ui.uni_btn_39.setEnabled(False)
            self.ui.uni_btn_40.setEnabled(False)
            self.ui.uni_btn_41.setEnabled(False)
            self.ui.uni_btn_42.setEnabled(False)
            self.ui.uni_btn_43.setEnabled(False)
            self.ui.uni_btn_44.setEnabled(False)
            self.ui.uni_btn_45.setEnabled(False)
            self.ui.uni_btn_46.setEnabled(False)
            self.ui.uni_btn_47.setEnabled(False)
            self.ui.uni_btn_48.setEnabled(False)
            self.ui.uni_btn_49.setEnabled(False)
            self.ui.uni_btn_50.setEnabled(False)
            self.ui.uni_btn_51.setEnabled(False)
            self.ui.uni_btn_52.setEnabled(False)
            self.ui.uni_btn_53.setEnabled(False)
            self.ui.uni_btn_54.setEnabled(False)
            self.ui.uni_btn_55.setEnabled(False)
            self.ui.uni_btn_56.setEnabled(False)
            self.ui.uni_btn_57.setEnabled(False)
            self.ui.uni_btn_58.setEnabled(False)
            self.ui.uni_btn_59.setEnabled(False)
            self.ui.uni_btn_60.setEnabled(False)
            self.ui.uni_btn_61.setEnabled(False)
            self.ui.uni_btn_62.setEnabled(False)
            self.ui.uni_btn_63.setEnabled(False)
        else:
            self.ui.frame_btn_home_1.setEnabled(True)
            self.ui.frame_btn_home_2.setEnabled(True)
            self.ui.frame_btn_home_3.setEnabled(True)
            self.ui.frame_btn_home_4.setEnabled(True)
            self.ui.frame_btn_home_5.setEnabled(True)
            self.ui.frame_btn_home_6.setEnabled(True)
            self.ui.frame_btn_home_7.setEnabled(True)
            self.ui.frame_btn_home_8.setEnabled(True)
            self.ui.frame_btn_home_9.setEnabled(True)
            self.ui.frame_btn_home_10.setEnabled(True)
            self.ui.frame_btn_home_11.setEnabled(True)
            self.ui.frame_btn_home_12.setEnabled(True)
            self.ui.table_btn_1.setEnabled(True)
            self.ui.table_btn_2.setEnabled(True)
            self.ui.table_btn_3.setEnabled(True)
            self.ui.table_btn_4.setEnabled(True)
            self.ui.table_btn_5.setEnabled(True)
            self.ui.table_btn_6.setEnabled(True)
            self.ui.table_btn_7.setEnabled(True)
            self.ui.table_btn_8.setEnabled(True)
            self.ui.table_btn_9.setEnabled(True)
            self.ui.table_btn_10.setEnabled(True)
            self.ui.table_btn_11.setEnabled(True)
            self.ui.table_btn_12.setEnabled(True)
            self.ui.table_btn_13.setEnabled(True)
            self.ui.table_btn_14.setEnabled(True)
            self.ui.table_btn_15.setEnabled(True)
            self.ui.table_btn_16.setEnabled(True)
            self.ui.table_btn_17.setEnabled(True)
            self.ui.table_btn_18.setEnabled(True)
            self.ui.table_btn_19.setEnabled(True)
            self.ui.table_btn_20.setEnabled(True)
            self.ui.table_btn_21.setEnabled(True)
            self.ui.table_btn_22.setEnabled(True)
            self.ui.table_btn_23.setEnabled(True)
            self.ui.table_btn_24.setEnabled(True)
            self.ui.table_btn_25.setEnabled(True)
            self.ui.table_btn_26.setEnabled(True)
            self.ui.table_btn_27.setEnabled(True)
            self.ui.table_btn_28.setEnabled(True)
            self.ui.table_btn_29.setEnabled(True)
            self.ui.table_btn_30.setEnabled(True)
            self.ui.table_btn_31.setEnabled(True)
            self.ui.table_btn_32.setEnabled(True)
            self.ui.table_btn_33.setEnabled(True)
            self.ui.table_btn_34.setEnabled(True)
            self.ui.table_btn_35.setEnabled(True)
            self.ui.table_btn_36.setEnabled(True)
            self.ui.table_btn_37.setEnabled(True)
            self.ui.table_btn_38.setEnabled(True)
            self.ui.table_btn_39.setEnabled(True)
            self.ui.table_btn_40.setEnabled(True)
            self.ui.table_btn_41.setEnabled(True)
            self.ui.table_btn_42.setEnabled(True)
            self.ui.table_btn_43.setEnabled(True)
            self.ui.table_btn_44.setEnabled(True)
            self.ui.table_btn_45.setEnabled(True)
            self.ui.table_btn_46.setEnabled(True)
            self.ui.table_btn_47.setEnabled(True)
            self.ui.table_btn_48.setEnabled(True)
            self.ui.table_btn_49.setEnabled(True)
            self.ui.table_btn_50.setEnabled(True)
            self.ui.table_btn_51.setEnabled(True)
            self.ui.table_btn_52.setEnabled(True)
            self.ui.table_btn_53.setEnabled(True)
            self.ui.table_btn_54.setEnabled(True)
            self.ui.table_btn_55.setEnabled(True)
            self.ui.table_btn_56.setEnabled(True)
            self.ui.table_btn_57.setEnabled(True)
            self.ui.table_btn_58.setEnabled(True)
            self.ui.table_btn_59.setEnabled(True)
            self.ui.table_btn_60.setEnabled(True)
            self.ui.table_btn_61.setEnabled(True)
            self.ui.table_btn_62.setEnabled(True)
            self.ui.table_btn_63.setEnabled(True)
            self.ui.uni_btn_1.setEnabled(True)
            self.ui.uni_btn_2.setEnabled(True)
            self.ui.uni_btn_3.setEnabled(True)
            self.ui.uni_btn_4.setEnabled(True)
            self.ui.uni_btn_5.setEnabled(True)
            self.ui.uni_btn_6.setEnabled(True)
            self.ui.uni_btn_7.setEnabled(True)
            self.ui.uni_btn_8.setEnabled(True)
            self.ui.uni_btn_9.setEnabled(True)
            self.ui.uni_btn_10.setEnabled(True)
            self.ui.uni_btn_11.setEnabled(True)
            self.ui.uni_btn_12.setEnabled(True)
            self.ui.uni_btn_13.setEnabled(True)
            self.ui.uni_btn_14.setEnabled(True)
            self.ui.uni_btn_15.setEnabled(True)
            self.ui.uni_btn_16.setEnabled(True)
            self.ui.uni_btn_17.setEnabled(True)
            self.ui.uni_btn_18.setEnabled(True)
            self.ui.uni_btn_19.setEnabled(True)
            self.ui.uni_btn_20.setEnabled(True)
            self.ui.uni_btn_21.setEnabled(True)
            self.ui.uni_btn_22.setEnabled(True)
            self.ui.uni_btn_23.setEnabled(True)
            self.ui.uni_btn_24.setEnabled(True)
            self.ui.uni_btn_25.setEnabled(True)
            self.ui.uni_btn_26.setEnabled(True)
            self.ui.uni_btn_27.setEnabled(True)
            self.ui.uni_btn_28.setEnabled(True)
            self.ui.uni_btn_29.setEnabled(True)
            self.ui.uni_btn_30.setEnabled(True)
            self.ui.uni_btn_31.setEnabled(True)
            self.ui.uni_btn_32.setEnabled(True)
            self.ui.uni_btn_33.setEnabled(True)
            self.ui.uni_btn_34.setEnabled(True)
            self.ui.uni_btn_35.setEnabled(True)
            self.ui.uni_btn_36.setEnabled(True)
            self.ui.uni_btn_37.setEnabled(True)
            self.ui.uni_btn_38.setEnabled(True)
            self.ui.uni_btn_39.setEnabled(True)
            self.ui.uni_btn_40.setEnabled(True)
            self.ui.uni_btn_41.setEnabled(True)
            self.ui.uni_btn_42.setEnabled(True)
            self.ui.uni_btn_43.setEnabled(True)
            self.ui.uni_btn_44.setEnabled(True)
            self.ui.uni_btn_45.setEnabled(True)
            self.ui.uni_btn_46.setEnabled(True)
            self.ui.uni_btn_47.setEnabled(True)
            self.ui.uni_btn_48.setEnabled(True)
            self.ui.uni_btn_49.setEnabled(True)
            self.ui.uni_btn_50.setEnabled(True)
            self.ui.uni_btn_51.setEnabled(True)
            self.ui.uni_btn_52.setEnabled(True)
            self.ui.uni_btn_53.setEnabled(True)
            self.ui.uni_btn_54.setEnabled(True)
            self.ui.uni_btn_55.setEnabled(True)
            self.ui.uni_btn_56.setEnabled(True)
            self.ui.uni_btn_57.setEnabled(True)
            self.ui.uni_btn_58.setEnabled(True)
            self.ui.uni_btn_59.setEnabled(True)
            self.ui.uni_btn_60.setEnabled(True)
            self.ui.uni_btn_61.setEnabled(True)
            self.ui.uni_btn_62.setEnabled(True)
            self.ui.uni_btn_63.setEnabled(True)

    def lockBtnHome(self):
        _translate = QCoreApplication.translate
        if self.stateLockBtn == "Disable":
            self.stateLockBtn = "Enable"
            icon = QIcon()
            icon.addPixmap(
                QPixmap("photo/outline_lock_black_24dp.png"), QIcon.Normal, QIcon.Off)
            self.ui.lock_btn.setIcon(icon)
            self.ui.lock_btn.setToolTip(_translate("MainWindow", "Lock"))
            self.disableAndEnableBtn(True)
        elif self.stateLockBtn == "Enable":
            self.stateLockBtn = "Disable"
            icon = QIcon()
            icon.addPixmap(
                QPixmap("photo/outline_lock_open_black_24dp.png"), QIcon.Normal, QIcon.Off)
            self.ui.lock_btn.setIcon(icon)
            self.ui.lock_btn.setToolTip(_translate("MainWindow", "Unlock"))
            self.disableAndEnableBtn(False)


def setup():
    app = QApplication([])
    ui = Table()
    ui.show()
    app.exec_()


setup()
