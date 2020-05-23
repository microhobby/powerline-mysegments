
I created scripts to return random sad and angry emojis for each command with an error result in the terminal, for both Windows PowerShell Core and Bash powerline:

![](https://github.com/microhobby/powerline-mysegments/blob/master/Documentation/img/randomEmojisMain.gif?raw=true)

```powershell
$ERROR_EMOJI = "😖", "😵", "🥴", "😭", "😱", "😡", "🤬", "🙃", `
    "🤔", "🙄", "🥺", "😫", "💀", "💩", "😰"
```

In this article I will show how you can use them.

⚠ **DISCLAIMER: these scripts are meant to be useful to me. I can help with any questions, but I do not intend to maintain it or fix issues. Feel free to use and modify as you wish.**

# Random Emojis When CMD Result Errors

## Windows PowerShell Core

First follow the steps from the [How To Install Powerline For Windows Terminal](https://microhobby.com.br/blog/2020/05/23/how-to-install-powerline-for-windows-terminal/) article. After this just edit your PowerShell profile  `%USERPROFILE%\Documents\PowerShell\Microsoft.PowerShell_profile.ps1` adding the content of the follow file: [powerline-mysegments/PowerShell/Microsoft.PowerShell_profile.ps1](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1)

Now close the current tab from Windows Terminal or open a new PowerShell Core tab to see your new terminal. Try to input some incorrect commands to test the random emojis:

![](https://github.com/microhobby/powerline-mysegments/blob/master/Documentation/img/pwsEmojisErrorsExplained.png?raw=true)

Here I used an 👽 emoji to decorate my username. You can change this emoji by modifying the line `99` from [powerline-mysegments/PowerShell/Microsoft.PowerShell_profile.ps1](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1#L99):

```powershell
    # my user name
    { " $env:USERNAME 🦄" }
```

### Extra Segments

In that same file I added some more custom segments that I found useful for my environment:

![enter image description here](https://github.com/microhobby/powerline-mysegments/blob/master/Documentation/img/pwsExtraSegmentsExplained.png?raw=true)

Each block script from:

```powershell
[System.Collections.Generic.List[ScriptBlock]]$Prompt
```

will be a segment. Beginin on line `20` from [powerline-mysegments/PowerShell/Microsoft.PowerShell_profile.ps1](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1#L20). So if you do not want to use any of these extra custom segments just remove the corresponding script block.

⚠ **WARNING: if you are going to remove any script block but keep the script block from the random emojis segment you will have to fix the color index. Lines [`70`](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1#L70), [`77`](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1#L77),  [`78`](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1#L78),  [`84`](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1#L84),  [`90`](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1#L90),  [`91`](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1#L91). You will also have to adjust the colors set for each segment passed during the `Set-PowerLinePrompt` line [`110`](https://github.com/microhobby/powerline-mysegments/blob/master/PowerShell/Microsoft.PowerShell_profile.ps1#L110)**

## Linux Bash

First follow the steps from the [How To Install Powerline For Bash](https://microhobby.com.br/blog/2020/05/23/how-to-install-powerline-for-bash/) article. After this follow the steps:

```bash
cd ~
git clone https://github.com/microhobby/powerline-mysegments
cd powerline-mysegments/Bash/segments
pip3 install --editable ./
```

To verify that the installation was successful, run the following command:

```bash
pip3 list
```

You will need to have the following entry in the list:

```bash
mysegments 0.0.1 /home/<your-user>/powerline-mysegments/Bash/segments
```

### Install Custom Configurations

For this custom segments I am also using some colors and customized settings. To apply these settings, run the following commands:

```bash
powerline-daemon --replace
cd ~
cd powerline-mysegments/Bash
cp -r .config ~
```

After that the new style with the customized segments should already be displayed.  Try to input some incorrect commands to test the random emojis::

![](https://github.com/microhobby/powerline-mysegments/blob/master/Documentation/img/bashRandomEmojisExplained.png?raw=true)

Here I used a 🦄 emoji to decorate my username. You can change this emoji by modifying the line `68` from [powerline-mysegments/Bash/segments/mysegments/custom.py](https://github.com/microhobby/powerline-mysegments/blob/master/Bash/segments/mysegments/custom.py#L68):

```python
    return [{
    'contents': "{} 👽".format(usr),
    'highlight_groups': ['cool'],
    }]
```

### Extra Custom Segments

In the same `mysegments` package I added some more custom segments that I found useful for my environment:

![](https://github.com/microhobby/powerline-mysegments/blob/master/Documentation/img/bashExtraSegmentsExplained.png?raw=true)

The segments to be used are set in the file [powerline-mysegments/Bash/.config/powerline/themes/shell/default_leftonly.json](https://github.com/microhobby/powerline-mysegments/blob/master/Bash/.config/powerline/themes/shell/default_leftonly.json). For example if you want to remove the Docker segment just edit the file and remove the block:

```json
{
	"function": "mysegments.custom.docker",
	"priority": 10
},
```

Easy peasy 😁 


