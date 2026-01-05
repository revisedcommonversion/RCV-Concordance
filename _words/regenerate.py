#!/usr/bin/python

####################################################################### License.
#  The Holy Bible: Revised Common Version
#  Copyright (c) 2026 William Masopust
#  http://www.revisedcommonversion.com
#  The source code of the RCV text is available at http://source.rcv.xyz.
#
#  This project and the accompanying materials are made available under the
#  terms of the Eclipse Public License 2.0 which is available at
#  https://www.eclipse.org/legal/epl-2.0/.
#
#  SPDX-License-Identifier: EPL-2.0
################################################################################

# Before running this script, make sure the current rcv.db file is in the same
#   directory as this script.

import os
from contextlib import chdir

# Add each letter that needs to be regenerated as a string to this list.
letter_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "Z"]

for letter in letter_list:
    with chdir(letter):
        print("Generating " + letter + " files.")
        os.system("python3 build.py")
        print("Moving " + letter + " files.")
        os.system("\\mv -v *.adoc ../../" + letter) # Precede the mv command with a '\' to bypass any aliases.

# Eventually, I would like to expand this script to be the only Python script to
#   handle the regeneration of the concordance. So, instead of having a build.py
#   script in each letter subdirectory, I want this script to enter each letter
#   subdirectory and build the concordance. This file is just a working starting
#   point to reach that goal.
