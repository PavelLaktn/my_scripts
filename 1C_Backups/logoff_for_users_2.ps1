$1cv8 = Get-WMIObject win32_process | where {$_.ProcessName -eq "1cv8.exe"}
$1cv8c = Get-WMIObject win32_process | where {$_.ProcessName -eq "1cv8c.exe"}
foreach ($proc in $1cv8)
{
    logoff $proc.SessionID
}
foreach ($proc in $1cv8c)
{
    logoff $proc.SessionID
}