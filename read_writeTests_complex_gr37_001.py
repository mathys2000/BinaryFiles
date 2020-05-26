#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Read/Write Tests for complex-valued signals
# Author: P. Mathys
# GNU Radio version: 3.7.14.0
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import pmt
import sip
import sys
from gnuradio import qtgui


class read_writeTests_complex_gr37_001(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Read/Write Tests for complex-valued signals")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Read/Write Tests for complex-valued signals")
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

        self.settings = Qt.QSettings("GNU Radio", "read_writeTests_complex_gr37_001")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.Fs3 = Fs3 = 22050
        self.Fs2 = Fs2 = 32000
        self.Fs13 = Fs13 = 44100
        self.Fs12 = Fs12 = 48000

        ##################################################
        # Blocks
        ##################################################
        self.qtgui_sink_x_0_1_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Fs13, #bw
        	"x13t", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_1_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_0_win = sip.wrapinstance(self.qtgui_sink_x_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_1_0_win, 1, 1, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)


        self.qtgui_sink_x_0_1_0.enable_rf_freq(False)



        self.qtgui_sink_x_0_1 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Fs12, #bw
        	"x12t", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_1.set_update_time(1.0/10)
        self._qtgui_sink_x_0_1_win = sip.wrapinstance(self.qtgui_sink_x_0_1.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_1_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)


        self.qtgui_sink_x_0_1.enable_rf_freq(False)



        self.qtgui_sink_x_0_0 = qtgui.sink_c(
        	4096, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Fs3, #bw
        	"y3t", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_0_win = sip.wrapinstance(self.qtgui_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_0_win, 0, 1, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)


        self.qtgui_sink_x_0_0.enable_rf_freq(False)



        self.qtgui_sink_x_0 = qtgui.sink_c(
        	1024, #fftsize
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	Fs2, #bw
        	"y2t", #name
        	True, #plotfreq
        	True, #plotwaterfall
        	True, #plottime
        	True, #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_sink_x_0_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)


        self.qtgui_sink_x_0.enable_rf_freq(False)



        self.blocks_wavfile_source_0 = blocks.wavfile_source('sig_x3t_PAMint16_2ch_Fs22050.wav', True)
        self.blocks_wavfile_sink_0 = blocks.wavfile_sink('sig_x13t_PAMint16_2ch_Fs44100.wav', 2, Fs13, 16)
        self.blocks_throttle_0_1_0 = blocks.throttle(gr.sizeof_gr_complex*1, Fs13,True)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_gr_complex*1, Fs12,True)
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, Fs3,True)
        self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, Fs2,True)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, 'sig_x2t_complex64_Fs32000.bin', True)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_gr_complex*1, 'sig_x12t_complex64_Fs48000.bin', False)
        self.blocks_file_sink_0.set_unbuffered(False)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.analog_sig_source_x_0_0 = analog.sig_source_c(Fs13, analog.GR_TRI_WAVE, 100, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_c(Fs12, analog.GR_COS_WAVE, 1000, 1, 0)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0_1, 0))
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_throttle_0_1_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_wavfile_sink_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_wavfile_sink_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_throttle_0, 0))
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.blocks_throttle_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.qtgui_sink_x_0_0, 0))
        self.connect((self.blocks_throttle_0_1, 0), (self.blocks_file_sink_0, 0))
        self.connect((self.blocks_throttle_0_1, 0), (self.qtgui_sink_x_0_1, 0))
        self.connect((self.blocks_throttle_0_1_0, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_throttle_0_1_0, 0), (self.qtgui_sink_x_0_1_0, 0))
        self.connect((self.blocks_wavfile_source_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_wavfile_source_0, 1), (self.blocks_float_to_complex_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "read_writeTests_complex_gr37_001")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_Fs3(self):
        return self.Fs3

    def set_Fs3(self, Fs3):
        self.Fs3 = Fs3
        self.qtgui_sink_x_0_0.set_frequency_range(0, self.Fs3)
        self.blocks_throttle_0_0.set_sample_rate(self.Fs3)

    def get_Fs2(self):
        return self.Fs2

    def set_Fs2(self, Fs2):
        self.Fs2 = Fs2
        self.qtgui_sink_x_0.set_frequency_range(0, self.Fs2)
        self.blocks_throttle_0.set_sample_rate(self.Fs2)

    def get_Fs13(self):
        return self.Fs13

    def set_Fs13(self, Fs13):
        self.Fs13 = Fs13
        self.qtgui_sink_x_0_1_0.set_frequency_range(0, self.Fs13)
        self.blocks_throttle_0_1_0.set_sample_rate(self.Fs13)
        self.analog_sig_source_x_0_0.set_sampling_freq(self.Fs13)

    def get_Fs12(self):
        return self.Fs12

    def set_Fs12(self, Fs12):
        self.Fs12 = Fs12
        self.qtgui_sink_x_0_1.set_frequency_range(0, self.Fs12)
        self.blocks_throttle_0_1.set_sample_rate(self.Fs12)
        self.analog_sig_source_x_0.set_sampling_freq(self.Fs12)


def main(top_block_cls=read_writeTests_complex_gr37_001, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
