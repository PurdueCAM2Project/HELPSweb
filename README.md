# HELPS
HELPS website

TODO: we need to add more instructions on how to do the web development

## Make virtual environment

1. Set up venv folder (OS Universal)
    ```
    > <python> -m venv ./sphinx_env
    ```
2. OS Specific activation

     - Windows (CMD is less picky about permissions, use it over PowerShell in this scenerio)

    ```
     CMD: > sphinx_env\Scripts\activate.bat
     PS:  > ./sphinx_env/Scripts/Activate.ps1
    ```
    
    - POSIX

    ```
    $ source ./sphinx_env/bin/activate
    ```

3. Install necessary packages

    ```
    (sphinx_env) $ <python> -m pip install -r requirements.txt
    ```

## Edit .rst source files

All source files for the project are located in the /source folder. Visit https://www.markdownguide.org/ to learn more about the syntax used in the source files.

## Build the website from source, and look before pushing

While still in the virtual environment:

```
(sphinx_env) $ make html
(sphinx_env) $ python -m http.server --directory ./build/html
```

Then open up a web browser and visit http://localhost:8000

If everything looks good, push to a new branch and submit a pull request.


