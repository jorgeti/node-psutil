{
  'variables': {
    'library%': 'static_library',
  },
  'targets': [
    {
      'target_name': 'psutil_lib_osx',
      'sources': [
        'lib/psutil_lib_osx.cc',
        'lib/workers/worker.cc',
        'lib/workers/virtual_memory_worker.cc',
        'lib/workers/cpu_worker.cc',
        'lib/workers/sysconf_worker.cc',
        'lib/workers/disk_io_counters_worker.cc'
      ],
      'cflags!': [ '-fno-exceptions' ],
      'cflags_cc!': [ '-fno-exceptions' ],
      'conditions': [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ]
    }
  ]
}