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

file_list = ["cabon - carvings", "case - charming", "chase - chozeba", "christ - clusters", "cnidus - compete", "complain - consenting", "consider - cormorant", "cornelius - crafty", "crag - cyrus"]

for file_name in file_list:
    split_file_name = file_name.split() # Split at spaces.
    first_word = split_file_name[0]
    last_word = split_file_name[2]

    word_chunk = first_word + " - " + last_word
    escaped_word_chunk = first_word + "\\ -\\ " + last_word

    concordance_file = word_chunk + ".adoc"
    escaped_concordance_file = escaped_word_chunk + ".adoc"
    list_file = word_chunk + ".txt"
    file_title = first_word.upper() + " - " + last_word.upper()

    # Load the word list file into a list.
    with open(list_file) as word_list_file:
        word_list = word_list_file.readlines()

    # Strip the word list of new line characters.
    for i, line in enumerate(word_list):
        word_list[i] = line.strip()

    os.system("touch " + escaped_concordance_file) # Create the AsciiDoc file.
    os.system("echo '= " + file_title + "' >> " + escaped_concordance_file) # Add the page title.
    os.system("echo ':toc:\n' >> " + escaped_concordance_file)

    # Use the grep command to query the database for the current word in the list.
    for word in word_list:
        # Grep the rcv.db file for the current word and replace the contents of
        #   results-file.txt. The rcv.db file must be in the parent directory.
        os.system("grep -i '\\b" + word + "\\b' ../rcv.db > results-file.txt")

        # Use the sed command to find the word in each line of the file and format
        #   each occurence in AsciiDoc to be bold.
        os.system("sed -r -i -e 's|(\\b" + word + "\\b)|*_\\1_*|gi' results-file.txt")

        # Load the results file into a list.
        with open("results-file.txt") as results_list_file:
            results_list = results_list_file.readlines()

        # Strip the results list of new line characters.
        for i, line in enumerate(results_list):
            results_list[i] = line.strip()

        verses = [] # Start with an empty list for each word.

        # Split each item in the list at the pipe symbol and format each line to be
        #   an AsciiDoc unordered list. Also, format the verse designation as code,
        #   using back ticks, for readability.
        for i, result in enumerate(results_list):
            verse = result.split("|") # Verse ID and verse text split.
            verse_id = verse[0].split(":") # Break up the verse ID into its three parts.
            verses.append("* `" + verse_id[0].title() + " " + verse_id[1] + ":" + verse_id[2] + "` " + verse[1])

        # Insert the results for the current word in the AsciiDoc file.
        with open(concordance_file, "a") as concordance_text_file:
            # Add the heading for the current word.
            concordance_text_file.write("== " + word + "\n\n")

            # Write each verse from the verses list.
            for verse in verses:
                concordance_text_file.write(verse + "\n")

            # Display the number of results.
            if len(verses) == 1:
                concordance_text_file.write("\n_" + str(len(verses)) + " verse containing " + word + "_\n\n")
            else:
                concordance_text_file.write("\n_" + str(len(verses)) + " verses containing " + word + "_\n\n")

    # When all words have been added to the concordance file, delete the results
    #   file.
    os.system("rm results-file.txt")
