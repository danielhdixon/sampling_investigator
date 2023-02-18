# pyside6-uic sampling_app_v14_MAC.ui -o sampling_gui_v14_MAC.py

from PySide6 import QtGui, QtWidgets, QtCore

from sampling_gui_v14_MAC import Ui_Sampling_Investigator
# from sampling_gui_v7 import Ui_Sampling_Investigator
from math import sqrt, ceil

import inspect
# pyinstaller --noconsole --windowed --onefile sampling_investigator\\sampling_app.py
# pyinstaller --noconsole --windowed --onefile sampling_app.py

authors = 'DHDixon & TODixon'
email = 'dhdixon49@gsu.edu'

class MainWindow(QtWidgets.QMainWindow, Ui_Sampling_Investigator):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.tabWidget.setCurrentIndex(0)

        self.rse = 'x'
        self.t_crit_value = 1.96
        self.t_crit_value_tab_1 = 1.96
        self.mean_times = .05

        self.ci_percent = "95%"

        self.RSEcrit10 = 0.0510
        self.RSEcrit05 = 0.0255
        self.RSEcrit01 = 0.0051
        self.RSEcrit005 = 0.0026
        self.RSEcrit001 = 0.0005

        self.frame_not_adequate.hide()
        self.frame_adequate.hide()

        # push buttons connect to def for TAB 2
        self.pushButton_standard_error.clicked.connect(self.calc_standard_error)
        self.pushButton_relative_standard_error.clicked.connect(self.calc_rse)
        self.pushButton_results.clicked.connect(self.calc_results)

        self.RSE_crit_value = .0255
        self.label_rse_crit_not_adequate.setText(str(self.RSE_crit_value))
        self.label_rse_crit_adequate.setText(str(self.RSE_crit_value))

        self.radioButton_10.toggled.connect(self.set_tolerable_error)
        self.radioButton_05.toggled.connect(self.set_tolerable_error)
        self.radioButton_01.toggled.connect(self.set_tolerable_error)
        self.radioButton_005.toggled.connect(self.set_tolerable_error)
        self.radioButton_001.toggled.connect(self.set_tolerable_error)

        # Choose the critical value of t
        self.radioButton_tcrit_10.toggled.connect(self.t_crit)
        self.radioButton_tcrit_05.toggled.connect(self.t_crit)
        self.radioButton_tcrit_025.toggled.connect(self.t_crit)
        self.radioButton_tcrit_01.toggled.connect(self.t_crit)
        self.radioButton_tcrit_005.toggled.connect(self.t_crit)

        # TAB 1
        # calculate n size
        self.pushButton.clicked.connect(self.check_numbers)

        # radio buttons tab 1 critical value of t
        self.radioButton_tcrit_80.toggled.connect(self.t_crit_tab_1)
        self.radioButton_tcrit_90.toggled.connect(self.t_crit_tab_1)
        self.radioButton_tcrit_95.toggled.connect(self.t_crit_tab_1)
        self.radioButton_tcrit_98.toggled.connect(self.t_crit_tab_1)
        self.radioButton_tcrit_99.toggled.connect(self.t_crit_tab_1)

        # radio buttons tab 1 tolerable error et
        self.radioButton_n_10.toggled.connect(self.et_radios)
        self.radioButton_n_05.toggled.connect(self.et_radios)
        self.radioButton_n_01.toggled.connect(self.et_radios)
        self.radioButton_n_005.toggled.connect(self.et_radios)
        self.radioButton_n_001.toggled.connect(self.et_radios)

        # lineEdit change text
        self.lineEdit_pilot_mean.textChanged.connect(self.tab_1_change_values)
        self.lineEdit_pilot_standard_deviation.textChanged.connect(self.tab_1_change_values)

        for name, obj in inspect.getmembers(self):
            if isinstance(obj, QtWidgets.QRadioButton):
                obj.setStyleSheet('color: white;')

    # TAB 1
    def tab_1_change_values(self):
        mean_text = self.lineEdit_pilot_mean.text()
        sd_text = self.lineEdit_pilot_standard_deviation.text()
        if mean_text == "":
            mean_text = '<mean>'
        if sd_text == "":
            sd_text = '<standard deviation>'
        self.label_mean.setText(str(mean_text))
        self.label_std_dev.setText(str(sd_text))


    def et_radios(self):
        # self.reset_values_tab_1()
        self.lineEdit_pilot_mean.setText('')
        self.lineEdit_pilot_standard_deviation.setText('')
        if self.radioButton_n_10.isChecked():
            self.mean_times = .10
        elif self.radioButton_n_05.isChecked():
            self.mean_times = .05
        elif self.radioButton_n_01.isChecked():
            self.mean_times = .01
        elif self.radioButton_n_005.isChecked():
            self.mean_times = .005
        elif self.radioButton_n_001.isChecked():
            self.mean_times = .001
        self.label_10.setText(str(self.mean_times))

    def t_crit_tab_1(self):
        # self.reset_values_tab_1()
        self.lineEdit_pilot_mean.setText('')
        self.lineEdit_pilot_standard_deviation.setText('')
        if self.radioButton_tcrit_80.isChecked():
            self.t_crit_value_tab_1 = 1.28
            # self.mean_times = .20
        elif self.radioButton_tcrit_90.isChecked():
            self.t_crit_value_tab_1 = 1.645
            # self.mean_times = .10
        elif self.radioButton_tcrit_95.isChecked():
            self.t_crit_value_tab_1 = 1.96
            # self.mean_times = .05
        elif self.radioButton_tcrit_98.isChecked():
            self.t_crit_value_tab_1 = 2.33
            # self.mean_times = .02
        elif self.radioButton_tcrit_99.isChecked():
            self.t_crit_value_tab_1 = 2.58
            # self.mean_times = .01
        self.label_t.setText(str(self.t_crit_value_tab_1))
        # self.label_10.setText(str(self.mean_times))

    # check numbers for errors then go to calc_n
    def check_numbers(self):
        try:
            self.pilot_mean = float(self.lineEdit_pilot_mean.text())
        except:
            self.lineEdit_pilot_mean.setText('ERROR')
        try:
            self.pilot_standard_deviation = float(self.lineEdit_pilot_standard_deviation.text())
            self.calc_n()
        except:
            self.lineEdit_pilot_standard_deviation.setText('ERROR')

    def calc_n(self):
        # calculate first line
        self.et_tab_1 = self.pilot_mean * self.mean_times
        self.et_tab_1 = round(self.et_tab_1, 4)
        self.label_et.setText(str(self.et_tab_1))
        self.label_et_2.setText(str(self.et_tab_1))
        # calculate second line
        self.second_line_result = self.et_tab_1 / self.t_crit_value_tab_1
        self.second_line_result = round(self.second_line_result, 4)
        self.label_result_et_t.setText(str(self.second_line_result))

        # third line
        self.third_line_result = self.second_line_result ** 2
        # if self.third_line_result > 0.0001:
        #     self.third_line_result = round(self.third_line_result, 4)
        self.label_result_et_t_squared.setText(str(self.third_line_result))
        self.label_result_et_t_2.setText('<html><head/><body><p>(' + str(self.second_line_result) +
                                         ')<span style=" vertical-align:super;">2</span> = </p></body></html>')
        # fourth line
        self.fourth_line_result = self.pilot_standard_deviation ** 2
        self.fourth_line_result = round(self.fourth_line_result, 4)
        self.label_result_stdev_squared.setText(str(self.fourth_line_result))
        # fifth line
        self.label_result_stdev_squared_2.setText(str(self.fourth_line_result))
        self.label_result_et_t_squared_2.setText(str(self.third_line_result))
        self.n_size = self.fourth_line_result / self.third_line_result
        self.n_size = round(self.n_size, 4)
        self.label_result_required_n.setText(str(self.n_size))
        self.label_result_required_n_2.setText(str(ceil(self.n_size)) + " (rounded up from " +
                                               str(round(self.n_size, 4)) + ")")

    # TAB 2 ###########
    def margin_error(self):
        if self.rse != 'x':
            self.t_times_SE = self.t_crit_value * self.standard_error
            self.lower = round(self.mean - self.t_times_SE, 2)
            self.upper = round(self.mean + self.t_times_SE, 2)
            self.label_confidence_interval.setText("CI = [" + str(self.lower) + ", " + str(self.upper) + "]")
            self.label_margin_error.setText(str(self.mean) + " +- " + str(round(self.t_times_SE, 4)))

    def set_RSEcrit(self):
        self.RSEcrit10 = round(.10 / self.t_crit_value, 4)
        self.label_RSEcrit_10.setText(str(self.RSEcrit10))

        self.RSEcrit05 = round(.05 / self.t_crit_value, 4)
        self.label_RSEcrit_05.setText(str(self.RSEcrit05))

        self.RSEcrit01 = round(.01 / self.t_crit_value, 4)
        self.label_RSEcrit_01.setText(str(self.RSEcrit01))

        self.RSEcrit005 = round(.005 / self.t_crit_value, 4)
        self.label_RSEcrit_005.setText(str(self.RSEcrit005))

        self.RSEcrit001 = round(.001 / self.t_crit_value, 4)
        self.label_RSEcrit_001.setText(str(self.RSEcrit001))

        self.set_tolerable_error()

    # set values of t in RSEcrit table
    def t_crit(self):
        if self.radioButton_tcrit_10.isChecked():
            self.t_crit_value = 1.28
            self.ci_percent = "80%"
        elif self.radioButton_tcrit_05.isChecked():
            self.t_crit_value = 1.645
            self.ci_percent = "90%"
        elif self.radioButton_tcrit_025.isChecked():
            self.t_crit_value = 1.96
            self.ci_percent = "95%"
        elif self.radioButton_tcrit_01.isChecked():
            self.t_crit_value = 2.33
            self.ci_percent = "98%"
        elif self.radioButton_tcrit_005.isChecked():
            self.t_crit_value = 2.58
            self.ci_percent = "99%"
        self.label_confidence_interval_2.setText(self.ci_percent)
        self.label_margin_error.setText(self.ci_percent + " CI = [-t*SE, +t*SE]")

        self.label_t_10.setText(str(self.t_crit_value))
        self.label_t_05.setText(str(self.t_crit_value))
        self.label_t_01.setText(str(self.t_crit_value))
        self.label_t_005.setText(str(self.t_crit_value))
        self.label_t_001.setText(str(self.t_crit_value))

        self.set_RSEcrit()
        self.margin_error()

    def calc_results(self):
        try:
            self.rse = abs(self.rse)
            if self.rse > self.RSE_crit_value:
                self.frame_not_adequate.show()
                self.frame_adequate.hide()
            elif self.rse < self.RSE_crit_value:
                self.frame_adequate.show()
                self.frame_not_adequate.hide()
            self.margin_error()
        except:
            self.label_results.setText('Complete calculations to the left and choose tolerable error level. Then '
                                       'click "see results"')

    def set_tolerable_error(self):
        if self.radioButton_10.isChecked():
            self.RSE_crit_value = self.RSEcrit10
        elif self.radioButton_05.isChecked():
            self.RSE_crit_value = self.RSEcrit05
        elif self.radioButton_01.isChecked():
            self.RSE_crit_value = self.RSEcrit01
        elif self.radioButton_005.isChecked():
            self.RSE_crit_value = self.RSEcrit005
        elif self.radioButton_001.isChecked():
            self.RSE_crit_value = self.RSEcrit001
        self.label_rse_crit_not_adequate.setText(str(self.RSE_crit_value))
        self.label_rse_crit_adequate.setText(str(self.RSE_crit_value))

        self.frame_not_adequate.hide()
        self.frame_adequate.hide()


    def calc_standard_error(self):
        try:
            standard_dev = self.lineEdit_standard_deviation.text()
            standard_dev = float(standard_dev)
            sample_size = self.lineEdit_sample_size.text()
            sample_size = float(sample_size)
            self.standard_error = standard_dev / sqrt(sample_size)
            self.standard_error = round(self.standard_error, 4)
            self.label_standard_error_result.setText('SE = ' + str(self.standard_error))
            self.lineEdit_standard_error.setText(str(self.standard_error))

            self.frame_not_adequate.hide()
            self.frame_adequate.hide()
            self.margin_error()
        except:
            self.lineEdit_standard_deviation.setText('ERROR')

    def calc_rse(self):
        try:
            self.standard_error = float(self.lineEdit_standard_error.text())
            self.mean = self.lineEdit_mean.text()
            self.mean = float(self.mean)
            self.rse = round(self.standard_error / self.mean, 4)
            self.rse = abs(self.rse)
            self.label_relative_standard_error_result.setText('RSE = ' + str(self.rse))
            self.label_rse_not_adequate.setText(str(self.rse))
            self.label_rse_adequate.setText(str(self.rse))
            self.frame_not_adequate.hide()
            self.frame_adequate.hide()
            self.calc_results()

        except:
            self.lineEdit_mean.setText('ERROR')


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle('Fusion')
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())


