# from PyQt5.QtWidgets import QApplication, QFrame

from PyQt5.Qt import *

import sys
from Pyqt5_demo.resource.login import Ui_Form


class LoginPane(QFrame, Ui_Form):
    show_register_signal = pyqtSignal()
    check_login_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)
        # gif 动画播放
        move =QMovie(":/login/images/login_top_bg.gif")
        move.setScaledSize(QSize(500, 235))
        self.login_top_bg_label.setMovie(move)
        move.start()

    def show_register_pane(self):
        print("show_register_pane")
        # 发射信号
        self.show_register_signal.emit()

    def open_qq_link(self):
        # 点击button 打开网页
        print("open_qq_link")
        link = "https:www.baidu.com"
        QDesktopServices.openUrl(QUrl(link))

    def enable_login_btn(self):
        print("enable_login_btn")
        account = self.account_cb.currentText()
        password = self.login_pwd.text()
        if len(account) > 0 and len(password) > 0 :
            self.login_in_btn.setEnabled(True)
        else:
            self.login_in_btn.setEnabled(False)

    def login_in(self):
        print("login_in")
        account = self.account_cb.currentText()
        password = self.login_pwd.text()
        self.check_login_signal.emit(account, password)

    def auto_login(self, checked):
        print("auto_login")
        if checked:
            self.rember_pwd_cb.setChecked(True)

    def rember_pwd(self, checked):
        print("rember_pwd")
        if not checked:
            self.auto_login_cb.setChecked(False)

    def show_error_animation(self):
        print("show_error_animation")
        animation = QPropertyAnimation(self)
        animation.setTargetObject(self.widget_3)
        animation.setPropertyName(b"pos")
        animation.setKeyValueAt(0, self.widget_3.pos() + QPoint(15, 0))
        animation.setKeyValueAt(0.5, self.widget_3.pos())
        animation.setKeyValueAt(0.7, self.widget_3.pos() + QPoint(-15, 0))
        animation.setKeyValueAt(1, self.widget_3.pos() )
        animation.setDuration(20)
        animation.setLoopCount(3)
        animation.start(QAbstractAnimation.DeleteWhenStopped)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginPane()
    window.show()
    sys.exit(app.exec_())