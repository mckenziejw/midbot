#SingleInstance, Force
SendMode Input
SetWorkingDir, %A_ScriptDir%
^k::

Loop, Read, prompts.txt
{
    Send /imagine {Space}%A_LoopReadLine%{Enter}
    Random, sleepTime, 60000, 90000
    Sleep, sleepTime
}


Return