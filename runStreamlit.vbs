Set WshShell = Wscript.CreateObject("Wscript.Shell")

dirPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(Wscript.ScriptFullName)
pyFile = "main.py"
cmd = "streamlit run " & dirPath & "\" & pyFile
WshShell.Run cmd
