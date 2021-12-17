def FORM_CREATE_VBS(msg, title, style):
    Create_Form = f"""Dim MSG, Title, Style, Response
MSG = "{msg}"
Style = {style}
Title = "{title}"
Response = MsgBox(MSG, Style, Title)"""
    return Create_Form