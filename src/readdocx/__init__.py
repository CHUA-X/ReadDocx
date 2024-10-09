#! /usr/bin/python3
# copyright 2024 CHUA某人，版权所有。
# ReadDocx ——直接提取Word文档（不包含样式信息）
# 用法：import readdocx;text = readdocx.getText('文件名');print(text)

from docx import Document


def getText(file, tab=False, blank=0):
    doc = Document(file)
    full_text = []
    for paragraph in doc.paragraphs:
        if tab:
            full_text.append('  ' + paragraph.text)
        else:
            full_text.append(paragraph.text)
    blanks = (blank + 1) * '\n'  # 空行数
    return blanks.join(full_text)
