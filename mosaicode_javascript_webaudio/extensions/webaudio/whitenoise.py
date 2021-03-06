#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the WhiteNoise class.
"""
from mosaicode.GUI.fieldtypes import *
from mosaicode.model.plugin import Plugin

class WhiteNoise(Plugin):

    # --------------------------------------------------------------------------
    def __init__(self):
        Plugin.__init__(self)

        self.language = "javascript"
        self.framework = "webaudio"
        self.help = "White Noise"
        self.label = "White Noise"
        self.color = "50:150:250:150"
        self.out_ports = [{"type":"mosaicode_javascript_webaudio.extensions.ports.sound",
                "label":"Sound",
                "name":"sound"}
            ]
        self.group = "Sound"

        self.codes[0] = """
WhiteNoise = function(context) {
  var that = this;
  this.x = 0; // Initial sample number
  this.context = context;
  this.node = context.createScriptProcessor(1024, 0, 2);
  this.node.onaudioprocess = function(e) { that.process(e) };
}

WhiteNoise.prototype.process = function(e) {
  var data_l = e.outputBuffer.getChannelData(0);
  var data_r = e.outputBuffer.getChannelData(1);
  for (var i = 0; i < data_l.length; ++i) {
//    data[i] = Math.sin(this.x++);
      data_l[i] = (Math.random() * 2) - 1;
      data_r[i] = (Math.random() * 2) - 1;
  }
}
"""
        self.codes[1] = """
// block_$id$ = $label$
var block_$id$ =  new WhiteNoise(context);
var $out_ports[sound]$ = null;
"""

        self.codes[2] = "$out_ports[output]$ = block_$id$.node;\n"
