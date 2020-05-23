# Copyright (c) 2020 Matheus Castello
# MicroHobby licenses this file to you under the MIT license.
# See the LICENSE file in the project root for more information.

# command completion
$scriptblock = {
    param($wordToComplete, $commandAst, $cursorPosition)
        dotnet complete --position $cursorPosition $commandAst.ToString() `
                | ForEach-Object {
            [System.Management.Automation.CompletionResult]::new($_, $_,
                                                                 'ParameterValue',
                                                                  $_)
        }
}
Register-ArgumentCompleter -Native -CommandName dotnet -ScriptBlock $scriptblock

# I will use code-insiders as code
Set-Alias -Name code -Value code-insiders

# lets set the powerline in this profile
Import-Module PowerLine

# aux variables
$ERRORS_COUNT = 0
$ERROR_EMOJI = "😖", "😵", "🥴", "😭", "😱", "😡", "🤬", "🙃", "🤔", "🙄", `
    "🥺", "😫", "💀", "💩", "😰"

$global:EC = 0
$global:EXIT_CODE = 0

# clear the last win32 exit code
$global:LASTEXITCODE = 0

# set my powerline blocks
[System.Collections.Generic.List[ScriptBlock]]$Prompt = @(
    #{ "`t" } # On the first line, right-justify
    # docker ps
    {
        # firts block have to check the errors
        # check the cmdlets and win32 errors
        $global:EC = $error.count
        $global:EXIT_CODE = $global:LASTEXITCODE

        # count docker images and how many containers are running now
        $dpsc = docker images -q | Measure-Object | `
                    Select-Object count -ExpandProperty Count
        $runs = docker ps -q | Measure-Object | `
                    Select-Object count -ExpandProperty Count

        if ( $runs ) {
            "🐳 :: 📦 $dpsc :: ▶ $runs"
        } else {
            "🐳 :: 📦 $dpsc"
        }
    }
    # git modified
    {
        $diff = git status -s -uno | Measure-Object | `
                    Select-Object count -ExpandProperty Count

        if ( $diff ) {
            " 📑 :: $diff "
        } else {
            "."
        }
    }
    # my current path
    {
        -join(" &#x1F449; ", ($executionContext.SessionState.Path.CurrentLocation), " ")
    }
    { "`n" } # Start another line
    # git branch and cmd error check
    {
        $EC = $global:EC
        $ERRORS_COUNT = $global:EXIT_CODE

        # execute git to check current branch
        $gitRet = git rev-parse --abbrev-ref HEAD
        
        if ( $EC -gt $ERRORS_COUNT -or $EXIT_CODE -ne 0) {
            $ERRORS_COUNT = $EC
            
            if ( $gitRet ) {
                " &#xE0A0; $gitRet "
                $Global:Prompt.Colors[3] = "Gray"
            # not git repo and the last cmd return a error
            } else {
                # get a ramdom emoji
                $ERROR_EMOJI[(Get-Random -Maximum $ERROR_EMOJI.count)]
            }

            $Global:Prompt.Colors[3] = "Red"
            $Global:Prompt.Colors[5] = "Red"
        
        # not git repo and all clear
        } else {
            if ( $gitRet ) {
                " &#xE0A0; $gitRet "
                $Global:Prompt.Colors[3] = "Gray"
            # not git repo and the last cmd return a error
            } else {
                "😎"
            }

            $Global:Prompt.Colors[3] = "Green"
            $Global:Prompt.Colors[5] = "Gray"
        }
        
        # clear the errors and last exit code for the next interaction
        $error.clear()
        $global:LASTEXITCODE = 0
    }
    # my user name
    # WARNING: use $env:USERNAME, I am using 'castello' because I was
    # stupid and set the name of my user was mpro3 and not my last name
    { " castello 👽" }
    # pipe
    { '>' * ($nestedPromptLevel + 1) }
)

# execute
Set-PowerLinePrompt `
    -PowerLineFont `
    -SetCurrentDirectory `
    -RestoreVirtualTerminal `
    -HideError `
    -Colors "Gray", "Gray", "Gray", "Green", "Blue", "Gray"
