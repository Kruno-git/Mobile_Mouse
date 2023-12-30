Exploit is originaly written by Chokri Hammedi in 2022. 
Since I had problems with accessing the uploaded file, I consiered doing some changes which would ensure file execution

I broke the exploit in two seperate files, and as soon as upload script is over, you can run the execute script to gain the shell.
Shell can be msfvenom generated reverse shell of your choice in exe format.
I also added additional \ on the upload path, and chose to put it in C:\users\public folder just to make sure it will work.
For info about args just run scripts with
python3 execute.py or upload.py and it will print out usage

This is just an adaptation of the original exploit written by mentioned author to help offsec students in labs which require such an exploit, 
or anyone else to shorten their googling or modifying the code.

Take the rose people
