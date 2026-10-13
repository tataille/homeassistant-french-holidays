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
    def test_countdown_before_school_holidays(self):
        state = engine.states(date(2026, 4, 1), self.public, self.school)
        self.assertEqual(state["days_until_school_holidays"], 10)
        self.assertEqual(state["next_school_holidays_countdown"], 10)

    def test_unknown_public_year(self):
        self.assertIsNone(engine.states(date(2030,1,1),self.public,self.school)['public_holiday'])
    def test_invalid_payload(self):
        with self.assertRaises(ValueError): engine.validate_public({})
        with self.assertRaises(ValueError): engine.normalize_school([])
    def test_teacher_duplicates_excluded(self):
        self.assertEqual(engine.normalize_school([{'start_date':'2026-04-10T22:00:00Z','end_date':'2026-04-26T22:00:00Z','description':'Printemps','population':'Enseignants'}, {'start_date':'2026-04-10T22:00:00Z','end_date':'2026-04-26T22:00:00Z','description':'Printemps','population':'-'}]), self.school)

class NodeRedParityTests(unittest.TestCase):
    def setUp(self):
        self.public = {'2026-05-22':'Abolition de l’esclavage','2026-12-25':'Noël'}
        self.school = [
            {'start':'2026-04-11','end':'2026-04-27','name':'Printemps','zone':'Zone B'},
            {'start':'2026-07-04','end':'2026-09-01','name':'Été','zone':'Zone B'},
        ]
    def test_current_and_next_period_during_holidays(self):
        state=engine.states(date(2026,4,15),self.public,self.school)
        self.assertEqual(state['school_holiday_name'],'Printemps')
        self.assertEqual(state['school_holidays_end_date'],date(2026,4,27))
        self.assertEqual(state['next_school_holidays'],'Été')
        self.assertEqual(state['next_school_holidays_start'],date(2026,7,4))
        self.assertEqual(state['next_school_holidays_end'],date(2026,9,1))
        self.assertEqual(state['next_school_holidays_countdown'],80)
        self.assertEqual(state['days_until_school_holidays'],0)
    def test_current_public_name_and_strictly_future_next(self):
        state=engine.states(date(2026,5,22),self.public,self.school)
        self.assertEqual(state['public_holiday_name'],'Abolition de l’esclavage')
        self.assertEqual(state['next_public_holiday'],'Noël')
        self.assertEqual(state['next_public_holiday_date'],date(2026,12,25))
    def test_school_year_rollover(self):
        self.assertEqual(engine.states(date(2026,8,31),self.public,self.school)['school_period'],'2025-2026')
        self.assertEqual(engine.states(date(2026,9,1),self.public,self.school)['school_period'],'2026-2027')
    def test_metadata_and_javascript_day_number(self):
        state=engine.states(date(2026,4,12),self.public,self.school,academy='Nantes',region='martinique',version='0.1.1')
        self.assertEqual((state['day'],state['year'],state['academy'],state['region'],state['zones'],state['version']),(0,2026,'Nantes','martinique','Zone B','0.1.1'))
        self.assertEqual(engine.states(date(2026,4,11),self.public,self.school)['day'],6)
    def test_unknown_current_and_future_holidays(self):
        state=engine.states(date(2030,1,1),self.public,self.school)
        for key in ['public_holiday_name','school_holiday_name','school_holidays_end_date','next_school_holidays','next_school_holidays_start','next_school_holidays_end','next_school_holidays_countdown','next_public_holiday_date']:
            self.assertIsNone(state[key],key)
    def test_school_zone_survives_normalization_and_cache_json(self):
        import json
        rows=[{'start_date':'2026-04-10T22:00:00Z','end_date':'2026-04-26T22:00:00Z','description':'Printemps','population':'-','zones':'Zone B'}]
        school=json.loads(json.dumps(engine.normalize_school(rows)))
        self.assertEqual(engine.states(date(2026,4,12),self.public,school)['zones'],'Zone B')
