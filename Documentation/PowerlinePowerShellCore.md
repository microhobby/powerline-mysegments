
In this article I will show you how to quickly install and configure Powerline to make your new Windows Terminal with PowerShell Core really cool 😎

⚠ **WARNING: these steps have been tested for Windows 10 Insiders fast ring with PowerShell Core 7.1**

# Install Powerline

In this article I will use the project of [Joel Bennett](https://github.com/Jaykul) who did a great job developing [Jaykul/PowerLine](https://github.com/Jaykul/PowerLine) which, in my view, is the best, simplest to be customized and extended for PowerShell.

1. Install dependencies:

	```powershell
	Install-Module PANSIES -AllowClobber
	```

1. Install `powerline`:

	```powershell
	Install-Module PowerLine
	```

### Set Powerline Fonts

For the dividers between segments, the `powerline` uses some unicode glyphs that must be present in the font used by the terminal.

⚠ **WARNING: do not forget to select fonts that are compatible with these unicode glyphs on the `settings.json`**

A very cool font that I have been using, that have powerline glyphs support, is the [`Cascadia Code`](https://github.com/microsoft/cascadia-code/releases) from Microsoft, which is available on their [Github](https://github.com/microsoft/cascadia-code) for free and with open source license.

Search for the section thats define the settings for the `commandline` `pwsh.exe` and set the `fontFace` property to `Cascadia Mono PL` on Windows Terminal `settings.json`:

```json
"profiles" : 
    [
        {
...
            "commandline" : "C:\\Program Files\\PowerShell\\7\\pwsh.exe",
...
            "fontFace" : "Cascadia Mono PL",
...
```


⚠ **WARNING: do not copy and paste the above snippet into your `settings.json`! The lines with three dots mean that there is more `json` lines between it that I omitted. I am just giving you an example of what you should look for and modify in the file!**

#  Create Profile

For start the `powerline` for each PowerShell Core session we need to create a profile `Microsoft.PowerShell_profile.ps1` file on the folder `%USERPROFILE%\Documents\PowerShell\` with the follow content:

```powershell
Import-Module PowerLine
Set-PowerLinePrompt -PowerLineFont -SetCurrentDirectory -RestoreVirtualTerminal -Colors "#FFDD00", "#FF6600"

[System.Collections.Generic.List[ScriptBlock]]$Prompt = @(
    { "$env:USERNAME 👽" }
    { $executionContext.SessionState.Path.CurrentLocation }
    { '>' * ($nestedPromptLevel + 1) }
)
```

Now close the current tab from Windows Terminal or open a new PowerShell Core tab to see your new terminal with colors!

![](https://github.com/microhobby/powerline-mysegments/blob/master/Documentation/img/pwspowerline.PNG?raw=true)

## Extend and Customize

Each block from `$Prompt` will be a segment that you can code in PowerShell to extend the `powerline` functionality. Take a look at my other article where I made a script with some custom segments: [Linux/Windows Terminal - Script to Display Random Emojis 🥴/🤬 from Commands that Return Errors](https://microhobby.com.br/blog/2020/05/23/linux-windows-terminal-script-to-display-random-emojis-%f0%9f%a5%b4-%f0%9f%a4%ac-from-commands-that-return-errors/)
