from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField(_("Question"))
    answer = RichTextField(_("Answer"))
    question_hi = models.TextField(_("Question (Hindi)"), blank=True)
    question_bn = models.TextField(_("Question (Bengali)"), blank=True)
    answer_hi = RichTextField(_("Answer (Hindi)"), blank=True)
    answer_bn = RichTextField(_("Answer (Bengali)"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

    def get_translated_text(self, field, lang):
        # Only return translation if language is 'hi' or 'bn', otherwise fallback to English
        if lang == 'en':
            return getattr(self, field)  # Return English text
        elif lang == 'hi':
            return self.question_hi if self.question_hi else self.translate_field(field, lang)
        elif lang == 'bn':
            return self.question_bn if self.question_bn else self.translate_field(field, lang)
        return getattr(self, field)  # Default fallback to English

    def translate_field(self, field, lang):
        # Perform the translation and store it
        if lang not in ['hi', 'bn']:
            return getattr(self, field)  # Only translate to 'hi' or 'bn'
        
        # Use Google Translate API (or fallback to another translation service)
        translator = Translator()
        original_text = getattr(self, field)
        translation = translator.translate(original_text, dest=lang)
        
        # Save the translation directly to the field
        translated_field = f"{field}_{lang}"
        setattr(self, translated_field, translation.text)
        self.save()  # Save the updated FAQ with translations
        return translation.text

    def save(self, *args, **kwargs):
        # Translate question and answer fields on creation, save translation to other fields
        if not self.pk:  # Only translate on creation
            self.translate_on_create()
        super().save(*args, **kwargs)

    def translate_on_create(self):
        # Translate both question and answer to 'hi' and 'bn' on creation
        translator = Translator()
        self.question_hi = translator.translate(self.question, dest='hi').text
        self.question_bn = translator.translate(self.question, dest='bn').text
        self.answer_hi = translator.translate(self.answer, dest='hi').text
        self.answer_bn = translator.translate(self.answer, dest='bn').text

