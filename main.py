import schedule
import time
from datetime import datetime
from post_bot import post_to_telegram

# Daily messages
messages = {
    "Monday": "🌞 Monday Motivation: Start your week with a positive mindset! #MondayMotivation",
    "Tuesday": "💡 Tuesday Tips: Did you know that consistency is key to success? #TuesdayTips",
    "Wednesday": "🧠 Wednesday Wisdom: Keep pushing forward, you're halfway through the week! #WednesdayWisdom",
    "Thursday": "🤔 Thursday Thoughts: Reflect on your progress and set new goals! #ThursdayThoughts",
    "Friday": "🎉 Friday Fun: It's almost the weekend! What are your plans? #FridayFun",
    "Saturday": "🌴 Saturday Vibes: Take a break and enjoy some leisure time! #SaturdayVibes",
    "Sunday": "📖 Sunday Reflections: Prepare for the week ahead and set your intentions! #SundayReflections"
}

def job():
    today = datetime.now().strftime('%A')
    message = messages.get(today, "📢 Daily Reminder: Stay focused and keep going!")
    post_to_telegram(message)

def start_schedule():
    # Schedule once per day at 09:00 AM (you can change the time)
    schedule.every().day.at("09:00").do(job)
    


    print("📆 Telegram Daily Bot started. Waiting to post each morning...")

    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    start_schedule()

