##Simple package to update pip packages.

####You can update all packages:

`pip_updater -a`

####Or update packages installed locally for your user:

`pip_updater -l`


###To install `pip_updater` just clone the repo, then run:

```
# to install system-wide:
python setup.py install --user

# to install for just your user (eg. if you don't have write privileges on a shared filesystem):
python setup.py install --user
```

If the later route is taken, then just installs the package locally for your user, rather than installing system-wide; so in order to be able to use it, you need to tell your path where to look for it, like so:
( the following info can likely be narrowed down by executing:
 `python -c "import site; print site.getuserbase()"` )

#### For *nix's:
Add this to your `.bashrc`/`.zshrc`:

`export PATH=$HOME/.local/bin:$PATH`

#### For Mac:
Either add the same thing as used by *nix's above, or if that doesn't work, then add something like this in your `.bashrc`/`.zshrc`:

`export PATH=$HOME/Library/Python/[2.X or 3.X]/bin:$PATH`
    
#### For Windows:
Not sure, though you'd have to add the analogous thing to whatever is the equivalent of a shell config file (eg. would have to add to your path the area where executable stuff gets installed at the "user" level with python)
    
suggested as per [PEP370](http://www.python.org/dev/peps/pep-0370/) -- particularly see the "user script directory"  section:

`%APPDATA%/Python/Scripts`


...enjoy.

