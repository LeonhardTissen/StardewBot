import json
from .seasonNames import seasonNames

def checkReminders(day, seasonId, year):
	message = ""

	try:
		with open('reminders.json', 'r') as f:
			reminderJson = json.load(f)
			reminders = reminderJson['reminders']

			reminders_to_remove = []
			
			for reminder in reminders:
				if reminder['day'] == day and reminder['seasonId'] == seasonId and reminder['year'] == year:
					message += f"\n<@{reminder['initiator']}>, {reminder['reminder']}"

					reminders_to_remove.append(reminder)
			
			for reminder in reminders_to_remove:
				reminders.remove(reminder)

			with open('reminders.json', 'w') as f:
				json.dump(reminderJson, f, indent=4)

	except FileNotFoundError:
		pass

	return message

def getReminders():
	message = "### All pending reminders:"

	try:
		with open('reminders.json', 'r') as f:
			reminderJson = json.load(f)
			reminders = reminderJson['reminders']

			if len(reminders) == 0:
				return "### No pending reminders"
			
			reminders = sorted(reminders, key=lambda x: (x['year'], x['seasonId'], x['day']))

			for reminder in reminders:
				seasonName = seasonNames[reminder['seasonId']]
				reminderMessage = reminder['reminder']
				day = reminder['day']
				year = reminder['year']

				message += f"\n{seasonName} {day}, Year {year}: {reminderMessage}"

	except FileNotFoundError:
		pass

	return message
