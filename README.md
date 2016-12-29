# copy_dir_structure
Uses python to copy directory structure

The directories I have worked with contains Gigabytes/ Terrabytes of data. I need to delete or modify the file structure,
but I can't spend hours testing it using actualy data files. Since I'm just removing/moving data from one place to another,
this python file only copies the file names and directory structures.

This allows for a kind of "mock-testing" to be done. It's pretty useful. Once all files are copied, I can run my data_retention_policy code and see if it works.
If anyone else has a convuluted directory structure that they don't want to break, but still want to make sure the files they move/delete
are right, they can now use this code. :D

Let me know if there are any bugs. Took me bout 30 minutes to write, so there are probably cases I haven't thought of.
