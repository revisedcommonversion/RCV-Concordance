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

import os

# Open the source text file.
with open("source.txt") as source_text_file:
    source_text = source_text_file.readlines()

# Strip the source text of new line characters and convert each word to upper
#   case letters.
for i, line in enumerate(source_text):
    source_text[i] = line.strip().upper()

# Create a set to hold each word in the source text without duplicates.
word_set = set()

# Go through each line of the source text, split the line at the space characters
#   creating a list containing each word in the line, and then update word_set
#   with that list item.
for i, line in enumerate(source_text):
    word_set.update(line.split())

# Create a copy of the word set that is sorted alphabetically.
sorted_word_list = sorted(word_set)

# Write each word to the bank text file, with one word per line.
with open("bank.txt", "w") as bank_text_file:
    for word in sorted_word_list:
        bank_text_file.write(word + "\n")
