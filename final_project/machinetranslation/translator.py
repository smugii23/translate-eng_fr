"""This module takes english and french texts and translates them"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates a given english text to french.
    Input: english_text - str
    Output: french_text - str
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates a given french text to english.
    Input: french_text - str
    Output: english_text - str
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text

