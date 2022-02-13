from Pyqt5_demo.login_pane import LoginPane
from Pyqt5_demo.register_pane import RegisterPane
from Pyqt5_demo.Calculator_Pane import CaculatorPane

from PyQt5.Qt import *
import sys

# 问题 1  如何让Pyqt5 报出的错误，能够清楚

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = LoginPane()
    Login.show()

    Register = RegisterPane(Login)
    Register.move(0, Register.height())
    Register.show()

    calculator = CaculatorPane()


    def exit_register_pane():
        print("退出注册页面")
        animation = QPropertyAnimation(Register)
        animation.setTargetObject(Register)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, 0))
        animation.setEndValue(QPoint(Login.width(), 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.InBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def show_register_pane():
        print("展示登录页面")
        animation = QPropertyAnimation(Register)
        animation.setTargetObject(Register)
        animation.setPropertyName(b"pos")
        animation.setStartValue(QPoint(0, Login.height()))
        animation.setEndValue(QPoint(0, 0))
        animation.setDuration(1000)
        animation.setEasingCurve(QEasingCurve.OutBounce)
        animation.start(QAbstractAnimation.DeleteWhenStopped)

    def Check_login(account, password):
        if account == "2942098372" and password == "123":
            print("登录成功的处理")

            calculator.show()
            Login.hide()

        else:
            print("登录失败抖动")
            Login.show_error_animation()

    # 监听信号   show_register_signal     exit_signal
    Login.show_register_signal.connect(show_register_pane)

    Login.check_login_signal.connect(Check_login)
    Register.exit_signal.connect(exit_register_pane)
    Register.register_account_pwd_signal.connect(lambda account, password : print(account, password))

    sys.exit(app.exec_())
