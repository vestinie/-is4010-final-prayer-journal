#!/usr/bin/env python3
"""
Prayer Journal CLI - A tool to track and manage prayer requests
"""

import json
import os
import argparse
import sys
from datetime import datetime


class PrayerJournal:
    """Main class for managing prayer requests."""
    
    def __init__(self, filename='prayers.json'):
        self.filename = filename
        self.prayers = self.load_prayers()
    
    def load_prayers(self):
        """Load prayers from JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"Error: {self.filename} is corrupted. Starting with empty journal.", file=sys.stderr)
                return []
            except Exception as e:
                print(f"Error loading prayers: {e}", file=sys.stderr)
                return []
        return []
    
    def save_prayers(self):
        """Save prayers to JSON file."""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.prayers, f, indent=2)
        except Exception as e:
            print(f"Error saving prayers: {e}", file=sys.stderr)
            sys.exit(1)
    
    def add_prayer(self, text, category='General'):
        """Add a new prayer request."""
        if not text or not text.strip():
            raise ValueError("Prayer text cannot be empty")
        
        prayer = {
            'id': len(self.prayers) + 1,
            'text': text.strip(),
            'category': category.strip(),
            'date_created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'answered': False,
            'date_answered': None
        }
        self.prayers.append(prayer)
        self.save_prayers()
        return prayer
    
    def list_prayers(self, show_answered=True):
        """List all prayer requests."""
        if not self.prayers:
            print("\nNo prayers yet. Add your first prayer!\n")
            return
        
        print("\n" + "="*60)
        print("YOUR PRAYER JOURNAL")
        print("="*60)
        
        for prayer in self.prayers:
            if not show_answered and prayer['answered']:
                continue
            
            status = "✓ ANSWERED" if prayer['answered'] else "⏳ ACTIVE"
            print(f"\nID: {prayer['id']} | {status} | [{prayer['category']}]")
            print(f"Date: {prayer['date_created']}")
            print(f"Prayer: {prayer['text']}")
            
            if prayer['answered']:
                print(f"Answered: {prayer['date_answered']}")
        
        print("\n" + "="*60 + "\n")
    
    def mark_answered(self, prayer_id):
        """Mark a prayer as answered."""
        for prayer in self.prayers:
            if prayer['id'] == prayer_id:
                if prayer['answered']:
                    print(f"\n⚠️  Prayer {prayer_id} was already marked as answered.\n")
                    return True
                prayer['answered'] = True
                prayer['date_answered'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                self.save_prayers()
                return True
        return False
    
    def delete_prayer(self, prayer_id):
        """Delete a prayer by ID."""
        for i, prayer in enumerate(self.prayers):
            if prayer['id'] == prayer_id:
                self.prayers.pop(i)
                self.save_prayers()
                return True
        return False


def main():
    """Main entry point for the CLI."""
    parser = argparse.ArgumentParser(
        description='Prayer Journal CLI - Track and manage your prayer requests',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  py prayer_journal.py add "Please heal my friend" --category Health
  py prayer_journal.py list
  py prayer_journal.py list --active-only
  py prayer_journal.py answered 1
  py prayer_journal.py delete 2
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new prayer request')
    add_parser.add_argument('text', help='Prayer request text')
    add_parser.add_argument('--category', '-c', default='General', 
                           help='Category (e.g., Family, Health, Guidance)')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all prayers')
    list_parser.add_argument('--active-only', action='store_true',
                            help='Show only active (unanswered) prayers')
    
    # Answered command
    answered_parser = subparsers.add_parser('answered', help='Mark prayer as answered')
    answered_parser.add_argument('id', type=int, help='Prayer ID to mark as answered')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a prayer')
    delete_parser.add_argument('id', type=int, help='Prayer ID to delete')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return 0
    
    try:
        journal = PrayerJournal()
        
        if args.command == 'add':
            prayer = journal.add_prayer(args.text, args.category)
            print(f"\n✓ Prayer added successfully! (ID: {prayer['id']})\n")
        
        elif args.command == 'list':
            journal.list_prayers(show_answered=not args.active_only)
        
        elif args.command == 'answered':
            if journal.mark_answered(args.id):
                print(f"\n✓ Prayer {args.id} marked as answered! Praise God! 🙏\n")
            else:
                print(f"\n✗ Prayer ID {args.id} not found.\n", file=sys.stderr)
                return 1
        
        elif args.command == 'delete':
            if journal.delete_prayer(args.id):
                print(f"\n✓ Prayer {args.id} deleted.\n")
            else:
                print(f"\n✗ Prayer ID {args.id} not found.\n", file=sys.stderr)
                return 1
        
        return 0
        
    except ValueError as e:
        print(f"\n✗ Error: {e}\n", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.\n", file=sys.stderr)
        return 130
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}\n", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main()) 