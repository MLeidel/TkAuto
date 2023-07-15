
Sub Main()
    Dim currentRow As Integer
    Dim rng As Range
    Dim sValue As String
    
    ' Get the current row number
    currentRow = ActiveCell.Row
    sValue = ActiveCell.Value
    
    If sValue = "combo" Or _
        sValue = "options" Or _
        sValue = "scale" Or _
        sValue = "scrollx" Or _
        sValue = "scrolly" Or _
        sValue = "entry" Or _
        sValue = "spin" Then
        Set rng = Range(Cells(currentRow, 4), Cells(currentRow, 4))
    ElseIf sValue = "frame" Or _
        sValue = "list" Or _
        sValue = "text" Or _
        sValue = "calendar" Or _
        sValue = "notebook" Or _
        sValue = "progress" Then
        Set rng = Range(Cells(currentRow, 4), Cells(currentRow, 5))
    ElseIf sValue = "button" Or _
        sValue = "label" Or _
        sValue = "check" Or _
        sValue = "radio" Then
        MsgBox ("All Cells Required, Except label")
        GoTo filltext ' good-old goto
    ElseIf sValue = "popup" Or _
        sValue = "clip" Or _
        sValue = "messagebox" Or _
        sValue = "filedialog" Or _
        sValue = "simpledialog" Or _
        sValue = "toplevel" Then
        Set rng = Range(Cells(currentRow, 2), Cells(currentRow, 11))
    ElseIf sValue = "message" Then
        Set rng = Range(Cells(currentRow, 5), Cells(currentRow, 5))
    ElseIf sValue = "" Then
        MsgBox ("Invalid Widget")
        Exit Sub
    End If
  
    ' Set the color for the range
    rng.Interior.Color = RGB(0, 0, 0)
    
'   Now fill some help text for this widget
filltext:
    
    If sValue = "entry" Or _
        sValue = "label" Or _
        sValue = "spin" Or _
        sValue = "scale" Or _
        sValue = "options" Or _
        sValue = "combo" Then
        Cells(currentRow, 5).Value = "StringVar..."
    ElseIf sValue = "button" Then
        Cells(currentRow, 5).Value = "command..."
    ElseIf sValue = "scrollx" Or _
            sValue = "scrolly" Then
        Cells(currentRow, 5).Value = "widget..."
    ElseIf sValue = "check" Or _
            sValue = "radio" Then
        Cells(currentRow, 5).Value = "IntVar..."
    End If

End Sub
