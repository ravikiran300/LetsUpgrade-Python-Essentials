try:
    
    file = open("test.txt","r")
    
    file.write("\nI am from chennai.")
    
    print("\nWrite operation has done successfully in read only mode.")
    
except Exception as e:
    
    print("\nError has been occured")
    
    print("\nError message is :",e)
