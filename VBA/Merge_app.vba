Option Explicit

Public Sub MergeCsv_CMS()
    Dim selected As Variant
    Dim savePath As Variant
    Dim firstFile As Boolean
    Dim f As Variant
    Dim headerLine As String
    Dim content As String


    'CSVファイル選択
    selected = Application.GetOpenFilename(_FileFilter:="CSV(*.csv),*.csv",_
        MultiSelect:=True, Title:="マージするCSVファイルを選択してください")

    If VarType(selected) = vbBoolean Then Exit Sub

    '保存先選択
    savePath = Application.GetSaveAsFilename(_InitialFileName:=Environ("USERPROFILE") & "\Desktop\merged_CMS.csv", _
        FileFilter:="CSV(*.csv),*.csv",_ Title:="マージ後のCSVを保存")

    If savePath = False Then Exit Sub

    firstFile = True

    Dim stmOut As Object
    Set stmOut = CreateObject("ADODB.Stream")
    With stmOut
        .Type = 2 'テキスト
        .Charset = "utf-8"
        .Open
     
     'ファイルごとに読み込んでマージ
     For Each f In selected
        Dim stmIn As Object
        Dim lines() As String
        Dim i As Long

        Set stmIn = CreateObject("ADODB.Stream")
        With stmIn
            .Type = 2 'テキスト
            .Charset = "utf-8"
            .Open
            .LoadFromFile f
            content = .ReadText
            .Close
        End With
        Set stmIn = Nothing

        'LF改行に統一
        content = Replace(content, vbCrLf, vbLf)
        content = Replace(content, vbCr, vbLf)
        lines = Split(content, vbLf)

        For i = LBound(lines) To UBound(lines)
            Dim lineText As String
            lineText = Trim(lines(i))
            If lineText <> "" Then
                If firstFile Then
                    'ヘッダー行は最初のファイルの1行目だけ書き込む
                    headerLine = lineText
                    .WriteText lineText & vbLf
                    firstFile = False
                Else
                    'データ行はヘッダー行以降のみ書き込む書き込む
                    If i > 0 Then 
                        '行末の余計なカンマ削除
                        lineText = RemoveTrailingCommas(lineText)
                        .WriteText lineText & vbLf
                    End If
                End If
            End If
        Next i
     Next f

     .SaveToFile savePath, 2 '上書き
      .Close
    End With

    MsgBox "CMS対応CSVを保存しました:"& savePath, vbInformation
End Sub

'行末の余計なカンマを削除
Function RemoveTrailingCommas(s As String) As String
    Do While Right(s,1) = ","
        s = Left(s, Len(s) - 1)
    Loop
    RemoveTrailingCommas = s
End Function