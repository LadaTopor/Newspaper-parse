from pullenti.unitext import UnitextService
from pullenti.util import TextHelper

doc = UnitextService.UnitextService.create_document("Binder05.pdf")

# print(TextHelper.TextHelper.correct_whitespaces(doc))

print(TextHelper.TextHelper.extract_text("Binder05.pdf"))
