print "Enter File Path for Words Text File:"
filepath = raw_input()
words = open(filepath, "r")
for line in words:
    outputstring = "http://www.superai.online/solr/search.php?query="  + line.rstrip()

    f = open('seeds.txt', 'a')
    f.write(outputstring)  # python will convert \n to os.linesep
    f.write('\n')
    f.close()
