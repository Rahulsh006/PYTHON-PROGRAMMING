try:
    f1=open("t.txt","r")	#creating file by open() using w+ mode
    a = [x.rstrip() for x in f1]
    print(a)
    f1.close()
except FileNotFoundError:    		#handling exceptions
    print("FileNotFound exception occured ")
except EOFError:
    print(EOFError)
except IOError:
    print("file not found IOError")
else:
    print("\n file operation done successully")
