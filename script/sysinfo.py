# -*- coding: utf-8 -*-
"""
Information about the host computer system
"""
import sys
import subprocess

bash_cmd = ["system_profiler",
            "-xml",
            "SPHardwareDataType",
            "SPMemoryDataType",
            "SPSoftwareDataType",]

if sys.platform is "darwin":
    pass

sysinfo_xml = subprocess.check_output(bash_cmd)

# Read through XML and find the information I want.
# Turn the result into a dictionary.
# Print or otherwise output the data.
