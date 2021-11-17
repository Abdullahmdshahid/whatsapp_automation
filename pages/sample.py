import openpyxl as op


class SampleData():
    DEMO_TEXT = "Hello"
    exl = op.load_workbook(r'\whatsapp_automation\files\whatsapp_number.xlsx')
    sh1 = exl['Sheet1']
    NUMBER = sh1['A2'].value
    exl_save = (r'\whatsapp_automation\files\whatsapp_number.xlsx')
