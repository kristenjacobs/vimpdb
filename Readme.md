# vimpdb 

Simple integration of pdb and the VIM editor.

This will open an instance of vim/gvim, with 2 windows. The python debugger
will be running in a console in the bottom window whereas the top window is
used to display the current file/line of the source file being debugged.  This
window gets updated whenever the debugger stops.

Note: In terms of implementation, this relies on the user having the vim Conque
plugin installed, as this provides the ability to run a console application
(pdb in this case), from within vim.

## To Install

Clone then cd to this repo.


Copy *vimpdb.py* to a location on your python path. e.g:

```
cp vimpdb.py `python -m site --user-site`
```

Copy the *.pdbrc* file to your home area:

```
cp .pdbrc ~/
```

Add the following to your bashrc, such that the vimpdb and gvimpdb 
wrapper scripts can be found on your path:

```
export PATH=`pwd`:$PATH
```

## To Run

Using vim:

```
vimpdb test.py
```

Using gvim:

```
gvimpdb test.py
```
