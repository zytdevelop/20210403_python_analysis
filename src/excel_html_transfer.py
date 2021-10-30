#!/bin/env python
# -*- coding: utf-8 -*-

import win32com.client as win32


excel = win32.gencache.EnsureDispatch('Excel.Application')
excel.Visible = False
excel.DisplayAlerts = False
wb = excel.Workbooks.Open(r'D:\python_project\20210403_python_analysis\src\test1.xls')
ws = wb.Worksheets(1)
ws.Range("A1:D8").Copy()
ws.Close()

word_path = r'output.docx'
word = win32.gencache.EnsureDispatch('Word.Application')
doc = word.Documents.Open(word_path)
doc.Content.PasteExcelTable(False, False, True)
doc.Close()
