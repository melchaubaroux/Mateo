						# Définir les paramètres de la tâche

# nom de la tache 
$TaskName = "Maj_db"

# Chemin vers le script ou la commande à exécuter
$ScriptPath = "c:\Users\Utilisateur\Desktop\projets\briefs\b16_mateo\github\batch.py" 

# Définir le déclencheur (ici, quotidiennement à 9h)
$Trigger = New-ScheduledTaskTrigger -Daily -At 9am 

# Définir l'action (exécuter un script PowerShell)
$Action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File $ScriptPath" 

# Définir les paramètres de la tâche
$Settings = New-ScheduledTaskSettingsSet 

# Créer la tâche planifiée
Register-ScheduledTask -TaskName $TaskName -Trigger $Trigger -Action $Action # -Settings $Settings -User "Utilisateur" -Password "MotDePasse"