$1cv8 = Get-WMIObject win32_process | where {$_.ProcessName -eq "1cv8.exe"}
foreach ($proc in $1cv8)
{
    logoff $proc.SessionID
}
