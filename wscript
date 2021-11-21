## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('dash', ['internet','config-store','stats', 'quic'])
    module.includes = '.'
    module.source = [
        'model/stream-client.cc',
        'model/stream-server.cc',
        'model/tcp-stream-adaptation-algorithm.cc',
        'model/festive.cc',
        'model/panda.cc',
        'model/tobasco2.cc',
        'helper/stream-helper.cc',
        'model/stream-utils.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'dash'
    headers.source = [
        'model/stream-client.h',
        'model/stream-server.h',
        'model/tcp-stream-interface.h',
        'model/tcp-stream-adaptation-algorithm.h',
        'model/festive.h',
        'model/panda.h',
        'model/tobasco2.h',
        'helper/stream-helper.h',
        'model/stream-utils.h',
        ]

    if bld.env['ENABLE_EXAMPLES']:
        bld.recurse('examples')

    bld.ns3_python_bindings()
