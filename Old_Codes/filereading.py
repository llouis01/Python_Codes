# a program that reads files. Python 2 (@roiminuit)

from sys import argv # this line of code imports the features for the script

script, filetoberead = argv # pos0 is the script name, pos1 is file to be read

contnt = open(filetoberead) # declare variable to open file

print '\nHere\'s your file %r:' % filetoberead
print contnt.read() # print out file ; loc above displays code name

print "Type your file name again:\n"
file_anew = raw_input('-> ') # request filename from user

print "Again, this is your requested file: %r" % file_anew
file_uhgain = open(file_anew)
print file_uhgain.read() # filename.read prints out file content
