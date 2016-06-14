# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

`touch`: create an empty file with the provided filename, useful for laying out project structure
`less`: print contents of text file to terminal, save the time of firing up an editor
`grep`: find a text pattern inside a file
`cat`: concatenates text strings, streams and files. Could be useful for stitching CSV files together!
`find`: find a file with the given name
`man`: what people used before Google
`pushd/popd`: save directories in a list for easy moving around - like `cd ..` syntax for arbitary, non-adjacent dirs
`env`: shows envvars. good for troubleshooting dev setup issues.
`| < > >>`: pipes/redirection, used to send command outputs to other commands and chain them together. Need to practice!
`export / unset`: I have to Google this every time some config issue pops up, might as well remember.

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`: show directory contents
`ls -a`: include hidden directories beginning with a `.`
`ls -l`:  show long listings
`ls -lh`: long listings, with unit suffixes on file sizes
`ls -lah`: long listings with file size abbreviations, including hidden dirs
`ls -t`: sort files by time modified (most recently modified first)
`ls -Glp`: colorized output, in long format, notate directories with opening `/`


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

`ls -d`: show only directories
`ls -m`: show as comma-separated list
`ls -L`: resolve symbolic links
`ls -1`: one entry per line
`ls -u`: sort by access time

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > It allows you to generate a list of command arguments through another command, then "redirect" it to the subsequent command.
Example: `grep -h old list_of_files_to_delete.txt | xargs rm` -> finds all filenames containing string `old` inside the .txt file and deletes them

 

