REM  *****  BASIC  *****

Sub Main
    Dim oSheet As Object
    Dim oCell As Object
    Dim sValue As String
    Dim oCurCell As Object
    Dim oRange As Object
    
    oSheet = ThisComponent.CurrentController.ActiveSheet
    oCurCell = ThisComponent.CurrentSelection
    oCell = oSheet.getCellRangeByName(ThisComponent.CurrentSelection.AbsoluteName)
    sValue = oCell.getString()
   	
' 	blank out unused cells for this widget
   	
    If sValue = "combo" or _
    	sValue = "options" or _
    	sValue = "scale" or _
    	sValue = "scrollx" or _
    	sValue = "scrolly" or _
    	sValue = "entry" or _
    	sValue = "spin" then
        oRange = oSheet.getCellRangeByPosition(3, oCurCell.CellAddress.Row, 3, oCurCell.CellAddress.Row)
    Else If sValue = "frame" or _
    	sValue = "list" or _
    	sValue = "text" or _
    	sValue = "calendar" or _
    	sValue = "notebook" or _
    	sValue = "progress" then
        oRange = oSheet.getCellRangeByPosition(3, oCurCell.CellAddress.Row, 4, oCurCell.CellAddress.Row)
    Else If sValue = "button" or _
	   	sValue = "label" or _
	   	sValue = "check" or _
	   	sValue = "radio" then
		msgbox("All Cells Required, Except label")
		GOTO filltext ' good-old goto
    Else If sValue = "popup" or _
    	sValue = "clip" or _
    	sValue = "messagebox" or _
    	sValue = "filedialog" or _
    	sValue = "simpledialog" or _
    	sValue = "toplevel" then
        oRange = oSheet.getCellRangeByPosition(1, oCurCell.CellAddress.Row, 10, oCurCell.CellAddress.Row)
	Else If sValue = "message" then
		oRange = oSheet.getCellRangeByPosition(4, oCurCell.CellAddress.Row, 4, oCurCell.CellAddress.Row)
	Else If sValue = "" then
		msgbox("Invalid Widget")
		Exit Sub
    End If:End If:End If:End If:End If:End If ' kind of bizzar!
    
    ' background to black
    oRange.CellBackColor = RGB(0, 0, 0)

' 	Now fill some help text for this widget
filltext:

	oCell = oSheet.getCellByPosition(4,  oCurCell.CellAddress.Row)
	
    If sValue = "entry" or _
   		sValue = "label" or _
    	sValue = "spin" or _
    	sValue = "scale" or _
    	sValue = "options" or _
    	sValue = "combo" then
		oCell.setString("StringVar...")
	Else If sValue = "button" then
		oCell.setString("command...")
	Else If sValue = "scrollx" or _
    		sValue = "scrolly" then
    	oCell.setString("widget...")
    Else If sValue = "check" or _
	   		sValue = "radio" then
		oCell.setString("IntVar...")	
	End If:End If:End If:End If
	
End Sub

