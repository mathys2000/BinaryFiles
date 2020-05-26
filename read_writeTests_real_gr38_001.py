#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Read/Write Tests for real-valued signals
# Author: P. Mathys
# GNU Radio version: 3.8.1.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
import pmt
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation

from gnuradio import qtgui

class read_writeTests_real_gr38_001(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Read/Write Tests for real-valued signals")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Read/Write Tests for real-valued signals")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "read_writeTests_real_gr38_001")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.Fs3 = Fs3 = 22050
        self.Fs23 = Fs23 = 44100
        self.Fs22 = Fs22 = 48000
        self.Fs2 = Fs2 = 32000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_0_1_0_0 = qtgui.sink_f(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            Fs23, #bw
            "y23t", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0_1_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1_0_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_1_0_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0_1 = qtgui.sink_f(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            Fs22, #bw
            "y22t", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_1.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_1_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0_0 = qtgui.sink_f(
            4096, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            Fs3, #bw
            "y3t", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_sink_x_0 = qtgui.sink_f(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            Fs2, #bw
            "y2t", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.blocks_wavfile_source_0 = blocks.wavfile_source('sig_x3t_PAMint16_Fs22050.wav', True)
        self.blocks_throttle_0_0_0_0_0 = blocks.throttle(gr.sizeof_float*1, Fs23,True)
        self.blocks_throttle_0_0_0 = blocks.throttle(gr.sizeof_float*1, Fs22,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_float*1, Fs3,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, Fs2,True)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, 'sig_x2t_float32_Fs32000.bin', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.analog_sig_source_x_0_0_0 = analog.sig_source_f(Fs23, analog.GR_SAW_WAVE, 100, 1, 0, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(Fs22, analog.GR_SIN_WAVE, 1000, 1, 0, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0_0_0, 0))
        self.connect((self.analog_sig_source_x_0_0_0, 0), (self.blocks_throttle_0_0_0_0_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0_0_0, 0), (self.qtgui_sink_x_0_1, 0))
        self.connect((self.blocks_throttle_0_0_0_0_0, 0), (self.qtgui_sink_x_0_1_0_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_throttle_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "read_writeTests_real_gr38_001")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Fs3(self):
        return self.Fs3

    def set_Fs3(self, Fs3):
        self.Fs3 = Fs3
        self.blocks_throttle_0_0.set_sample_rate(self.Fs3)
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.Fs3)

    def get_Fs23(self):
        return self.Fs23

    def set_Fs23(self, Fs23):
        self.Fs23 = Fs23
        self.analog_sig_source_x_0_0_0.set_sampling_freq(self.Fs23)
        self.blocks_throttle_0_0_0_0_0.set_sample_rate(self.Fs23)
        self.qtgui_sink_x_0_1_0_0.set_frequency_range(0, self.Fs23)

    def get_Fs22(self):
        return self.Fs22

    def set_Fs22(self, Fs22):
        self.Fs22 = Fs22
        self.analog_sig_source_x_0.set_sampling_freq(self.Fs22)
        self.blocks_throttle_0_0_0.set_sample_rate(self.Fs22)
        self.qtgui_sink_x_0_1.set_frequency_range(0, self.Fs22)

    def get_Fs2(self):
        return self.Fs2

    def set_Fs2(self, Fs2):
        self.Fs2 = Fs2
        self.blocks_throttle_0.set_sample_rate(self.Fs2)
        self.qtgui_sink_x_0.set_frequency_range(0, self.Fs2)





def main(top_block_cls=read_writeTests_real_gr38_001, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
