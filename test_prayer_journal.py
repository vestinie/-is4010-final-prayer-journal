"""
Tests for Prayer Journal CLI
"""

import pytest
import json
import os
from prayer_journal import PrayerJournal


@pytest.fixture
def temp_journal(tmp_path):
    """Create a temporary prayer journal for testing."""
    test_file = tmp_path / "test_prayers.json"
    journal = PrayerJournal(filename=str(test_file))
    return journal


class TestPrayerJournal:
    """Test cases for PrayerJournal class."""
    
    def test_add_prayer(self, temp_journal):
        """Test adding a new prayer."""
        prayer = temp_journal.add_prayer("Test prayer", "Testing")
        assert prayer['text'] == "Test prayer"
        assert prayer['category'] == "Testing"
        assert prayer['answered'] == False
        assert prayer['id'] == 1
    
    def test_add_multiple_prayers(self, temp_journal):
        """Test adding multiple prayers."""
        temp_journal.add_prayer("Prayer 1", "Family")
        temp_journal.add_prayer("Prayer 2", "Health")
        
        assert len(temp_journal.prayers) == 2
        assert temp_journal.prayers[0]['id'] == 1
        assert temp_journal.prayers[1]['id'] == 2
    
    def test_mark_answered(self, temp_journal):
        """Test marking a prayer as answered."""
        prayer = temp_journal.add_prayer("Test prayer", "General")
        result = temp_journal.mark_answered(prayer['id'])
        
        assert result == True
        assert temp_journal.prayers[0]['answered'] == True
        assert temp_journal.prayers[0]['date_answered'] is not None
    
    def test_mark_answered_invalid_id(self, temp_journal):
        """Test marking non-existent prayer as answered."""
        result = temp_journal.mark_answered(999)
        assert result == False
    
    def test_delete_prayer(self, temp_journal):
        """Test deleting a prayer."""
        prayer = temp_journal.add_prayer("Test prayer", "General")
        result = temp_journal.delete_prayer(prayer['id'])
        
        assert result == True
        assert len(temp_journal.prayers) == 0
    
    def test_delete_invalid_id(self, temp_journal):
        """Test deleting non-existent prayer."""
        result = temp_journal.delete_prayer(999)
        assert result == False
    
    def test_load_prayers(self, tmp_path):
        """Test loading prayers from file."""
        test_file = tmp_path / "test_prayers.json"
        
        # Create a journal and add a prayer
        journal1 = PrayerJournal(filename=str(test_file))
        journal1.add_prayer("Test prayer", "General")
        
        # Create new journal instance and load
        journal2 = PrayerJournal(filename=str(test_file))
        assert len(journal2.prayers) == 1
        assert journal2.prayers[0]['text'] == "Test prayer"
    
    def test_save_prayers(self, tmp_path):
        """Test saving prayers to file."""
        test_file = tmp_path / "test_prayers.json"
        journal = PrayerJournal(filename=str(test_file))
        journal.add_prayer("Test prayer", "General")
        
        # Check file exists and contains data
        assert os.path.exists(test_file)
        with open(test_file, 'r') as f:
            data = json.load(f)
        assert len(data) == 1
        assert data[0]['text'] == "Test prayer"
    
    def test_empty_journal(self, temp_journal):
        """Test behavior with empty journal."""
        assert len(temp_journal.prayers) == 0
        assert temp_journal.delete_prayer(1) == False
        assert temp_journal.mark_answered(1) == False
    
    def test_prayer_categories(self, temp_journal):
        """Test different prayer categories."""
        categories = ['Family', 'Health', 'Guidance', 'Thanksgiving']
        
        for cat in categories:
            temp_journal.add_prayer(f"Prayer for {cat}", cat)
        
        assert len(temp_journal.prayers) == 4
        for i, cat in enumerate(categories):
            assert temp_journal.prayers[i]['category'] == cat