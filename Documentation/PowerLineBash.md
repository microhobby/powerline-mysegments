
In this article I will show you how to quickly install and configure Powerline to make your Linux terminal really cool 😎

⚠ **WARNING: these steps have been tested for Debian and Ubuntu distros (they also work if used in WSL with the new Windows Terminal)** ⚠

# Install Powerline

1. Install `pip3`:

    ```bash
    sudo apt-get install python3-pip
    ```

1. Install `powerline` using `pip3`:

    ```bash
    sudo pip3 install powerline-status
    ```

1. Install `powerline` fonts:

    ```bash
    sudo apt-get install fonts-powerline
    ```

## Start Powerline

For start the `powerline` for each `bash` session, we have to include the following content in the end of the `.bashrc` file in your user's `$HOME` folder:

```bash
# load powerline
if [ -f `which powerline-daemon` ]; then
    powerline-daemon -q
    POWERLINE_BASH_CONTINUATION=1
    POWERLINE_BASH_SELECT=1
fi
if [ -f /usr/local/lib/python3.8/dist-packages/powerline/bindings/bash/powerline.sh ]; then
    source /usr/local/lib/python3.8/dist-packages/powerline/bindings/bash/powerline.sh
fi
```
Now close the current `bash` session or open a new session to see your new terminal with colors!

![](https://github.com/microhobby/powerline-mysegments/blob/master/Documentation/img/ubuntupowerline.PNG?raw=true)

### Install Segments

Now you are ready to install custom segments that can return information and make your terminal even more useful. Take a look at my other article where I made a script with some custom segments: [Linux/Windows Terminal - Script to Put Random Emojis 🥴/🤬 for Command Errors]()

