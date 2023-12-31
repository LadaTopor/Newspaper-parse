﻿# SDK Pullenti Unitext, version 4.19, may 2023. Copyright (c) 2013, Pullenti. All rights reserved.
# Non-Commercial Freeware and Commercial Software.
# This class is generated using the converter UniSharping (www.unisharping.ru) from Pullenti C# project.
# The latest version of the code is available on the site www.pullenti.ru


from pullenti.unitext.CorrectDocumentParam import CorrectDocumentParam

class CreateDocumentParam:
    """ Параметры создания документа UnitextDocument функцией CreateDocument
    Параметры создания документа
    """
    
    def __init__(self) -> None:
        self.only_for_pure_text = False
        self.ignore_inner_documents = False
        self.extract_page_image_content = False
        self.split_table_rows = False
        self.load_document_structure = False
        self.correct_params = None;
        self.dont_generate_items_id = False
        self.ignore_word6 = False
        self.correct_params = CorrectDocumentParam()
        self.correct_params.choose_all = True
    
    @staticmethod
    def _new623(_arg1 : bool, _arg2 : bool) -> 'CreateDocumentParam':
        res = CreateDocumentParam()
        res.only_for_pure_text = _arg1
        res.ignore_inner_documents = _arg2
        return res