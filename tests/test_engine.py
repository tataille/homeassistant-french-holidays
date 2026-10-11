import importlib.util
from pathlib import Path
from datetime import date
import unittest
spec = importlib.util.spec_from_file_location("engine", Path(__file__).parents[1]/"custom_components/french_holidays/engine.py")
engine = importlib.util.module_from_spec(spec)
spec.loader.exec_module(engine)

class EngineTests(unittest.TestCase):
    def setUp(self):
        self.public = {"2026-05-22": "Abolition de l’esclavage", "2026-12-25": "Noël", "2027-01-01": "Jour de l’an"}
        self.school = engine.normalize_school([{"start_date":"2026-04-10T22:00:00Z","end_date":"2026-04-26T22:00:00Z","description":"Printemps","population":"-"}])
    def test_paris_dates(self):
        self.assertEqual(self.school[0]['start'], '2026-04-11')
        self.assertEqual(self.school[0]['end'], '2026-04-27')
    def test_school_start_inclusive_end_exclusive(self):
        self.assertTrue(engine.states(date(2026,4,11),self.public,self.school)['school_holidays'])
        self.assertTrue(engine.states(date(2026,4,26),self.public,self.school)['school_holidays'])
        self.assertIsNone(engine.states(date(2026,4,27),self.public,self.school)['school_holidays'])
    def test_martinique_holiday(self):
        state=engine.states(date(2026,5,22),self.public,self.school)
        self.assertTrue(state['public_holiday'])
        self.assertFalse(state['working_day'])
    def test_tomorrow_year_boundary(self):
        self.assertTrue(engine.states(date(2026,12,31),self.public,self.school)['public_holiday_tomorrow'])
    def test_weekend_and_countdown(self):
        state=engine.states(date(2026,4,12),self.public,self.school)
        self.assertTrue(state['weekend'])
        self.assertEqual(state['days_until_school_holidays'],0)
    def test_unknown_public_year(self):
        self.assertIsNone(engine.states(date(2030,1,1),self.public,self.school)['public_holiday'])
    def test_invalid_payload(self):
        with self.assertRaises(ValueError): engine.validate_public({})
        with self.assertRaises(ValueError): engine.normalize_school([])
    def test_teacher_duplicates_excluded(self):
        self.assertEqual(engine.normalize_school([{'start_date':'2026-04-10T22:00:00Z','end_date':'2026-04-26T22:00:00Z','description':'Printemps','population':'Enseignants'}, {'start_date':'2026-04-10T22:00:00Z','end_date':'2026-04-26T22:00:00Z','description':'Printemps','population':'-'}]), self.school)
