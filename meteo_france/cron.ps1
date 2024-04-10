# Définir les paramètres de la tâche
$TaskName = "MaTachePlanifiee"
$ScriptPath = "C:\chemin\vers\votre\script.ps1" # Chemin vers le script ou la commande à exécuter
$Trigger = New-ScheduledTaskTrigger -Daily -At 9am # Définir le déclencheur (ici, quotidiennement à 9h)
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File $ScriptPath" # Définir l'action (exécuter un script PowerShell)
$Settings = New-ScheduledTaskSettingsSet # Définir les paramètres de la tâche

# Créer la tâche planifiée
Register-ScheduledTask -TaskName $TaskName -Trigger $Trigger -Action $Action -Settings $Settings -User "Utilisateur" -Password "MotDePasse"