# SDDL_Converter
A quick Python script to convert SDDL strings into English. 

The script focuses on the DACL portion only, as its the primary part that holds
the permission information to the service. If any SACL strings are present they are simply ignored. 

Also, there is no support for conditional SDDL strings, they will simply break the code. 

## Installtion

Run: 

```bash
wget https://github.com/DanielIsaev/SDDL_Converter/blob/main/sddl_convert.py
```

Or simply download the script manually. 


## Usage 

Paste the output of the `sc sdshow` command from CMD surrounded in quotes as an argument to the script. 

```bash
./sddl_convert.py "<sddl_string>"
```

For example:


![usage](https://github.com/DanielIsaev/SDDL_Converter/blob/main/img/usage-01.png)


## Contributing                           

Pull requests are welcome. For major changes, please open an issue first                                                                                                  
to discuss what you would like to change.                                            

Please make sure to update tests as appropriate.                                     


## Lets link up!                          

You can always reach me on my [Linkedin](https://www.linkedin.com/in/daniel-isaev-757593228/)  
