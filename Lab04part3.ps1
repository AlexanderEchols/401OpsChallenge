# ensuring 'password must meet complexity requirements' are set to 'Enabled"
#This will set all local user accounts with passwords that do expire but that they can change
Set-LocalUser -Name '*' -PasswordNeverExpires $false -UserMayChangePassword $true
# here we set a variable to point to the location of the 'secedit.sdb' file, This file is the local security data base
$theway = C:\Windows\security\database\secedit.sdb
# here we are running the .exe file that actually configures the local security policy
& secedit.exe /configure /db $theway /cfg C:\Windows\INF\defltwk.inf /areas SECURITYPOLICY

# here we check the SMBv1 client driver setting
$SMBv1Status = Get-ItemPropertyValue "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" "AllowInsecureGuestAuth"
# here we change the status if it needs it
if ($SMBv1Status -ne 0) {
    Set-ItemProperty "HKLM:\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters" -Name "AllowInsecureGuestAuth" -Value 0 -Type DWord
    Restart-Service LanmanWorkstation
}