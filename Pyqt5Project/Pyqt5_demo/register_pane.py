# from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.Qt import *

import sys
from Pyqt5_demo.resource.register import Ui_Form


# from Pyqt5_demo.resource import images_rc

class RegisterPane(QFrame, Ui_Form):
    # 自定义信号
    exit_signal = pyqtSignal()
    register_account_pwd_signal = pyqtSignal(str, str)

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.setupUi(self)
        self.target = [self.about_menu_btn, self.reset_menu_btn, self.exit_menu_btn]
        self.target_pos = [i.pos() for i in self.target]

    def show_hide_menu(self, checked):
        print("show_hide_menu", checked)
        # 1.  序列动画组

        animation_group = QSequentialAnimationGroup(self)
        for idx, target in enumerate(self.target):
            animation = QPropertyAnimation()
            animation.setTargetObject(target)
            animation.setPropertyName(b"pos")
            if not checked:
                animation.setStartValue(self.target_pos[idx])
                animation.setEndValue(self.main_menue_btn.pos())
            else:
                animation.setStartValue(self.main_menue_btn.pos())
                animation.setEndValue(self.target_pos[idx])

            animation.setDuration(200)
            animation_group.addAnimation(animation)

        animation_group.start(QAbstractAnimation.DeleteWhenStopped)

    def show_lk(self):
        print("show_lk")
        QMessageBox.about(self, "信息框", "https://www.baidu.com")
        pass

    def reset(self):
        print("reset")
        self.account_le.clear()
        self.password_le.clear()
        self.confirm.clear()

    def exit_pane(self):
        print("exit_pane")
        # 将信号发射出去
        self.exit_signal.emit()

    def check_register(self):
        print("check_register")
        account = self.account_le.text()
        password = self.password_le.text()
        self.register_account_pwd_signal.emit(account, password)
        pass

    def enable_register_btn(self):
        print("enable_register_btn")
        account = self.account_le.text()
        password = self.password_le.text()
        confirm_pwd = self.confirm.text()
        if len(account) > 0 and len(password) > 0 and len(confirm_pwd) and password == confirm_pwd:
            self.register_btn.setEnabled(True)
        else:
            self.register_btn.setEnabled(False)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_window = RegisterPane()
    # 监听信号，执行槽函数
    my_window.exit_signal.connect(lambda: print("退出"))
    # my_window.register_account_pwd_signal.connect(lambda account, password: print(account, password))

    my_window.show()
    sys.exit(app.exec_())
